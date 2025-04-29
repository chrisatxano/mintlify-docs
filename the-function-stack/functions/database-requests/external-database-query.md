# External Database Query

In Xano, you can connect to the following types of external databases:

* PostgreSQL
* MS SQL
* Oracle
* MySQL

Add a new function to your function stack that corresponds to the type of database you'd like to connect to. The external connection functions are located under Database Operations.

<figure><img src="../../../.gitbook/assets/CleanShot 2024-10-09 at 18.54.05@2x.png" alt=""><figcaption></figcaption></figure>

Once you've added your desired connection function, you'll need to define a **connection string**. A connection string is just a URL that contains all of the information we need to connect to your database, such as a hostname or IP address, port, username, and password. We've added an easy to use panel to help you generate a connection string for your database.

<figure><img src="../../../.gitbook/assets/CleanShot 2024-10-09 at 18.55.53@2x.png" alt="" width="375"><figcaption></figcaption></figure>

Fill in the required information and click **Save** at the bottom to generate your connection string.

For more information on building a query to run against your database, see our [Direct Database Query documentation](direct-database-query.md).
