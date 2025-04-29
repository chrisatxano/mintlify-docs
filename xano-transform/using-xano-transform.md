---
icon: arrow-down-up-across-line
---

# Using Xano Transform

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>❓ <mark style="color:blue;"><strong>What?</strong></mark></td><td>Get a quick overview of what Xano Transform can do</td><td></td><td><a href="using-xano-transform.md#what-is-xano-transform">#what-is-xano-transform</a></td></tr><tr><td>🤔 <mark style="color:blue;"><strong>Why?</strong></mark></td><td>Explaining the need for something like Xano Transform</td><td></td><td><a href="using-xano-transform.md#why-xano-transform">#why-xano-transform</a></td></tr><tr><td>🔍 <mark style="color:blue;"><strong>How?</strong></mark></td><td>The basics of how to utilize Xano Transform</td><td></td><td><a href="using-xano-transform.md#how-do-i-use-xano-transform">#how-do-i-use-xano-transform</a></td></tr><tr><td><mark style="color:blue;">♾️ <strong>Expression Data Type</strong></mark></td><td>Use the Expression data type to quickly build complex expressions</td><td></td><td><a href="../the-function-stack/data-types/expression.md">expression.md</a></td></tr><tr><td>📖 <mark style="color:blue;"><strong>GET Filter</strong></mark></td><td>Xano Transform's GET Filter syntax and examples</td><td></td><td><a href="using-xano-transform.md#retrieval-with-get">#retrieval-with-get</a></td></tr><tr><td><span data-gb-custom-inline data-tag="emoji" data-code="1f58c">🖌️</span> <mark style="color:blue;"><strong>SET Filter</strong></mark></td><td>Xano Transform's SET Filter syntax and examples</td><td></td><td><a href="using-xano-transform.md#transformation-with-set">#transformation-with-set</a></td></tr><tr><td>💡 <mark style="color:blue;"><strong>Examples</strong></mark></td><td>Real-world examples of Xano Transform in action, with comparisons to other methods</td><td></td><td><a href="using-xano-transform.md#examples">#examples</a></td></tr></tbody></table>

## What is Xano Transform?

The Xano Transform Engine is a new technology built by Xano that takes the traditional dot notation syntax and upgrades it to support data manipulation. This syntax is friendly to objects and arrays and supports conditional filtering using the new [Expression data type](../the-function-stack/data-types/expression.md).

Xano Transform encompasses some updates to our GET and SET filters, allowing you to use a powerful and expansive new type of filtering syntax to parse, return, and transform your data in exactly the way you need. Consider it an alternative to chaining several filters and functions together to accomplish a specific result.

***

## Why Xano Transform?

Xano is, and will always remain, a No-Code first platform. That doesn't mean that we don't want to offer you more ways to accomplish your goals in the fastest way possible. While this may feel like a leap to "traditional development" methods, at its core, Xano Transform is here to provide both traditional developers a more familiar way to work with their data, and empower the no-code audience to work faster with a specific set of easy to learn syntax.

Xano Transform also offers you an easy way to share solutions with other Xano users by just copying and pasting an expression to them. This is an incredibly helpful tool while we work behind the scenes to offer other methods of function stack portability.

***

## How do I use Xano Transform?

Xano Transform has two different operating 'modes', as an extension of our GET filter, and a separate [_expression_ data type](../the-function-stack/data-types/expression.md), which all work from utilizing a standardized syntax, outlined in this documentation.

Please note that you can use standard mathematical operators to compare values in areas where they would normally be accepted, such as >, <, ==, !=, etc...

***

## The \$$ special variable <a href="#double-dollar-sign" id="double-dollar-sign"></a>

Throughout this documentation, there will be repeated mentions of the `$$` special variable. This is our version of the standard `this` variable, which is commonly used in various programming languages and Lambda filters.  This concept is used to represent the context that is being referenced within a function/filter.

{% hint style="info" %}
In this example, \$$ represents the expression`1+2+3`
{% endhint %}

```json
(1+2+3)|transform:$$+1                   // 7
```

One common problem with the `$$/this` variable concept, is what happens when you need to reference 2 or more different versions of it?

```json
(1+2+3)|transform:$$+(1|transform:$$+1)
```

What if I wanted to reference the first `$$` in the second transform? There isn't a way to do this because the existence of the second transform has taken over the previous value of the \$$ variable. The solution tends to involve manually creating new variables and assigning them to different copies of the \$$ variable. &#x20;

Xano gets around this by having `$$` represent more than just a value - it represents the top most value of anything binded to it.

All \$$ variables are available via the following syntax. $0, $1, $2 - or $\[0], $\[1], $\[2], etc. This number keeps increasing as values are bounded to it. This means that the above example could also be written as the following:

```json
(1+2+3)|transform:$0+(1|transform:$1+1)
```

Therefore, if we needed to access the first \$$ within the 2nd transform, we could do so by referencing $\[0].

```json
(1+2+3)|transform:$$+(1|transform:$$+$0)
```

Sometimes, it is easier to reference items from the top instead of the bottom. Since Xano supports [negative indexes](broken-reference), the second item from the top is represented as `-2`. Therefore, we could also use the following syntax using the array notation:

```json
(1+2+3)|transform:$$+(1|transform:$$+$[-2])
```

## Retrieval with GET

{% embed url="https://youtu.be/O-eDey79cWo" %}

#### Example Data Payload

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "v": 10,
  "items": [
    {
      "id": 1,
      "name": "s1",
      "score": 100,
      "tags": [
         {"tag":"beta","weight":5},
	 {"tag":"test","weight":50}
      ]
    },
    {
      "id": 2,
      "name": "x9",
      "score": 87,
      "tags": [
        {"tag":"abc","weight":10},
	{"tag":"def","weight":90}
      ]
    }
  ]
}
</code></pre>

| Syntax                 | Result                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| v                      | <pre class="language-json"><code class="lang-json">10
</code></pre>                                                                                                                                                                                                                                                                                                                         |
| items                  | <pre class="language-json"><code class="lang-json">[
    {
      "id": 1,
      "name": "s1",
      "score": 100,
      "tags": [
         {"tag":"beta","weight":5},
	 {"tag":"test","weight":50}
      ]
    },
    {
      "id": 2,
      "name": "x9",
      "score": 87,
      "tags": [
        {"tag":"abc","weight":10},
	{"tag":"def","weight":90}
      ]
    }
  ]
</code></pre> |
| items\[0]              | <pre class="language-json"><code class="lang-json">{
  "id": 1,
  "name": "s1",
  "score": 100,
  "tags": [
    {"tag":"beta","weight":5},
    {"tag":"test","weight":50}
  ]
}
</code></pre>                                                                                                                                                                                               |
| items\[0].id           | <pre class="language-json"><code class="lang-json">1
</code></pre>                                                                                                                                                                                                                                                                                                                          |
| items\[0].tags\[0]     | <pre class="language-json"><code class="lang-json">{"tag":"beta","weight":5}
</code></pre>                                                                                                                                                                                                                                                                                                  |
| items\[0].tags\[0].tag | <pre class="language-json"><code class="lang-json">"beta"
</code></pre>                                                                                                                                                                                                                                                                                                                     |

### Array Retrieval

| Syntax         | Result                                                                                                                                                                                   |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| items.id       | <pre class="language-json"><code class="lang-json">[1,2]
</code></pre>                                                                                                                   |
| items.tags     | <pre class="language-json"><code class="lang-json">[
  {"tag":"beta","weight":5},
  {"tag":"test","weight":50},
  {"tag":"abc","weight":10},
  {"tag":"def","weight":90}
]
</code></pre> |
| items.tags.tag | <pre class="language-json"><code class="lang-json">["beta","test","abc","def"]
</code></pre>                                                                                             |

### Conditional Retrieval

Conditional retrieval is made possible by using the expression syntax within the array brackets of an item.

The `$$` special variable is used to represent the current context of the iterated item of the array.

As seen below, this syntax is supported across multiple levels for deeply nested arrays.

| Syntax                                       | Result                                                                                                                                                                                        |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| items\[\$$.id > 1]                           | <pre class="language-json"><code class="lang-json">[{
  "id": 2,
  "name": "x9",
  "score": 87,
  "tags": [
    {"tag":"abc","weight":10},
    {"tag":"def","weight":90}
  ]
}]
</code></pre> |
| items\[\$$.id > 1].id                        | <pre class="language-json"><code class="lang-json">[2]
</code></pre>                                                                                                                          |
| items\[\$$.id > 1].tags.tag                  | <pre class="language-json"><code class="lang-json">["abc","def"]
</code></pre>                                                                                                                |
| items\[\$$.id > 1].tags\[\$$.weight>=90].tag | <pre class="language-json"><code class="lang-json">["def"]
</code></pre>                                                                                                                      |

### Automatic Anchoring

Sometimes you may need to reference something outside of the `$$` special variable. For example, you may want to conditionally select something based on a value that is located in the original root of the object.

This type of reference is supported through automatic anchoring. Each item element of the breadcrumb hierarchy is numerically indexed through `$0`, `$1`, `$2`, `$N` variables.

#### Example: items\[\$$.id > 1].tags\[\$$.weight>=90].tag

{% hint style="info" %}
$2 and $4 have multiple values since they represent an array iteration. The example below is just showing the snapshot of one iteration of their value.
{% endhint %}

| Special Variable | Result                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $0               | <pre class="language-json"><code class="lang-json">{
  "v": 10,
  "items": [
    {
      "id": 1,
      "name": "s1",
      "score": 100,
      "tags": [
         {"tag":"beta","weight":5},
	 {"tag":"test","weight":50}
      ]
    },
    {
      "id": 2,
      "name": "x9",
      "score": 87,
      "tags": [
        {"tag":"abc","weight":10},
	{"tag":"def","weight":90}
      ]
    }
  ]
}
</code></pre> |
| $1               | <pre class="language-json"><code class="lang-json">[
  {
    "id": 1,
    "name": "s1",
    "score": 100,
    "tags": [
      {"tag":"beta","weight":5},
      {"tag":"test","weight":50}
    ]
  },
  {
    "id": 2,
    "name": "x9",
    "score": 87,
    "tags": [
      {"tag":"abc","weight":10},
      {"tag":"def","weight":90}
    ]
  }
]
</code></pre>                                                     |
| $2               | <pre class="language-json"><code class="lang-json"><strong>{
</strong>  "id": 2,
  "name": "x9",
  "score": 87,
  "tags": [
    {"tag":"abc","weight":10},
    {"tag":"def","weight":90}
  ]
}
</code></pre>                                                                                                                                                                                                          |
| $3               | <pre class="language-json"><code class="lang-json">[
  {"tag":"abc","weight":10},,
  {"tag":"def","weight":90}
]
</code></pre>                                                                                                                                                                                                                                                                                        |
| $4               | <pre class="language-json"><code class="lang-json">{"tag":"def","weight":90}
</code></pre>                                                                                                                                                                                                                                                                                                                            |
| $5               | <pre class="language-json"><code class="lang-json">"def"
</code></pre>                                                                                                                                                                                                                                                                                                                                                |

{% hint style="info" %}
The \$$ special variable is available to be used as a convenience. It always represents the top most numerically indexed special variable that is available within its context.
{% endhint %}

| Syntax                                       | Result                                                                   |
| -------------------------------------------- | ------------------------------------------------------------------------ |
| items\[\$$.id > 1].tags\[\$$.weight>=90].tag | <pre class="language-json"><code class="lang-json">["def"]
</code></pre> |
| items\[$2.id > 1].tags\[\$$.weight>=90].tag  | <pre><code>["def"]
</code></pre>                                         |
| items\[\$$.id > 1].tags\[$4.weight>=90].tag  | <pre><code>["def"]
</code></pre>                                         |
| items\[$2.id > 1].tags\[$4.weight>=90].tag   | <pre><code>["def"]
</code></pre>                                         |

#### Advanced Examples

| Syntax                                                  | Result                                                                         |
| ------------------------------------------------------- | ------------------------------------------------------------------------------ |
| items\[\$$.id > 1].tags\[\$$.weight>=$0.v].tag          | <pre class="language-json"><code class="lang-json">["abc","def"]
</code></pre> |
| items\[\$$.id > (\[$0.v,2,3]\|max)].id                  | <pre class="language-json"><code class="lang-json">[]
</code></pre>            |
| items\[\$$.id > (\[$0.v,2,3]\|min) \|\| \$$.id == 1].id | <pre class="language-json"><code class="lang-json">[1,3]
</code></pre>         |

***

## Transformation with SET

In addition to the syntax above for data retrieval, SET supports new syntax for data transformation.

The SET filter leverages the targeting mechanism of the GET filter and allows you to transform the data that is retrieved. It is important to note that after the transformation, the complete object (not just what got changed) is returned. By doing so, it allows for this process to be repeated as many times as you need to complete your transformations.

Below are some examples combining the above syntax with the SET filter.

{% embed url="https://youtu.be/PtxMkxmRNAk" %}

Multiple SET filters may be required for each transformation.

| Syntax                                                                                                                                                                                                 | Result                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><em>Change the value of "v"</em></p><p></p><p><strong>Path</strong>: v<br><strong>Value</strong>: 50</p>                                                                                            | <pre class="language-json"><code class="lang-json">{"v": 50,...
</code></pre>                                                                                                                                                                                                                                                                                                                                                                                              |
| <p><em>Change the value of all IDs in the items</em></p><p></p><p><strong>Path</strong>: items.id<br><strong>Value</strong>: 99</p>                                                                    | <pre class="language-json"><code class="lang-json">{
  "v": 10,
  "items": [
    {
      "id": 99,
      "name": "s1",
      "score": 100,
      "tags": [
         {"tag":"beta","weight":5},
	 {"tag":"test","weight":50}
      ]
    },
    {
      "id": 99,
      "name": "x9",
      "score": 87,
      "tags": [
        {"tag":"abc","weight":10},
	{"tag":"def","weight":90}
      ]
    }
  ]
}
</code></pre>                                                    |
| <p><em>Add 1 to all item IDs</em></p><p></p><p><strong>Path</strong>: items.id<br><strong>Value</strong>: $$+1</p>                                                                                     | <pre class="language-json"><code class="lang-json">{
  "v": 10,
  "items": [
    {
      "id": 2,
      "name": "s1",
      "score": 100,
      "tags": [
         {"tag":"beta","weight":5},
	 {"tag":"test","weight":50}
      ]
    },
    {
      "id": 3,
      "name": "x9",
      "score": 87,
      "tags": [
        {"tag":"abc","weight":10},
	{"tag":"def","weight":90}
      ]
    }
  ]
}
</code></pre>                                                      |
| <p><em>Uppercase all item tags</em></p><p></p><p><strong>Path</strong>: items.tags.tag<br><strong>Value</strong>: $$|to_upper</p>                                                                      | <pre class="language-json"><code class="lang-json">{
  "v": 10,
  "items": [
    {
      "id": 1,
      "name": "S1",
      "score": 100,
      "tags": [
         {"tag":"BETA","weight":5},
	 {"tag":"TEST","weight":50}
      ]
    },
    {
      "id": 2,
      "name": "X9",
      "score": 87,
      "tags": [
        {"tag":"ABC","weight":10},
	{"tag":"DEF","weight":90}
      ]
    }
  ]
}
</code></pre>                                                      |
| <p><em>Add the value of an input to each tag weight</em></p><p></p><p><strong>Path</strong>: items.tags.weight<br><strong>Value</strong>: $input.add+$$<br><strong>Input</strong>: 500</p>             | <pre class="language-json"><code class="lang-json">{
  "v": 10,
  "items": [
    {
      "id": 1,
      "name": "S1",
      "score": 100,
      "tags": [
         {"tag":"BETA","weight":505},
	 {"tag":"TEST","weight":550}
      ]
    },
    {
      "id": 2,
      "name": "X9",
      "score": 87,
      "tags": [
        {"tag":"ABC","weight":510},
	{"tag":"DEF","weight":590}
      ]
    }
  ]
}
</code></pre>                                                 |
| <p><em>Add a new total_weight key for each item that contains the sum of all tag weights</em></p><p></p><p><strong>Path</strong>: items.total_weight<br><strong>Value</strong>: $1.tags.weight|sum</p> | <pre class="language-json"><code class="lang-json">{
  "v": 10,
  "items": [
    {
      "id": 1,
      "name": "S1",
      "score": 100,
      "tags": [
         {"tag":"BETA","weight":5},
	 {"tag":"TEST","weight":50}
      ],
      "total_weight": 55
    },
    {
      "id": 2,
      "name": "X9",
      "score": 87,
      "tags": [
        {"tag":"ABC","weight":10},
	{"tag":"DEF","weight":90}
      ],
      "total_weight": 100
    }
  ]
}
</code></pre> |

***

## Expression Data Type

The expression data type can be applied to any value input and allows you to perform certain operations on your data when establishing new values. You can also reference other variables and inputs in your expressions which allows for faster data manipulation.

{% embed url="https://youtu.be/xJweDspuVNo" %}

Please see our full, in-depth documentation on the Expression data type [here](../the-function-stack/data-types/expression.md).

***

## Expression Filters

The Xano Transform Engine provides several filters to assist in making transformation easier using the expression syntax. It also includes custom implementations of the [higher order filters](using-xano-transform.md#higher-order-filters).

### as

The `as` filter provides a way to dynamically assign a variable to an expression while chaining together filters. This is useful for long or dynamic expressions that need to be referenced more than once.

Arguments

* name - the new variable name

Context  Variables

* **\$$** - the context variable that represents the element of the array being processed.

#### Examples

```json
// initial data
$obj.really.long.ref.company             // foobar, inc https://foo.bar

// without as
$obj.really.long.ref.company|substr:0:($obj.really.long.ref.company|index:http)|trim
// foobar, inc

// with as
$obj.really.long.ref.company|as:C|substr:0:($C|index:http)|trim
// foobar, inc

```

### transform

{% hint style="info" %}
This filter is similar to the map filter, except it can bind to all data - not just an array.
{% endhint %}

The `transform` filter is universal way to transform data. It works with arrays, objects, and scalar values.

Arguments

* expression - the expression being used to transform `$$`.&#x20;

Context  Variables

* **\$$** - the context variable that represents the element of the array being processed.

#### Examples

```json
[1,2,3]|transform:($$|count)          // 3
[1,2,3]|transform:($$|count)+($$|sum) // 9

{first:Alpha,last:Beta}|transform:$$.first~" "~$$.last
// Alpha Beta
```

### to\_expr

{% hint style="info" %}
It is very important to sanitize your data, if you are using this with user generated expressions. This filter provides a way to dynamically reference your variables and use the filters within Xano.
{% endhint %}

The `to_expr` filter is introduces the possibility of dynamic programming. It converts text into an expression.

Arguments (none)

Context  Variables (none)

#### Examples

```json
"1+2+3"|to_expr                      // 6

$input.score = 10
"1+2+3+$input.score"|to_expr         // 16
```

### get

{% hint style="info" %}
See above for a detailed walkthrough of the improvements to the [get filter](using-xano-transform.md#retrieval-with-get).
{% endhint %}

### set

{% hint style="info" %}
See above for a detailed walkthrough of the improvements to the [set filter](using-xano-transform.md#transformation-with-set).
{% endhint %}

## Higher Order Filters

These filters resemble their Lambda counterparts, but if used within an Expression, they have a simplified syntax along with their own high performance implementation. All of these have the requirement of binding to an array. There is also a subtle change where the Lambda `$this` variable is represented as the Expression `$$` variable.

### map

{% hint style="info" %}
This filter binds to an array. If you need to transform an object or scalar value, try the transform filter.
{% endhint %}

The `map` filter is used to do transformations on array elements.

Arguments

* expression - the expression being applied to each iteration of the array

Context  Variables

* **\$$** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed
* **$parent** - the context variable that represents the entire array with all of its elements.

#### Examples

<pre class="language-json"><code class="lang-json">[1,2,3]|map:$$+1                      // [2,3,4]
[1,2,3]|map:$$+1+$index               // [2,4,6]
[1,2,3]|map:$$+1+($parent|count)      // [5,6,7]

<strong>[{name:foo},{name:bar}]|map:$$.name   // [foo,bar]
</strong></code></pre>

### some

The `some` filter (also called **has** or **has any element**) returns true, if the conditional expression matches any of the array elements - otherwise, false is returned.

Arguments

* expression - the expression being applied to each iteration of the array

Context  Variables

* **\$$** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.

#### Examples

```json
[1,2,3]|some:$$==2                    // true
[1,2,3]|some:$$>10                    // false
```

### every

The `every` filter (also called **find every element**) returns true if the conditional expression matches all of the array elements - otherwise, false is returned.

Arguments

* expression - the expression being applied to each iteration of the array

Context  Variables

* **\$$** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.

#### Examples

```json
[1,2,3]|every:$$>=1 && $$<=3          // true
[1,2,3]|every:$$>10                   // false
```

### find

The `find` filter (also called **find first element**) returns the array item, that first matches the conditional expression - otherwise, null is returned.

Arguments

* expression - the expression being applied to each iteration of the array

Context  Variables

* **\$$** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.

Examples

```json
[1,2,3]|find:$$==2                    // 2
[1,2,3]|find:$$>1                     // 2

[{name:foo},{name:bar}]|find:($$.name|starts_with:b)
// {name:bar}
```

### findIndex

The `findIndex` filter (also called **find first element index**) returns the index of the array item, that first matches the conditional expression - otherwise, null is returned.

Arguments

* expression - the expression being applied to each iteration of the array

Context  Variables

* **\$$** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.

Examples

```json
[1,2,3]|findIndex:$$==2               // 1
[1,2,3]|findIndex:$$>1                // 1

[{name:foo},{name:bar}]|findIndex:($$.name|starts_with:b)
// 1
```

### filter

The `filter` filter (also called **find all elements**) returns a new array of items that match the conditional expression.

Arguments

* expression - the expression being applied to each iteration of the array

Context  Variables

* **\$$** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.

Examples

```json
[1,2,3]|filter:$$==2                  // [2]
[1,2,3]|filter:$$>1                   // [2,3]
```

### reduce

{% hint style="info" %}
This also has an optional 2nd argument that represents the initial value. If not specified, it defaults to 0.
{% endhint %}

The reduce filter is a bit more complicated than the other because it has state that changes through each iteration of the array elements. The purpose of this filter is to perform some calculation based on all of the array items. A common example would be summing a list of numbers together one after another.

Arguments

* expression - the expression being applied to each iteration of the array
* initialValue - (optional) the initial value for `$result`. This defaults to 0, if not specified.&#x20;

Context  Variables

* **\$$** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.
* **$result** - the context variable that is used to represent the result of the previous iteration or the initial value on the first iteration.

Examples

```json
[1,2,3]|reduce:$$+$result             // 6
[1,2,3]|reduce:$$+$result:10          // 16
```

## Use Cases & Examples

Xano Transform is almost limitless. Some of the most common use cases for Transform are as follows. Please note that this is not an extensive list, and we recommend reading on for more information and examples.

For the sake of these examples, assume we are working with the following data set. You can download the full list of products as CSV or JSON below as well if you want to try these yourself.

{% file src="../.gitbook/assets/products-example-json.txt" %}

{% file src="../.gitbook/assets/products-example.csv" %}

<pre class="language-json"><code class="lang-json">{
    result:
            [
                {
                    id: 1,
                    created_at: 1702311936290,
                    title: iPhone 9,
                    description: An apple mobile which is nothing like apple,
<strong>                    price: 549,
</strong>                    discountPercentage: 12.96,
                    rating: 4.69,
                    stock: 94,
                    brand: Apple,
                    category: smartphones
                },
                {
                    id: 2,
                    created_at: 1702311936290,
                    title: iPhone X,
                    description: SIM-Free, Model A19211 6.5-inch Super Retina HD display with OLED technology A12 Bionic chip with ...,
                    price: 899,
                    discountPercentage: 17.94,
                    rating: 4.44,
                    stock: 34,
                    brand: Apple,
                    category: smartphones
                },
            ...]
}
</code></pre>

Using Xano Transform, we could use one or more of the following:

* Find me all of the products with a price greater than $700
* Find me all of the smartphones that have a rating of at least 4.5 and are less than $300
* Find me all of the iPhones that have a total price of their returned price + 7.5% to account for tax

These are just a few examples of what Xano Transform could accomplish.

#### Find all products with a price greater than $700

{% tabs %}
{% tab title="Xano Transform (GET Filter)" %}
<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

```
result[$$.price>700]
```

* **result (**_**Find all products)**_
  * Selects something in the JSON, in this case the 'list' key
* **\[]**
  * Indicates that we want to apply a condition to the selection
* **\$$.price** (with a price)
  * Use the value of 'price' as part of the expression
* **>700** (greater than 700)
  * The expression used to define the data we want returned
{% endtab %}

{% tab title="No-Code" %}
<figure><img src="../.gitbook/assets/image (8).png" alt="" width="563"><figcaption></figcaption></figure>

* **Create Variable**
  * Create a variable to hold our list of qualifying results
* **For Each Loop**
  * Use a For Each Loop to begin to iterate through the list of data we are working with
  * **Conditional**
    * Check to see if the item we are currently iterating through has a price greater than $700
    * **Then**
      * If the item qualifies, add it to the variable created before the loop began
    * **Else**
      * Go to the next iteration of the loop
{% endtab %}

{% tab title="High Order Filters" %}
<figure><img src="../.gitbook/assets/image (9).png" alt="" width="563"><figcaption></figcaption></figure>

Using the higher order filter called 'filter', apply the following code:

```javascript
return $this.price > 700;
```
{% endtab %}

{% tab title="Javascript" %}
```javascript
return $var.products.filter(product => product.price > 700);
```
{% endtab %}
{% endtabs %}

#### Find all products with a price greater than $700 and a rating greater than 4.5

{% tabs %}
{% tab title="Xano Transform (GET Filter)" %}
<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

```
result[$$.price>700 && $$.rating>4.5]
```

* **result (**_**Find all products)**_
  * Selects something in the JSON, in this case the 'list' key
* **\[]**
  * Indicates that we want to apply a condition to the selection
* **\$$.price** (with a price)
  * Use the value of 'price' as part of the expression
* **>700** (greater than 700)
  * The first part of the expression used to define the data we want returned
* **&&** (and)
  * Indicate that this expression contains multiple conditions
* **\$$.rating** (a rating)
  * Select the 'rating' value as a part of this condition
* **>4.5** (greater than 4.5)
  * The second part of the expression used to define the data we want returned
{% endtab %}

{% tab title="No-Code" %}
<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

* **Create Variable**
  * Create a variable to hold our list of qualifying results
* **For Each Loop**
  * Use a For Each Loop to begin to iterate through the list of data we are working with
  * **Conditional**
    * Check to see if the item we are currently iterating through has a price greater than $700 and a rating greater than 4.5
    * **Then**
      * If the item qualifies, add it to the variable created before the loop began
    * **Else**
      * Go to the next iteration of the loop
{% endtab %}

{% tab title="High Order Filters" %}
<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

Using the higher order filter called 'filter', apply the following code:

<pre class="language-javascript"><code class="lang-javascript"><strong>return $this.price > 700 &#x26;&#x26; $this.rating > 4.5;
</strong></code></pre>
{% endtab %}

{% tab title="Javascript" %}
```javascript
return $var.products.filter(product => product.price > 700 && product.rating > 4.5);
```
{% endtab %}
{% endtabs %}

#### Find all products with a price greater than $700 and a rating greater than 4.5, that are in stock

{% tabs %}
{% tab title="Xano Transform (GET Filter)" %}
<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

```
result[$$.price>700 && $$.rating>4.5 && $$.stock>0]
```

* **result (**_**Find all products)**_
  * Selects something in the JSON, in this case the 'list' key
* **\[]**
  * Indicates that we want to apply a condition to the selection
* **\$$.price** (with a price)
  * Use the value of 'price' as part of the expression
* **>700** (greater than 700)
  * The first part of the expression used to define the data we want returned
* **&&** (and)
  * Indicate that this expression contains multiple conditions
* **\$$.rating** (a rating)
  * Select the 'rating' value as a part of this condition
* **>4.5** (greater than 4.5)
  * The second part of the expression used to define the data we want returned
* **&&** (and)
  * Indicate that this expression contains multiple conditions
* **\$$.stock>0** (that are currently in stock)
  * The third part of the expression used to define the data we want returned
{% endtab %}

{% tab title="No-Code" %}
<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

* **Create Variable**
  * Create a variable to hold our list of qualifying results
* **For Each Loop**
  * Use a For Each Loop to begin to iterate through the list of data we are working with
  * **Conditional**
    * Check to see if the item we are currently iterating through has a price greater than $700 and a rating greater than 4.5, that also have a stock count greater than 0
    * **Then**
      * If the item qualifies, add it to the variable created before the loop began
    * **Else**
      * Go to the next iteration of the loop
{% endtab %}

{% tab title="High Order Filters" %}
<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

Using the higher order filter called 'filter', apply the following code:

```javascript
return $this.price > 700 && $this.rating > 4.5 && $this.stock > 0;
```
{% endtab %}

{% tab title="Javascript" %}
```javascript
return $var.products.filter(product => product.price > 700 && product.rating > 4.5 && product.stock > 0);
```
{% endtab %}
{% endtabs %}

#### Take the returned list of products and capitalize all product names

{% tabs %}
{% tab title="Xano Transform (SET Filter)" %}
<figure><img src="../.gitbook/assets/CleanShot 2023-12-21 at 14.27.47.png" alt="" width="408"><figcaption></figcaption></figure>

```
Path: name
Value: $$|to_upper
```

* **Path: name**
  * Set the 'path' option to _name_ to indicate this is the key to update
* **Value: \$$|to\_upper**
  * **\$$**
    * Select the current name
  * **|to\_upper**
    * Apply the to\_upper filter
{% endtab %}

{% tab title="No-Code" %}
<figure><img src="../.gitbook/assets/CleanShot 2023-12-21 at 14.29.32.png" alt=""><figcaption></figcaption></figure>

* **Create Variable**
  * Create a variable to hold our list of qualifying results
* **For Each Loop**
  * Use a For Each Loop to begin to iterate through the list of data we are working with
  * **Conditional**
    * Check to see if the item we are currently iterating through has a price greater than $700 and a rating greater than 4.5, that also have a stock count greater than 0
    * **Then**
      * Update the product's name by applying a to\_upper filter
      * If the item qualifies, add it to the variable created before the loop began
    * **Else**
      * Go to the next iteration of the loop
{% endtab %}

{% tab title="High Order Filters" %}
<figure><img src="../.gitbook/assets/CleanShot 2023-12-21 at 14.30.19.png" alt="" width="404"><figcaption></figcaption></figure>

Using the filter **filter**, apply the following code:

```javascript
return $this.price > 700 && $this.rating > 4.5 && $this.stock > 0;
```

Using the filter **map**, apply the following code:

```javascript
return {
        ...$this,
        name: $this.name.toUpperCase()
    };
```
{% endtab %}

{% tab title="Javascript" %}
```javascript
let filteredProducts = $var.products.filter(product => product.price > 700 && product.rating > 4.5 && product.stock > 0);
let modifiedProducts = filteredProducts.map(product => {
    return {
        ...product,
        name: product.name.toUpperCase()
    };
});
return modifiedProducts;
```
{% endtab %}
{% endtabs %}

#### Take the returned list of products, capitalize all product names, and conditionally update the price based on the stock value while applying proper price formatting

{% tabs %}
{% tab title="Xano Transform (GET Filter)" %}
<figure><img src="../.gitbook/assets/CleanShot 2023-12-21 at 14.37.11.png" alt="" width="413"><figcaption></figcaption></figure>

_To complete this example, you'll want to apply the SET filter for name as described in the previous example._

```
Path: price
Value: $1.stock>50 ? ("$"~($$*0.9|number_format:2:.:,)) : ("$"~($$*1.3|number_format:2:.:,))
```

* **Path: price**
  * Set the path option to 'price' to indicate this is the key to update
* **Value: $1.stock>50 ? ("$"\~(\$$\*0.9|number\_format:2:.:,)) : ("$"\~(\$$\*1.3|number\_format:2:.:,))**
  * **$1.stock>50**
    * Use anchored selection to get the stock count and check to see if it is greater than 50
  * **?**
    * Apply a condition based on what the previous portion of the expression returns
  * **If the stock > 50**
    * **("$"\~**
      * Begin the value with a $ character
    * **(\$$\*0.9**
      * Multiply the price by 0.9
    * **|number\_format:2:.:,))**
      * Apply the number\_format filter to format the number as a standard price (2 decimal points, a . decimal separator, and a , thousands seperator)
  * **If the stock < 50**
    * **("$"\~**
      * Begin the value with a $ character
    * **(\$$\*1.3**
      * Multiply the price by 1.3
    * **|number\_format:2:.:,))**
      * Apply the number\_format filter to format the number as a standard price (2 decimal points, a . decimal separator, and a , thousands seperator)
{% endtab %}

{% tab title="No-Code" %}
<figure><img src="../.gitbook/assets/CleanShot 2023-12-21 at 14.48.23.png" alt="" width="563"><figcaption></figcaption></figure>



* **Create Variable**
  * Create a variable to hold our list of qualifying results
* **For Each Loop**
  * Use a For Each Loop to begin to iterate through the list of data we are working with
  * **Conditional**
    * Check to see if the item we are currently iterating through has a price greater than $700 and a rating greater than 4.5, that also have a stock count greater than 0
    * **Then**
      * Update the product's name by applying a to\_upper filter
      * **Conditional**
        * Check to see if the product stock is greater than 50
          * **Then**
            * Update the product price, multiplying it by 0.9
          * **Else**
            * Update the product price, multiplying it by 1.3&#x20;
      * Update the product's price and apply the number\_format filter
    * **Else**
      * Go to the next iteration of the loop
{% endtab %}

{% tab title="High Order Filters" %}
<figure><img src="../.gitbook/assets/CleanShot 2023-12-21 at 15.10.13.png" alt="" width="407"><figcaption></figcaption></figure>

Using the filter **filter**, apply the following code:

```javascript
return $this.price > 700 && $this.rating > 4.5 && $this.stock > 0;
```

Using the filter **map**, apply the following code:

```javascript
return {
    ...$this,
    name: $this.name.toUpperCase(),
    price: $this.stock > 50 
           ? ($this.price * 0.9).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",") 
           : ($this.price * 1.3).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",")
};
```
{% endtab %}

{% tab title="Javascript" %}
```javascript
let filteredProducts = $var.products.filter(product => product.price > 700 && product.rating > 4.5 && product.stock > 0);

let modifiedProducts = filteredProducts.map(product => {
    let adjustedPrice = product.stock > 50 
                        ? product.price * 0.9 
                        : product.price * 1.3;
    
    return {
        ...product,
        name: product.name.toUpperCase(),
        price: adjustedPrice.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",")
    };
});

return modifiedProducts;

```
{% endtab %}
{% endtabs %}

## Troubleshooting

### Text vs Expression

The get and set filters parse the path argument using the [Xano expression](../the-function-stack/data-types/expression.md) syntax. If you have a path that looks like an expression, but needs to be interpreted as text, then wrap it with brackets and quotes.

Some 3rd party APIs (like Stripe) rely on dot notation arguments being sent as text and then interpreted on their side. In this scenario, it is important to wrap them with the bracket syntax below using double quotation marks.

{% hint style="info" %}
The [Import cURL](../the-function-stack/functions/apis-and-lambdas/external-api-request.md) feature has been updated to properly escape all arguments.
{% endhint %}

|        AS ARRAY       |           AS TEXT          |
| :-------------------: | :------------------------: |
|       expand\[0]      |       \["expand\[0]"]      |
| line\_item\[0]\[data] | \["line\_item\[0]\[data]"] |



