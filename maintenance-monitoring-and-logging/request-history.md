---
icon: comment-question
---

# Request History

## API Request History

From the dashboard, easily view the high-level statistics of the API request history from your entire Workspace. You can toggle between your database and top API requests to see which of your API endpoints are being hit the most. To the right, visualize your API request history with a graph displaying the statistics of the past 24 hours. Select 'View Request Details' to see a detailed view and history of each API call made in your Workspace.

You can expand each individual call to review detailed information including inputs, response and request headers, and the output. You can even drill-down on a per-user basis to see the activity of each user in your application. Furthermore, you can view failed API calls here in order to help debug what went wrong. Finally, you can use these details to understand Webhook payloads to make it easier to build API endpoints that receive Webhooks.

![](https://s3.amazonaws.com/olvy-production/media/organisation_a63a9786-9404-4582-9fdd-1f8e7b2cb6ca/images/0f9571bc-99ac-416c-bb9a-4e4ccf3edc66.gif)

You can also choose whether to see the request history for the specific branch you have active, or all branches, and download your request history as a CSV. If you would like to access your request history via API, you can do so using our [Metadata API](../xano-features/metadata-api/).

The Request History panel allows you to filter by the following metrics:

* **Time** - when the request was received
* **Duration** - how long the request took
* **Status** - if there was a standard code returned, filter by that status
* **Input / Output Size** - how much data was sent to or sent from the request

<figure><img src="../.gitbook/assets/CleanShot 2024-04-02 at 11.43.30.png" alt="" width="500"><figcaption></figcaption></figure>

API and Custom Function request history panels will also show the average runtime of all of your requests, giving you quick visibility into the state of your application.

<figure><img src="../.gitbook/assets/CleanShot 2024-09-11 at 14.51.30.png" alt=""><figcaption></figcaption></figure>

It doesn't stop at the entire Workspace level. From each API group, you can see the detailed history of the entire group. And from each API endpoint, you can see the history of the individual endpoint.

![](https://s3.amazonaws.com/olvy-production/media/organisation_a63a9786-9404-4582-9fdd-1f8e7b2cb6ca/images/29956df3-531c-4c0c-8334-e7c5f27db306.gif)

## Function Request History

[Custom Functions](../the-function-stack/functions/custom-functions.md) are similar to API endpoints in Xano, in the sense that they have the same No-Code API builder UI. However, custom functions can only be called by other internal function stacks in Xano whether that's an API, other function, or background task.

Functions also have a request history for any time a function is part of a live API request.&#x20;

First, open the request history of a function from the top right menu icon.

<figure><img src="../.gitbook/assets/CleanShot 2024-01-15 at 17.11.27.png" alt=""><figcaption><p>Open request history for a function</p></figcaption></figure>

Once opened, you can see all the requests from the past 24 hours.

<figure><img src="../.gitbook/assets/CleanShot 2024-01-15 at 17.13.19.png" alt=""><figcaption></figcaption></figure>

At the top, you can filter the requests by the time they occurred up until and by the duration of the how long the function took to run.

{% hint style="info" %}
The duration filter can be useful for identifying potential performance issues.
{% endhint %}

You can click on any of the requests to see the specific details of the inputs, output (response), and the function stack run time information.

<figure><img src="../.gitbook/assets/CleanShot 2024-01-15 at 17.17.15.png" alt=""><figcaption><p>Granular information on the function request.</p></figcaption></figure>

### Task History

Task history behaves a little differently than APIs and functions. Tasks maintain a history over 7 days instead of 24 hours. Tasks also do not deliver responses, so no response data will be recorded, but you will still be able to review the statement log, execution status, and the timing details.

### Middleware History

Middleware history will behave the same as API and function history.

### Triggers History

Request history for triggers behaves most similar to a task, as there is no output returned with a trigger. You can, however, review the inputs (new, old, action, datasource) and the timing details for each step.

## Managing Request History

### Branch Defaults

In your workspace settings, you can manage the request history for your entire workspace in the Branch Defaults panel.

<figure><img src="../.gitbook/assets/CleanShot 2024-04-02 at 12.30.06.png" alt="" width="375"><figcaption></figcaption></figure>

From this panel, we can define the request history defaults for each object type (query, function, task, middleware, trigger) that maintains history.

<figure><img src="../.gitbook/assets/CleanShot 2024-04-04 at 18.59.26.png" alt=""><figcaption></figcaption></figure>

* **Enable / Disable** - Performs the selected action on the object type
* **Function Statement Limit** - The number of statements to record for each object type. You can choose between:
  * No statements
  * 100 statements
  * 1,000 statements
  * 10,000 statements
  * Store all statements

{% hint style="warning" %}
Please note that request history utilizes your Database (SSD) storage. It is important to consider this when determining how many statements can be stored, or if they need to be stored at all.
{% endhint %}

#### Inheriting Settings

In each individual API, function, task, middleware, or trigger's settings, you can also control the request history for that object specifically.

By default, these will be set to **inherit**, which means it will obey the branch defaults. Otherwise, you can adjust this for specific objects as necessary.

## Clearing Request History

From your Instance settings, you have the option to manually clear your request history at any time.

<figure><img src="../.gitbook/assets/CleanShot 2024-04-02 at 12.26.46.png" alt=""><figcaption></figcaption></figure>

{% include "../.gitbook/includes/clearing-request-history.md" %}
