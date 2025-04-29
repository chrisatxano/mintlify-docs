# Xano Link

{% hint style="success" %}
The Xano Link feature is an additional add-on. Please contact your Xano representative or support for details.&#x20;
{% endhint %}

### What is Single-Tenancy vs Multi-Tenancy

Single-tenancy means that a user is on their own dedicated server environment. Their data is completely separated and isolated from any other user. A multi-tenancy environment means users share the same server resources across a shared environment.

### How Xano Link Works

Xano Link is a feature that allows you to use a separate workspace for each client (aka tenant). Each workspace is a separate environment with its own copy of all schema, which includes the database, API, Addons, Functions, and Background Tasks. This allows for a single-tenant solution to be built on Xano.&#x20;

{% hint style="info" %}
Xano Link still shares the same Instance server resources across all tenants, so Link is not a true form of single-tenancy. However, it is a similar solution through data separation and workspace isolation.&#x20;
{% endhint %}

Xano Link provides the Instance owner an interface where they can publish one source workspace to many client workspaces. Changes or updates can be made to the source workspace and published to many client workspaces. This is a manual process so it requires keeping track of which client workspaces need to be updated. It is recommended to use naming conventions for the workspaces to help keep track (e.g. product\_name:source, product\_name:user\_id).&#x20;

Xano Link can be accessed from the settings of the source workspace.

<figure><img src="../../.gitbook/assets/CleanShot 2023-03-22 at 13.47.50.png" alt=""><figcaption><p>Accessing Xano Link</p></figcaption></figure>

Once inside, you can choose to Link APIs, functions, addons, and database tables. Take note of the **Select All/None** and **Auto include dependencies** options to assist in ensuring that the Link only merges the data you want. You also have the option to include records from the selected database tables, or only merge the schema.

{% hint style="info" %}
**Select All/None** allows you to quickly bulk select or de-select items.

**Auto include dependencies** will scan and auto-include in the Link any items that are dependent on what you have already selected. For example, if you are choosing API endpoints that include custom functions, the functions will also be merged without you having to select them manually.
{% endhint %}

<figure><img src="../../.gitbook/assets/CleanShot 2023-03-22 at 13.49.24.png" alt=""><figcaption></figcaption></figure>

### Merging Database Tables

<figure><img src="../../.gitbook/assets/CleanShot 2023-03-22 at 14.32.53.png" alt=""><figcaption><p>Choosing Database Tables and Records</p></figcaption></figure>

You have the option to choose specific tables and records to merge when using Xano Link. Click on the record count to select specifically which records you want to merge, or select all.

<figure><img src="../../.gitbook/assets/CleanShot 2023-03-22 at 14.35.05@2x.png" alt=""><figcaption><p>Choosing records to merge</p></figcaption></figure>

{% hint style="danger" %}
When you use Xano Link to merge database tables, and the destination workspace already has that table created, you will need to change the GUID of the destination table to match, otherwise you will have duplicate tables. The steps below will outline how to change the GUID. Please proceed with caution as you change these advanced settings.
{% endhint %}

1. Head to the **source table**, click the three dots in the top-right, and choose Security.

<figure><img src="../../.gitbook/assets/CleanShot 2023-03-22 at 14.16.59@2x.png" alt=""><figcaption></figcaption></figure>

2. Click "Show Advanced Settings" and copy the GUID that is shown in the box.

<figure><img src="../../.gitbook/assets/CleanShot 2023-03-22 at 14.20.19.png" alt=""><figcaption><p>Copying the GUID from the source table</p></figcaption></figure>

3. After you've copied the GUID, head to the **destination table** in the new workspace, and replace the GUID with the copied value from the source table and save your changes.

Once you're ready to publish an update select which client workspaces the update should be pushed to. You also have the option to merge the newly created branch with whatever branch in the target workspace is set to live, and / or set the newly created branch as the live branch.

{% hint style="info" %}
**Merge New Branch with existing Live Branch** will merge the newly created branch with the branch in the destination workspace that is currently set to live.

**Set New Branch Live** will set the newly created branch as the live branch immediately.
{% endhint %}

<figure><img src="../../.gitbook/assets/CleanShot 2023-03-22 at 13.52.50.png" alt=""><figcaption></figcaption></figure>

#### Customization

Customization on a per-client basis is possible by using **additional** tables or APIs that are independent of the source workspace. Customization to the schema from the source workspace would get overwritten with any new updates.&#x20;

### Compare Differences

Xano Link allows you to view and compare differences before merging a branch from the source workspace into a branch from the destination workspace.

Be sure to select the Merge New Branch option and the destination workspace before selecting "view.

<figure><img src="../../.gitbook/assets/CleanShot 2024-01-17 at 10.20.33.png" alt=""><figcaption></figcaption></figure>

By selecting view, you can see which items contain differences.

<figure><img src="../../.gitbook/assets/CleanShot 2024-01-17 at 10.23.16.png" alt=""><figcaption><p>Changed items.</p></figcaption></figure>

By selecting "changes" next to an item, you can see a snapshot of the differences.

<figure><img src="../../.gitbook/assets/CleanShot 2024-01-17 at 10.14.34.png" alt=""><figcaption></figcaption></figure>

In the above example there are six changes:

1. Created\_at input deleted
2. Name input edited
3. Category input edited
4. Value input edited
5. API Request function added
6. Create Variable function added
