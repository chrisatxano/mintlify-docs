# RAM Usage

In this screenshot, we can see a usage graph showing Database RAM is almost at 100%. **This is okay.** What we should be focusing on is the consistency. All this tells us is that the database is using as much RAM as it can to do the job it needs to be doing at a steady pace. Everything looks good!

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M8Si5XvG2QHSLi9JcVY%2Fuploads%2FJpxfXYc4Mk4iqiGa7wFc%2Fimage.png?alt=media\&token=66363a03-34a6-4b6f-9c4a-ca441a0993cf)

Let's look at another example where we might have a problem.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M8Si5XvG2QHSLi9JcVY%2Fuploads%2FSVKWvQg8qjoYLskZyUCo%2Fimage.png?alt=media\&token=0373aa27-8ec2-4446-b69d-8e3997a8cfa4)

In this screenshot, we can see that this instance's Lambda RAM isn't showing steady utilization -- there are significant peaks, valleys, and spikes. This tells us that there is sporadic intense load with Lambda functions we are using, and it will likely cause problems such as:

* Temporary system restarts and downtime
* Slow performance
* Failed requests

This is something that should be investigated further.

### Reducing RAM Usage <a href="#reducing-ram-usage" id="reducing-ram-usage"></a>

If you are finding yourself in a situation where you are experiencing symptoms of RAM exhaustion, there are a few things you can to do try and mitigate the situation. It's important to note that in some cases, when mitigation is not possible, that may signal it's time to upgrade your Xano subscription tier to increase your available RAM. You can always reach out to Xano Support for further clarification.

### **Database RAM**

Spikes in Database RAM can be caused by one or more of the following:

* Tables that contain fields with large amounts of data, such as JSON payloads or sizable text content
  * Try moving these large fields to a separate table or determining if you can reduce the amount of data stored.
  * Depending on how often the data needs to be accessed, you can also store the large data in text files and store the file path in the table instead.
* Table references to other tables with a high number of fields
  * Use the [Auto Complete](../../the-database/database-basics/relationships.md#auto-complete) setting on the referenced table to reduce the amount of data loaded when viewing the table
* Running queries with joins on large tables
  * Make sure you are using proper [indexing](../../the-database/database-performance-and-maintenance/indexing.md) on large tables
  * Use pagination on your base query

### **API RAM**

Spikes in API RAM can be caused by one or more of the following:

* Function stacks that process large volumes of data
  * Clear the contents of variables as they become unnecessary by updating them to blank values
  * Move large data processing jobs to [background tasks](../../the-function-stack/building-with-visual-development/background-tasks.md)​
  * Use post processing to execute any functions that aren't necessary to deliver a response

### **Lambda RAM**

Spikes in Lambda RAM are **incredibly rare**, and we would recommend reaching out to support if you see this happen. Lambda is only used for internal instance operability, such as facilitating Realtime.

### **Deno RAM**&#x20;

{% hint style="success" %}
## Deno is what you previously knew as Lambda

**Deno** is the engine that powers your Lambda functions behind the scenes.

Previously, the Lambda pod was also responsible for some internal instance operations; this is no longer the case, which means that your instance should remain up and active even if Deno goes down.
{% endhint %}

Please note that when using Lambda functions, the contents of **all variables** are loaded into Deno memory. This is most often the cause of memory issues when using Lambda functions, and can be mitigated by wrapping your Lambda in a [custom function](../../the-function-stack/building-with-visual-development/custom-functions/) giving it access to only the data it needs to run.

Spikes in Deno RAM can be caused by one or more of the following:

* Contents of other variables are too large for the Lambda to handle during processing
* Using file resources in conjunction with Lambdas
* Loading large or multiple NPM packages in your functions. Any library you call will be loaded into memory.
  * If you use packages frequently, they may be retained in memory for increased speed.
  * If you hit your RAM limit for Deno, the "pod" or section of your instance that is responsible for Lambda functions will clear memory and restart, which will potentially cause Out Of Memory errors or timeout errors.

To mitigate issues with Lambda RAM, try using [expressions](../../the-function-stack/data-types/expression.md) instead.

### **Redis RAM**

Spikes in Redis RAM can be caused by one or more of the following:

* Heavy and/or inappropriate reliance on data caching functions

If you are not using data caching functions and still experiencing spikes in Redis RAM, please reach out to support.

### **Tasks RAM**

Spikes in task RAM should be handled as you would handle spikes in API RAM.\
