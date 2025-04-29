---
hidden: true
---

# Fundamentals

## How do frontend connections work?

A frontend can connect with Xano in a few different ways.

### APIs (most common)

When you build APIs in Xano, each API has an **endpoint URL** which your frontend can use to send requests to the API. This is the most common method a frontend can connect to what you have built in Xano.

:blue\_book: [**Read more about building APIs**](../the-function-stack/building-with-visual-development/apis/)

### Direct Database Connection

Some frontends might support connecting to your Xano database directly, eliminating the need for any API endpoints — however, this typically only facilitates simple tasks like adding, updating, and changing data.

:blue\_book: [**Read more about direct database connections**](../xano-features/instance-settings/direct-database-connector.md)

### Metadata API

The Metadata API is a set of API endpoints that Xano provides, enabling you to programmatically manage data inside of your workspaces, including retrieving information about tables, table data, and API endpoints. Some frontends utilize this method to facilitate the connection between itself and Xano, providing an easier way to utilize your Xano APIs with that platform.

:blue\_book: [**Read more about the Metadata API**](../xano-features/metadata-api/)

## How do I choose the right frontend?

Xano is **frontend agnostic**, meaning that as long as the frontend can interact with REST APIs, you shouldn't have any trouble connecting it to Xano. In some cases, you might use multiple frontends — for example, a website and a mobile application.

Choosing the right frontend can be challenging, but typically revolves around the following considerations:

<table><thead><tr><th width="306"></th><th></th></tr></thead><tbody><tr><td>Targeted platforms</td><td>This is what the frontend is designed to deliver — a website, web app, mobile application, or similar. Where do you intend your users to utilize what you are building?</td></tr><tr><td>Features and functionality</td><td>What do you need your frontend to do? Are you looking for more of a traditional developer experience, or do you want super-simple drag and drop building? Do you want to be able to export code or have the service deploy for you?</td></tr><tr><td>Cost</td><td>While just like the backend, the frontend is a crucial piece of your application and you should expect some cost associated with it, what fits in your budget? </td></tr></tbody></table>

## Can I build my own frontend from scratch?

Of course! We make this easier with the [Xano Javascript SDK](https://go.xano.co/sdk).

## What frontends can connect to Xano?

Visit our [Connect page](https://xano.com/connect) for more information on several of the frontends that work with Xano.
