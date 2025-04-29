---
icon: rocket-launch
---

# Database Performance and Maintenance

Database performance in Xano is typically dependent on three key areas.

{% stepper %}
{% step %}
### Indexing of large tables

As your database table grows in size, queries against that table become more resource intensive. Every time you search for specific records in that table, the table has to go through each record, one by one, to find the matching data.

We can combat this by using indexing. Like the index in the back of a book, this helps to let the table know where to find the requested information more quickly.

:book: [**Learn more about indexing**](indexing.md)
{% endstep %}

{% step %}
### Creating efficient queries

#### Using Addons

Addons are an easy way to get related data from multiple tables, such as users and orders. Using addons enables more efficient querying of both tables instead of using two separate queries.

:book: [**Learn more about addons**](../../the-function-stack/functions/database-requests/query-all-records/#using-addons)

#### Pagination

Access your query settings to adjust pagination when retrieving significant amounts of records at once.
{% endstep %}

{% step %}
### Efficient database design

Utilizing proper database design practices is paramount to ensuring your backend is as performant as possible. Even if you are well on your way to deploying your application, don't be afraid to make changes to your database design now to avoid future headaches.

:book: [**Read our documentation on database design**](../designing-your-database.md)
{% endstep %}
{% endstepper %}

