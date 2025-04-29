---
icon: lock-keyhole-open
---

# Channel Permissions

Channels are opened with your front-end's implementation of Realtime.

```javascript
const marvelChannel = this.xanoClient.channel("marvel-chat-room");
```

Each channel needs to have permissions defined to ensure that they behave in the way that you expect and remain secure. On this page, we'll go over the various permission settings available and show you how to apply them.

Securing your Realtime channels is a multi-step process, and is not always solely reliant on the channel permissions you set. This includes:

* Setting the proper channel permissions for your use case
* Using nested channels to separate data
* Using [Realtime Triggers](../the-function-stack/building-with-visual-development/triggers.md) to act as a primary or secondary measure to block messages from being sent to the channel
* Generating separate authentication tokens for connecting to the realtime server
* Obfuscating the implementation on your front-end, and ensuring that channel creation is handled properly

## Permissions

### Anonymous Clients

Anonymous Clients means that you allow unauthenticated users to connect to your channels, but they can not send messages.

### Presence

Every client connected to this channel will receive a the list of all the other clients (including yourself). Note that authenticated client details will be augmented with the extra information stored in their JWT token.

### Client Public Messaging

This option allows authenticated and unauthenticated clients to send messages to the channel. These messages will be sent to all the users connected to the channel.

### Authenticated Only (Client Public Messaging)

Similar to Client Public Messaging, this permission allows only authenticated users to send messages to the channel. Unauthenticated clients can still see the messages being sent to the channel.

### Client Authenticated Messaging

Every message sent to the channel by authenticated clients will only broadcasted to all other authenticated clients. This means that anyone can connect to that channel, but only authenticated client will receive messages broadcasted by the channel. Anonymous client will not receive any messages.

### Client Private Messaging

This enables clients to send messages directly to other clients without requiring authentication as long as both clients are present in the channel.

### Authenticated Only (Client Private Messaging)

This permission enables client private messaging only between authenticated clients. Unauthenticated clients can not send private messages.

{% hint style="warning" %}
It's important to note that some of these permissions may appear to have logical dependencies, but they do not. For example, if you enable **Client Public Messaging**, this implies that **Anonymous Clients** is also enabled.
{% endhint %}

## Applying Permissions

From the Realtime Settings panel, click the icon shown below to define channel permissions.

<figure><img src="../.gitbook/assets/CleanShot 2024-05-07 at 21.31.05@2x.png" alt="" width="375"><figcaption></figcaption></figure>

On the next panel that opens, fill in the options shown.

#### Channel Status

Defines whether or not these channel permissions are utilized

#### Channel Target

This is essentially the name of the channel you are creating permissions for. Channel names can be dynamic to support creation of new channels from your front-end by enabling the **nested channels** option. Using nested channels along with a name like "chatroom/\*" will allow you to create channels that begin with "chatroom/" and anything else afterwards, such as a unique channel identifier. If you do not enable nested channels, the permissions will just apply to the channel name you specify.

#### Description

Give your permission layout a description for organizational purposes, if you wish.

#### Permissions

Using the list of permissions on this page, determine the correct set of permissions to apply to any channels that match the name pattern.

**Channel Triggers**

Triggers are function stacks that can run when messages or events are sent to the channel(s) impacted by these permissions. You need to first save your changes to enable adding triggers when creating new permissions.

For more information about Realtime Triggers, see [this section](../the-function-stack/building-with-visual-development/triggers.md) of our documentation.

## Permission Examples

{% hint style="info" %}
Please note that **Presence** is usually optional no matter the scenario and is just based on if you want to utilize presence updates in your realtime channels.
{% endhint %}

| Context                                                                                                                                                                                                                                                      | Permissions                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| A chat application where users can both connect and send messages anonymously                                                                                                                                                                                | <img src="../.gitbook/assets/CleanShot 2024-05-30 at 10.42.07@2x.png" alt="" data-size="original"> |
| A chat application where users can connect anonymously, but authentication is required to send messages                                                                                                                                                      | <img src="../.gitbook/assets/CleanShot 2024-05-30 at 10.44.22@2x.png" alt="" data-size="original"> |
| A notification system that allows for unauthenticated users to connect so they can receive notifications, but sending messages is not allowed. You would send notifications to this type of channel through the [Realtime Event](broken-reference) function. | <img src="../.gitbook/assets/CleanShot 2024-05-30 at 14.10.39@2x.png" alt="" data-size="original"> |
| A chat application that only allows authenticated users to connect and send messages                                                                                                                                                                         | <img src="../.gitbook/assets/CleanShot 2024-05-30 at 10.53.17@2x.png" alt="" data-size="original"> |
| A chat application that only allows authenticated users to connect, and allows direct client-client private messaging for authenticated users                                                                                                                | <img src="../.gitbook/assets/CleanShot 2024-05-30 at 10.54.27@2x.png" alt="" data-size="original"> |
