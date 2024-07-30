// Export a function named "run" that takes three parameters: client, message, args
module.exports.run = async (client, message, args) => {
    // Send a message to the channel indicating the bot's latency
    const msg = await message.channel.send("Pinging...");

    // Calculate the bot's latency
    const latency = msg.createdTimestamp - message.createdTimestamp;

    // Edit the previous message to display the bot's latency
    msg.edit(`Pong! Latency is ${latency}ms.`);
};

// Export a help object providing information about the command
module.exports.help = {
    name: "ping",
    description: "Check the bot's latency."
};