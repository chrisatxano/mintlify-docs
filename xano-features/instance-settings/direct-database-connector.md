---
description: Establish a direct connection to your instance's PostgreSQL database
---

# Direct Database Connector

{% hint style="info" %}
## Note

Direct Database Connector is available as a paid add-on. Please visit your [Billing page](https://app.xano.com/billing?mode=master) to add this to your plan.
{% endhint %}

Database Connector is a premium add-on that is available for Launch and Scale plans. Please visit your Billing page for the most up-to-date pricing for this additional feature.

You have the option to connect your Xano instance's PostgreSQL database directly with an external application or service. This can be useful if there is a platform for manipulating your database that you prefer to use over the Xano interface, creating custom backup and restore solutions, or even performing data analytics.

Use care when accessing your database directly. This type of connection removes a significant portion of normal checks and balances for data validity that using Xano directly provides.

**Proceed with caution.**

**How to Access the Database Connector**

On your instance selection screen, click the ⚙️ icon, and in the panel that opens, choose Database Connector.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252Fbva4pABZQRkdxaTFgEF8%252FCleanShot%25202023-08-16%2520at%252013.18.14.png%3Falt%3Dmedia%26token%3D3ebffa8a-ac22-48cf-9831-49d37795711e\&width=768\&dpr=4\&quality=100\&sign=b56ed3c\&sv=2)![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FLH2VNwWcmVMhISoSzAAt%252FCleanShot%25202023-08-16%2520at%252013.21.19.png%3Falt%3Dmedia%26token%3D6be56cd2-6040-4aa0-b7fe-2dd53702998a\&width=768\&dpr=4\&quality=100\&sign=af506598\&sv=2)

The panel that opens is split into two sections, Details and Settings.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FAyD90vNwvU2Olvpi9oOA%252FCleanShot%25202023-08-16%2520at%252013.22.58.png%3Falt%3Dmedia%26token%3D3a02f7da-8706-4f69-be55-a097282ffcd7\&width=768\&dpr=4\&quality=100\&sign=1659b479\&sv=2)

Details allows you to retrieve the access information for a direct database connection.

Settings allows you to enable and use an allow list, to limit direct database connections to specific IP addresses.

1. Get your database's public IP
2. Get your database credentials
3. Settings Panel
4. Add an IP address to your allow list

Clicking both of the "Get" buttons will provide us with the database IP and two sets of credentials, full-access and read-only.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FtDJ38RyZjDC9eQiwGROW%252FCleanShot%25202023-08-21%2520at%252007.47.08.png%3Falt%3Dmedia%26token%3Dd1a9a18c-c0cd-4da9-8b84-f0f629b9a90c\&width=768\&dpr=4\&quality=100\&sign=f17c368b\&sv=2)

From this panel, you can also **revoke and re-generate** your database credentials, should the need arise.

**Establishing a Database Connection (Example)**

You can use any application you'd like that is capable of connecting to a PostgreSQL database. In this example, we'll be using Navicat.

Select 'Connection' in the top-left, and fill in your credentials and the IP recieved from Xano.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FFUiRBkNbG1G0TQL97a3C%252FCleanShot%25202023-08-16%2520at%252013.39.09.png%3Falt%3Dmedia%26token%3D65e31cd1-2a78-4034-8486-645a51b3011d\&width=768\&dpr=4\&quality=100\&sign=6188df4\&sv=2)

Click 'Save' to save the connection. We can now navigate the PostgreSQL database from Xano using Navicat. We can even add / update data, run queries, etc...

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FVOIm1fX5IgwBKIL7bUtd%252FCleanShot%25202023-08-16%2520at%252013.41.35.gif%3Falt%3Dmedia%26token%3D77716497-f44c-4896-a2f2-3bda1a11f951\&width=768\&dpr=4\&quality=100\&sign=782a399b\&sv=2)
