# Manipulation

{% include "../../.gitbook/includes/filter-note.md" %}

## fill

Create an array of a certain size with a default value.

| Parameter    | Purpose                          | Example         |
| ------------ | -------------------------------- | --------------- |
| parent value | The default value to fill        | "default value" |
| start        | The starting index of the array  | 0               |
| length       | The number of items in the array | 10              |

### Examples <a href="#fillexamples" id="fillexamples"></a>

<table><thead><tr><th width="342.8411865234375">Example</th><th>Result</th></tr></thead><tbody><tr><td><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 09.22.26.png" alt="" data-size="original"></td><td><p></p><pre class="language-json"><code class="lang-json">[
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value",
     "Default Value"
]
</code></pre></td></tr></tbody></table>

***

## fill\_keys

Creates an object of a certain size with a default value and a list of keys.

| Parameter    | Purpose                   | Example                                                                                               |
| ------------ | ------------------------- | ----------------------------------------------------------------------------------------------------- |
| parent value | The default value to fill | "default value"                                                                                       |
| keys         | The array of keys to use  | <p></p><pre class="language-json"><code class="lang-json">[
	"key1",
	"key2",
	"key3"
]
</code></pre> |

### Examples <a href="#fill_keys_examples" id="fill_keys_examples"></a>

| Example                                                                                            | Output                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="../../.gitbook/assets/CleanShot 2025-03-19 at 09.27.52.png" alt="" data-size="original"> | <p></p><pre class="language-json"><code class="lang-json">{
	"key1": "Default Value",
	"key2": "Default Value",
	"key3": "Default Value"
}
</code></pre> |

***

## first\_notempty

Applies the first value that is not **empty** (0, null, "", empty string)

Useful if you need to determine a value to apply based on what is provided, such as editing a database record and being uncertain if an input will be provided to replace a value.

| Parameter    | Purpose                                       | Example                             |
| ------------ | --------------------------------------------- | ----------------------------------- |
| parent value | The value to check if empty                   | Can contain any value, or no value. |
| value        | The value to use if the parent value is empty | "default"                           |

### Examples <a href="#first_notempty_examples" id="first_notempty_examples"></a>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 09.52.57.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 09.39.01.png" alt=""><figcaption></figcaption></figure>

***

## first\_notnull

Applies the first value that is not **`null`**

Useful if you need to determine a value to apply based on what is provided, such as editing a database record and being uncertain if an input will be provided to replace a value.

{% hint style="info" %}
## Hint

Remember, **`null`** is its own value entirely. It is not the same as "null", an empty string, or any other similar empty state.
{% endhint %}

| Parameter    | Purpose                                        | Example          |
| ------------ | ---------------------------------------------- | ---------------- |
| parent value | The value to check if `null`                   | Can be any value |
| value        | The value to use if the parent value is `null` | "default"        |

### Examples <a href="#first_notnull_examples" id="first_notnull_examples"></a>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 09.59.51.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 09.59.31.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 09.54.10.png" alt=""><figcaption></figcaption></figure>

***

## get

Gets a value at the specified path inside of an array or object.

For arrays, the path can be an index, such as `0`, `1,` or `2`, which will get the specific item at that index in the array.

For arrays of objects, you can specify the index + a path, such as `2.name`

For single objects, you can just specify the path, such as `name`.

This filter is useful if you aren't sure if the value you need will exist, and need to provide a default value in place of it.

{% hint style="success" %}
## Hint

Are you getting errors in your function stacks because certain values don't exist all the time? The **GET** filter can be a great fix for this.
{% endhint %}

| Parameter     | Purpose                                                     | Example                                                                                                                                                                                                                                   |
| ------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| parent value  | The object or array to search for the value                 | This can be an object, array, a variable, or the result of one of the Get All Input functions [\[1\]](../functions/utility-functions.md#get-all-input) [\[2\]](../functions/utility-functions.md#get-all-raw-input)                       |
| path          | The path to look for inside of the parent value             | <p>For getting a specific array item:<br><code>0</code><br><br>For getting a specific path inside of an object:<br><code>pathName</code><br><br>For getting a specific path inside of an array of objects:<br><code>0.pathName</code></p> |
| default value | The value to provide in place of the value that isn't found | This value can be whatever you'd like.                                                                                                                                                                                                    |

### Examples <a href="#get_examples" id="get_examples"></a>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 10.50.15 (1).png" alt=""><figcaption><p>An age is provided in the input, so it is provided by the GET filter.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 10.50.47.png" alt=""><figcaption><p>No age is provided in the input, so the default value is used instead.</p></figcaption></figure>

***

## has

Checks if a value is present (similar to get), but only returns a true or false.

| Parameter    | Purpose                                         | Example                                                                                                                                                                                                                                   |
| ------------ | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| parent value | The object or array to search for the value     | This can be an object, array, a variable, or the result of one of the Get All Input functions [\[1\]](../functions/utility-functions.md#get-all-input) [\[2\]](../functions/utility-functions.md#get-all-raw-input)                       |
| path         | The path to look for inside of the parent value | <p>For getting a specific array item:<br><code>0</code><br><br>For getting a specific path inside of an object:<br><code>pathName</code><br><br>For getting a specific path inside of an array of objects:<br><code>0.pathName</code></p> |

### Examples <a href="#has_examples" id="has_examples"></a>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 10.53.10.png" alt=""><figcaption><p>An age is provided, so the filter returns <strong>true</strong></p></figcaption></figure>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 10.52.51.png" alt=""><figcaption><p>An age is not provided, so the filter returns <strong>false</strong></p></figcaption></figure>

***

## set

Replaces or inserts new data at a specified path.

| Parameter    | Purpose                                           |
| ------------ | ------------------------------------------------- |
| parent value | The object or array to target with the set filter |
| path         | The path at which to insert the supplied value    |
| value        | The supplied value to use                         |

### Examples <a href="#set_examples" id="set_examples"></a>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 10.57.53.png" alt=""><figcaption><p>Replace a value with another</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 10.59.23.png" alt=""><figcaption><p>Set a new key inside of an object</p></figcaption></figure>

***

## set\_conditional

Use set\_conditional to set a new value in an object based on whether a condition evaluates as true.

{% @arcade/embed flowId="CxgMoWBBckff0sO4P3ik" url="https://app.arcade.software/share/CxgMoWBBckff0sO4P3ik" %}

| Parameter    | Purpose                                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| parent value | The data to insert the result, such as an object                                                                         |
| path         | The path to insert the result                                                                                            |
| value        | The value to insert at the specified path                                                                                |
| conditional  | The condition to check. This can either come from an earlier function,or another filter that returns a `true` or `false` |

### Examples <a href="#set_conditional_examples" id="set_conditional_examples"></a>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 11.01.54.png" alt=""><figcaption><p>The age provided is greater than 20, so we return the value set in our set_conditional filter</p></figcaption></figure>

***

## set\_ifnotempty

## set\_ifnotnull



Sets a new value in an object if the value provided is not empty. An empty value can be 0, `null`, or an empty string.

set\_ifnotnull works the same, but only checks for `null`

| Parameter    | Purpose                                                      | Example                                 |
| ------------ | ------------------------------------------------------------ | --------------------------------------- |
| parent value | Where to set the value                                       | This will usually be an existing object |
| path         | The path to set the value if the checked value exists        | <p>"name"<br>"age"<br>"location"</p>    |
| value        | The value to set if the checked value is not empty (or null) | Any value                               |

### Examples <a href="#set_ifnotempty_ifnotnull_examples" id="set_ifnotempty_ifnotnull_examples"></a>

{% stepper %}
{% step %}
### First, we're getting an existing record from the database.

In this function stack, we're simulating a user submitting changes to their user profile.
{% endstep %}

{% step %}
### Then, we use an Update Variable with set\_ifnotempty (or set\_ifnotnull) to determine whether or not the returned record needs to be updated.


{% endstep %}

{% step %}
### Finally, we edit the record using the result of step 2 for all of our values.


{% endstep %}
{% endstepper %}

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 11.20.25.png" alt=""><figcaption></figcaption></figure>

***

## transform

The `transform` filter is universal way to transform data. It works with arrays, objects, and scalar values. It uses the [expression data type](../data-types/expression.md) to specify the transformation.

{% hint style="info" %}
## Hint

This filter is similar to the [map filter](transform.md#map), except it can bind to all data - not just an array.

You can use the context variable \$$ to target the parent value.
{% endhint %}

| Parameter    | Purpose                                  | Example                      |
| ------------ | ---------------------------------------- | ---------------------------- |
| parent value | The value to apply the transformation to | Can be any value or variable |
| expression   | The expression to run                    | Any expression               |

Read more about expressions and Xano Transform below.

{% content-ref url="../data-types/expression.md" %}
[expression.md](../data-types/expression.md)
{% endcontent-ref %}

{% content-ref url="broken-reference" %}
[Broken link](broken-reference)
{% endcontent-ref %}

### Examples <a href="#transform_examples" id="transform_examples"></a>

```json
[1,2,3]|transform:($$|count)                              // returns 3
[1,2,3]|transform:($$|count)+($$|sum)                     // returns 9
{first:Alpha,last:Beta}|transform:$$.first~" "~$$.last    // returns Alpha Beta
```

***

## unset

Removes a key from an object

| Parameter    | Purpose                                       |
| ------------ | --------------------------------------------- |
| parent value | The object to target                          |
| path         | The name of the key to remove from the object |

### Examples <a href="#unset_examples" id="unset_examples"></a>

<figure><img src="../../.gitbook/assets/CleanShot 2025-03-19 at 11.28.06.png" alt=""><figcaption><p>The user record normally returns a "name", but using <strong>unset</strong> has removed it.</p></figcaption></figure>

***
