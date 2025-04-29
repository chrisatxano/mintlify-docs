---
hidden: true
---

# XanoScript for Background Tasks

{% include "../.gitbook/includes/xs-beta-alpha-notice.md" %}

## Accessing XanoScript in your Background Tasks

Use the XanoScript toggle above the function stack to access XanoScript.

<figure><img src="../.gitbook/assets/CleanShot 2025-03-11 at 15.44.48.gif" alt=""><figcaption></figcaption></figure>

## What does a XanoScript Background Task look like?

This is a typical background task that loops through some database records on a cadence.

<figure><img src="../.gitbook/assets/CleanShot 2025-03-11 at 15.46.24.png" alt=""><figcaption></figcaption></figure>

This is what the XanoScript version looks like.

```javascript
task "My background task" {
  description = "Here's my description"
  stack {
    db.query user as user1
    foreach ($user1) {
      each as item {
        db.edit user {
          field_name = "id"
          field_value = $item.id
          data = {name: $item.name|upper}
        } as user2
      }
    }
  }

  schedule {
    events = [
      {
        starts_on: 2025-03-16 10:00:00+0000
        freq     : 604800
        ends_on  : 2025-03-30 05:00:00+0000
      }
    ]
  }
}
```

{% stepper %}
{% step %}
### Definition and settings

Give your task a name, and include a { at the end.

```
task "My background task" {
```

You can add a description as the first line inside of the braces.

```
  description = "Here's my description"
```
{% endstep %}

{% step %}
### The function stack

Please refer to [**XanoScript for Function Stacks**](fs/#part-2-the-function-stack) to learn how function stacks are written in XanoScript.
{% endstep %}

{% step %}
### Schedule

The scheduling of a background task begins with:

```
  schedule {
    events = [
```

Inside of the Events array, you'll want to add an object for each scheduling item. These objects contain a `starts_on` date/time, a `frequency` in seconds at which the task should run, and an `ends_on` date/time.

#### Scheduling Examples

A daily recurring task that starts on Monday, March 17, 2025 at 9:00 AM UTC and runs for five business days, ending on Friday, March 21, 2025 at 9:00 AM UTC. The frequency is 86400 seconds (1 day).

```json
{
  starts_on: 2025-03-17 09:00:00+0000
  freq     : 86400
  ends_on  : 2025-03-21 09:00:00+0000
}
```

This represents a weekly recurring task that starts on Sunday, March 16, 2025 at 10:00 AM UTC and runs for two weeks, ending on Sunday, March 30, 2025 at 5:00 AM UTC. The frequency is set to 604800 seconds (7 days).

```json
{
  starts_on: 2025-03-16 10:00:00+0000
  freq     : 604800
  ends_on  : 2025-03-30 05:00:00+0000
}
```
{% endstep %}
{% endstepper %}
