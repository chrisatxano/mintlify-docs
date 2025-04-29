---
icon: file
---

# Custom Report Generation

## Report Generation using Database Views

Xano offers an easy way to share read-only views of your database tables. If the data is already presented in a readable format, you can quickly share it with others, even if they are not Xano users.

{% content-ref url="../the-database/database-basics/database-views.md" %}
[database-views.md](../the-database/database-basics/database-views.md)
{% endcontent-ref %}

## Report Generation in the Function Stack

Sometimes, your data may not be in what would be considered a human readable format, and you need to make modifications to it, or present it in an alternative format.

### Using APIs

If you need reports to be generated on demand, use an API endpoint for this functionality.

{% content-ref url="../the-function-stack/building-with-visual-development/apis/" %}
[apis](../the-function-stack/building-with-visual-development/apis/)
{% endcontent-ref %}

### Using Background Tasks

If you want to generate reports based on a schedule, utilize a background task.

{% content-ref url="../the-function-stack/building-with-visual-development/background-tasks.md" %}
[background-tasks.md](../the-function-stack/building-with-visual-development/background-tasks.md)
{% endcontent-ref %}

### Key Functions and Concepts

For most report generation, you'll want to ensure familiarity with the following concepts, depending on your specific needs.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Query All Records</strong></td><td>For retrieving data from your database</td><td><a href="../the-function-stack/functions/database-requests/query-all-records/">query-all-records</a></td></tr><tr><td><strong>For Each Loops</strong></td><td>For iterating through retrieved records and transforming the data</td><td><a href="../the-function-stack/functions/data-manipulation/loops.md#for-each-loop">#for-each-loop</a></td></tr><tr><td><strong>Filters</strong></td><td>Filters are typically used to apply modifications to pieces of data, such as math operations or comparing values.</td><td><a href="../the-function-stack/filters/">filters</a></td></tr></tbody></table>











