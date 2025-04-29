---
icon: magnifying-glass
---

# Fuzzy Search

Xano offers robust search capabilities, commonly referred to as _fuzzy search_, that you can utilize while querying records in a function stack. This includes normalization of words (ie. party vs parties), case-insensitive support, flexible expressions (words, phrases, and negations), and weighted priorities (ie. title vs description) for relevance.

The following demonstrates how to set up search in your database, the logic behind the search functionality, and best practices for utilizing search queries.

{% embed url="https://youtu.be/5_XkvyAX2C0" %}

[**Watch more videos on Fuzzy Search**](https://www.youtube.com/results?search_query=xano+fuzzy+search+)

### **Creating a Search Index**

First, create an [index](../the-database/database-performance-and-maintenance/indexing.md). Indexes are used to quickly locate data without having to search every row in a database table every time a database table is accessed. An index is used to define which fields of the database table you want to search. You can even build multiple search indexes on the same table to build different search criteria. For example, if you have both public and private data in the same table, you can build a "normal user" and an "administrator" search.

To create an index, click **Indexes** at the top of the table you would like to build search for, and then click **Create Index.**

![](<../.gitbook/assets/image (38).png>)

Choose **search** as the index type, and give the index a name. Next, specify the language for the data you are searching, the fields you are searching, and the ranking order of the fields being searched.

<div align="center"><img src="../.gitbook/assets/image (39).png" alt="An example of creating a search index."></div>

In this example, we created a new search index on a database of movies called **search\_movies**, in English, and are searching two fields in that database: title and overview. The title field will rank higher than data in the overview field in the qualified search results.&#x20;

Once ready, click **Save** and Xano will build your index. This can take a few minutes depending on the volume of data of the table.

### Building a Search API

After generating the index, it can be implemented it into a query in the function stack. Use the **Custom Query** feature in the **Filter** tab of the [**Query All Records**](../the-function-stack/functions/database-requests/query-all-records/) function.&#x20;

When adding a custom query, the newly created index is available in the expression builder, noted by the **$** symbol. It is also labeled as _search_ underneath the name.

![Look for the $ symbol as well as the word search to easily find your search index when configuring your query.](<../.gitbook/assets/image (40).png>)

Next, set the operator to **search** and specify the search query. In this example, we are using an input called **search\_query.**&#x20;

![Setting the operator to Search and specifying our search query.](<../.gitbook/assets/image (41).png>)

Congratulations! 🥳 You've just implemented super-fast search inside your function stack.

### Ranking

You can implement a ranking system and sort the search results by this rank for more precise search results. To do this, go to the **Output** tab of the **Query All Records** function, add an **eval** on the search index, and apply the **search\_query** filter. This tells Xano to "use my search index to generate a ranking score of my results based on my search query".

![Create and Eval on the search index by applying the search\_rank filter so we can sort by ranking.](../.gitbook/assets/Screenshot_2022-07-08_19-23-25.png)

After, add a sort to the query using the newly created eval (in this example, called "rank"). You may also consider to enable paging especially on larger queries.

{% hint style="info" %}
Add a Sort to the Query by clicking on the Return portion of the Output tab.
{% endhint %}

![](<../.gitbook/assets/image (42).png>)

{% hint style="info" %}
Order by in descending order will provide the most relevant search results first.
{% endhint %}

### Different Search Methods

Search queries can be written in different ways to fulfill specific search requirements.&#x20;

1. Words separated by a space imply an AND.\
   **Example:** A query of _"toy story"_ means _search for toy AND story_
2. Exact phrase searches are possible using double quotes.\
   **Example:** If you wanted to search for _"Toy Story"_ as an exact match, your query would be _"Toy Story" with the quotation marks_.\
   **Note:** if you are entering this search expression directly into a JSON payload, then you may need to escape the quotes with a backslash. example: `{"search": "\"Toy Story\""}`
3. Partial phrase matching\
   **Example:** `"Toy * Story"` would return any results that contain Toy Story with one word in between. `"Toy *** Story"` would return any results that contain Toy Story with three words in between.
4. Wildcard matching\
   **Example:** `Sto:*` would return any results that contain words that start with sto.
5. Expression groups\
   **Example:** `(Woody or Buzz) Toy` would return multiple matches for the word Toy that also include either Woody or Buzz.
6. Negation of specific words is possible by using a - character.\
   **Example:** If you wanted to search for movies that have _Toy_ in the title, but not _Toy Story_, your query would be _`"toy -story"`_.
7. You can also use a combination of these to get even more specific.\
   **Example:** Searching for `"toy story" day -night` would mean _search for the phrase Toy Story and the word day, without the word night._
8. Priority targets allow you to specify which priority defined in your search index to use for the specific expression. This can be combined with wildcard matching as well.\
   **Example:** `Toy Story:2` would search for all records containing the word Toy, as well as the word Story in any fields representing priority 2 in your search index.\
   **Example:** `Toy Sto:*2` would search for all records containing the word Toy, as well as words starting with Sto in any fields representing priority 2 in your search index.
9. Single vs Plural is supported.\
   For example, _"toy"_ will also return results that contain _"toys"_.

**Stop Words** -- are commonly used words such as articles, pronouns and prepositions. For example: _is, and, an, or, the._ Stop words are not included in your search query.

### Search Results

Search results are returned just like any other API response and the data works just like any other variable inside Xano.

<figure><img src="../.gitbook/assets/CleanShot 2023-01-17 at 11.07.11.png" alt=""><figcaption></figcaption></figure>
