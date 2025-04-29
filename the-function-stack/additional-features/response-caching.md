# Response Caching

#### Response Caching <a href="#response-caching" id="response-caching"></a>

[**Watch a practical example**](https://youtu.be/TTQky7FqRQE) of Response Caching using the [Star Wars API](https://swapi.dev/)

From the settings of an [API Endpoint](../building-with-visual-development/apis/) or [Custom Function](../functions/custom-functions.md) response caching can be accessed. Response caching is an abstracted caching method to cache the response of an endpoint or function.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8Si5XvG2QHSLi9JcVY%252F-MfjDlawtMnevbHx45uw%252F-MfjK_cyiFbXxTGORZLt%252Fcaching.png%3Falt%3Dmedia%26token%3D91dea8b1-08ec-4c0e-b820-843a5f31a09d\&width=768\&dpr=4\&quality=100\&sign=2f79e768\&sv=2)

You can choose from a number of different settings to determine how to cache the response.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8Si5XvG2QHSLi9JcVY%252F-MfjDlawtMnevbHx45uw%252F-MfjLdGctLvT-WNeHBMp%252Fcaching%2520%281%29.png%3Falt%3Dmedia%26token%3D3b769e18-6e47-4fbc-9a5e-1cf5cce1b814\&width=768\&dpr=4\&quality=100\&sign=11aae88a\&sv=2)

**TTL** - Stands for time to live. This defines how long to cache the response for. Options range from 5 seconds to 7 days. After the TTL expires, the query will run normally and reset the response cache.

**Use inputs for caching signature** - This is defaulted to yes. It will create a response cache for each new or unique set of inputs for the duration of the TTL.

**Use IP address for caching signature** - This is defaulted to no. It can be used if you wish to record a response cache on a per IP address basis.

**HTTP Request Header Names** - This is optional. You are able to cache the HTTP request headers of the response. Add the request header name or names that you wish to cache.

**Environment Variable Names** - This is optional. It allows you to cache any defined [environment variable](https://docs.xano.com/what-xano-includes/workspace/settings/environment-variables) names to the response cache.

**Use Authentication ID for caching signature** - When an API endpoint requires [authentication](https://docs.xano.com/building-features/authentication-sign-up-and-log-in/authentication), this option becomes available. This can be turned on to enable a caching on a per user basis for authenticated endpoints.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8Si5XvG2QHSLi9JcVY%252F-MfoE9ds9tUfjoofzMUU%252F-MfoFDfB70ntclRxZDPd%252Fcaching%2520%282%29.png%3Falt%3Dmedia%26token%3D55616bd0-c466-4cb8-bb52-15270bac0cbb\&width=768\&dpr=4\&quality=100\&sign=b09d4684\&sv=2)

#### Example Use Cases <a href="#example-use-cases" id="example-use-cases"></a>

**Use inputs and disable authentication ID for caching signature**

Company statistics for your entire team. If you need to display company statistics for your entire team then you may consider using inputs and disabling authentication ID for caching signature. You API endpoint would require authentication so that only your team can access the API but you would disable the authentication ID for caching. This would make it so the cache response is not on a per user basis. Since it is company statistics you want each user to see the same statistics. Using inputs enables each searched or inputted value gets cached, so if other team members search or input the same values then the response will already be there.

**Use inputs and use authentication ID for caching signature**

Personal statistics. In this scenario you would enable both inputs and authentication ID for caching signature. This would cache responses on a per user basis. For example, you might have each individual sales rep reviewing their own statistics for the quarter. Enabling inputs would cache the response for each inputted value. Additionally, enabling authentication ID for caching signature (with the appropriate business logic) would cache the responses on a per user basis.

**Disable inputs and disable authentication ID for caching signature**

There's a movie night event and you want to generate a random movie. Imagine you have an API that inputs a category or genre of movie and based on that, returns a random movie. By disabling both inputs and authentication ID for caching signature, this will allow for the first search on this API to generate a random movie to be played during movie night. It won't matter what other people search. So if the first person searched Science-Fiction and the result is Star Wars then all other searches (drama, action, comedy, etc.) will return Star Wars. Now you have your random movie for movie night.
