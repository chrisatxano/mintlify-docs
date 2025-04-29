# External API Request

## What is an external API request?

The External API Request function is used to send requests to external APIs. You'll use this anytime you want to interact with a third party service, such as a payment platform or email provider.

## Using the External API Request Function

{% stepper %}
{% step %}
### Add an External API Request function


{% endstep %}

{% step %}
### Use the AI Assistant to help you build your API request

{% include "../../../.gitbook/includes/ai-request-assistant.md" %}
{% endstep %}

{% step %}
### Or, build the request manually or with a cURL command

You can copy cURL commands from API documentation, and paste them using ![](<../../../.gitbook/assets/CleanShot 2025-01-13 at 13.20.09.png>). Xano will build the request for you.

<table><thead><tr><th width="180">Option</th><th>Description</th></tr></thead><tbody><tr><td>url</td><td>The URL of the API you're calling, such as:<br><code>https://api.service.com/send_message</code></td></tr><tr><td>method</td><td>The verb the API is designed to respond to, such as GET, POST, DELETE, etc...</td></tr><tr><td>params</td><td>Also known as "query parameters", these are options sent along with the request, such as searching and filtering options, or other data that the request needs to execute.<br><br>You may also see this referred to as <strong>request body</strong>. <br><br>Hover over the params value space and click <mark style="color:blue;"><strong>set</strong></mark> to add a new parameter.<br><img src="../../../.gitbook/assets/CleanShot 2025-02-05 at 16.35.54.png" alt=""></td></tr><tr><td>headers</td><td>Any headers you need to send with the request, such as authentication.<br><br>Add headers by hovering over the value space and click <mark style="color:blue;"><strong>push</strong></mark><br><br><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tWsL4o1vHmDGb2UAUDD%2Fuploads%2FpAWCEAw4h7e2OfMOAFJk%2FCleanShot%202025-02-05%20at%2016.37.28.png?alt=media&#x26;token=ba4e92fc-4b3c-4358-9e13-ccbe3e15711c" alt=""><br></td></tr><tr><td>timeout</td><td>How long Xano should allow the request to take before considering it timed out (failed)</td></tr><tr><td>follow_location</td><td><p>Determines if you wish to automatically follow the redirects (if there are any) in the API call.</p><p></p><p>An example of this would be an API that generates a file for you, then gives you a redirect to get that file.</p></td></tr></tbody></table>
{% endstep %}
{% endstepper %}

## Understanding API Documentation

{% stepper %}
{% step %}
### Start by evaluating the four key sections that almost every API documentation has.

The Getting Started guide is your entry point - it typically covers the basics of authentication, shows a simple example request, and helps you make your first API call successfully.

The Authentication section explains how to get your API keys and how to include them in your requests. This is crucial since you'll need this working before you can try anything else.

The API Reference details every possible endpoint and operation. Don't try to read this cover-to-cover. Instead, find the specific endpoint that matches what you're trying to do, then study its parameters, required headers, and example responses.

The Examples/Tutorials section often has complete code snippets showing common use cases. These are invaluable for seeing how different API calls work together to accomplish a task.
{% endstep %}

{% step %}
### Finding the endpoint(s) you need

When you find the endpoint you need, focus on three things:

1. What URL you'll be calling
2. What parameters or data you need to send
3. What the response will look like

Most API documentation also includes **cURL commands**, which you can copy and paste right into Xano by clicking ![](<../../../.gitbook/assets/CleanShot 2025-01-13 at 13.20.09.png>)on the External API Request function panel. This is the optimal way to create external API request in Xano, as it ensures consistency with what the API requires and is much faster.

{% hint style="info" %}
**Tip**

Most API documentation has a "try it out" or interactive portion that allows you to experiment with the API — it's the fastest way to understand how everything works.
{% endhint %}
{% endstep %}
{% endstepper %}

## Multipart (File) Support

Xano has support for sending images through the external API request function. You can send a file resource - either as an input or variable - through the parameters section of the external API request as a key-value pair or as the entire parameter (depending on what the specific API requires).\


## Security Settings

### Host Verification

When an API request is sent to a secure server (you'll know if it's a secure request if the URL starts with https — most requests will), the domain's secure connection is verified using a certificate. Enabling host verification checks the certificate to make sure that it matches the domain you're sending the request to.

This value can be `true` or `false`

**Recommended Setting:** `true`

You might want to set Host Verification to 'false' in a few specific scenarios:

1. **Development and Testing Environments**: When working with development servers that use self-signed certificates or have hostnames that don't match their certificates
2. **Internal Services with Misconfigured Certificates**: In corporate environments where internal services may have certificates that don't exactly match the hostnames used to access them, especially in legacy systems.
3. **Troubleshooting SSL Issues**: To isolate whether hostname verification is causing connection problems when debugging API connectivity issues.

### Peer Verification

Secure certificates are usually issued by certain trusted authorities, such as [LetsEncrypt](https://letsencrypt.org/). Peer Verification enables checking whether or not the certificate is issued by one of these known trusted authorities, validating its authenticity.

This value can be `true` or `false`

**Recommended Setting:** `true`

You might want to set this to false if the server you're sending the request to falls under one of the scenarios outlined above under **Host Verification**.

### SSL Authentication

This is a set of additional options you can use to validate the security of the request being made. The provider of the service you're calling should be able to provide these for you, if necessary.

* `certificate`: The content of the client certificate file. Usually, you'd be provided with a .crt or a .pem file — just open it up in your text editor of choice and paste the contents here.
* `certificate_pass`: Password for the certificate if it's password-protected
* `private_key`: The contents of the private key file. Usually, you'd be provided with a .pem file for this — just open it up in your text editor of choice and paste the contents here.
* `private_key_pass`: Password for the private key if it's password-protected

### CA Certificate

Custom CA certificates allow you to specify your own trusted Certificate Authority for peer verification. This is an advanced option that is useful when connecting to servers that use certificates signed by private or internal CAs — as in, a CA that is not listed as a known trusted authority.

A custom certificate is usually provided as a file that you'd just open up in a text editor and paste here. It will look something like this:

```
-----BEGIN CERTIFICATE-----
MIIDITCCAgmgAwIBAgIUJqrGM2rS34H8YryJJLAMarvab8AwDQYJKoZIhvcNAQEL
BQAwIDEeMBwGA1UEAwwVbXlDdXN0b21DZXJ0aWZpY2F0ZUNKX...
-----END CERTIFICATE-----
```
