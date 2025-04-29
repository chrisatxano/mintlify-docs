# Add or Edit Record

Add or Edit Record takes the best of both Add and Edit Record, and combines them into one function. Using this will...

* Edit the record if the record is found
* Add it if it isn't

Functionally, it is the same as using Edit Record.

{% @arcade/embed flowId="o8TxUc6du5D35Vv2XRKs" url="https://app.arcade.software/share/o8TxUc6du5D35Vv2XRKs" %}

{% tabs %}
{% tab title="Filter" %}
You need to tell Xano which record you want to edit by providing a field\_name and field\_value. `Field_name` is the name of the database field to look inside of, and `field_value` is the value to look for in that field — for example, `field_name: id` & `field_value: 1`

{% include "../../../.gitbook/includes/add-or-edit-record.md" %}
{% endtab %}

{% tab title="Output" %}
{% include "../../../.gitbook/includes/response-customization.md" %}


{% endtab %}

{% tab title="Settings" %}
{% include "../../../.gitbook/includes/function-descriptions.md" %}


{% endtab %}
{% endtabs %}

