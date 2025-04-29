# Data Sources

{% hint style="info" %}
**Quick Summary**

Data sources are like separate versions of tables that contain different data sets — typically, they are separated into **live** or **production** data, and **test** data. The advantage to using separate data sources is so when you are building or iterating on your backend functionality, your actual live data stays safe. All data sources share the same [database schema](#user-content-fn-1)[^1]. They only differ by allowing different copies of the database records.
{% endhint %}

In Xano, data sources are essentially different sets of tables within your application's database. These data sources are crucial because they provide a way to separate the actual, live data that your business relies on from the data you use for testing or development purposes. This separation is beneficial as it ensures that any changes you make while testing new features do not affect the actual operational data.

Data sources typically have two main variants: **live data** and **test data**. You can have as many data sources as you'd like if additional separation makes sense for your backend. Live data is what your application uses in real-time—it’s the actual data that reflects real-world activities. In contrast, test data is used for experimentation and development, allowing developers to try out new features or changes without risking the integrity of the live data. By keeping these data sources distinct, Xano enables businesses to safely innovate and enhance their backend functionality without compromising the data they depend on every day.

## Creating Data Sources

{% stepper %}
{% step %}
### Access your data sources from the left-side navigation menu

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-01-02 at 08.02.27.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Add a new data source from the panel that opens

![](<../../.gitbook/assets/CleanShot 2025-01-02 at 08.04.38.png>)&#x20;
{% endstep %}

{% step %}
### Customize the new data source

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-01-02 at 08.04.38 (1).png" alt="" width="381"><figcaption></figcaption></figure></div>

Give it a name, and choose a distinct color to assign to the data source. The color assigned is important, as it is used throughout the Xano interface to remind you of the currently selected data source.

When you're done, click ![](<../../.gitbook/assets/CleanShot 2025-01-02 at 08.06.46.png>)
{% endstep %}
{% endstepper %}

***

## Using Data Sources

### Switching Data Sources

When you switch data sources, any action you take in Xano such as running and debugging a function stack will target the selected data source. It is recommended to use a test data source whenever possible to avoid accidentally impacting live application data.

Switch your data source at any time by clicking the data source indicator in the left-side navigation.

{% hint style="info" %}
This **does not** impact your live application; only the work you are performing inside of Xano.
{% endhint %}

### Setting a Data Source as Active

If you want your backend to use a different data source by default, select it from the data sources panel and choose ![](<../../.gitbook/assets/CleanShot 2025-01-02 at 08.16.43.png>). All future activity, unless otherwise specified using one of the alternative methods below, will use the active data source.

{% hint style="warning" %}
Proceed with caution. Changing the active data source can have unintended consequences on your live application. You do not need to change the **active data source** to work with other data sources in Xano.
{% endhint %}

### Targeting Specific Data Sources

When running function stacks in Xano or calling them externally, you can target a specific data source a number of ways. If you do not specify a data source, Xano will use the&#x20;

{% stepper %}
{% step %}
### Use the Set Data Source function

The **Set Data Source** function, located under **Utility Functions**, allows you to manually set a data source at any time. Any future database operations, such as reads and writes, will use the defined data source.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-01-02 at 08.10.14.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Send a data source header in your request

If you're calling one of your Xano APIs externally, you can specify the data source to use in the request headers.

The header to send is as follows. Replace 'test' with the name of the data source you wish to target.

```
X-Data-Source: test
```
{% endstep %}

{% step %}
### Send a URL argument in your request

If you don't have the ability to modify the request headers but still want to specify the data source in an external request, you can use a URL argument.

```
https://x1xx-abcd-efgh.a1.xano.io/api:x123abc/user?x-data-source=test
```
{% endstep %}

{% step %}
### Change the settings of the function stack

In some function stack types, such as background tasks, you can set the data source to target if you would like it to be different from the live data source.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-01-02 at 08.18.59.png" alt="" width="394"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### Migrating Data Between Data Sources

{% @arcade/embed flowId="OfK50mi7hWjjYeFmvDQC" url="https://app.arcade.software/share/OfK50mi7hWjjYeFmvDQC" %}

{% stepper %}
{% step %}
### Access the Migration panel

Click the data sources indicator and choose :gear: **Manage Data Sources**. In the panel that opens, click Migrate.
{% endstep %}

{% step %}
### Select the source and destination data source.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-01-02 at 08.38.28.png" alt="" width="326"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Select the tables to migrate.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-01-02 at 08.39.10.png" alt="" width="329"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Confirm your changes to begin the migration.

You can check the progress of the migration via the indicator in the left-hand navigation. You'll also see a banner at the top of the screen once the migration has completed.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-01-02 at 08.40.28.png" alt=""><figcaption></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/CleanShot 2025-01-02 at 08.40.53.png" alt=""><figcaption></figcaption></figure>


{% endstep %}
{% endstepper %}









[^1]: **Database schema** is the collection of fields that make up the specific table.
