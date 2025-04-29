---
icon: nfc-lock
---

# Environment Variables

Environment Variables are persistent variables that are available across your entire workspace. Typically, these are used to store things like external API keys or other sensitive information that you need to use across multiple function stacks, without storing it in a database table.

{% @arcade/embed flowId="tKoCMy9H9eGLCgrNGSUc" url="https://app.arcade.software/share/tKoCMy9H9eGLCgrNGSUc" %}

## Adding Environment Variables

{% stepper %}
{% step %}
### From the left-hand navigation, click Settings


{% endstep %}

{% step %}
### On the next screen, click ![](<../.gitbook/assets/CleanShot 2025-01-13 at 13.01.29.png>) to edit your environment variables


{% endstep %}

{% step %}
### Click ![](<../.gitbook/assets/CleanShot 2025-01-13 at 13.01.51.png>) to add a new environment variable.

Give your environment variable a name that you can easily recognize; this is how you'll identify it when calling it in function stacks.

Provide a value for the variable.

{% hint style="info" %}
Environment variables can only be updated from your workspace settings.
{% endhint %}
{% endstep %}

{% step %}
### Use environment variables in your function stacks

They'll be available in the dropdown under <mark style="color:blue;">**ENV**</mark>

<div align="left"><figure><img src="../.gitbook/assets/CleanShot 2025-01-13 at 13.03.44.png" alt="" width="447"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

## Xano-generated Environment Variables

Xano maintains several environment variables you can use.

<table><thead><tr><th width="242">Variable Name</th><th>Contents</th></tr></thead><tbody><tr><td>$remote_ip</td><td>Contains the IP address the request came from</td></tr><tr><td>$http_headers</td><td>Contains the headers of the request</td></tr><tr><td>$request_uri</td><td>Contains the URL of the request</td></tr><tr><td>$request_querystring</td><td>Contains any URL parameters attached to the request URL</td></tr><tr><td>$datasource</td><td>Contains the datasource the request is targeting</td></tr><tr><td>$branch</td><td>Contains the branch the request is targeting</td></tr><tr><td>$request_method</td><td>Contains the request method (GET, POST, DELETE, etc...)</td></tr></tbody></table>
