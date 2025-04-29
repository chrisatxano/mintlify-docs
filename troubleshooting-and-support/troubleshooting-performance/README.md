---
icon: turtle
---

# Troubleshooting Performance

### Debugging Performance Issues

502 errors when calling APIs or otherwise experiencing slow performance typically means that you are maxing out your instance resources. This means you should consider ways to increase performance. It is almost impossible to make a strict determination on “what package do I need” because everyone’s logic and data volume is different.

There are several variables to look at when addressing performance issues, including:

* The volume of API requests and the time between them
* The complexity of the business logic
* The amount of data being sent/received.

{% hint style="warning" %}
If your instance hits maximum resource usage, reported statistics may no longer be accurate.
{% endhint %}

{% content-ref url="when-a-single-workflow-feels-slow.md" %}
[when-a-single-workflow-feels-slow.md](when-a-single-workflow-feels-slow.md)
{% endcontent-ref %}

{% content-ref url="when-everything-feels-slow.md" %}
[when-everything-feels-slow.md](when-everything-feels-slow.md)
{% endcontent-ref %}
