---
icon: paintbrush-fine
---

# Designing your Database

{% hint style="info" %}
**Quick Summary**

Good database design starts with organizing your information into logical groups, like putting customer details in one table and order history in another. These groups are then connected through common identifiers using a [table reference field](#user-content-fn-1)[^1] - like a customer ID that links a person to all their orders - which helps maintain accuracy and avoid duplicating information.
{% endhint %}

Think of designing a database like organizing your home. Before you buy storage containers or rearrange your furniture, you need a plan. The same goes for databases - careful planning prevents headaches later.

{% hint style="info" %}
<mark style="color:blue;">**Hint**</mark>

Use a tool like [**Excalidraw**](https://excalidraw.com/) to help you when designing your database.
{% endhint %}

Start by listing everything you need to store. If you're building a bookstore database, you'll need to track books, authors, customers, and sales. Just like you wouldn't store your kitchen items in your bathroom, each type of information needs its own logical home in the database.

<figure><img src="../.gitbook/assets/CleanShot 2024-12-14 at 12.56.18.png" alt="" width="563"><figcaption><p>Using Excalidraw to begin the database design process.</p></figcaption></figure>

Let's draw these to look like individual items — these will represent the tables that we'll create.

<figure><img src="../.gitbook/assets/CleanShot 2024-12-14 at 12.57.04.png" alt="" width="563"><figcaption></figcaption></figure>

## Table Relationships

{% hint style="info" %}
To illustrate multiple examples, we've added a **Publishers** table to our visualization.
{% endhint %}

Consider how these pieces connect. A book has one or more authors, and an author can write multiple books. A customer can buy many books, and a book can be bought by many customers. These relationships are crucial - they're like the hallways connecting rooms in your house, allowing you to move naturally between related information.

**One-to-One**

* Each thing on one side matches exactly one thing on the other side. Like a person and their social security number: one person has one number, and each number belongs to one person

**One-to-Many**

* One thing on one side can connect to multiple things on the other side, but those multiple things each only connect back to one thing. Like a mother and her children: one mother can have many children, but each child has only one mother

**Many-to-Many**

* Things on both sides can connect to multiple things on the other side. Like students and classes: one student takes many classes, and each class has many students

For our book store example, let's visualize the relationships between our tables.

{% @arcade/embed flowId="eYYLSo6Vi1ZVYOkLk5i8" url="https://app.arcade.software/share/eYYLSo6Vi1ZVYOkLk5i8" %}

## Database Fields

**Think about the essential characteristics that describe each thing**. Just like how a person's profile might include their name, birthday, and contact info, each table should contain the core pieces of information that defines that thing. When referring to all of the fields in a database table as a whole, we'll call this **schema**.

Let's use our bookstore example:

* For Books: You'll want the ISBN (like a book's fingerprint), title, publication date, current price, and maybe format (hardcover/paperback). You don't need to store the author's name here - that's what the connection to the Authors table is for.
* For Authors: You'll store their name, perhaps birth date, nationality, and a brief biography. You don't need to store a list of their books - the relationship between tables handles that.
* For Customers: You'll want their name, contact information, shipping addresses, and maybe their preferences or a membership status. You don't need to store their purchase history here - that's tracked through the Sales table.

**"Does this information describe the core thing I'm tracking, or is it really about something else?"**\
If you find yourself wanting to store a list of things (like "all books by this author" or "all orders from this customer"), that's usually a sign you need a relationship between tables rather than storing that data directly.

**Consider whether the information might change over time**.\
For example, book prices change frequently, so you might want both a "currentPrice" in the Books table and a "salePrice" in the Sales Items table. This lets you track both what a book costs now and what customers actually paid for it in the past.

**Watch out for duplicate information.**\
If you're storing an author's contact details, store them once and reference them when needed, rather than copying them into every book record. This is like having one toolbox in your garage instead of keeping duplicate tools in every room. In Xano, this is accomplished with [table reference fields](database-basics/field-types.md#table-reference).

## Planning for the Future

**Think about what information you'll need to find quickly.**\
Just as you might keep frequently used items in easily accessible drawers, consider what data you'll search for most often. This helps you decide how to organize and [<mark style="color:blue;">index</mark>](#user-content-fn-2)[^2] your information.

**Think about how information might expand in the future.** \
Initially, you might only need basic book formats (hardcover and paperback). But what happens when you want to add audiobooks? You'll need new fields like runtime, narrator, and audio format. Instead of hard-coding format types, you could create a separate formats table, and use a table reference in your books table that lets you add new types without changing your core structure.

Suppose you create a database table for storing book formats directly within the books table:

**Books Table**

| BookID | Title | Author | Hardcover | Paperback | Audiobook |
| ------ | ----- | ------ | --------- | --------- | --------- |
|        |       |        |           |           |           |

This design is inflexible because each time you introduce a new format, you must alter the table structure. Instead, use a separate formats table and establish a relationship with the books table.

**Books Table**

| BookID | Title | Author |
| ------ | ----- | ------ |
|        |       |        |

**Formats Table**

| FormatID | FormatType |
| -------- | ---------- |
|          |            |

**BookFormats Table**

| BookID | FormatID |
| ------ | -------- |
|        |          |

This flexible table design allows you to add new formats easily without changing the core structure.

**Finally, remember that simple is usually better.**\
Like a well-organized home where everything has its place, a good database design should feel natural and intuitive. If you find yourself creating complicated structures to store simple information, step back and reconsider your approach.

Remember: **A well-designed database makes everything else easier.**



[^1]: A **table reference** field refers to a field type that contains the IDs of records in other tables, "linking" them together.

[^2]: An **index** is just like it sounds; similar to the index in the back of a book, it helps your table more quickly find the exact information you're looking for.\
    \
    To learn more about indexes, just proceed through the documentation and you'll get there soon. If you want to jump ahead, you can read the indexing documentation [here](database-performance-and-maintenance/indexing.md).
