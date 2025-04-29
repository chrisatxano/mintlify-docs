# Realtime Functions

While Realtime is fully functional without implementing anything in your function stacks, you may find yourself wanting to build function stacks to extend the functionality of Realtime.

This is possible with the new **Realtime Event** function, located under APIs & Lambdas in the function panel.

<figure><img src="../../../.gitbook/assets/CleanShot 2024-05-09 at 16.38.39.png" alt="" width="563"><figcaption></figcaption></figure>

### Using the Realtime Event Function

This function sends a message of type 'event' to the channel specified. Remember, a message can be anything from plain text to a JSON object for even further flexibility.

<figure><img src="../../../.gitbook/assets/CleanShot 2024-05-09 at 17.02.27.png" alt="" width="446"><figcaption></figcaption></figure>

**Channel** - The channel to send the event to

**Data** - The payload of the event

**Database** - If this channel requires authentication, select the corresponding database that handles your authentication here

You can use variables for Channel and Data to make the event behave dynamically.

{% hint style="info" %}
Please note that Event is different than Message, and will need to be handled accordingly by your frontend.
{% endhint %}

### Example

Realtime connections do not log message history. This means that once a user leaves our Marvel chat room, if they come back, they won't be able to see any of the previous messages. So, we want to store our messages in a database table as they are sent to the channel.

We could approach this in a couple of different ways.

1. Have our frontend send an API request at the same time a message is sent to the channel to log the message.
2. Have our frontend only send an API request, and our API can handle delivering the message once it is stored.

For this example, we will use the second option. We need to first modify our frontend code to send the API request, instead of sending the message directly to the channel. We'll do this by defining a new function and then calling it when our button is clicked.

```javascript
function sendMessageToRealtime(channel, message) {
        fetch('ENDPOINT URL THAT RECEIVES THE MESSAGE', {
        method: 'POST',
        headers: {
           'Content-Type': 'application/json'
           },
        body: JSON.stringify({
        channel: 'your_channel_name',
        message: 'your_message'
    })
  });
}

document.getElementById('form').addEventListener('submit', (event) => {
         event.preventDefault();
         sendMessageToRealtime('marvel_chat_room', document.getElementById(message.value))
         event.target.message.value = '';
});
```

<details>

<summary><strong>Code Explanation</strong></summary>

First, we define the function and make sure we define two parameters: channel for the channel to send the message to, and message for the message body.

```javascript
function sendMessageToRealtime(channel, message) {
```

After that, we're using fetch, a Javascript function to send API requests, to our endpoint. We don't need to worry much about the technical details here if you aren't comfortable, but you may need to change the method and/or add new parameters to the body of the request depending on your use case. For this example, all our API needs is that channel name and message.

```javascript
fetch('ENDPOINT URL THAT RECEIVES THE MESSAGE', {
        method: 'POST',
        headers: {
           'Content-Type': 'application/json'
           },
        body: JSON.stringify({
        channel: channel,
        message: message
    })
  });
```

Now, we need to handle what happens when our Send button is clicked. We'll start by looking for that element and adding an event listener to it. It just looks for our form, which has an ID of form, and a submit button inside of it.

```javascript
document.getElementById('form').addEventListener('submit', (event) => {
```

We'll add a line to ensure that no 'default' behavior occurs when a user clicks the send button.

```javascript
event.preventDefault();
```

Next, we'll call our sendMessageToRealtime function and give it our 'marvel-chat-room' channel name and the value of the message input box. Right after that, we clear the input to prepare for the next message.

```javascript
sendMessageToRealtime('marvel_chat_room', document.getElementById(event.target.message.value))
event.target.message.value = '';
```

</details>

We need to set up a database table to log the messages.

<figure><img src="../../../.gitbook/assets/CleanShot 2024-05-09 at 19.18.59@2x.png" alt="" width="563"><figcaption></figcaption></figure>

Here's the API endpoint we are sending these requests to.

<figure><img src="../../../.gitbook/assets/CleanShot 2024-05-09 at 19.20.06@2x.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/CleanShot 2024-05-09 at 19.26.11@2x.png" alt=""><figcaption></figcaption></figure>

This endpoint takes in the channel name and message data, fires our Realtime Event function, and then stores the message in the database table.

At this point, we have modified our frontend code and set up the API in Xano to handle the requests. Now, when our users send messages, they will be logged in the database table, and we still get all of the benefits of utilizing the realtime connection.
