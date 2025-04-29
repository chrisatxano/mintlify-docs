# Transform

### Lambda Filters

Higher Order Filters operate on a list of items and process a Lambda individually for each item. The Lambda has access to several context variables that represent various states of the iteration process. Details of each of these context variables are mentioned below.

## map

* **$this** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed
* **$parent** - the context variable that represents the entire array with all of its elements.

The map filter is extremely powerful because it allows you to easily transform the elements of one array into another. Here is an example of using using a map on a variable that contains a list of user objects. We will convert that into a list of user usernames.

![List of user objects.](<../../.gitbook/assets/CleanShot 2022-03-31 at 14.58.41.png>)

![Map filter used to transform the list of user objects](<../../.gitbook/assets/CleanShot 2022-03-31 at 14.59.38.png>)

![The result is the list of usernames.](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.00.32.png>)

```javascript
return $this.username;
```

The above example changes the type of the array. Previously it was an array of user objects, but now it is an array of text. You can also use the map filter to return a subject each object while still maintaining the object type.

![](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.07.50.png>)

```javascript
return {id: $this.id, username: $this.username};
```

## some

* **$this** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.

The some filter (also called **has** or **has any element**) allows you to easily determine if there is at least one element of an array that matches your condition. A common use case would be having an array of role objects and you wanted to see if a certain role was present.

![List of user objects.](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.14.56.png>)

![This will generate a true value if a role of admin is found in the array and a false value if it is not.](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.11.27.png>)

```javascript
return $this.role == "admin";
```

## every

* **$this** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.

This filter (also called **find every element**) is identical to the **some** filter except that it requires that all elements of the array match the condition. A common use case would be a list of products and determining if they all have a price greater than 10.

![In this example, Every filter will determine if every price in the products array is greater than 10.](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.14.03.png>)

```javascript
return $this.price > 10;
```

## find

* **$this** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.

This filter (also called **find first element**) is identical to the **some** filter except that it returns the actual element that matches the condition instead of returning whether or not it was found. A common use case would be finding the first product that has a price greater than 10.

![In this example, the first product object with a price greater than 10 will be returned. ](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.27.05.png>)

```javascript
return $this.price > 10;
```

## findIndex

* **$this** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.

This filter (also called **find first element index**) is identical to the **some** filter except that it returns the index of the element that matches the condition instead of returning whether or not it was found. A common use case would be finding the index of the first product that has a price greater than 10.

![In this example, findIndex will return the first element index where the price is greater than 10.](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.31.26.png>)

```javascript
return $this.price > 10;
```

## filter

* **$this** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.

This filter (also called **find all elements**) is identical to the **find** filter except that it returns it returns all elements that match the condition. Even if there is only one match, it would return an array of one. A common use case would be finding all products that have a price greater than 10.

![In this example, filter will return all elements where the price is greater than 10.](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.32.25.png>)

```javascript
return $this.price > 10;
```

## reduce

* **$this** - the context variable that represents the element of the array being processed.
* **$index** - the context variable that represents the numerical index of the element of the array being processed.
* **$parent** - the context variable that represents the entire array with all of its elements.
* **$result** - the context variable that is used to represent the result of the previous iteration or the initial value on the first iteration.

This reduce filter is a bit more complicated than the higher order examples because its environment changes each time the Lambda is processed. The reduce filter starts out with an initial value (normally 0) and then is responsible for turning the array into a single result. Because of this, there is a new context variable named `$result` which can be referenced. The `$result` variable is the state of the reduction process. The first time the Lambda runs, the `$result` variable is the same as the initial variable. The return statement of the Lambda will be the `$result` variable for the 2nd iteration and so forth until there are no iterations left. The final value of the `$result` variable will be assigned to whatever is referencing the reduce filter.

The details above may feel like a mouthful, but things should start to click when seeing a few examples.

The most basic example would be sum a list of values.

![Here's an example array of \[1, 10, 100\].](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.40.36.png>)

![In this example, the reduce filter will result in a sum of the array or 111.](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.47.52.png>)

Using an initial value of 0 we would get the sum of numbers with the following Lambda.

```javascript
return $this + $result;
```

If the above example was a list of objects instead of a list of scalar values, then the Lambda would change slightly.

![In this example, we have an array of objects.](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.50.01.png>)

![Using the reduce filter in this example, we sum the values of num for each object resulting in 111.](<../../.gitbook/assets/CleanShot 2022-03-31 at 15.50.58.png>)

```javascript
return $this.num + $result;
```

###
