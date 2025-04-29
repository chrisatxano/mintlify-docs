# Triggers

{% hint style="info" %}
**Quick Summary**

Triggers are workflows that can run based on other events that happen in your workspace. Xano offers triggers for:

* Database operations (adds, edits, deletes)
* Realtime events
* Workspace events (currently limited to branching operations)
{% endhint %}

## What are triggers?

Triggers in Xano are workflows that will run only when triggered by another event. You can build triggers for the following events.

| Event Type    | Event                                 |
| ------------- | ------------------------------------- |
| **Database**  | New records                           |
|               | Record edits                          |
|               | Record deletes                        |
|               | Table truncate (deleting all records) |
| **Realtime**  | Channel events                        |
| **Workspace** | New branch                            |
|               | Branch merge                          |
|               | Live branch change                    |

## Accessing and Creating Triggers

{% stepper %}
{% step %}
### Database Triggers

You can find database triggers on each table by clicking the ![](<../../.gitbook/assets/CleanShot 2025-01-03 at 09.34.46.png>) settings icon in the top-right corner.

Click ![](<../../.gitbook/assets/CleanShot 2025-01-03 at 09.35.22.png>) to create a new database trigger.

You can specify what [data sources](../../the-database/database-basics/data-sources.md) the trigger will execute on. If no data source is set, then it will execute on all data sources.

Select the **actions** that will activate this trigger.

**Inserts**\
Any time a record is added to the table

**Updates**\
Any time a record is edited

**Deletes**\
Any time a record is deleted

**Truncates**\
When the content of the database table is cleared

Finally, you can set up custom filters so that the trigger only runs if the record matches certain conditions. For example, if you only want the trigger to run if a new order is created for a user, or a new user is created with a certain role.

***

Database triggers have predefined inputs that contain all of the information you'll need to build a workflow based on the database event.

**new**\
This is the contents of the new record — if you're adding a record, this will contain the contents of the new record, and if you're updating a record, this will contain the contents of the updated record. On deletes and truncates, this will be empty.

**old**\
This is the contents of the old record — if you're deleting or editing a record, this will contain the contents of the record before the change. On inserts and truncates, this will be empty.

**action**\
The action that activated the trigger

**data source**\
The datasource this trigger has been executed against

***
{% endstep %}

{% step %}
### Realtime Triggers

Realtime triggers are created per-channel. Once you've created a realtime channel, click the ![](<../../.gitbook/assets/CleanShot 2025-01-03 at 09.45.44.png>)button to create a new channel trigger.

Select the **actions** that will activate the trigger.

**Message**\
Any time a new message is sent to the channel

**Join**\
Any time a new connection is made to the channel

***

Realtime triggers have predefined inputs that contain all of the information you'll need to build a workflow based on the realtime event.

**Action** and **Command**\
This will be either 'join' or 'message' depending on what was responsible for executing the trigger.

_**Action** and **Command** currently have the same values, but behind the scenes, the values do not come from the same source. We maintain two separate inputs for the purpose of expanding this functionality in the future._

**Channel**\
The channel that this command or message is being sent to

**commandOptions**\
Any options that are provided with the command being sent to the channel

**payload**\
The contents of the command, such as the message body

**client**\
An internal client ID

***
{% endstep %}

{% step %}
### Workspace Triggers

Workspace triggers can be created to execute workflows based on certain workspace-wide events. Currently, these are limited to branch changes.

You can find workspace triggers by clicking the ![](<../../.gitbook/assets/CleanShot 2025-01-03 at 09.34.46.png>) settings icon in the top-right corner of your workspace dashboard.

Click ![](<../../.gitbook/assets/CleanShot 2025-01-03 at 09.50.13.png>) to create a new workspace trigger.

Select the **action(s)** that will execute this trigger.

**Branch Live**\
Any time a branch status is set to live

**Branch Merge**\
When a branch is merged

**Branch New**\
When a new branch is created
{% endstep %}
{% endstepper %}
