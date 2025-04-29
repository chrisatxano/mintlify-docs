# Workspace Import and Export

{% hint style="info" %}
**Before you proceed...**

Workspace exports will only contain one branch which defaults to live unless you specify a branch in the request.

Drafts are not exported.

Imports overwrite the entire contents of the destination workspace.

These endpoints will only function properly on **paid Xano plans**.
{% endhint %}



{% embed url="https://youtu.be/Tv0puLXd6B0" %}

{% openapi src="../../.gitbook/assets/apispec_meta (1).json" path="/workspace/{workspace_id}/export-schema" method="post" %}
[apispec_meta (1).json](<../../.gitbook/assets/apispec_meta (1).json>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/apispec_meta (1).json" path="/workspace/{workspace_id}/export" method="post" %}
[apispec_meta (1).json](<../../.gitbook/assets/apispec_meta (1).json>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/apispec_meta (1).json" path="/workspace/{workspace_id}/import-schema" method="post" %}
[apispec_meta (1).json](<../../.gitbook/assets/apispec_meta (1).json>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/apispec_meta (1).json" path="/workspace/{workspace_id}/import" method="post" %}
[apispec_meta (1).json](<../../.gitbook/assets/apispec_meta (1).json>)
{% endopenapi %}
