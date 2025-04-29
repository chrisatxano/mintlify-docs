---
hidden: true
---

# Tool Rate Limit

{% hint style="warning" %}
**This page only applies to our free plan. None of our paid plans include or enforce any sort of rate limiting.**
{% endhint %}

To keep Xano's free plan safe and fair for everyone sharing the resources of our free server instance, a rate limit of **20 requests every 10 seconds** is enforced for your MCP server tools.

When you encounter the rate limit, you'll see a message like this:

```
{"code":"ERROR_CODE_TOO_MANY_REQUESTS","message":"Whoa there! Your plan only supports 20 requests every 10 seconds. Upgrade options and additional information is available at: https://xano.gitbook.io/xano/instances/api-rate-limit"}
```

### What can I do when I hit the rate limit?

* Wait up to 10 seconds before sending a new request
* Upgrade to a [paid plan](https://www.xano.com/pricing).

{% hint style="info" %}
Rate limits **do not apply** when testing inside of Xano — you can use our [Run and Debug features](the-function-stack/building-with-visual-development/#testing-a-draft) to test as much as you'd like!
{% endhint %}
