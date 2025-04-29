# Connecting Clients

{% include "../../.gitbook/includes/release-rollout-note.md" %}

## <img src="../../.gitbook/assets/cursorlogo.png" alt="" data-size="line"> Cursor <a href="#cursor" id="cursor"></a>

The below instructions will allow you to connect your Xano MCP server to Cursor and make them available across any project. The below method does not support authentication. If you need authentication or want to define per-project MCPs, use these instructions instead.

{% stepper %}
{% step %}
### Open your Cursor settings

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-18 at 09.34.48.png" alt="" width="412"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Under the <mark style="background-color:blue;">Features</mark> subsection, scroll down to MCP Servers


{% endstep %}

{% step %}
### Click <mark style="background-color:blue;">+ Add new MCP Server</mark>&#x20;

Give your server a name.

The `type` should be `sse`

Paste your server URL in the Server URL section. You can retrieve your server URL by navigating to your server in Xano and clicking **Copy Connection URL**.
{% endstep %}

{% step %}
### You should now see your MCP Server ready in Cursor

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-18 at 09.39.11.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### In your chat window, you can now interact with the tools included in your MCP server that's connected

Make sure the conversation type is set to Agent

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-18 at 09.39.59.png" alt=""><figcaption></figcaption></figure></div>

In our example, we have a tool that checks if a user is marked as an administrator.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-18 at 09.41.26.png" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

## <img src="../../.gitbook/assets/cursorlogo.png" alt="" data-size="line"> Cursor (per-project) <a href="#cursor" id="cursor"></a>

{% hint style="danger" %}
**Please note that Cursor does not currently support authentication headers for SSE connections. You can only use tools that do not require authentication.**
{% endhint %}

{% stepper %}
{% step %}
### In your project's root directory, create a new folder called `.cursor`
{% endstep %}

{% step %}
### Create a new file inside of that folder called `mcp.json`
{% endstep %}

{% step %}
### Fill out the required details inside of `mcp.json`

If the file is blank, start with the basic structure and replace the placeholder values with your own.

```json
{
  "mcpServers": {
    "YOUR SERVER NAME HERE": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "YOUR CONNECTION URL HERE"
      ]
    }
  }
}
```

You can add multiple entries if you have multiple MCP servers. See the below example.

```json
{
  "mcpServers": {
    "xano_development": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "CONNECTION URL HERE"
      ]
    },
    "xano_production": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "CONNECTION URL HERE"
      ]
    },
    "xano_tools": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "CONNECTION URL HERE"
      ]
    }
  }
}
```
{% endstep %}

{% step %}
### Restart Cursor.

In your chat window, you can now interact with the tools included in your MCP server that's connected

Make sure the conversation type is set to Agent

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-18 at 09.39.59.png" alt=""><figcaption></figcaption></figure></div>

In our example, we have a tool that checks if a user is marked as an administrator.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-18 at 09.41.26.png" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

***

## <img src="../../.gitbook/assets/image (90).png" alt="" data-size="line"> Claude Desktop <a href="#claudedesktop" id="claudedesktop"></a>

{% stepper %}
{% step %}
### Install the prerequisites

You need Node.js installed on your system.

Download the latest installer from the [Node.js official website](https://nodejs.org/en) for your specific platform.
{% endstep %}

{% step %}
### Open Claude Desktop's config file in your text / code editor of choice

* Mac OS: `~/Library/Application Support/Claude/claude_desktop_config.json`
* Windows: `%APPDATA%\Claude\claude_desktop_config.json`
{% endstep %}

{% step %}
### Add an entry in the config file for your Xano MCP server

Click **Edit Config** and in the window that opens, open `claude_desktop_config.json` in your favorite text or code editor.

If the file is blank, start with the basic structure and replace the placeholder values with your own.

```json
{
  "mcpServers": {
    "YOUR SERVER NAME HERE": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "YOUR CONNECTION URL HERE"
      ]
    }
  }
}
```

If any of your tools require authentication, you can add that to your config file. See the below example.

```json
{
  "mcpServers": {
    "xano": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "YOUR CONNECTION URL HERE",
        "--header",
        "Authorization: Bearer ${AUTH_TOKEN}"
      ],
      "env": {
        "AUTH_TOKEN": "YOUR AUTH TOKEN HERE"
      }
    }
  }
}
```

You can add multiple entries if you have multiple MCP servers. See the below example.

```json
{
  "mcpServers": {
    "xano_development": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "CONNECTION URL HERE"
      ]
    },
    "xano_production": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "CONNECTION URL HERE"
      ]
    },
    "xano_tools": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "CONNECTION URL HERE"
      ]
    }
  }
}
```
{% endstep %}

{% step %}
### Relaunch Claude Desktop to interact with your MCP server(s)

In Claude, you should see a new icon under your chat box with a :tools: icon.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-18 at 17.07.30.png" alt="" width="563"><figcaption></figcaption></figure></div>

You can click on this to view information about your available tools.

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-18 at 17.08.56.png" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

***

## Windsurf

{% stepper %}
{% step %}
### Head to your Windsurf settings

<div align="left" data-full-width="false"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-23 at 16.59.59 (1).png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Click Cascade, and then Add Server

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-23 at 17.01.44.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Click 'Add Custom Server'

<figure><img src="../../.gitbook/assets/CleanShot 2025-04-23 at 17.02.22.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Fill out the config file with your MCP server details

If the file is blank, start with the basic structure and replace the placeholder values with your own.

```json
{
  "mcpServers": {
    "YOUR SERVER NAME HERE": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "YOUR CONNECTION URL HERE"
      ]
    }
  }
}
```

If any of your tools require authentication, you can add that to your config file. See the below example.

```json
{
  "mcpServers": {
    "xano": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "YOUR CONNECTION URL HERE",
        "--header",
        "Authorization: Bearer ${AUTH_TOKEN}"
      ],
      "env": {
        "AUTH_TOKEN": "YOUR AUTH TOKEN HERE"
      }
    }
  }
}
```

You can add multiple entries if you have multiple MCP servers. See the below example.

```json
{
  "mcpServers": {
    "xano_development": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "CONNECTION URL HERE"
      ]
    },
    "xano_production": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "CONNECTION URL HERE"
      ]
    },
    "xano_tools": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "CONNECTION URL HERE"
      ]
    }
  }
}
```
{% endstep %}

{% step %}
### Click the Refresh button, and you should see your MCP server(s) available


{% endstep %}
{% endstepper %}

***

## FAQ and Troubleshooting

#### How do I use my MCP server in one of these clients?

Once you're connected following the instructions above, you should be able to converse with the AI like you would any other, asking real-world questions that the tools you built should be able to answer.

For example, if we have a tool that just returns a true or false, we'd probably be asking yes or no questions, such as "Does this user, john@email.com, have administrator access?"

<div align="left"><figure><img src="../../.gitbook/assets/CleanShot 2025-04-21 at 08.22.44.png" alt="" width="375"><figcaption><p>An example of using a Xano MCP server in Claude Desktop</p></figcaption></figure></div>

#### I can't connect to my server from my client of choice.

Check the error message you're receiving for clues. This could be due to one of the following:

* An incorrectly formatted configuration file
* Your Xano MCP Server is not set to allow connections
* You're not providing an authentication token to a server that requires it

#### For MCP servers with tools that require authentication, after a long waiting period, I get a connection error.

In our current testing, we are finding that running multiple MCP clients causes this issue. Our recommendation is to stick with a single client for the time being.

Try these steps:

* Close any open MCP clients
* Ensure that your authentication token is not expired
*   On Mac, run&#x20;

    ```
    rm -rf ~/.mcp-auth
    ```
* Restart your MCP client and try connecting again
