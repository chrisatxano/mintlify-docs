# Static IP (Outgoing)

{% hint style="info" %}
At this time, Static IP is only available for instances in the United States, Saudi Arabia, France, Indonesia, South Korea, and Japan.

For users who have had long-standing instances on the United States region, you may not immediately have Static IP available as an option. Please reach out to our Support team for further clarification and next steps.
{% endhint %}

Static IP address is available on any paid plan address for outgoing API requests. This is commonly required by 3rd party API providers requiring an IP whitelist.

Your static IP will only apply to outgoing requests -- meaning requests you make to third-party APIs using the [External API Request](../../the-function-stack/functions/apis-and-lambdas/external-api-request.md) function.

### How to Enable Static IP

To add Static IP to your Xano instance, head to your Billing screen, and choose Change Plan.

On the next screen, choose Select Additional Upgrades, and then choose to enable Static IP from the panel that opens.

<figure><img src="../../.gitbook/assets/CleanShot 2023-08-21 at 17.09.40.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/CleanShot 2023-08-21 at 17.10.37.png" alt=""><figcaption></figcaption></figure>

After proceeding through checkout, you'll be taken to the instance selection screen where you'll see that your instance has a pending upgrade.

Adding Static IP to your Xano plan requires migrating your data to a new instance. This means that your API endpoint base URL will change. We do not process the migration manually to give you time to update any connections that may be necessary prior to the transition. Just click the prompt whenever you're ready.

### Finding your Static IP

From your instance selection screen, click the ⚙️ icon.

<figure><img src="../../.gitbook/assets/CleanShot 2023-08-21 at 17.16.13.png" alt=""><figcaption></figcaption></figure>

On the panel that opens, choose Instance Details.

<figure><img src="../../.gitbook/assets/CleanShot 2023-08-21 at 17.17.40.png" alt=""><figcaption></figcaption></figure>

On the next pane, you can scroll down to the bottom and see your new static IP address for outgoing requests, which you can then provide to any third-party services that require it.

<figure><img src="../../.gitbook/assets/CleanShot 2023-08-21 at 17.18.36.png" alt="" width="296"><figcaption></figcaption></figure>
