---
icon: building-lock
---

# Role-based Access Control (RBAC)

{% hint style="success" %}
Role-Based Access Control (Permissions) is included with our **Scale** and **Enterprise** plans.&#x20;
{% endhint %}

Xano Enterprise allows granular permissions control for each team member and workspace within an Instance.

## Permissions Center

The Permissions Center, when enabled, allows the Instance owner full control over role-based permissions across each workspace within the Instance.

To access the Permissions Center, open the menu panel on the Instance then choose Permissions (RBAC).

<figure><img src="../.gitbook/assets/CleanShot 2023-04-19 at 16.49.04.png" alt=""><figcaption><p>Open the menu panel of your instance.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/CleanShot 2023-04-19 at 16.50.26.png" alt=""><figcaption><p>Open Permissions (RBAC).</p></figcaption></figure>

### Roles

Roles can be managed and created from the Roles view of the Permission Center.

<figure><img src="../.gitbook/assets/CleanShot 2023-04-19 at 16.53.19.png" alt=""><figcaption><p>Manage Role in the Permissions Center.</p></figcaption></figure>

#### Default Roles

Xano includes two default roles, which permissions are standard and cannot be modified. These roles are admin and developer.&#x20;

#### Permissions

Permission types can be set on the various workspace objects in Xano. The permission types are as follows:

* **(C) Create** - permission to create the specified object.
* **(R)** **Read** - permission to read the specific object.
* **(U) Update** - permission to update or modify the specified object.
* **(D) Delete** - permission to delete the specified object.
* **Full** - permission to Create, Read, Update, and Delete (CRUD).
* **Enabled/Disabled** - some objects only require enabling or disabling the permission.
* **Inherit\*** - inherit is a special permission type. This permission will inherit the same permission from the parent role type. Meaning, inherit is chosen for Jane Doe on Workspace A for Run & Debug, then Jane's permission on Run & Debug will inherit the permission of her assigned role.&#x20;

#### Objects

Please read each description carefully to understand the permissions for each object. The objects with role-based access control include:

* Instance Billing - access to manage Instance billing.
* Instance Workspace - access to manage Instance workspaces.
* Workspace Export - allows usage of the workspace export feature.
* Workspace Run & Debug -  allows usage of the workspace Run & Debug feature.
* Workspace Addons - allows access to workspace Addons.
* Workspace API Groups - allows access to workspace API groups.
* Workspace Connect - allows access to workspace Connect Center.
* Workspace Content - allows access to workspace content (database records).
* Workspace Live Data Source - allows access to workspace content (database records) **on the live data source**.&#x20;

{% hint style="info" %}
When disabled, users can still access non-live data source content (if Workspace Content permission is enabled). **Use this permission to protect access to production data.**
{% endhint %}

* Workspace Database - allows access to workspace database.
* Workspace Env - allows access to workspace Environment Variables.
* Workspace Files - allows access to workspace Files and File Management.
* Workspace Functions - allows access to workspace Custom Functions in the Library.
* Workspace Marketplace - allows access to workspace Marketplace.
* Workspace Request History - allows access to workspace API Request History.
* Workspace Task - allows access to workspace Background Tasks.
* Additional objects coming soon.

#### Create a Custom Role

To create a new role select **+ Add new custom role**.

<figure><img src="../.gitbook/assets/CleanShot 2023-04-19 at 17.10.15.gif" alt=""><figcaption><p>Create a new Custom Role.</p></figcaption></figure>

#### Edit Role Permissions

To edit the permissions on a custom role, double-click the permission level to modify and select the new permission from the dropdown.&#x20;

<figure><img src="../.gitbook/assets/CleanShot 2023-04-19 at 17.13.00.gif" alt=""><figcaption><p>Modify Permissions of a Role.</p></figcaption></figure>

### Workspaces View

The initial view in the Permissions Center provides a view of all the Workspaces, team members, and permissions in the Instance.

<figure><img src="../.gitbook/assets/CleanShot 2023-05-03 at 15.43.00.png" alt=""><figcaption></figcaption></figure>

You can easily filter by team member and workspace to see which permissions are enabled for a particular person and workspace.&#x20;

<figure><img src="../.gitbook/assets/CleanShot 2023-05-03 at 15.43.51.png" alt=""><figcaption><p>In this example, we are looking at Michael's permissions across all workspaces.</p></figcaption></figure>

#### **Copy/Paste Permissions**&#x20;

Copy/Paste Permission enables you to quickly assign a team member the same permissions as another one. This is useful when you have team members that need the exact same access across each Workspace.&#x20;

To do this, choose the Copy/Paste button, then the team member you want to copy permissions from, and the team member you wish to paste permissions to.&#x20;

<figure><img src="../.gitbook/assets/CleanShot 2023-05-03 at 15.40.04.png" alt=""><figcaption><p>COPY/PASTE Permissions of one team member to another.</p></figcaption></figure>

#### Edit Permissions on a Workspace

You can edit specific permissions on a Workspace for a team member by [clicking on the permission](role-based-access-control-rbac.md#edit-role-permissions) you want to modify.&#x20;

#### Bulk-Assigning Roles and Permissions

Click the three dots above your roles list to open a menu, offering quick access to managing roles and permissions.

<figure><img src="../.gitbook/assets/CleanShot 2023-05-22 at 12.54.51.png" alt=""><figcaption></figcaption></figure>

**Managing Team Roles**

Choose the role you would like to apply and then select the users you would like to apply the role to.

<figure><img src="../.gitbook/assets/CleanShot 2023-05-22 at 12.56.12.png" alt=""><figcaption></figcaption></figure>

**Bulk Editing Permissions**

Select the users who you would like to modify permissions for. After that, select the workspaces you would like to modify the permissions for with each user. Finally, you can modify the permissions as desired. Any row left **Unmodified** will not be changes,&#x20;

<figure><img src="../.gitbook/assets/CleanShot 2023-05-22 at 12.58.20.png" alt=""><figcaption></figcaption></figure>
