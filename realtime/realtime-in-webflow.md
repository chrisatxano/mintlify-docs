---
icon: webflow
---

# Realtime in Webflow

{% hint style="warning" %}
**Realtime is in beta, and this documentation can change at any time.**
{% endhint %}

## Getting Started

* Make sure you've reviewed the Realtime documentation [here](broken-reference), as it is helpful to understand the process and how to use the Xano SDK before continuing.
* You need to be comfortable adding and modifying custom code in your Webflow project.

## Building a Live Chat in Webflow (Example)

Head to your Site Settings.

<figure><img src="../.gitbook/assets/CleanShot 2024-05-08 at 10.10.23.png" alt="" width="563"><figcaption></figcaption></figure>

In the Custom Code section, paste the following line of code. This loads the Xano SDK and enables us to use it in the rest of our project. It also defines our 'xanoClient', which we'll call in our separate pages to enable Realtime functionality. Make sure to place your API group base URL and realtime connection hash in the appropriate places, and click Save.

If you prefer, you can change the variable name `const`` `**`xanoClient`** to something else. Please note that any of our examples here will continue to use `xanoClient`, and you'll need to update them accordingly.

```javascript
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@xano/js-sdk@latest/dist/xano.min.js"></script>

<script type="text/javascript">
  const xanoClient = new XanoClient({
  apiGroupBaseUrl: 'YOUR BASE URL HERE',
  realtimeConnectionHash: 'YOUR REALTIME CONNECTION HASH HERE',
});
</script>
```

{% hint style="info" %}
At this point, Webflow will ask you to publish your site to see the changes. Please note that you may need to view a published version of the site to verify that Realtime is enabled and working as expected.
{% endhint %}

<figure><img src="../.gitbook/assets/CleanShot 2024-05-08 at 10.18.41.png" alt=""><figcaption></figcaption></figure>

Head back to the Designer, and we can start building realtime functionality into our project.&#x20;

For this example, we've set up a simple chat application, similar to the example prepared in the main Realtime documentation.

<figure><img src="../.gitbook/assets/CleanShot 2024-05-08 at 12.26.11.png" alt=""><figcaption></figcaption></figure>

We know that we want this page to connect to a specific channel, so let's head to our page settings and add some custom code.

```javascript
<script type="text/javascript">
const marvelChannel = xanoClient.channel("marvel-chat-room");
marvelChannel.on((message) => {
  switch (message.action) {
    case 'message':
      messageReceived(message.body);
      break;
    default:
      console.info(message);
  }
});
</script>
```

{% hint style="info" %}
Please note that when it comes to how you want to handle realtime implementation for your specific project, your custom code and configuration may look vastly different. The code provided in this section is for demonstration purposes only.\
\
Typically when performing an action like this in Webflow, it follows a basic structure, where we...

1. Create an element on our page to serve as a template, and assign it a class.&#x20;
2. Once you have styled the element to your liking, give it a subclass. Change the properties of the subclass to set Display to None.
3. In your custom code, when it's time to render a message, you'll need to generate a copy of the original element containing the message or other content to show.
{% endhint %}

This piece of code, placed in the 'before \</body> tag' section, tells the page that we want to connect to the marvel-chat-room channel and listen for messages. Any time we receive a new message, we want to execute another function called messageReceived, which will handle rendering the new message on the page.

Now that we've set up actually connecting to the realtime server, we can start working with our messages. This is an example code snippet that lives right above our \</body> tag to render new messages on the page.

```javascript
function messageReceived(payload) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message");
  const messageText = document.createElement("div");
  messageText.classList.add("message-text");
  messageText.textContent = payload;
  messageDiv.appendChild(messageText);
  messageDiv.style.display = 'block';
  const chatboxes = document.getElementsByClassName("chatbox");
  for (const chatbox of chatboxes) {
    chatbox.appendChild(messageDiv);
  }
}
```

<details>

<summary><strong>Code Explanation</strong></summary>

In this code, we start by defining our function and the data it needs to run.

```javascript
function messageReceived(payload) {
```

We then define a couple of variables, messageDiv and messageText, targeting newly created div elements to contain our message. We're also applying some styling to the message block to make sure it displays.

```javascript
const messageDiv = document.createElement("div");
  messageDiv.classList.add("message");
const messageText = document.createElement("div");
  messageText.classList.add("message-text");
  messageText.textContent = payload;
  messageDiv.appendChild(messageText);
  messageDiv.style.display = 'block';
```

In the final section, we look for the element on our page with the class of 'chatbox' and place the new div inside of it.

```javascript
const chatboxes = document.getElementsByClassName("chatbox");
  for (const chatbox of chatboxes) {
    chatbox.appendChild(messageDiv);
  }
}
```

</details>

We're almost there. The last thing we need to do is add the ability to send new messages.

```javascript
function sendMessage() {
      const message = document.getElementById("messageInput").value;
      marvelChannel.message(message);
      document.getElementById("messageInput").value = "";
    }

    document.getElementById("sendButton").addEventListener("click", sendMessage);
```

<details>

<summary>Code Explanation</summary>

First, we define a new function called sendMessage that is triggered every time we need to send a new message to the channel.

```javascript
function sendMessage() {
```

Inside of this function, we define our message as the value of our input.

```javascript
const message = document.getElementById("messageInput").value;
```

We can then send our message to the channel, and then clear the input value to prepare for a new message.

```javascript
     marvelChannel.message(message);
      document.getElementById("messageInput").value = "";
    }
```

The last line of the code adds an event listener to our sendButton. This makes sure that every time the button is clicked, the function is executed.

```javascript
  document.getElementById("sendButton").addEventListener("click", sendMessage);
```

</details>

And with that, you've just built live chat in your Webflow site. Publish your changes and check it out!

### View the sample Webflow project [here](https://preview.webflow.com/preview/realtime-b964af?utm_medium=preview_link\&utm_source=designer\&utm_content=realtime-b964af\&preview=c483fbe91f630dec469a273e58c9c8c6\&workflow=preview).

You'll want to clone this project so you can fill in your API group base URL and connection hash in the site settings.
