# Expression

Expressions are a flexible data type that Xano parses in real-time to support an inline syntax to expressing data with mathematical expressions. Anything you can do with Xano filters, can also be done inline within an expression.

When building expressions, make sure you have the 'expression' data type selected. You can also click Use Expression under any value box to quickly switch.

Expression building in Xano leverages auto-complete, which will auto-populate references to inputs and variables, filters, and other common notation.

{% embed url="https://youtu.be/xJweDspuVNo" %}

## Using the Expression Editor & Playground <a href="#editor-playground" id="editor-playground"></a>

When using the Expression data type, you will be presented with an Expression Editor & Playground to enable easier editing and testing of your expression.

{% hint style="success" %}
To get the most value out of the expression editor and playground, make sure to add any variable contents you'd like to use in the Context panel, and make sure to Run & Debug your function stack to enable auto-complete.
{% endhint %}

| **Expression Editor**                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="../../.gitbook/assets/CleanShot 2024-07-09 at 10.08.39.png" alt="" data-size="original"> | <ol><li>Build and edit your expression here with easy auto-complete</li><li>Test your expression in the playground or apply the changes</li><li>Get quick context for variables accessible by your expression and their data types</li><li>Search the library of transformers (filters) available to use, and see examples of how they work</li><li>Take a quick Expressions tutorial</li><li>Enable new variables to be set to Expression type by default</li></ol> |
| **Playground**                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <img src="../../.gitbook/assets/CleanShot 2024-07-09 at 10.12.13.png" alt="" data-size="original"> | <ol><li>Edit your expression here</li><li>Run and test your expression</li><li>The result of the last execution</li></ol><p>The playground also retains access to the transformers (filters) library and the tutorial. You'll need to edit your variable context here if testing with variable data. Just copy and paste the contents into the context panel.</p>                                                                                                    |

## Mathematical Operators

<table><thead><tr><th width="203">Operator</th><th>Function</th><th>Example</th><th>Result</th></tr></thead><tbody><tr><td>+</td><td>addition</td><td>100 + 101</td><td>201</td></tr><tr><td>-</td><td>subtraction</td><td>100 - 101</td><td>-1</td></tr><tr><td>*</td><td>multiplication</td><td>100 * 101</td><td>10101</td></tr><tr><td>/</td><td>division</td><td>100 / 10</td><td>10</td></tr></tbody></table>

### Operator Precedence

For the most part expressions are evaluated left to right. Using parentheses to illustrate a point, the following would be the same assuming all operators were being evaluated left to right.

```
1 + 2 + 3     == 6
1 + (2 + 3)   == 6
```

However, there are a few operators which get special priority and get evaluated first. These operators are the multiplication and divide operators.

```
1 + 2 * 3    == 7          // if left to right, then 9 (which is incorrect)
1 + (2 * 3)  == 7

1 + 4 / 2    == 3          // if left to right, 2.5 (which is incorrect)
1 + (4 / 2)  == 3
```

## Text Operators

<table><thead><tr><th width="203">Operator</th><th>Function</th><th>Example</th><th>Result</th></tr></thead><tbody><tr><td>~</td><td>concatenation</td><td>a ~ b</td><td>ab</td></tr></tbody></table>

{% hint style="info" %}
To add separation when concatenating, add an empty string between the values: ​`a~" "~b`
{% endhint %}

## Array Operators

<table><thead><tr><th width="203">Operator</th><th>Function</th><th>Example</th><th>Result</th></tr></thead><tbody><tr><td>...</td><td>spread items within an array</td><td>[1,2,3, ...[4,5,6],7]</td><td>[1,2,3,4,5,6,7]</td></tr><tr><td>..</td><td>range operator</td><td>1..10</td><td>[1,2,3,4,5,6,7,8,9,10]</td></tr></tbody></table>

## Array Indexes

Expressions have the ability to reference array elements using all integer values (0, positive numbers, and negative numbers). Using a negative number represents starting from the top of the list rather the beginning of the list.

| Expression        | Result |
| ----------------- | ------ |
| \[a,b,c,d,e]\[0]  | a      |
| \[a,b,c,d,e]\[1]  | b      |
| \[a,b,c,d,e]\[-1] | e      |
| \[a,b,c,d,e]\[-2] | d      |

## Object Operators

<table><thead><tr><th width="203">Operator</th><th>Function</th><th>Example</th><th>Result</th></tr></thead><tbody><tr><td>...</td><td>spread items within an object</td><td>{a:1, b:2, ...{c:3}, d: 4}</td><td>{a:1,b:2,c:3,d:4}</td></tr></tbody></table>

## Comparison Operators

| Operator | Function                     | Example   | Result |
| -------- | ---------------------------- | --------- | ------ |
| ==       | equals (type conversion)     | 1 == "1"  | true   |
| ===      | strict equals                | 1 === "1" | false  |
| !=       | not equals (type conversion) | 1 != "1"  | false  |
| !==      | strict not equals            | 1 !== "1" | true   |
| >        | greater than                 | 1 > 2     | false  |
| >=       | greater than or equals       | 1 >= 2    | false  |
| <        | less than                    | 1 < 2     | true   |
| <=       | less than or equals          | 1 <= 2    | true   |

## Logical Operators

| Operator | Function | Example           | Result |
| -------- | -------- | ----------------- | ------ |
| !        | not      | !true             | false  |
| \|\|     | or       | 1 < 2 \|\| 1 != 1 | true   |
| &&       | and      | 1 < 2 && 1 != 1   | false  |

{% hint style="info" %}
All of these operators evaluate their expressions as truthy statements. This means that a comparison operator is not required. For example: 0 || 1 would evaluate to true since 1 evaluates as true.
{% endhint %}

## Conditional Operators

| Operator  | Function                      | Example       | Result |
| --------- | ----------------------------- | ------------- | ------ |
| a ? b : c | ternary (if/else)             | 1 < 2 ? 3 : 4 | 3      |
| a ?: b    | shorthand ternary (this/that) | 1 ?: 2        | 1      |
| a ?? b    | null coalescing               | null ?? 10    | 10     |

{% hint style="info" %}
The ternary operator has 2 forms - the traditional if/else based on expression and the shorthand (this/that). The shorthand version will use either the left (this) or the right (that) based on which one evaluates to a truthy statement first going from left to right.
{% endhint %}

{% hint style="info" %}
The null coalescing operator is very similar to the shorthand ternary, except that instead of relying on a truthy statement, it only checks for the null value.
{% endhint %}

## Variable Syntax

Variables can be referenced using the same [syntax](https://docs.xano.com/working-with-data/lambdas-javascript#special-variables) that is available within Lambdas.

### Variables

Variables within the function stack are accessible through `$var` root variable.

<figure><img src="../../.gitbook/assets/CleanShot 2023-12-19 at 09.52.50.png" alt=""><figcaption></figcaption></figure>

### Inputs

Inputs are accessible through the `$input` root variable.

<figure><img src="../../.gitbook/assets/CleanShot 2023-12-19 at 09.54.20.png" alt=""><figcaption></figcaption></figure>

### Authentication

Authentication values are accessible through the `$auth` root variable.

<figure><img src="../../.gitbook/assets/CleanShot 2023-12-19 at 09.54.39.png" alt=""><figcaption></figcaption></figure>

### Environment Variables

Environment variables are accessible through the `$env` root variable. This includes both system variables ($remote\_ip, $datasource, etc.) as well as workspace environment variables.

<figure><img src="../../.gitbook/assets/CleanShot 2023-12-19 at 09.55.02.png" alt=""><figcaption></figcaption></figure>

### Auto-Complete

When building expressions, you'll see autocomplete suggestions as you type. This works for variables, inputs, and environment variables, as well as filters.

For variables with nested data, such as objects, you'll also be presented with an auto-complete of the fields inside of that object. In this example, we're targeting a variable called **`log`**&#x61;nd are presented with the fields inside of that variable by the expression builder, as well as a description of each.

<figure><img src="../../.gitbook/assets/CleanShot 2024-04-03 at 11.34.22.png" alt="" width="402"><figcaption></figcaption></figure>

## Data Types

The Xano expression engine supports a more relaxed syntax for its data types to make it easier to reference text and variables without the strict requirements of using quotation marks.

| Expression       | Type                        | Result         |
| ---------------- | --------------------------- | -------------- |
| abc              | text                        | "abc"          |
| 123              | integer                     | 123            |
| $var.score       | integer                     | 123            |
| "$var.score"     | text                        | "$var.score"   |
| "\\""            | text with escaped character | "              |
| true             | boolean                     | true           |
| false            | boolean                     | false          |
| "true"           | text                        | "true"         |
| null             | null                        | null           |
| "null"           | text                        | "null"         |
| "123"            | text                        | "123"          |
| \[1,2,3]         | array of integers           | \[1,2,3]       |
| \["1","2","3"]   | array of text               | \["1","2","3"] |
| \[a,b,c]         | array of text               | \["a","b","c"] |
| \["a","b","c"]   | array of text               | \["a","b","c"] |
| {a:1}            | object                      | {"a":1}        |
| {"a":a}          | object                      | {"a":"a"}      |
| {"a":$var.score} | object                      | {"a":123}      |

## Dot Notation

The same relaxed syntax used for data types also applies to dot notation.

| Dot Notation           | JSON Equivalent        |
| ---------------------- | ---------------------- |
| $var.items             | $var.items             |
| $var.items\[1]         | $var.items\[1]         |
| $var.items\["1"]       | $var.items\["1"]       |
| $var.items\[a]         | $var.items\["a"]       |
| $var.items\[a\~b\~c]   | $var.items\["abc"]     |
| $var.items\["a\~b\~c"] | $var.items\["a\~b\~c"] |

## Filters

All of the Xano filters are available within the expression syntax. To use these, you need to follow the pipe expression syntax.

```
variable | pipe : arg1 : arg2 : argN
```

For example, to uppercase text using the upper filter, you would do the following.

```
"xano"|upper

// result = XANO
```

Here is another example using a filter with an argument.

```
1 + 2 + (3|add:1)

// result = 7
```

{% hint style="info" %}
This particular example is using both a mathematical "+" and an add filter to illustrate how they can be mixed together.
{% endhint %}

You can also chain filters together.

```
1 + 2 + (3|add:1|mul:2)

// result = 11
```

## Importing Expressions

When importing cURL or pasting JSON into Xano, Xano can automatically detect the Expression data type, provided the expression begins with a $ character.

As an example, the following JSON...

```
{"id":"0a1612ca-37d3-4d45-85ad-841a7522e000","created_at":"$test.0.id"}
```

...will import as:

<figure><img src="../../.gitbook/assets/CleanShot 2024-04-09 at 15.02.30.png" alt="" width="539"><figcaption></figcaption></figure>

## Advanced Examples

As showcased above, the Xano expression engine is very powerful. Here we can look into some more advanced use cases that bring everything together.

### Conditional

#### Sample Data

```json
$input = {
  "scores": [1,2,3]
}

$var = {
  "numbers": [4,5,6]
}
```

Expression

```
($input.scores|max) > ($var.numbers|min)

// result = false
```

### Null coalescing

#### Sample Data

```json
$input = {
  "scores": [1,2,3]
}

$var = {
  "numbers": [4,5,6]
}
```

#### Expression

```
(($input.scores|merge:[100,101,102])|max)+($var.bad_syntax ?? 100)

// result = 202
```

### Ternary

#### Sample Data

```json
$input = {
  "scores": [1,2,3]
}

$var = {
  "numbers": [0,1,2,3,4,5,6]
}
```

#### Expression

```
($input.scores[2] == 3 ? 10 : 100) + (($var.numbers|min) ?: $var.numbers|max))

// result = 16
```
