---
icon: vial
---

# Unit Tests

## Building a Unit Test <a href="#building-a-unit-test" id="building-a-unit-test"></a>

The fastest way to create a unit test is by using Run & Debug. Once you are achieving the desired result by running your function stack, you can click **Create Unit Test** under the result.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252Fd8QAuFky4jq4QY7Zo4Yo%252FCleanShot%25202024-09-10%2520at%252005.43.27.png%3Falt%3Dmedia%26token%3D95ee6f57-7435-474c-8523-fcae5b6786c4\&width=768\&dpr=4\&quality=100\&sign=2592b5d\&sv=2)

You can also create a test manually at any time from the API settings menu.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FS5kzPGf5ZnoN0sjpMJ7U%252FCleanShot%25202024-09-10%2520at%252005.45.03.png%3Falt%3Dmedia%26token%3D0e22606a-9210-49b3-a056-9acaf6cbde15\&width=768\&dpr=4\&quality=100\&sign=74b24706\&sv=2)

Give your unit test a name, a description, and the data source that it should use to run the test if different from your live data source.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FR2ZeXoqGWgAZt4FAW7Z5%252FCleanShot%25202024-09-10%2520at%252005.46.54.png%3Falt%3Dmedia%26token%3Dfdd3d0d1-42b3-4a9d-8071-371b44ee25f3\&width=768\&dpr=4\&quality=100\&sign=5d27e382\&sv=2)

Unit tests are defined by your **input** and **expects**.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FDpSj6I1BNxCUmNH8Eze3%252FCleanShot%25202024-09-10%2520at%252005.47.50.png%3Falt%3Dmedia%26token%3D17b8d548-f3bf-447a-8918-e55a05623c7a\&width=768\&dpr=4\&quality=100\&sign=2421b858\&sv=2)\
In this example, we are providing an input of 2 and expect a response of 2.

* **Inputs** align with the inputs that your function stack expects. You can fill out any desired values here that you would like to use to run the test. If you used the **Create Unit Test** option in Run & Debug, this should already be populated for you.
* **Expects** are the statements that are used to validate your test. These could be anything from a simple equals statement, or use more complex operators based on your needs.

Your unit test can have multiple expect statements, which can be added by clicking the **+ Add an expect statement** option.

* Use the ✏️ button to delete expect statements.
* Use the ⏩ button to check all expect statements, or you can run them selectively with the ▶️ button.

**Unit Tests and Authentication**

When creating a unit test on a function stack that requires authentication, you can provide an auth token and extras just like you would during Run & Debug.

To avoid having to recycle the auth token upon expiration, we have added the ability to ignore auth token expiration when running your unit tests.

<div align="left"><figure><img src="https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FVlwgA1OeFRRlyELKkOAM%252FCleanShot%25202024-09-13%2520at%252017.59.04.png%3Falt%3Dmedia%26token%3Dae65562c-1ec5-4562-af16-ea3b1cd03daa&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=7149fa6d&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure></div>

#### Using the Testing Suite <a href="#using-the-testing-suite" id="using-the-testing-suite"></a>

Once you have your unit tests built, you can always run them individually from that API's testing panel. If you want to run all of your tests at once, you can use the testing suite.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FZSGA72ssP4eS8ip6QsdU%252FCleanShot%25202024-09-10%2520at%252005.53.13.png%3Falt%3Dmedia%26token%3D998ccc77-677a-480d-bde3-c237ab552f6f\&width=768\&dpr=4\&quality=100\&sign=b9784734\&sv=2)

In the left-hand navigation menu, find your Library and click Unit Tests.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252Fp8td4VX4PZFmyKfpu9cR%252FCleanShot%25202024-09-10%2520at%252005.54.27.png%3Falt%3Dmedia%26token%3D2ec24698-4491-4297-9b5f-44959c357372\&width=768\&dpr=4\&quality=100\&sign=493ca6ae\&sv=2)

Once inside the testing suite, you can perform the following actions:

* Review where your application has and is missing coverage.
* Run all tests at once.

For complex applications with a significant number of objects, you have the ability to dial down further into checking coverage and tests for functions, APIs, and middleware separately. You can also filter your tests by tested / untested only, or failed only, to quickly understand where your attention should be to ensure 100% coverage and success.
