---
hidden: true
---

# Adjust Server Performance

### How does Xano scale to meet demand?

Once you're on the Scale Plan, you're on an instance that has dedicated resources, can handle multiple concurrent operations, and has the ability to scale to millions of users.  There are a lot of nuances around scaling your instance to meet high traffic demands, however, there are two basic infrastructure components that can be scaled up:

**API Nodes**&#x20;

Xano leverages API nodes to handle the business logic demands of your application.  You might have thousands of users on your app just browsing which doesn't require much, but when they all start hitting the API or complex endpoints that you might have created, you'll need more API nodes to distribute the load and keep things running smoothly.

**Database Nodes**

Similar to how the API nodes work, a Database node powers how many users can request information from your database at the same time.  The more users you have accessing the Database at the same time, the more power you'll need to service their requests.

**Database Horizontal Scaling** (Enterprise Plans Only)

Vertical scaling or "Scaling up" usually involves adding more power (e.g. CPU or RAM) to meet the demands of your users. This tends to work just fine as long as it is possible to keep increasing resources, but eventually, you hit a limit with today's technology and have to rely on scaling horizontally to keep up with usage requirements. Horizontal scaling or "Scaling out" usually means scaling by adding more nodes to your pool of resources. There are different methods of horizontal scaling: database replicas and data sharding. Both options are possible with Xano due to the PostgreSQL database engine.&#x20;

_Why Scale a Database horizontally?_

Imagine that you have a sheet of paper that users can request copies of.  Each time a user makes a request, you have to hit the button on the copier and wait for the copy to print before giving it to them.  Now imagine 100,000,000 users asking for a copy at the same time. Single node Databases simply aren't built to handle this many requests no matter how powerful it is, so you'll need to leverage read replicas and region-specific delivery to ensure things are as real-time as possible.

### Upgrading your Scale plan

We can add more power to your existing scale plan by adding more capacity through node quantity or vCPUs.&#x20;

<table><thead><tr><th width="150">Scale Plan</th><th>API Nodes</th><th width="164">Database Nodes</th><th>Cost</th></tr></thead><tbody><tr><td>Scale 1x</td><td><strong>2 x (1x vCPU)</strong> </td><td><strong>1 x (2x vCPU)</strong></td><td>$225/mo</td></tr><tr><td>Scale 2x </td><td><strong>4 x (1x vCPU)</strong> </td><td><strong>1 x (4x vCPU)</strong></td><td>$405/mo (10% off)</td></tr><tr><td>Scale 4x </td><td><strong>8 x (1x vCPU)</strong></td><td><strong>1 x (8x vCPU)</strong></td><td>$765/mo (15% off)</td></tr><tr><td>Scale 8x</td><td><strong>16 x (1x vCPU)</strong></td><td><strong>1 x (16x vCPU)</strong></td><td>$1,440/mo (20% off)</td></tr><tr><td>Scale ++</td><td>custom</td><td>custom</td><td>custom</td></tr></tbody></table>

Xano's servers are hosted on Google Cloud and we use their Compute engine to scale

{% hint style="info" %}
[Read more about Google Cloud's Compute Engine (vCPUs](https://cloud.google.com/compute/docs/faq))
{% endhint %}

### What package do I need?

Not all projects are created equal, so this is a difficult question to answer. For example, 100 API requests per second for project A might be dramatically different than 100 API requests per second for project B. This is because different types of business logic can be layered inside an API request making one more complicated and resource-intensive than another. If you aren't sure which package you need and **are already on a Scale plan**, our support team can help gradually ease you into a plan by temporarily upgrading you to a higher package so you can test the performance. We can repeat this process until we find something that works for your needs.

If you would like to explore which Scale package will meet your requirements, schedule a time with our Support team to experiment with these packages.

### I'm ready to upgrade - what's next?

You can simply log into Xano and click on the [Billing](https://app.xano.com/admin/billing) menu item.  Click change plan, and you'll be able to upgrade your scale plan.

If you have more comprehensive needs, we'd recommend checking out our [Enterprise Plan](broken-reference) which has features such as auto-scaling, horizontal database scaling, and more.&#x20;
