# When everything feels slow

## When every request feels slow

### Step 1. - Check if your server is being overloaded with requests



<figure><img src="../../.gitbook/assets/CleanShot 2022-09-12 at 16.19.32.png" alt=""><figcaption></figcaption></figure>

**A. Look at Instance Usage** - When you log into Xano, the Instance Dashboard will reflect where there might be a usage spike based on your capacity. This is a near real-time graph (delayed by a few min) of the last 24 hours. Ideally, you want to keep things below 50% at all times, but if you aren't on the appropriate Scale plan, usage spikes could push your Database and API capacity up. &#x20;

* **If Database usage is high** - When the Database (blue) request line is high as shown above, this usually means that your Database is not optimized or indexed properly.  Please visit the [Database performance](../../the-database/database-performance-and-maintenance/) section to look at ways to fix the tables that are being queried. Usually, API usage goes hand-in-hand with Database usage, so it isn't surprising to see them at the same level in the above example. Once fixed, you should see both Database and API usage go down.  \

* **If API usage is high** - When the API usage is high on its own, this usually indicates that there is a traffic spike and your server is running out of capacity.  This normally happens when multiple users are trying to request data from your API at the same time.  You can increase your capacity by upgrading to a different Scale package.

If you need hands-on private help diagnosing this, you can schedule a [premium support call](../getting-help/) with one of our Xano team members.&#x20;

**B.** **Instance Stats** You can see the volume of requests happening across all your workspaces here. This is also across a 24-hour window and is updated every hour.  If you see a large volume of requests as pictured above, proceed to step 2 to see where it's coming from.

To dig deeper into the details of each request, you can proceed to Step 2 below.

### Step 2. Look at the API requests for each workspace

<figure><img src="../../.gitbook/assets/CleanShot 2022-09-13 at 08.24.46.png" alt=""><figcaption></figcaption></figure>

Each workspace has a dashboard item of request history. **Click DETAILS** at the top right of the graph to see each request.

<figure><img src="../../.gitbook/assets/CleanShot 2022-09-13 at 09.03.46.png" alt=""><figcaption></figcaption></figure>

**A.** You can filter down the requests that are taking the longest. Select the magnifying class to do this. A good rule of thumb is to select requests that are **greater than 5s**.

**B.** You can click the refresh button to ensure you're getting the latest data.

**C.** Click on the request that takes a long time to show the details. \
[_How to diagnose a slow API endpoint_](when-everything-feels-slow.md#when-a-single-api-endpoint-feels-slow)
