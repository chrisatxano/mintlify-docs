# Tenant Center

{% hint style="info" %}
## Quick Summary

The Tenant Center allows you to deploy your current workspace to multiple tenant environments. Think of your tenants as things like your **stage** or **dev** environment, and **your users**.

Each tenant is given a separate, isolated database and business logic, and you have the ability to selectively roll out new releases to one or more users simultaneously.
{% endhint %}

## What is the Tenant Center?

The Tenant Center is designed to bring a more traditional CI/CD[^1] workflow into Xano.

With Tenant Center, you can:

* Easily manage separate development, stage, and production environments
* Isolate your users into separate environments and roll out new releases to them selectively, or all at once
* Organize your users into different groups to enable easier deployment of beta or exclusive features to select users

## How do I use the Tenant Center?

### Creating New Tenants

{% stepper %}
{% step %}
#### From your production / main development workspace, head to the Tenant Center from the left-hand navigation menu.

You'll find it located under the Marketplace (if you have it enabled) or the Library.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-15 at 09.01.41.png" alt="" width="282"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
#### Click ![](<../../.gitbook/assets/CleanShot 2025-04-15 at 09.03.02.png>) to create a new tenant.

Remember, tenants can be either your own stage and production environments, or actual separate user workspaces.

When adding a new tenant, you'll need to provide some basic information.

<table><thead><tr><th width="150.47015380859375">Parameter</th><th>Purpose</th><th>Example</th></tr></thead><tbody><tr><td>Display Name</td><td>The name of the tenant workspace</td><td><p>Stage</p><p>Beta<br>Customer ABC</p></td></tr><tr><td>Description</td><td>A description of the tenant workspace</td><td>"Staging changes for testing"<br>"Workspace for customer ABC"<br>"Beta access"</td></tr><tr><td>Tags</td><td><p>Apply tags to your tenants to easily filter them when searching and deploying new changes. Great for things like separating subscription tiers or tagging development-specific, internal tenants</p><p><br><strong>This is optional, but highly recommended</strong></p></td><td>dev<br>customers<br>build plan<br>launch plan<br>scale plan</td></tr></tbody></table>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
## A note on new tenant creation

Creating a new tenant does not deploy a release to it by default.
{% endhint %}

***

### Managing Tenants

Once you've created a tenant, you can click the ![](<../../.gitbook/assets/CleanShot 2025-04-15 at 09.14.43.png>) icon to access tenant settings.

#### Edit Tenant

Change the settings applied when creating the tenant, such as the display name or description.

#### Deploy Release

Push a release to this specific tenant.

#### Impersonate

Access the tenant in its current state. Great for troubleshooting tenant specific issues and manual verification of pushed changes

#### Environment Variables

You can access and manage this tenant's environment variables from here. Use these to store things like API keys and other sensitive information to be used in that tenant's function stacks.

For example, if you are pushing a feature that calls OpenAI, and each tenant has their own OpenAI API key, you'd put that here and just make sure the name of the variable matches what you have in development.

#### Backups

Create or restore a backup of a tenant

#### Logs

Review logs directly associated with that tenant, such as release deployments, backups, and impersonations.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-15 at 09.32.44 (1).png" alt="" width="307"><figcaption></figcaption></figure></div>

***

### Developing and Deploying Releases

{% stepper %}
{% step %}
### Make any changes you'd like to deploy in your development tenant. Push them to your stage tenant if you're using one.

Just make sure you're deploying from the tenant that contains your final, tested round of changes to push live to your tenants.
{% endstep %}

{% step %}
### Use the tag selector to filter only the tenants you want to deploy to.

Select the appropriate tags and click **Apply**. Remember, you can also deploy to a single tenant by clicking the ![](<../../.gitbook/assets/CleanShot 2025-04-15 at 09.14.43.png>) icon on that specific tenant.&#x20;

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-15 at 09.46.42.png" alt="" width="305"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Set up a new release by clicking ![](<../../.gitbook/assets/CleanShot 2025-04-15 at 09.48.23.png>) at the top of the page.

In the Releases panel, click ![](<../../.gitbook/assets/CleanShot 2025-04-15 at 09.49.19.png>)

Give your new release a name, a description, and choose the source branch you'll be deploying changes from.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-15 at 09.50.17.png" alt="" width="305"><figcaption></figcaption></figure></div>

When you're ready, click ![](<../../.gitbook/assets/CleanShot 2025-04-15 at 09.51.05.png>) at the bottom of the panel.
{% endstep %}

{% step %}
### Select the tenants you'd like to deploy to.

You can click the checkbox at the top to select all currently shown tenants, or select individual tenants yourself.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-15 at 09.52.30.png" alt="" width="275"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Click ![](<../../.gitbook/assets/CleanShot 2025-04-15 at 09.54.52.png>) at the top of the page to deploy a release to your selected tenants.

Select the release to deploy and click the Deploy button at the bottom of the panel.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-15 at 09.55.39.png" alt="" width="309"><figcaption></figcaption></figure></div>

After deployment, the **Release Stats** table at the top will give you quick visibility into your deployment metrics.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-15 at 10.05.09.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

***

## Best Practices

{% stepper %}
{% step %}
### Tag your tenants

Using tags is crucial to quick and consistent work inside of the Tenant Center, especially as the number of tenants you have grows.
{% endstep %}

{% step %}
### Follow a traditional deployment framework

This would include developing on a **development** tenant, pushing final changes to a **stage** tenant where all of your [QA and testing](../../testing-debugging/test-suites.md) happens, and then deploying releases from **stage**.

Read more about the entire Development Lifecycle [here](../../before-you-begin/the-development-life-cycle.md).
{% endstep %}

{% step %}
### Inform your users of upcoming deployments

In most cases, it's good practice to make sure your users are aware of upcoming changes.
{% endstep %}

{% step %}
### Use backups

Tenant backups are incredibly important when deploying new changes, so you can use them to quickly roll back changes.
{% endstep %}
{% endstepper %}

[^1]: CI/CD stands for Continuous Integration and Continuous Deployment (or Continuous Delivery), a set of practices and tools that automate the software development process to enable faster and more reliable code delivery.  - [_Github_](https://github.com/resources/articles/devops/ci-cd)
