# Loops

Loops are used to iterate over a set of items, or run a set of steps a certain number of times.

There are a few different kinds of loops that you can use in Xano.

## For Each Loop

A For Each loop is designed to iterate over a list of items, such as all records returned by a database query, or items returned from an external API request.

{% @arcade/embed flowId="q3YxulNkiKFFppNHIa8N" url="https://app.arcade.software/share/q3YxulNkiKFFppNHIa8N" %}

{% hint style="info" %}
If you are iterating through a list of database records, set the return type in the query to **stream** to enable super memory-efficient looping. This is especially helpful the larger the list is.
{% endhint %}

{% stepper %}
{% step %}
### Add a For Each loop function.


{% endstep %}

{% step %}
### Specify the list that the loop will iterate through.

Select the variable that contains your list of items.\
![](<../../../.gitbook/assets/CleanShot 2025-01-13 at 10.19.49.png>)
{% endstep %}

{% step %}
### Define the variable that will hold each item as the loop runs.

By default, this is called <mark style="color:orange;">**item**</mark>, but you can name it whatever you'd like. Use this variable inside of your loop.\
![](<../../../.gitbook/assets/CleanShot 2025-01-13 at 10.20.37.png>)
{% endstep %}

{% step %}
### Add functions inside of your loop.

Make sure these steps target the right variable.\
![](<../../../.gitbook/assets/CleanShot 2025-01-13 at 10.21.15.png>)
{% endstep %}
{% endstepper %}

## For Loop

A For loop is used to repeat a stack of steps a certain number of times.

Refer to the For Each loop instructions to see how it works. The only difference between a For and a For Each loop is...

* In a For loop, you need to specify the number of times the loop runs.\
  ![](<../../../.gitbook/assets/CleanShot 2025-01-13 at 10.11.19.png>)
* Because we aren't building the loop against a list of items directly, we don't have a variable that houses the individual item. Instead, Xano keeps track of which iteration is running inside of an **index variable**, which you can set here.\
  ![](<../../../.gitbook/assets/CleanShot 2025-01-13 at 10.16.47.png>)

## While Loop

A While loop is used to repeat a set of steps infinitely as long as the condition(s) defined evaluate as true.

{% hint style="warning" %}
Proceed with caution when using While loops, as they can not be easily stopped once started.

To ensure that your loop works as intended, make sure to **stop the loop with a Break statement** while testing and debugging.

If you are concerned that you have entered an infinite loop and want to break it, learn how to restart your instance [here](../../../xano-features/instance-settings/#maintenance).
{% endhint %}

You'll use the expression builder to define the conditions that tell the loop whether or not it should continue.

{% include "../../../.gitbook/includes/expression-builder.md" %}

## Additional Loop Functions

### Loop: Break

Breaks the currently running loop, meaning the loop is exited and the next function will run.

### Loop: Continue

Immediately begins executing the next iteration of the loop. This is very useful for conditionals inside of loops that determine what happens to the item being iterated through.

### For Each Loop: Remove Entry

This will remove the item being iterated through from the parent list.









