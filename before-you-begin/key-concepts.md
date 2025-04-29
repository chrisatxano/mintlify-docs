---
icon: key
description: >-
  Get a quick primer on the key concepts and terminology that we use throughout
  the product and documentation to get you started quickly.
---

# Key Concepts

***

### :desktop: Instance

{% embed url="https://youtu.be/nBW9XuzKBAE" %}



Your Xano instance is the heart of everything you do in Xano. An **instance** is a dedicated server that we manage for you and it contains all of your Xano data, including APIs, databases, user data, and more.

On all of our paid plans, each instance has its own dedicated resources, is always available, and completely isolated from other Xano users. This means that even if, in the rare occurrence that one user experiences an issue with their own Xano backend, it won't impact anybody else.

On our free plan, you are on a shared instance with other Xano users.

***

### :open\_file\_folder: Workspace

{% embed url="https://youtu.be/lCIjFBVJ8HM" %}

In your Xano instance, you can have multiple **workspaces**. Think of a workspace as a separate container for each project you're building in Xano. Your workspaces are completely isolated from each other, but all share the same compute resources provided by your instance.

***

### &#x20;🧠 Backend

{% embed url="https://youtu.be/igzPKoqYpR0" %}

Think of the backend as the brains of a website or app. It's all the behind-the-scenes action that users don't see. When you're browsing an online store, the backend is figuring out what products to show you, keeping track of your shopping cart, and making sure your payment goes through. It's like the engine room of a ship - not glamorous, but absolutely crucial.

***

### 📱 Frontend

{% embed url="https://youtu.be/ddwSQ2d5rng" %}

The frontend is everything you see and interact with on a website or app. It's the pretty face that greets you when you land on a page. This includes the layout, colors, buttons, and forms you fill out. A good frontend makes using a website feel smooth and intuitive, like a well-designed cockpit in an airplane. It's all about creating a great user experience.

***

### 🗄️ Database

{% embed url="https://youtu.be/oTsGKqo_py4" %}

A database is essentially a digital warehouse for information. It's where websites and apps store all their data in an organized way. Need to look up a customer's order history? That's stored in a database. Want to see all products under $50? The database has that info too. It's like a super-efficient librarian who can find any piece of information in milliseconds.

***

### 🔌 API

{% embed url="https://youtu.be/ROCHqKMwtBM" %}

{% include "../.gitbook/includes/definition-of-an-api.md" %}

***

## 🏷️ Variables

Variables are like containers or labels that store information you want to use later in a workflow. Think of them as named boxes where you can keep different types of items, such as numbers, words, or lists. You give each box a name so you can easily find and use the information it holds whenever you need it in your project. This makes it simple to update or change the data without needing to rewrite everything.

Variables are temporary and exist only while a workflow is running, used for storing information you need to access quickly, whereas values in a database are like records in a filing cabinet, stored permanently until you decide to update or delete them, accessible across various workflows and sessions. This makes databases ideal for managing large sets of data over time, and variables more appropriate for temporary data handling.

***

### 🗃️ JSON

{% embed url="https://youtu.be/ouVQFne9IpI" %}

JSON is a handy way of formatting data that's easy for both humans and computers to understand. JSON organizes information into simple key-value pairs, kind of like a really well-structured grocery list. It's lightweight and flexible, which is why developers love using it to pass data between servers and web applications.

For an example of how JSON can supercharge your data structure, take this example of a hand-written grocery list compared to a JSON equivalent.

{% tabs %}
{% tab title="Handwritten List" %}
<figure><img src="../.gitbook/assets/CleanShot 2024-09-20 at 10.45.42.png" alt="" width="340"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="JSON" %}
```json
[
  {
    "category": "Dairy",
    "items": [
      "Eggs",
      "Milk",
      "Cheddar cheese"
    ]
  },
  {
    "category": "Bakery",
    "items": [
      "Bread"
    ]
  },
  {
    "category": "Meat",
    "items": [
      "Chicken breast",
      "Ground beef"
    ]
  },
  {
    "category": "Household",
    "items": [
      "Candles",
      "Laundry detergent"
    ]
  },
  {
    "category": "Grains",
    "items": [
      "Rice"
    ]
  },
  {
    "category": "Supplements",
    "items": [
      "Protein powder"
    ]
  },
  {
    "category": "Produce",
    "items": [
      "Grapes"
    ]
  }
]
```
{% endtab %}
{% endtabs %}



JSON follows a structure of `key: value` pairs. The key typically defines what the value represents, and the value is the actual value itself.

While it may seem similar, **JSON is not code**. It is just a standard way to structure data. For a real-world comparison, maybe you have a favorite news site or blog that you visit daily. You are used to the format they provide so the information is easily digestible. Now, imagine if every day, they decided to follow a different, unorganized structure instead. This is why data standardization is important, and JSON is a very effective way of achieving this.

#### 📄 Objects

An object represents the whole of a thing, such as a person, place, vehicle, form submission -- the possibilities are endless and fully dependent on what you are building. A JSON object can have multiple keys and values inside.

Here is an example of a JSON object that represents user data.

```json
{
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "isStudent": false
    }
```

As you can see, we have our **keys**, such as `name`, `age`, and `city`, as well as our values, which are the actual data that belongs to this user.

#### 📑 Arrays

JSON can also represent lists of items, like the example below. It looks almost exactly the same, but now we have multiple people inside of an **array**, or list, denoted by square brackets.

```json
[
  {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "isStudent": false
  },
  {
    "name": "Jane Smith",
    "age": 25,
    "city": "San Francisco",
    "isStudent": true
  },
  {
    "name": "Bob Johnson",
    "age": 35,
    "city": "Chicago",
    "isStudent": false
  }
]
```

#### 🪺 Nested Data

Values don't just have to be single items, such as a person's name or email. You can also supply other objects or arrays for your values. In the below example, we've added an interests key and supplied an array of text strings for the value.

```json
  {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "isStudent": false,
    "interests": ["tennis",
                  "visual development",
                  "pizza"]
  }
```

### ℹ️ JSON Data Types

You may have noticed a few mentions of things like integers or strings when learning about JSON. It is important to know what types of data are valid representations inside of a JSON object. One of the most important things to remember when working with JSON is that quotation marks are incredibly important and can be the difference between something working or falling apart.

🔤 **Strings** are surrounded by "quotation marks" and are just plain text.

```json
  {
    "name": "John Doe"
  }
```

🔢 **Integers** are numbers that are not decimals. Notice how we do not have quotation marks around `1994` in the example below. If we used `"1994"` instead, this would become a string.

```json
  {
    "year": 1994
  }
```

🔢 **Decimals** are numbers that contain a decimal point.

```json
  {
    "price": 9.99
  }
```

✅ **Booleans** are true or false values.

```json
    "exists": true
```

⛔ **Null** is a special data type that represents nothing in situations where you need to specify that nothing is provided.

```json
    "phone": null
```

📑 **Arrays** are lists of things. These could be any other valid JSON data type. You could even have an array of arrays if you wanted.

```json
[
    "red",
    "blue",
    "green"
    ]
```

📄 **Objects** are collections of key-value pairs enclosed in curly braces. Keys are always strings, but values can be any valid JSON data type.

```json
{
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "isStudent": false
  }
```
