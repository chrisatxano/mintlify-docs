---
description: >-
  Use async functions to ensure that your custom functions execute exactly as
  you intend
---

# Async Functions

## What are async functions?

When working with custom functions in Xano, you can choose to have them execute asynchronously. An async function works like a [background task](../background-tasks.md), allowing your main process to continue without waiting for the custom function to finish.

## When should I use async functions?

Asynchronous execution can be particularly beneficial in scenarios where you don't want certain tasks to hold up the entire process. For instance, if you're running a complex data fetch or a time-consuming operation, doing it asynchronously means your main application or interface remains responsive to user inputs while the background operation continues independently. This can enhance user experience by reducing wait times.

Here are a few examples of when to use async functions:

* **Loading Data:** When fetching data from a server, such as pulling in user information or loading a list of products, async functions allow the page to display its initial content quickly without waiting for the entire data request to complete.
* **File Uploads:** Starting a file upload process without freezing the interface lets users continue interacting with the application while the file is being processed.
* **Notification Systems:** Sending notifications through email or messaging services asynchronously ensures that users continue their tasks without interruption while the messages are sent in the background.

## Enabling Async Execution

{% stepper %}
{% step %}
### Insert a custom function into your function stack.

If you haven't built any custom functions yet, you can review our documentation on them [here](../../functions/custom-functions.md).
{% endstep %}

{% step %}
### Click ![](<../../../.gitbook/assets/CleanShot 2025-02-13 at 08.00.40.png>)on the function to change the execution mode.


{% endstep %}

{% step %}
### If necessary, retrieve the output of the async function.

If a function is set to async, it will return an ID that represents that execution, similar to the value shown below.

```
6f10cc09-d3e0-4ead-9a98-a0bc66bbe673
```

You can use the **Async Function Await** function to retrieve the output of the function once execution completes. Just provide it with an array of the ID(s) returned when the function runs.

<div align="left"><figure><img src="../../../.gitbook/assets/CleanShot 2025-02-13 at 08.03.59.png" alt="" width="485"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}







\


