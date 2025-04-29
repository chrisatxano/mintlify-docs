# Restricting Access (RBAC)

RBAC (Role-based access control) or role-based permissions is a way to restrict access based on a user's defined role. This guide will cover two different methods of enforcing access / RBAC to an API endpoint based on the user's role.&#x20;

{% embed url="https://youtu.be/LZMTEEdnd5o" %}

Let's use the following user table for both examples of RBAC. Make note of the role field and the values for each user.

<figure><img src="../../.gitbook/assets/image (50).png" alt=""><figcaption><p>In this example, each user has one of two roles: admin or staff.</p></figcaption></figure>

#### **RBAC Example 1: Use Get Record**

Now, let's set up an API endpoint that GETs all users but only if the user trying to call the endpoint has a role of admin.&#x20;

Take note of the endpoint below, user authentication is required. Additionally, take note of the Function Stack:

1. Get Record from user: This will use the authToken to find the user's ID and look up their information.
2. Precondition: This will enforce that the user's role is equal to admin. If it is not, then it will throw and error and stop the endpoint.&#x20;
3. Query all records from user: This will only be performed if the user's role is an admin by passing the precondition.&#x20;

<figure><img src="../../.gitbook/assets/image (51).png" alt=""><figcaption><p>In this example, the API endpoint requires an authenticated user. Then the Function Stack is set up to perform only if the user's role is equal to admin. </p></figcaption></figure>

Get the record of the user who's calling the endpoint (requester) with the auth ID.&#x20;

<figure><img src="../../.gitbook/assets/image (52).png" alt=""><figcaption><p>In this example, we are getting the record of the user based on their authenticated ID.</p></figcaption></figure>

Next, set a precondition to enforce that the user (called requester in the example) has a role equal to admin.

<figure><img src="../../.gitbook/assets/image (53).png" alt=""><figcaption><p>Click on the pencil icon to open the Expression Builder and set the conditions for the precondition. Additionally, set your error type and message if the conditions are not met.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (54).png" alt=""><figcaption><p>In this example, the requester.role must be equal to admin in order to pass the precondition.</p></figcaption></figure>

If the precondition is met, then the user who is the requester will have permission to execute the rest of the Function Stack and complete the API endpoint.



#### RBAC Example 2: Use Extras

[Extras](./#extras) allow you to store data within the authentication token, which you can access and use on authenticated API endpoints.&#x20;

First, you must set up the [sign-up & login](./) to include the user's role at the time of authentication.&#x20;

In this example, we will use the login endpoint to pass the user's role into extras of the auth token at the time of authentication.&#x20;

<figure><img src="../../.gitbook/assets/image (55).png" alt=""><figcaption><p>In this example, we are passing the user's role into the authToken at the time of login by utilizing extras.</p></figcaption></figure>

Now that the user's role is passed into the authToken, we can eliminate the Get Record function from the previous example and reference "extras.role" in the precondition to enforce the user's role.

<figure><img src="../../.gitbook/assets/image (56).png" alt=""><figcaption><p>In this example, we can use the extras of the authenticated user to access the user's role and set the precondition equal to admin.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (57).png" alt=""><figcaption><p>Set extras.role (as defined in the creation of the authentication token) equal to admin.</p></figcaption></figure>

If the user's role is equal to admin then they will pass the precondition and have permission to execute the rest of the Function Stack. &#x20;
