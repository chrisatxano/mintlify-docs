# Maintenance

## How do I perform maintenance on my Xano instance?

All paid plans include access to the Maintenance panel, accessible via your instance settings. There are different maintenance operations you can perform to help troubleshoot issues you might be having in Xano, or to manage your database storage.

## Accessing the Maintenance Panel

Head to your instance settings from your instance selection screen and choose Maintenance.

<figure><img src="../../.gitbook/assets/CleanShot 2023-05-22 at 11.50.15.png" alt=""><figcaption></figcaption></figure>

From the next panel that appears, you can choose between several maintenance options.

## **Clear Internal Cache**

This maintenance action clears the internal cache within the instance. This does not affect any drafts or redis storage. You should use this option first if you are experiencing any or multiple of the following symptoms:

* Slow loading in Xano or function stacks not loading
* APIs not responding or responding with strange errors such as "invalid app"

## **Database Maintenance**

* [**Analyze**](maintenance.md#analyze)
* [**Vacuum**](maintenance.md#vacuum)

Database maintenance is automatically done daily but Xano does offer ways to manually run PostgreSQL analyze and vacuum commands through the Instance Maintenance panel.\
\
PostgreSQL's VACUUM and ANALYZE functions are essential maintenance tasks for optimizing database performance. \
\
Together, VACUUM and ANALYZE help keep the database running smoothly by managing storage and providing accurate statistics for optimal query planning and execution.

### Analyze

ANALYZE gathers statistics about the data distribution in tables, enabling the query optimizer to generate efficient execution plans. It updates the query planner's knowledge of the data, improving query performance by enabling better index selection and join strategies.

### Vacuum

VACUUM reclaims storage space by removing obsolete or dead data that remains after updates or deletions. It helps prevent performance degradation caused by fragmentation and frees up disk space.

#### Partial VACUUM

This command analyzes and cleans up the database, but it does not necessarily reclaim all available disk space. It marks the space previously occupied by deleted rows as reusable for future inserts and updates. VACUUM also updates statistics used by the query planner to improve query performance.

#### Full VACUUM

{% hint style="warning" %}
**Full VACUUM requires at least 50% free storage space before continuing. Proceeding with a Full VACUUM without enough free storage can fail or cause instance downtime.**
{% endhint %}

This command performs a more thorough cleanup compared to partial. It reclaims all available disk space by rewriting the entire table and indexes from scratch. This process can be more resource-intensive and time-consuming, as it involves copying the data to a new file and rebuilding the indexes. Full VACUUM can significantly improve disk space utilization but **may cause downtime** for larger tables.

## Server Maintenance

Your Xano instance is separated into 'pods' that are all responsible for their own functions. Use the guide here to determine what should be restarted and when. You can also use this panel to view the status of your backend. Use the ![](<../../.gitbook/assets/CleanShot 2025-03-03 at 18.42.15.png>) button to check the progress of any restarts performed.

{% hint style="info" %}
If you aren't sure which option to choose, please reach out to support. None of these options are typically destructive in any capacity, but we can provide specific guidance based on the behaviors you are observing.
{% endhint %}

### Backend

This is a full reboot of your Xano instance. A good, quick catch-all for any issues you might be seeing. This option is also appropriate for stopping things like infinite loops.

### Database

If you are experiencing issues with your database, or want to halt an ongoing database transaction, such as an import or bulk operation.

### Frontend

If you are experiencing issues with the Xano UI, you can try restarting it from here.

### Node

This pod is responsible for some backend operations and Lambda functions.

### Realtime

This pod is responsible for our [realtime](broken-reference) functionality

### Redis

This pod is responsible for caching both to facilitate Xano functionality, and caching functions inside of your function stacks. Restarting this pod can assist with various issues related to performance and downtime if the cache is full and unable to clear automatically. If you believe you are experiencing issues related to Redis, please reach out to support.

### Task

This pod is responsible for running your background tasks. You can restart this pod if you'd like to halt any ongoing tasks.

{% hint style="warning" %}
Please note that restarting your tasks will not impact the schedule of those tasks — they will continue to execute as defined. Make sure to disable any tasks either before or after the restart if you want to make sure they do not run again until you are ready.
{% endhint %}

## Async Function Maintenance

If you are utilizing asynchronous functions and are experiencing issues such as your functions not completing execution, you can clear the asynchronous queue from this panel.

Use the ![](<../../.gitbook/assets/CleanShot 2025-03-03 at 18.44.19.png>) option to clear any queued functions from memory.

## Request History

Use this option to manually clear your request history and free up space in your database.

{% hint style="info" %}
Request history is typically purged automatically, but you can clear it anytime from here if you find it necessary.

Make sure to define branch defaults for your request history so you're only logging what you need.
{% endhint %}

{% include "../../.gitbook/includes/clearing-request-history.md" %}















