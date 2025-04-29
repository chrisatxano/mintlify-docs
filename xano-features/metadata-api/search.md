# Search

This section is broken down into Browse Content and Search. [Browse Content](search.md#browse-content) is a simple method of getting or reading the content of a database table. It can be optionally combined with paging.

[Search](search.md#search) is an advanced method of filtering, sorting, and paging database content. It is flexible and powerful and enables you to return content based on the parameters you define.

{% hint style="info" %}
Please note that the Metadata APIs for browsing content do not react to API Access settings. All fields will be returned regardless of this setting.
{% endhint %}

## Browse Content

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

## Search

Search via the Metadata API is powerful and flexible to return the exact database content you are searching for.&#x20;

#### Search where ID = 10

In this example, we will search the Items table where ID = 10

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 17.45.22@2x.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Search can be done as a single object or array if there is only one search parameter. If there are multiple parameters then it must be an array.\


You can pass just what you want in the request body. For example, if all we want to do is search then we just need to pass search to the body.
{% endhint %}

With paging, sort, and search as an array.

```
{
  "page": 1,
  "per_page": 50,
  "sort": {
    "id": "desc"
  },
  "search": [{
   "id": 10
}]
}
```

With paging, sort, and search as a single object.

```
{
  "page": 1,
  "per_page": 50,
  "sort": {
    "id": "desc"
  },
  "search": {
   "id": 10
}
}
```

With just search, as an array.

```
{
  "search": [{
   "id": 10
}]
}
```

With just search, as a single object.

```
{
  "search": {
   "id": 10
}
}
```

For this example, all of the above are acceptable for the request body.&#x20;

Example response body:

```
{
  "items": [
    {
      "id": 10,
      "created_at": 1681346185431,
      "name": "Air Fryer",
      "description": "A new way to fry food without all the grease and oil",
      "category_id": 2,
      "price": 75
    }
  ],
  "itemsReceived": 1,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 1,
  "pageTotal": 1
}
```

#### Search where Price > 30 and Price < 70

In this example, we are searching for content where price is > 30 and price is < 70.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 17.57.16@2x.png" alt=""><figcaption></figcaption></figure>

Example request body:

```
{
  "search": [{
   "price|>": 30
},
{
   "price|<": 70
}]
}
```

Example response body:

```
{
  "items": [
    {
      "id": 5,
      "created_at": 1681346183608,
      "name": "Microwave",
      "description": "Reheat leftovers quickly",
      "category_id": 2,
      "price": 40
    },
    {
      "id": 8,
      "created_at": 1681346184305,
      "name": "Blender",
      "description": "Make smoothies and more",
      "category_id": 2,
      "price": 65
    },
    {
      "id": 9,
      "created_at": 1681346184508,
      "name": "Running Shoes",
      "description": "Comfy footwear for long runs",
      "category_id": 1,
      "price": 45
    }
  ],
  "itemsReceived": 3,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 3,
  "pageTotal": 1
}
```

#### Search where Price < 30 or Price > 70

In this example, we will search for where the price is < 30 or the price is > 70

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 18.10.11@2x.png" alt=""><figcaption></figcaption></figure>

Example request body:

```
{
  "search": [
{
   "price|<": 30
},
{
   "price|>|or": 70
}
]
}
```

{% hint style="info" %}
Notice how the or is formatted after the Price is > 70 expression.
{% endhint %}

Example response body:

```
{
  "items": [
    {
      "id": 1,
      "created_at": 1681336868222,
      "name": "Basketball",
      "description": "round ball to shoot hoops",
      "category_id": 1,
      "price": 10
    },
    {
      "id": 2,
      "created_at": 1681336868456,
      "name": "French Press",
      "description": "Make delicious coffee with this",
      "category_id": 2,
      "price": 5
    },
    {
      "id": 4,
      "created_at": 1681336868931,
      "name": "Camera",
      "description": "Take photos with this",
      "category_id": 3,
      "price": 80
    },
    {
      "id": 6,
      "created_at": 1681346183823,
      "name": "Resistance Bands",
      "description": "Stretchy bands for working out",
      "category_id": 1,
      "price": 15
    },
    {
      "id": 7,
      "created_at": 1681346184107,
      "name": "Tablet",
      "description": "Browse, stream, and more with a portable tablet",
      "category_id": 3,
      "price": 120
    },
    {
      "id": 10,
      "created_at": 1681346185431,
      "name": "Air Fryer",
      "description": "A new way to fry food without all the grease and oil",
      "category_id": 2,
      "price": 75
    }
  ],
  "itemsReceived": 6,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 6,
  "pageTotal": 1
}
```

#### In and Not In

The IN and NOT IN operators are great for working with lists and can also be thought of as another version of "or" operators. In the first example, we will search where the ID is IN \[2,3,7].

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 18.15.18.png" alt=""><figcaption></figcaption></figure>

Example request body:

```
{

  "search": {
  "id|in": [2,3,7]
}
}
```

Example response body:

```
{
  "items": [
    {
      "id": 2,
      "created_at": 1681336868456,
      "name": "French Press",
      "description": "Make delicious coffee with this",
      "category_id": 2,
      "price": 5
    },
    {
      "id": 3,
      "created_at": 1681336868658,
      "name": "Bluetooth Speaker",
      "description": "Portable music player",
      "category_id": 3,
      "price": 30
    },
    {
      "id": 7,
      "created_at": 1681346184107,
      "name": "Tablet",
      "description": "Browse, stream, and more with a portable tablet",
      "category_id": 3,
      "price": 120
    }
  ],
  "itemsReceived": 3,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 3,
  "pageTotal": 1
}
```

In the second example, we will search where ID is NOT IN \[1,2,3,4,6,7,8,9]

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 18.17.43@2x.png" alt=""><figcaption></figcaption></figure>

Example request body:

```
{

  "search": {
  "id|not in": [1,2,3,4,6,7,8,9]
}
}
```

Example response body:

```
{
  "items": [
    {
      "id": 5,
      "created_at": 1681346183608,
      "name": "Microwave",
      "description": "Reheat leftovers quickly",
      "category_id": 2,
      "price": 40
    },
    {
      "id": 10,
      "created_at": 1681346185431,
      "name": "Air Fryer",
      "description": "A new way to fry food without all the grease and oil",
      "category_id": 2,
      "price": 75
    }
  ],
  "itemsReceived": 2,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 2,
  "pageTotal": 1
}
```

### Sort

Sort is flexible, like search, in the sense that it accepts a single object or an array for a single sort parameter. It also supports multiple sorts, which require an array format.

#### Single Sort

In this example, we will sort the category table by the name in ascending order.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 18.49.41@2x.png" alt=""><figcaption></figcaption></figure>

Example request body:

```
{

  "sort": {
    "name": "asc"
  }
}
```

Also acceptable:

```
{

  "sort": [{
    "name": "asc"
  }]
}
```

Example response body:

```
{
  "items": [
    {
      "id": 5,
      "created_at": 1681350452709,
      "name": "Decor",
      "rating": 3
    },
    {
      "id": 3,
      "created_at": 1681337773911,
      "name": "Electronics",
      "rating": 5
    },
    {
      "id": 2,
      "created_at": 1681337772998,
      "name": "Kitchen",
      "rating": 4
    },
    {
      "id": 4,
      "created_at": 1681350451208,
      "name": "Outdoor",
      "rating": 4
    },
    {
      "id": 1,
      "created_at": 1681337772458,
      "name": "Sports equipment",
      "rating": 4
    }
  ],
  "itemsReceived": 5,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 5,
  "pageTotal": 1
}
```

#### Multi-Sort

In this example, we will first sort the content by rating in descending order, then the name in ascending order.

<figure><img src="../../.gitbook/assets/CleanShot 2023-04-12 at 18.53.35@2x.png" alt=""><figcaption></figcaption></figure>

Example request body:

```
{

  "sort": [{
    "rating": "desc"
  },
  {
    "name": "asc"
  }
]
}
```

Example response body:

```
{
  "items": [
    {
      "id": 3,
      "created_at": 1681337773911,
      "name": "Electronics",
      "rating": 5
    },
    {
      "id": 2,
      "created_at": 1681337772998,
      "name": "Kitchen",
      "rating": 4
    },
    {
      "id": 4,
      "created_at": 1681350451208,
      "name": "Outdoor",
      "rating": 4
    },
    {
      "id": 1,
      "created_at": 1681337772458,
      "name": "Sports equipment",
      "rating": 4
    },
    {
      "id": 5,
      "created_at": 1681350452709,
      "name": "Decor",
      "rating": 3
    }
  ],
  "itemsReceived": 5,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 5,
  "pageTotal": 1
}
```
