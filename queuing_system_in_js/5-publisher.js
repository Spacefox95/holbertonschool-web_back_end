import { createClient } from "redis";

const client = createClient();

client.on("error", (err) => {
	console.log("Redis Client Redis client not connected to the server:", err)
});

client.on("connect", () => {
	console.log("Redis client connected to the server");

function publishMessage(message, time) {
	console.log("About to send", message)
	setTimeout(() => {
		client.publish('holberton school channel', message)
	}, time)
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
});
