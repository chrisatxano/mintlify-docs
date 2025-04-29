# MCP Functions

{% include "../../.gitbook/includes/release-rollout-note.md" %}

## Run API Endpoint

Executes an API endpoint as part of an MCP Server Tool function stack

<table><thead><tr><th width="125.25311279296875">Parameter</th><th>Purpose</th></tr></thead><tbody><tr><td>API Group</td><td>The API group that contains the API you'd like to run</td></tr><tr><td>Endpoint</td><td>The API endpoint to run</td></tr><tr><td>Return as</td><td>The variable to store the output of the API call</td></tr></tbody></table>

{% hint style="danger" %}
## Note

When using the Run API Endpoint function, authentication tokens are not checked.
{% endhint %}

## Run Task

Executes a task as part of an MCP Server Tool function stack

<table><thead><tr><th width="125.25311279296875">Parameter</th><th>Purpose</th></tr></thead><tbody><tr><td>Task</td><td>The task to run</td></tr></tbody></table>

{% hint style="info" %}
Tasks have no output.
{% endhint %}

{% include "../../.gitbook/includes/function-mcp-list-tool.md" %}

{% include "../../.gitbook/includes/function-mcp-call-tool.md" %}
