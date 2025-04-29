# Database Transaction

## What are database transactions?

Database transactions allows you to treat a set of functions as a whole. This means that every function must succeed properly in order for all of them to be executed. Usually, you would use this if you have two or more database operations that are mission critical for the end result.

> Let's consider a financial application as an example. During a money transfer, if money is successfully withdrawn from one account but something goes wrong with the deposit to the second account, then you would want the entire transfer to be cancelled. Otherwise, the money would still be withdrawn from the first account even though it was never received by the second account.

{% hint style="warning" %}
Only **database operations** are considered when determining whether or not to roll back the changes made to the database. This means that for other function types, like conditionals or data transformation, those can still encounter errors without impacting the database transaction.
{% endhint %}

## Using Database Transactions

{% @arcade/embed flowId="SbCUI1OkMs2paTuaucOa" url="https://app.arcade.software/share/SbCUI1OkMs2paTuaucOa" %}



{% stepper %}
{% step %}
### Add a Database Transaction function to your function stack.

There are no additional settings for a database transaction, so just click Save on the panel that opens.
{% endstep %}

{% step %}
### Add steps to the database transaction.

You can click and drag to move existing steps into the transaction, or add new functions.


{% endstep %}
{% endstepper %}

