---
icon: vials
---

# Test Suites

Workflow Testing allows you to create sets of different tests to validate user flows are working as expected.

## What is Workflow Testing? <a href="#what-is-workflow-testing" id="what-is-workflow-testing"></a>

Workflow Testing in Xano allows you to quickly build sets of tests that you can use to make sure a specific flow is working as expected. You can think of a 'flow' as a set of separate actions, such as multiple APIs that a user might hit when utilizing your application, or data processing across multiple function stacks.

Workflow Testing allows you to validate these sets or flows with a single click and get instant visibility into your backend functionality.

## How do I build workflow tests? <a href="#how-do-i-build-workflow-tests" id="how-do-i-build-workflow-tests"></a>

From the left-hand navigation menu, choose **Library** > **Workflow Tests** ![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FkzjkcirGezN3F7HXGLol%252FCleanShot%25202024-11-21%2520at%252010.05.53.png%3Falt%3Dmedia%26token%3D5d69d39c-4c57-441a-b566-1d0130d725fd\&width=300\&dpr=4\&quality=100\&sign=580bfc46\&sv=2)

Choose **Add Workflow Test** in the top-right corner. In the panel that opens, you can give your test a name, description, and add tags for easy access later.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FxPg927bf3WIps6n3vIPg%252FCleanShot%25202024-11-21%2520at%252010.07.50.png%3Falt%3Dmedia%26token%3D6daccf37-93fc-4a4b-b28a-9619d706f913\&width=768\&dpr=4\&quality=100\&sign=60a96a50\&sv=2)

Click the ![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FEi2Idvvw387q1XOc8gaV%252FCleanShot%25202024-11-21%2520at%252010.09.15.png%3Falt%3Dmedia%26token%3D159bde54-83f8-45be-97ba-1e8905c2f39d\&width=300\&dpr=4\&quality=100\&sign=5841edc4\&sv=2) button to add a step to your Workflow Test. We've introduced some new functions to assist you in building your tests.

**Run Stacks**

Run stacks are functions you can add to your workflow tests to run other function stacks, such as APIs, custom functions, and middleware.

<table><thead><tr><th width="322">Function Name</th><th>Use Case</th></tr></thead><tbody><tr><td>Run API Endpoint</td><td>Sends a request to one of your API endpoints and returns the result</td></tr><tr><td>Run Addon</td><td>Runs an addon</td></tr><tr><td>Run Function</td><td>Runs a custom function and returns the result</td></tr><tr><td>Run Middleware</td><td>Runs a middleware and returns the result</td></tr><tr><td>Run Trigger</td><td>Runs a trigger and returns the result</td></tr><tr><td>Run Task</td><td>Runs a background task and returns the result</td></tr></tbody></table>

#### Test Expressions

Test Expressions are functions used typically in conjunction with a Run Stack to determine if the output of a Run Stack is valid.

| Function Name                                                                                                                                                              | Use Case                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Expect a variable to be defined<br>Expect a variable to not be defined</p>                                                                                              | <p>Checks to see if a variable has been defined.<br><br><strong>Example</strong>:<br>You have an API that returns a <code>user</code> object with a name key inside of it. You can use this to check if <code>user.name</code> is defined.</p>                                                                                          |
| Expect variable to be empty                                                                                                                                                | <p>Checks to see if a variable exists, but is empty.<br><br><strong>Example:</strong><br>You are calling an external API that is used to process data. If the API call is successful, you know that <code>response.result</code> is empty because the API just returns a status code informing you that the job is being processed.</p> |
| <p>Expect variable to be false<br>Expect variable to be true</p>                                                                                                           | Checks to see if a variable with a boolean data type is returning `false` or `true`                                                                                                                                                                                                                                                     |
| <p>Expect variable to be greater than<br>Expect variable to be less than<br>Expect variable to equal<br>Expect a variable to not equal<br>Expect variable to be within</p> | Checks to see if a variable matches the specific condition, such as >, <, =, or is within a certain range.                                                                                                                                                                                                                              |
| Expect variable to be null                                                                                                                                                 | Checks to see if a variable contains a `null` value                                                                                                                                                                                                                                                                                     |
| <p>Expect variable to start with<br>Expect variable to end with</p>                                                                                                        | Checks to see if the value inside of a variable starts or ends with a specific value                                                                                                                                                                                                                                                    |
| Expect function to throw                                                                                                                                                   | Checks a function to see if it throws an error                                                                                                                                                                                                                                                                                          |
| Expect function to match                                                                                                                                                   | Checks to see if the output of a variable matches a [regular expression](https://regexr.com/)                                                                                                                                                                                                                                           |

### Using Workflow Tests

In this example, we've built a workflow test to make sure our login flow works as expected.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FAtO4icqQdr0Z99GPU2In%252FCleanShot%25202024-11-21%2520at%252011.35.34.png%3Falt%3Dmedia%26token%3D7193d39e-1eca-40ad-80f2-ecfea92eeff9\&width=768\&dpr=4\&quality=100\&sign=b093fc96\&sv=2)

We've added a **Run Stack** function to run our auth/login endpoint, and provided it with a username and password.

After that, our **Test Expression** checks to make sure that the login function is returning an authToken, which is what our login endpoint returns if a valid username and password is provided. When we click ![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FCtCMyxNqw2XgZg1LKRdO%252FCleanShot%25202024-11-21%2520at%252011.37.53.png%3Falt%3Dmedia%26token%3D78efed5c-c645-4e6a-870f-519d4eef5b85\&width=300\&dpr=4\&quality=100\&sign=2d7160de\&sv=2) we can see that our test passes!

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252Fyz3GKPAeNyWAVWVMidvR%252FCleanShot%25202024-11-21%2520at%252011.38.25.png%3Falt%3Dmedia%26token%3D2645622a-4717-41ff-b66b-0c2c61ea18f5\&width=768\&dpr=4\&quality=100\&sign=308cfa99\&sv=2)

If we modify our **Run API Endpoint** run stack to provide an invalid password, we can see that by running our test again, we get an error. This test has failed because an authToken was not returned.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FuhcT7KZYYU34GEJXIrJe%252FCleanShot%25202024-11-21%2520at%252011.38.58.png%3Falt%3Dmedia%26token%3D91767e8c-dadc-4ac6-87b2-f409fd1d71d8\&width=768\&dpr=4\&quality=100\&sign=b38cbe33\&sv=2)

From the main **Workflow Tests** page, we can run each of our tests by clicking the individual ![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FoUpmTJCuZWivL1Xef6vj%252FCleanShot%25202024-11-21%2520at%252011.40.15.png%3Falt%3Dmedia%26token%3Dd3a18f86-c6d7-40dd-b0be-41546795cfaa\&width=300\&dpr=4\&quality=100\&sign=22d347a9\&sv=2)buttons, or we can click ![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F88Llfh1J3bxE448maCnq%252FCleanShot%25202024-11-21%2520at%252011.40.32.png%3Falt%3Dmedia%26token%3D53e80427-90bd-4724-8c8e-bc7e1bb47ed2\&width=300\&dpr=4\&quality=100\&sign=3982857a\&sv=2)to run all of our workflow tests at once.

We can see by running all of our workflow tests the following information:

* We have **38% coverage**. This means that out of all of the function stacks that exist across our backend, 3/8 of them are used in our tests.
* We have **50% success**. This means that out of all of our workflow tests, half of them are successful.
* To run all of our tests takes less than a second.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252Fy6lLVBkFiLNglKPZrHkW%252FCleanShot%25202024-11-21%2520at%252011.40.59.png%3Falt%3Dmedia%26token%3Df3d5413e-9178-4a52-9b63-797bc798146e\&width=768\&dpr=4\&quality=100\&sign=185e5bab\&sv=2)

#### Additional Information <a href="#additional-information" id="additional-information"></a>

* Click the ![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FLPHsa11b8F2TzEe184rI%252FCleanShot%25202024-11-21%2520at%252011.42.45.png%3Falt%3Dmedia%26token%3Ddca4c485-4b65-4f1f-835a-82bf3ef64e85\&width=300\&dpr=4\&quality=100\&sign=7edfa678\&sv=2) icon next to a workflow test to clone or delete it.
* When adding a Run Stack, you can click the ![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FLlcWXlYGhURhcWz07Mbc%252FCleanShot%25202024-11-21%2520at%252011.43.16.png%3Falt%3Dmedia%26token%3D17af8493-034e-43d0-8dc5-42820e33f8e1\&width=300\&dpr=4\&quality=100\&sign=fedad151\&sv=2) icon to open that function stack being tested in a new window or tab and quickly make changes.
* When you test a function stack that currently is in draft mode, your workflow test will run the drafted version.
* You can change the data source that all of your workflow test's functions run against by clicking the ![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FNJ4vUPWG333vjoeSxdLp%252FCleanShot%25202024-11-21%2520at%252011.45.12.png%3Falt%3Dmedia%26token%3De0ad1fa9-ecb2-4877-83d6-b601e13b7335\&width=300\&dpr=4\&quality=100\&sign=f1fe621f\&sv=2) button at the top of the workflow test function stack.
