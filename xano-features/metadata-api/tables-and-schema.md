# Tables and Schema

The following are various examples of how to leverage the Metadata API to create and modify database tables including the schema and indexes included within them.

{% embed url="https://youtu.be/jsFTr4ihUYY" %}

### Get Workspaces

Browse the workspaces of the instance. This API endpoint does not require any parameters. Retrieving the workspaces gives you information on the workspace name and ID. The workspace ID is particularly important for use in other Metadata API endpoints.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 14.54.55@2x.png" alt=""><figcaption></figcaption></figure>

Example response body:

```
[
  {
    "id": 1,
    "name": "my workspace 1",
    "description": ""
  },
  {
    "id": 3,
    "name": "test",
    "description": ""
  },
  {
    "id": 2,
    "name": "to do app",
    "description": "my to do app example"
  }
]
```

### Get Tables of a Workspace

Browse workspace tables. This API endpoint requires a workspace ID and will provide various information about each database table in a workspace, including database table ID, which is needed in various Metadata API endpoints.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 15.19.51.png" alt=""><figcaption></figcaption></figure>

Example response body:

```
[
  {
    "id": 7,
    "created_at": "2023-04-12 22:00:38+0000",
    "updated_at": "2023-04-12 22:00:42+0000",
    "name": "category",
    "description": "",
    "guid": "yu2eB8E0dSEtL6MbBPzzJUM06gA",
    "auth": false
  },
  {
    "id": 8,
    "created_at": "2023-04-12 22:00:51+0000",
    "updated_at": "2023-04-12 22:01:07+0000",
    "name": "items",
    "description": "",
    "guid": "eP9O-rD-7sGKpbLOEhdED6YGrmA",
    "auth": false
  },
  {
    "id": 1,
    "created_at": "2022-03-24 20:20:26+0000",
    "updated_at": "2022-03-24 20:20:26+0000",
    "name": "user",
    "description": "",
    "guid": "nTOiqqb31ecz1Te6v_3YMkfp5xc",
    "auth": true
  }
]
```

### Create Table and Add Schema One by One

First, create a new table in the desired workspace. The default request values suffice. In this example, first, we will create a table and then add schema individually. The Metadata API is capable of adding schema in bulk but that will be covered in another example.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 15.40.34@2x.png" alt=""><figcaption></figcaption></figure>

Example response body:

```
{
  "id": 9
}
```

Taking the newly created database table ID, we can add schema 1 by 1 to the table.

1. A text field called name.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 16.05.20@2x.png" alt=""><figcaption></figcaption></figure>

Example response body:

```
{
  "name": "name"
}
```

Next, let's add an integer field called score with a default value of 30

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 16.15.51@2x.png" alt=""><figcaption></figcaption></figure>

As we execute these Metadata API calls, our new table in Xano is being created along with the new schema, one by one.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 16.24.07.png" alt=""><figcaption></figcaption></figure>

### Create an Index

The Metadata API gives control over indexes on database tables. In this example, let's create a Unique Index on the name field of new table 123.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 16.27.18.png" alt=""><figcaption></figcaption></figure>

Example response body:

```
{
  "id": "baa524c4"
}
```

The API responds with the ID of the index. In Xano, we can see the index has been created:

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 16.27.52.png" alt=""><figcaption></figcaption></figure>

### Create Table with Schema and an Index in One Call

In this example, we will create a new database table along with schema and an index in the same API call. The Metadata API is flexible enough to accommodate this method.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 17.10.58@2x.png" alt=""><figcaption></figcaption></figure>

Here's the example request body:

```
{
  "name": "new stuff",
  "description": "",
  "auth": null,
  "guid": null,
  "schema": [
    {
      "name": "id",
      "type": "int",
      "description": "",
      "nullable": false,
      "default": "",
      "required": true,
      "access": "public",
      "style": "single"
    },
    {
      "name": "created_at",
      "type": "timestamp",
      "description": "",
      "nullable": false,
      "default": "",
      "required": true,
      "access": "public",
      "style": "single"
    },
    {
      "name": "name",
      "type": "text",
      "description": "",
      "nullable": false,
      "default": "",
      "required": true,
      "access": "public",
      "style": "single"
    }
  ],
  "index":[
    {
      "type": "btree",
      "fields": [
        {
          "name": "name",
          "op": "desc"
        }
      ]
    }
  ]
}
```

This creates a new table called "new stuff" with three fields: id, created\_at, and name with an index on the name field.

{% hint style="info" %}
For defining schema, the Metadata API needs a minimum of "name" and "type" but the other fields aren't required. If you are defining schema during table creation, the first field must be the ID field.

For Request body examples of schema and index, check out the PUT examples in Swagger for table/schema and table/index.&#x20;
{% endhint %}

### Browse Content

Browse table content is a simple method of getting content (database records) in a database table.  It requires a workspace ID and table ID, while paging is optional.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 17.29.24.png" alt=""><figcaption></figcaption></figure>

Example response body:

```
{
  "items": [
    {
      "id": 1,
      "created_at": 1681336868222,
      "name": "Basketball",
      "description": "round ball to shoot hoops",
      "category_id": 1
    },
    {
      "id": 2,
      "created_at": 1681336868456,
      "name": "French Press",
      "description": "Make delicious coffee with this",
      "category_id": 2
    },
    {
      "id": 3,
      "created_at": 1681336868658,
      "name": "Bluetooth Speaker",
      "description": "Portable music player",
      "category_id": 3
    },
    {
      "id": 4,
      "created_at": 1681336868931,
      "name": "Camera",
      "description": "Take photos with this",
      "category_id": 3
    }
  ],
  "itemsReceived": 4,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 4,
  "pageTotal": 1
}
```

###

