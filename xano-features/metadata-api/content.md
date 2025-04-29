# Content

The Metadata API enables you to interact with database table content (database records). The following are various of examples of how to create, update, delete, and truncate content.

### Create Content

In this example, we will create content. The endpoint requires a workspace ID and table ID. In addition, the name of the field(s) and value(s) that you wish to create.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 18.30.40@2x.png" alt=""><figcaption></figcaption></figure>

Example response body:

```
{
  "id": 11,
  "created_at": 1681349436618,
  "name": "headphones",
  "description": "high quality listening device",
  "category_id": 3,
  "price": 99
}
```

### Update Existing Content

To update an existing record, the content ID (primary ID of the record) is also required. In this example, we will update the price from the above example to be 500

{% hint style="info" %}
The Metadata is flexible with updates: We only need to pass what we want to update. For example, if we want all the other fields to remain the same for ID 11 but want to update price then we can just pass the new value for price.
{% endhint %}

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 18.36.27@2x.png" alt=""><figcaption></figcaption></figure>

Example response body:

```
{
  "id": 11,
  "created_at": 1681349436618,
  "name": "headphones",
  "description": "high quality listening device",
  "category_id": 3,
  "price": 500
}
```

### Delete Content

Deleting content is straightforward, it requires the content ID, table ID, and workspace ID.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 18.37.59.png" alt=""><figcaption></figcaption></figure>

The response will be null since we are just deleting a record.

### Truncate Content

Truncate content will clear all the content of a table. You can optionally reset the primary key back to 1 for the table.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 18.41.30.png" alt=""><figcaption></figcaption></figure>

The response will be null since we are truncating the table.

{% hint style="danger" %}
This action cannot be done and will result in the loss of content (records).
{% endhint %}

### Search and Browse Content

To see examples of getting content via browse and search please visit the next page:

{% content-ref url="search.md" %}
[search.md](search.md)
{% endcontent-ref %}
