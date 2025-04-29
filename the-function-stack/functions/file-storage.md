# File Storage

### Read more about how file management works in Xano

{% content-ref url="../../file-storage/file-storage-in-xano.md" %}
[file-storage-in-xano.md](../../file-storage/file-storage-in-xano.md)
{% endcontent-ref %}

## The Content Upload Flow <a href="#the-content-upload-flow" id="the-content-upload-flow"></a>

When working with files in Xano, they can exist in a few different states.

* **File Resource**
  * The file resource can be thought of as a reference to your raw file data. It is a base64 encoded string that represents the file during execution, enabling you to pass the data through variables and functions that handle content management with ease.
* **Raw File Data**
  * When necessary, you do also have the ability to turn your file resource into raw file data, and manipulate it inside of the function stack when appropriate, such as a CSV file.
* **Metadata**
  * While the metadata is not a representation of the file data itself, the metadata is necessary when the file needs to be referenced inside of a database table. The tables do not store the files themselves, but hold onto the metadata, so that when the record is retrieved, you can also retrieve the file data, or deliver a link to the file.

Files in Xano always start with a **file resource**. Here's what a typical flow looks like. In this example, we'll be adding a file to our database table.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252Fz1c3AmlgI9FmAjPWiuO7%252FCleanShot%25202024-02-23%2520at%252015.21.05.png%3Falt%3Dmedia%26token%3D66a1d3d0-8be2-45d1-bc9d-6e4273ad2981\&width=768\&dpr=4\&quality=100\&sign=474df55b\&sv=2)

1. Files in a function stack always start with a **file resource.** The file resource can come via a **file resource input**, or by using a **Create File Resource** function in the function stack itself (such as if the file comes from an external API request).
2. After we have our file resource (in this case, our File Resource input), we need to generate **metadata** for that file in preparation to store it in our database table.
3. Finally, once we have our **metadata**, we can write it to our database table, adding the metadata to the appropriate field in the record.

This is the simplest and most typical scenario when working with files in Xano. Following this flow will allow you to ingest files through your API and store them in your database. You can then read the metadata from the table and use the URL from there to deliver those files back to your front-end.

## Input, Field Types, and Functions <a href="#input-field-types-and-functions" id="input-field-types-and-functions"></a>

### The File Resource Input <a href="#the-file-resource-input" id="the-file-resource-input"></a>

Your content upload function stacks should always start with a **file resource input**, if your users are uploading files through your application. You can then utilize the file resource input in future functions, such as **metadata generation,** to store the file in your database or return a URL to the file.

### Field Types <a href="#field-types" id="field-types"></a>

Xano supports several different field types in the database related to content upload.

* **Image** - For storing images
* **Video** - For storing video
* **Audio** - For storing audio
* **Attachment** - For storing anything else

### Functions <a href="#functions" id="functions"></a>

The Content Upload Functions are:

* **Create Image Metadata** - Creates image metadata from a file resource so that it can be formatted properly to be stored in Xano.
* **Create Video Metadata** - Creates video metadata from a file resource so that it can be formatted properly to be stored in Xano.
* **Create Audio Metadata** - Creates auto metadata from a file resource so that it can be formatted properly to be stored in Xano
* **Create Attachment Metadata** - Creates attachment metadata from a file resource so that it can be formatted properly to be stored in Xano.
* **Create File Resource** - This functions is able to create a file resource in the function stack from a variable. Typically, you will use a file resource as an input. However, there are certain use cases, for example, where you may hit an external API which is providing you with a raw image or file. In this event, you will want to first use this function to create a file resource then use one of the create metadata functions.
* **Delete File Resource** - This function will permanently delete files stored in your Xano file storage. You'll usually pair this with a database operation like Get Record / Query All Records, or you can delete a file created earlier in your function stack as long as one of the Metadata functions have been executed, as the Delete File Resource function requires you to specify the path to the file.\
  **Files are not recoverable. Proceed with caution**.
* **Zip: Create File Resource** - Creates a new, empty zip file that you can add files to in your function stack
* **Zip: Add File Resource** - Used to add additional files into an existing zip file
* **Zip: Remove File Resource** - Used to remove files from an existing zip file
* **Zip: Extract Zip File Resource** - Used to extract a zip file and generate separate file resources for each file extracted
* **Zip: View Contents** - Show details about the files contained inside of a zip file

## Serving File Downloads

There are a couple of different ways you can serve downloads of files, depending on your use case.

{% stepper %}
{% step %}
### Provide the URL for your frontend to process.

When you use one of the **Create Metadata** steps to store the file in your Xano files library, it returns a **path** key which contains a path to the file.

Returning a complete URL requires prepending this path with the URL to your Xano instance.

If our metadata looks like this...

```json
{
    "access":"public",
    "path":"/vault/T3q1DKy7/MA_gz1v6HaNQnLEf6xZqVtrOVII/1Rl7QA../form_submission_1741703680742.pdf",
    "name":"form_submission_1741703680742.pdf",
    "type":"pdf",
    "size":3247192,
    "mime":"application/pdf",
    "meta":{
        "validated":false
        }
    }
```

...our full URL would look like this:

```
https://my-xano-instance.xano.io/vault/T3q1DKy7/MA_gz1v6HaNQnLEf6xZqVtrOVII/1Rl7QA../form_submission_1741703680742.pdf
```
{% endstep %}

{% step %}
### Serve the raw file contents for direct download.

If you want an API call to immediately initiate a file download, add the following headers to your function stack using the [**HTTP Header**](utility-functions.md#http-header) function.

1. `Content-Disposition: attachment; filename="replaceme"`
2. `Content-Type: application/octet-stream`

These headers will tell any browser accessing the API that we're serving a direct download. Just make sure to change "replaceme" to the actual filename you are serving.

Add a **Get File Resource Data** function so we have the raw file data to be delivered.

Finally, in your response, return the .`data` path from the output of **Get File Resource Data**.

Your function stack should look something like this:

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-11 at 09.39.47.png" alt=""><figcaption></figcaption></figure>

To ensure it's working as expected, when you run it in Xano, you should see a **Download** button available in the Run panel.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-03-11 at 09.40.41.png" alt="" width="450"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

## Private File Storage <a href="#private-file-storage" id="private-file-storage"></a>

Private file storage is available as a premium add-on for our Launch plans, or included with **Scale** or HIPAA compliance.

All files stored as private files are only accessible through on-demand time sensitive URL generation. This means that all files in your Private Storage are inaccessible until you generate a new URL in your function stack.

To work with private file storage, there are two key components to understand: **private file database fields** and the **Private File: Sign URL function.**

### **Private File Database Field**

To store files in your private files library and have them accessible from your function stacks, you'll need to use a database field that is enabled for private file storage. You can enable this for any of the current file field types. Keep in mind that the file access is defined per field, which means that you can not store both public and private files in the same field.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F1jnsdLtk7EJfX236q7cm%252FCleanShot%25202023-10-25%2520at%252008.19.10.png%3Falt%3Dmedia%26token%3Dc3045abe-9f28-439a-8a93-bb50833eaedb\&width=768\&dpr=4\&quality=100\&sign=4a665ef9\&sv=2)

When private files are enabled for a file storage field, a lock icon is displayed in the field name. You will also notice that private files do not display previews from the database view; this is by design, as the files are not accessible until a new URL is generated.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FC3DZqLTrrdZKiEjRiMfw%252FCleanShot%25202023-10-25%2520at%252008.21.58.png%3Falt%3Dmedia%26token%3Dc9e48de6-ef90-4322-9431-11413c0cbbf9\&width=768\&dpr=4\&quality=100\&sign=a87052e2\&sv=2)

### **Private File: Sign URL function**

To generate a signed URL that enables a private file to be accessible, you first need to retrieve the path of the file, which is stored in the database record. In this example, we have queried our files table and this is the expected return for a private image. The main difference here is that on public files, a URL is returned. For private files, no URL is provided.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F1zYeOYy1aD7N2vbqrnY0%252FCleanShot%25202023-10-25%2520at%252013.59.21.png%3Falt%3Dmedia%26token%3D9f200845-d011-4141-97ac-c2d3b38b3007\&width=768\&dpr=4\&quality=100\&sign=a61f96db\&sv=2)

We can then leverage the **Private File: Sign URL** function to generate a publicly accessible link to the file. Provide the path as offered from the database record, a TTL (how long in seconds the link should be valid for), and finally a return variable to contain the output of the function

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F4cCINjbuvGFMo6fyslVN%252FCleanShot%25202023-10-25%2520at%252014.01.35.png%3Falt%3Dmedia%26token%3D1099b153-0bdf-4e16-8b34-78c35db9f9f9\&width=768\&dpr=4\&quality=100\&sign=a38c5ef\&sv=2)

When we run this function, we are returned our new signed URL.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FhROeGM5xd0MulT2W2WrX%252FCleanShot%25202023-10-25%2520at%252014.16.58.png%3Falt%3Dmedia%26token%3Dd854ef27-56f3-4d9a-9324-cd26cfe54cf0\&width=768\&dpr=4\&quality=100\&sign=13e65d86\&sv=2)

## Zip Management

{% embed url="https://www.youtube.com/watch?v=XORZu0GGHzY" %}

### Viewing Zip File Contents <a href="#viewing-zip-file-contents" id="viewing-zip-file-contents"></a>

In this example, all we want to do is upload a zip file and review its contents in our function stack.

We've added our file resource input to ingest the file, and then utilize the **Zip: View Contents** function, targeting our file resource input. We can also provide a password to this function if our zip file requires one to open.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FFKJumiF8eIMH2duura5d%252FCleanShot%25202024-02-26%2520at%252010.27.15.png%3Falt%3Dmedia%26token%3D258b31d3-a080-4446-b8a7-3d0a40e9244b\&width=768\&dpr=4\&quality=100\&sign=df1c4289\&sv=2)

1. **Zip: View Contents** - Returns the contents of our zip file to a variable

### Extracting a Zip File <a href="#extracting-a-zip-file" id="extracting-a-zip-file"></a>

In this example, our users will be uploading a zip file. We then want to extract all of those files from the zip file in order to add those files individually to our database.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FV0G3erkpYaeykhdcoi7X%252FCleanShot%25202024-02-26%2520at%252010.41.23.png%3Falt%3Dmedia%26token%3D42ddcad6-5e97-48d8-ba10-beabe809c01d\&width=768\&dpr=4\&quality=100\&sign=4ae4080d\&sv=2)

1. **Create Attachment Metadata** - Creates metadata for the uploaded zip file so we can get the filename
2. **Zip: Extract Zip File Resource** - Extracts the zip file and returns individual file resources for each file\
   &#x20;![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F19UWvgCZaRim9XxP6qrT%252FCleanShot%25202024-02-26%2520at%252010.43.50.png%3Falt%3Dmedia%26token%3D89962564-22ee-440b-96d1-10440b3c1d55\&width=300\&dpr=4\&quality=100\&sign=31f4395c\&sv=2)
3. **Create Variable** - Creates an empty array to store our individual files metadata
4. **For Each Loop** - Loops against the array of file resources created in step 2
   1. **Conditional** - Checks for junk files generated by Mac OS and skips them. This step is optional.
      1. **Create Attachment** - Creates metadata for the file resource that the loop is currently iterating through
      2. **Array: Add to End** - Adds the generated metadata to our metadata array established in step 3
5. **Add Record** - Adds our metadata to the database
6. **Delete File** - Deletes the zip file. This is only necessary if you generate metadata for it as we did in step 1.

### Adding to a zip file <a href="#adding-to-a-zip-file" id="adding-to-a-zip-file"></a>

In this example, our users are uploading a zip file, and we want to add another file to that same zip file. We have two file resource inputs: one is for the zip file, and one is for the new file to add.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FXvjBen1Q9x2wgjsnEy91%252FCleanShot%25202024-02-26%2520at%252012.17.42.png%3Falt%3Dmedia%26token%3Db64e0142-5cfd-4bb8-9895-e36ba9dfede5\&width=768\&dpr=4\&quality=100\&sign=f771f851\&sv=2)

1. **Zip: Add File Resource** - Adds the new file into the existing zip file
2. **Zip: View Contents** - Allows us to view the contents of the updated zip file

### Removing from a zip file <a href="#removing-from-a-zip-file" id="removing-from-a-zip-file"></a>

In this example, our users are uploading a zip file, as well as specifying a file to remove, and we want to remove that file from the zip file. We have two inputs: a file resource input for the zip file, and a text input for the file name to remove.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F04EDrdbJ3fhV322pBgbV%252FCleanShot%25202024-02-26%2520at%252012.19.42.png%3Falt%3Dmedia%26token%3D437af8a1-204d-49c3-be5c-5c5906929701\&width=768\&dpr=4\&quality=100\&sign=3631fdad\&sv=2)

1. **Zip: Delete File Resource** - Removes the file matching the filename from the existing zip file
2. **Zip: View Contents** - Allows us to view the contents of the updated zip file

### Creating a zip file from scratch <a href="#creating-a-zip-file-from-scratch" id="creating-a-zip-file-from-scratch"></a>

{% hint style="info" %}
See [#serving-file-downloads](file-storage.md#serving-file-downloads "mention") to learn how to provide a download of a created ZIP file.
{% endhint %}

In this example, our users are uploading multiple files, and we want to store them inside of a zip file.

**From multiple file resource inputs**

In this scenario, we have multiple file resource inputs for each incoming file.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F4lFoUSBztI8MtAFeoZBt%252FCleanShot%25202024-02-26%2520at%252012.23.35.png%3Falt%3Dmedia%26token%3D2ea9018c-beaa-4114-a551-2e5bb78a073b\&width=768\&dpr=4\&quality=100\&sign=e998af89\&sv=2)

1. **Zip: Create File Resource** - Creates our zip file that we can add to in the rest of the function stack
2. **Zip: Add File Resource** - Adds the data from file1 into our zip file
3. **Zip: Add File Resource** - Adds the data from file2 into our zip file
4. **Zip: View Contents** - Allows us to review the zip file contents after completion

**From an array of files via a single file resource input**

In this scenario, we have a single file resource input, formatted as a list. This is good if you need to dynamically determine how many files your API is ingesting.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FzLUVKuHFlUZvrOOez05P%252FCleanShot%25202024-02-26%2520at%252012.27.37.png%3Falt%3Dmedia%26token%3D0177f337-79b4-4996-9d11-71a6c0491ff5\&width=768\&dpr=4\&quality=100\&sign=37153687\&sv=2)

1. **Zip: Create File Resource** - Creates our zip file that we can add to in the rest of the function stack
2. **For Each Loop** - Loops against our list file resource input
   1. **Zip: Add File Resource** - Adds the file the loop is currently iterating through to our zip file established in step 1
3. **Zip: View Contents** - Allows us to review the zip file contents after completion

### A note about encryption <a href="#a-note-about-encryption" id="a-note-about-encryption"></a>

Xano supports creating and working with encrypted zip files. In the zip functions available, you'll notice one or both of the following fields:

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FCg3h9582DJttDEJTTD4J%252FCleanShot%25202024-02-26%2520at%252012.29.58.png%3Falt%3Dmedia%26token%3D94fdfe8a-10ed-45fc-ad13-9da567549196\&width=768\&dpr=4\&quality=100\&sign=aff7dd1e\&sv=2)

The **password** field is to set the password you want applied to the zip file.

The **password\_encryption** field is available for you to set the encryption method applied to the zip file upon creation. The following encryption methods are available:

* **Standard** - This is the most compatible form of encryption (Traditional PKWARE encryption). This is required if you need to be able to extract your zip files using Windows' native zip extraction.
* **AES-128**
* **AES-256**
* **AES-512**



