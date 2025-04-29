# Comparison

​Comparison filters are useful for comparisons and checking data types, especially for conditional logic. They will result in a true or false boolean value.

* [**bitwise\_not**](comparison.md#bitwise_not) **-** Returns the existing value with its bits flipped.
* [**equals**](comparison.md#equals) **-** Returns a boolean if both values are equal.
* [**even**](comparison.md#even) **-** Returns whether or not the value is even.
* [**greater\_than**](comparison.md#greater_than) **-** Returns a boolean if the left value is greater than the right value.
* [**greater\_than\_or\_equal**](comparison.md#greater_than_or_equal) **-** Returns a boolean if the left value is greater than or equal to the right value.
* [**in**](comparison.md#in) **-** Returns whether or not the value is in the array.
* [**is\_array**](comparison.md#is_array) **-** Returns whether or not the value is a numerical indexed array.
* [**is\_bool**](comparison.md#is_bool) **-** Returns whether or not the value is a boolean.
* [**is\_decimal**](comparison.md#is_decimal) **-** Returns whether or not the value is a decimal value.
* [**is\_empty**](comparison.md#is_empty) **-** Returns whether or not the value is empty ("", null, 0, \[], {}).
* [**is\_int**](comparison.md#is_int) **-** Returns whether or not the value is an integer.
* [**is\_null**](comparison.md#is_null) **-** Returns whether or not the value is null
* [**is\_object**](comparison.md#is_object) **-** Returns whether or not the value is an object.
* [**is\_text**](comparison.md#is_text) **-** Returns whether or not the value is text.
* [**less\_than**](comparison.md#less_than) **-** Returns a boolean if the left value is less than the right value
* [**less\_than\_or\_equal**](comparison.md#less_than_or_equal) **-** Returns a boolean if the left value is less than or equal to the right value
* [**not**](comparison.md#not) **-** Returns the opposite of the existing value evaluated as a boolean
* [**not\_equals**](comparison.md#not_equals) **-** Returns a boolean if both values are not equal
* [**odd**](comparison.md#odd) **-** Returns whether or not the value is odd

#### **bitwise\_not**

Returns the existing value with its bits flipped.

#### **equals**

Returns a boolean if both values are equa&#x6C;**.**

![var\_2 is also 7, so in this example, the result will be true.](<../../.gitbook/assets/CleanShot 2022-01-13 at 15.01.13.png>)

#### even

Returns whether or not the value is even, this returns a response of true or false.

![In this example, we have a variable with the int 23 after applying the even filter the variable becomes false.](<../../.gitbook/assets/CleanShot 2022-01-13 at 15.04.49.png>)

#### greater\_than

Returns a boolean if the left value is greater than the right value.

![The result will be true because 23 is greater than 5.](<../../.gitbook/assets/CleanShot 2022-01-13 at 15.07.33.png>)

#### greater\_than\_or\_equal

Returns a boolean if the left value is greater than or equal to the right value.

![The result will be true because 23 is equal to 23.](<../../.gitbook/assets/CleanShot 2022-01-13 at 15.09.29.png>)

#### in

Returns whether or not the value is in the Array, this returns a response of true or false.

![var\_2 is the array \[1,2,7,23\]. The result will be true because 23 is IN the array.](<../../.gitbook/assets/CleanShot 2022-01-13 at 15.14.49.png>)

#### is\_array

Returns whether or not the value is a numerical indexed array.

![var2 is the array \[1,2,7,23\]. The result will be true because var\_2 is an array.](<../../.gitbook/assets/CleanShot 2022-01-13 at 15.19.49.png>)

#### is\_bool

Returns whether or not the value is a boolean.

![False is a boolean so the result will be true.](<../../.gitbook/assets/CleanShot 2022-01-13 at 15.21.41.png>)

#### is\_decimal

Returns whether or not the value is a decimal value.

![9.86 is a decimal so the result will be true.](<../../.gitbook/assets/CleanShot 2022-01-13 at 15.22.46.png>)

#### is\_empty

Returns whether or not the value is empty ("", null, 0, \[], {}).

![The result will be true because the value is an empty object {}.](<../../.gitbook/assets/CleanShot 2022-01-13 at 15.25.25.png>)

#### is\_int

Returns whether or not the value is an integer.

![-9 is an integer so the result will be true.](<../../.gitbook/assets/CleanShot 2022-01-13 at 15.28.01.png>)

#### is\_null

Returns whether or not the value is null, this returns a response of true or false.

![In this example, we have a variable with the int 23 after applying the is\_null filter the variable becomes false.](<../../.gitbook/assets/CleanShot 2022-01-13 at 15.40.32.png>)

#### is\_object

Returns whether or not the value is an object.

![The result is true because the value is an object {}.](<../../.gitbook/assets/CleanShot 2022-01-13 at 16.17.50.png>)

#### &#x20;is\_text

Returns whether or not the value is text.

![Hello there is a text string so the result will be true.](<../../.gitbook/assets/CleanShot 2022-01-13 at 16.19.56.png>)

#### less\_than

Returns a boolean if the left value is less than the right value

![The result will be true because 5 is less than 12.](<../../.gitbook/assets/CleanShot 2022-01-13 at 16.21.54.png>)

#### less\_than\_or\_equal

Returns a boolean if the left value is less than or equal to the right value.

![5 is not less than or equal to 1 so the result will be false.](<../../.gitbook/assets/CleanShot 2022-01-13 at 16.23.18.png>)

#### not

Returns the opposite of the existing value evaluated as a boolean.

![In this example, we first have the odd filter applied to 5 which results in a true boolean. Then, the not filter is applied resulting in the opposite existing value - making the result false.](<../../.gitbook/assets/CleanShot 2022-01-13 at 16.25.56.png>)

#### not\_equals

Returns a boolean if both values are not equal.

![The result will be true because 5 is not equal to 6.](<../../.gitbook/assets/CleanShot 2022-01-13 at 16.28.13.png>)

#### odd

Returns whether or not the value is odd, this returns a response of true or false.

![5 is an odd number so the result will be true.](<../../.gitbook/assets/CleanShot 2022-01-13 at 16.29.47.png>)
