# Schema Versioning

{% embed url="https://youtu.be/93IHBZH01L0" %}

You can leverage versioning to help you solve problems, see differences in your work, test ideas, and easily revert back to previous versions. It also tracks who from your team made a change, and when the change was made.&#x20;

Schema versioning is for database tables, API groups, API endpoints, functions, Addons, and background tasks. It allows you to easily roll back to a previous version in case you make a mistake.&#x20;

The Launch and Scales plans have schema versioning enabled. The Launch plan tracks the 3 most recent versions of each database table, API group, API endpoint, function, Addon, and background task. The Scale plan keeps a record of 20 versions.&#x20;

## **How to open schema version history**

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption><p>Open Version History by selecting Versions from the menu icon.</p></figcaption></figure>

View your active (current) version, select from a previous one to roll-back, and see who made a change and when.&#x20;

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption><p>Version History captures which is your active version, a history of previous versions with data on when the change was made and by who, and the ability to select a previous one.</p></figcaption></figure>

Version history will keep track of changes you make anywhere on a query, whether you make a change to a function or a filter. For API endpoints and functions, version history keeps a count of how many inputs, functions, and results were included in each version.

<figure><img src="../../.gitbook/assets/CleanShot 2024-01-12 at 14.50.31.png" alt=""><figcaption><p>Counts of each versions' inputs, functions, and results allow you to determine which version you may wish to roll-back to.</p></figcaption></figure>

Tasks will show how many functions and schedules there were for each version.

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption><p>Version history of a background task.</p></figcaption></figure>

Addons will show a count of how many inputs each version had.&#x20;

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption><p>Version history of an Addon.</p></figcaption></figure>

## Compare Differences

When selecting a previous version, you can view a screenshot of the version and the differences compared to the active version. This gives you full context of the different versions to see exactly what changes were made and whether or not you indeed want to revert to the previous version.

### APIs

For example, here is the live version of an API endpoint:

<figure><img src="../../.gitbook/assets/CleanShot 2024-01-12 at 14.55.47.png" alt=""><figcaption><p>Example of a live version of a function stack.</p></figcaption></figure>

After selecting Version History, we can see the different versions with some metadata and publish notes about each:

<figure><img src="../../.gitbook/assets/CleanShot 2024-01-12 at 14.56.46.png" alt=""><figcaption><p>The available versions of the API endpoint.</p></figcaption></figure>

By clicking on a version, in this example we selected version #2, a modal opens showing the differences present in the current live version #4 as compared to the state of version #2.

<figure><img src="../../.gitbook/assets/CleanShot 2024-01-12 at 14.59.00.png" alt=""><figcaption></figcaption></figure>

The difference comparison tells us a few things.

* The live version (indicated at the top) and when it was created.
* The email of who created the version.
* What differences the live version has compared to the old version selected.
* When the old version was created.
* Indications of what's been changed from the old version compared to the state of things in the live version.&#x20;

Lastly, you can easily navigate through the screenshots of the different old versions.

<figure><img src="../../.gitbook/assets/CleanShot 2024-01-15 at 10.34.29.gif" alt=""><figcaption><p>Navigate through the previous versions.</p></figcaption></figure>

### Database

Difference comparison in schema versioning is also available on the database. In addition to information about the version number, created at time, and creator. Difference comparison on the database will include differences in:

* Schema (columns)
* Indexes
* View

<figure><img src="../../.gitbook/assets/CleanShot 2024-01-15 at 13.13.09.png" alt=""><figcaption><p>An example of comparing version differences of a database table.</p></figcaption></figure>

