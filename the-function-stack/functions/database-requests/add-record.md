# Add Record

Add Record allows you to add a new record to an existing table.

{% @arcade/embed flowId="4tLbIYlynMcDDSpqRvb5" url="https://app.arcade.software/share/4tLbIYlynMcDDSpqRvb5" %}



{% tabs %}
{% tab title="Filter" %}
{% include "../../../.gitbook/includes/add-or-edit-record.md" %}

{% hint style="warning" %}
You are able to manually specify a record ID, but proceed with caution. If you have workflows that rely on sequential IDs, or multiple requests try and add records with the same ID simultaneously, you might run into problems. By default, Xano will auto-increment the ID for you, which is usually best practice.
{% endhint %}
{% endtab %}

{% tab title="Output" %}
{% include "../../../.gitbook/includes/response-customization.md" %}
{% endtab %}

{% tab title="Settings" %}
{% include "../../../.gitbook/includes/function-descriptions.md" %}
{% endtab %}
{% endtabs %}

