# Get Record

Get Record allows you to retrieve a single record from a database table using a single field to search by.

{% @arcade/embed flowId="lZOuWcUumARAVBkZLcb7" url="https://app.arcade.software/share/lZOuWcUumARAVBkZLcb7" %}



{% tabs %}
{% tab title="Filter" %}
In Get Record, you'll provide the name of the field to search inside of, and the value to search for. These can come from inputs, variables, or you can manually specify a value.

**field\_name** is the name of the field to look inside of. For example, if we wanted to search for a record with a specific ID, we'd type `id` here.

**field\_value** is the value to search for in the provided field. Assuming we are searching in the `id` field, we would put the ID to search for here.

{% hint style="info" %}
If you need to find a record based on multiple fields, use [Query All Records](query-all-records/) instead.
{% endhint %}

{% include "../../../.gitbook/includes/lock-record-s.md" %}
{% endtab %}

{% tab title="Output" %}
{% include "../../../.gitbook/includes/response-customization.md" %}
{% endtab %}

{% tab title="Settings" %}
{% include "../../../.gitbook/includes/function-descriptions.md" %}
{% endtab %}
{% endtabs %}

