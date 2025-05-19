import { createClient } from "redis";

const client = createClient();

client.on("error", (err) => console.log("Redis Client Redis client not connected to the server:", err.message))
client.set("message", "Redis client connected to the server");
client.get('message', (err, value) => {
console.log(value)
})
