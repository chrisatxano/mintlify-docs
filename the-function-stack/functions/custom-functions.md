# Custom Functions

## What are custom functions?

Custom functions are pieces of reusable logic that you can insert into other function stacks. This is most useful when you have a set of steps that remain the same, but need to be executed in multiple places. Placing those steps inside of a custom function allows you to quickly use those steps in other function stacks, while only needing to maintain them in one place.

### Using Custom Functions

{% @arcade/embed flowId="VGexEWGI0KkHspK9BMQH" url="https://app.arcade.software/share/VGexEWGI0KkHspK9BMQH" %}

{% stepper %}
{% step %}
### From the left-side navigation, click ![](<../../.gitbook/assets/CleanShot 2025-01-14 at 07.19.54.png>) to access the Library section, and choose Functions from the submenu that appears.


{% endstep %}

{% step %}
### To create a custom function, click ![](<../../.gitbook/assets/CleanShot 2025-01-14 at 07.20.43.png>)

Building a custom function is just like building an API. Refer to [that documentation](../building-with-visual-development/) for specific instructions on building the function stack.
{% endstep %}

{% step %}
### ![](<../../.gitbook/assets/CleanShot 2025-01-14 at 07.22.33.png>) your changes

You can Publish the custom function to ensure that every place it is called uses the same version.

{% hint style="info" %}
**Hint**

When using Run & Debug, you have the option of running draft versions of functions as well, so you don't have to publish changes until you are ready.
{% endhint %}
{% endstep %}

{% step %}
### Insert the custom function any place you need to use it.

In the functions panel, you'll see an option labeled Custom Functions, shown below. Just click it to see a list of your custom functions and add them to other function stacks.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-01-14 at 07.24.07.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### When you make changes to the custom function, the changes populate across everywhere it is used.
{% endstep %}
{% endstepper %}

***

## Async Execution <a href="#async" id="async"></a>

Once you've built your custom function and added it to another function stack, you have the option of running the function **asynchronously**. This just means that the functions will be queued for execution, and the rest of your function stack will continue to execute right away.

{% embed url="https://www.youtube.com/watch?v=-1wxYgc5i0U" %}

Asynchronous functions will utilize your background task resources (unless you are on an Enterprise plan), so it's important to manage expectations when it comes to execution speed. It would be most appropriate to use asynchronous functions when you need to trigger an operation as part of a larger function stack, but do not need to reference the output in the same stack.

To enable asynchronous execution, right-click on the custom function in your function stack, and choose **Async Settings**.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FTVQwgFKz56wtmn2bRbQQ%252FCleanShot%25202024-09-04%2520at%252009.57.21.png%3Falt%3Dmedia%26token%3D8b8bbf39-f568-4bad-821a-cf9faffe8552\&width=768\&dpr=4\&quality=100\&sign=3a825ef\&sv=2)

In the panel that opens, choose your desired execution type.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FCLFEy3Z9hZOlsILQVag8%252FCleanShot%25202024-09-04%2520at%252009.58.16.png%3Falt%3Dmedia%26token%3D61781b0f-7411-46b2-84fe-117d8743eb53\&width=768\&dpr=4\&quality=100\&sign=a4ab9bc9\&sv=2)

* **Synchronous** means that the function stack will wait for the custom function to execute before continuing. The custom function will output the result to the defined variable. This is the standard behavior that has always existed for custom functions.
* **Async** means that the functions will be queued for execution using your background task resources. The function's output variable will be populated with a unique identifier for the queued excecution.
* **Async (dedicated)** is available for Enterprise plans and gives you a method of specificity around the resources used to execute the custom function.

When using async functions, the function request history will still populate, so you can review the requests once they have finished executing. Each request will be labeled with the execution method.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F2WwVUhi42A6C64FSwcyz%252FCleanShot%25202024-09-04%2520at%252010.02.02.png%3Falt%3Dmedia%26token%3D03f12d88-c0f9-4db5-a237-c4abb1a534b9\&width=768\&dpr=4\&quality=100\&sign=4910475a\&sv=2)

#### Async Function Await <a href="#async-function-await" id="async-function-await"></a>

In scenarios where you want to use the output of your async functions later in the function stack, you can utilize the **Async Function Await** function, which accepts the UUIDs returned when an async function is executed.

You can provide an array of IDs to get the output of, and specify how long you'd like to wait for those functions to finish executing in seconds using the timeout parameter.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FbKzc0c12DgBii2uiAzte%252FCleanShot%25202024-09-13%2520at%252017.57.01.png%3Falt%3Dmedia%26token%3D64298353-c685-4bec-b89a-4322e2d97413\&width=768\&dpr=4\&quality=100\&sign=34ecc06c\&sv=2)\
