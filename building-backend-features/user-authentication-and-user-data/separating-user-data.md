# Separating User Data

Separating and restricting access to data are two common features of building a backend. Separating data is crucial for multi-tenant systems. It means that even though all your users have data in the same table, they are only able to see and access the data that belongs to them.&#x20;

[Restricting Access](restricting-access-rbac.md) (Role-Based Access Control) takes this to another level if, for example, there are special roles assigned to users like an admin who may have permission to access more data than a standard user. You can read more on restricting access or RBAC by clicking the link at the beginning of this paragraph.&#x20;

{% embed url="https://youtu.be/ohL2vR5wp3o" %}

### Separating Data Example 1

For this example, we have three users in our user table: Steph, Klay, and Jordan.

![](<../../.gitbook/assets/CleanShot 2022-04-25 at 15.03.58.png>)

There is also an items table. Each item belongs to a user.

![](<../../.gitbook/assets/CleanShot 2022-04-25 at 15.05.51.png>)

#### How to enforce a user only sees the items that belongs to them

Here we have an API endpoint, which gets all the items from the items table. The first step is to require user [authentication](./) on the endpoint.

![Require authentication for the API endpoint.](<../../.gitbook/assets/CleanShot 2022-04-25 at 15.09.05.png>)

Now that authentication is required, the next step is to open the [Query All Records](../../the-function-stack/functions/database-requests/query-all-records/) function and add an expression to the by custom query section.

```
WHERE
db: items.user_id = auth id
```

![Add an expression to the Query All Records function for items.](<../../.gitbook/assets/CleanShot 2022-04-25 at 15.13.25.png>)

![Filter the record where the user\_id must be equal to the auth id.](<../../.gitbook/assets/CleanShot 2022-04-25 at 15.14.44.png>)

When we go to run the API endpoint in Run\&Debug, an auth token is required to run the API. In Xano, we can easily search for a user to use a auth token for testing. In your application, the user will need to [authenticate](./) first by logging in or signing up.

Let's select user 2, Klay and run the API endpoint:

![](<../../.gitbook/assets/CleanShot 2022-04-25 at 15.15.43.png>)

The result is all the items associated with user id = 2:\


![Items only belonging to user 2 are returned. ](<../../.gitbook/assets/CleanShot 2022-04-25 at 15.41.23.png>)

#### Added layer of security with precondition

We can add an additional layer of security with the use of preconditions.

First, use a Get Record on the user table with a field value of the auth id.

![Get the user record with the auth id.](<../../.gitbook/assets/CleanShot 2022-04-25 at 15.51.11.png>)

Then use a precondition to enforce the auth ID is equal to the id from the Get Record.

```
WHERE
auth id = var: user.id
```

![Set a precondition where the ID of the user record is equal to the auth id.](<../../.gitbook/assets/CleanShot 2022-04-25 at 16.00.24.png>)

#### How to enforce the user can only edit data that belongs to them

When it comes to editing data, the function stack will also use a precondition. The API endpoint will once again require authentication.

First, we need to Get the Record of the item that the user wants to edit.

![First, Get the Record that the user is trying to edit.](<../../.gitbook/assets/CleanShot 2022-04-25 at 16.31.09.png>)

Getting the existing record allows us to check if it belongs to the user.

Next, use a Precondition to say:

```
WHERE
var: items_1 |GET| "user_id" = auth id
```

![The precondition enforces that the record belongs to the user trying to edit it. Using the GET filter makes sure that the record exists - if it doesn't the precondition will fail.](<../../.gitbook/assets/CleanShot 2022-05-12 at 16.33.07.png>)

Here we use the GET filter with a default value of 0. This helps us account for existence of the record we want to edit. If the record does not exist, the precondition will trigger because a user\_id value of 0 will not match the auth ID.

If the precondition passes, then the function stack will continue to run and edit the data. If it fails, it will throw an error and stop execution.
