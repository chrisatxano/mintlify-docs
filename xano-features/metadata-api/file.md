# File

The Metadata API allows you to interact with the files of a given workspace. You can upload, get, delete, and bulk delete files.

{% embed url="https://youtu.be/JeKnXnGTRJU" %}

### Upload

Upload a file to a workspace.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-21 at 11.04.25.png" alt=""><figcaption></figcaption></figure>

* workspace\_id - required to determine which workspace the file should live.
* content - the file that is being uploaded.
* type - optionally enforce a file type: image, video, or audio. An attachment is the default selection.

Example Response Body:

```
{
  "created_at": "2023-04-21T18:05:57.000000Z",
  "id": 16,
  "name": "Pizza.jpg",
  "size": 3724142,
  "type": "image",
  "mime": "image/jpeg",
  "path": "/vault/-TJh6gvN/GgwIFTsoTTIxlacoz01j1xwGY3w/U0y4tw../Pizza.jpg"
}
```

#### Upload a File then Add it as Content to a Table

Taking part of the response body from the previous example, we can add the file to a database table.

```
// required metadata object from the previous example (created_at and id not needed):

{
  "name": "Pizza.jpg",
  "size": 3724142,
  "type": "image",
  "mime": "image/jpeg",
  "path": "/vault/-TJh6gvN/GgwIFTsoTTIxlacoz01j1xwGY3w/U0y4tw../Pizza.jpg"
}
```

We can take the metadata object and use it for creating content of an image field.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-21 at 11.12.59.png" alt=""><figcaption><p>In this example, we take part of the object from the Upload File endpoint and use it to create content that includes an image field.</p></figcaption></figure>
