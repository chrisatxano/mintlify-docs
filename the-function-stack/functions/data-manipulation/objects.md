# Objects

These functions are used when you need to get the properties of an objection in the function stack.

#### Examples <a href="#examples" id="examples"></a>

For each of these examples, we will create a variable called `object` with the value

```
{
   "a":"3",
   "b":"2",
   "c":"1"
}
```

## **Get Keys** <a href="#get-keys" id="get-keys"></a>

Get the property names of an object as an array.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FwJgNTmeIxiB133AiRuZY%252FCleanShot%25202023-01-18%2520at%252010.12.58%25402x.png%3Falt%3Dmedia%26token%3D77117418-bc28-43c8-8331-eb8b91c8aed9\&width=768\&dpr=4\&quality=100\&sign=a9b5d32c\&sv=2)

In the above example, the object is changed to an array

```
{
   "a",
   "b",
   "c"
}
```

## **Get Values** <a href="#get-values" id="get-values"></a>

Get the property values of an object as an array.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FUreZ83cuc4OUyJLwYGyI%252FCleanShot%25202023-01-18%2520at%252010.13.27%25402x.png%3Falt%3Dmedia%26token%3D2a1d4513-2d25-4ac0-86b0-0dc674c0365e\&width=768\&dpr=4\&quality=100\&sign=9ebee223\&sv=2)

In the above example, the object is changed to an array

```
{
   "3",
   "2",
   "1"
}
```

## **Get Entries** <a href="#get-entries" id="get-entries"></a>

Get the property entries of an object as an array

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FLxGVL2eWv2FD1DuUpmwy%252FCleanShot%25202023-01-18%2520at%252010.13.57%25402x.png%3Falt%3Dmedia%26token%3Db85fce2d-4958-4b2d-886e-6829ee8a7dc9\&width=768\&dpr=4\&quality=100\&sign=4714b398\&sv=2)

In the above example, the object is changed to an array

```
[
   {
      "key":"a",
      "value":"3"
   },
   {
      "key":"b",
      "value":"2"
   },
   {
      "key":"c",
      "value":"1"
   }
]
```

\
