import { createClient } from "redis";

const client = createClient();

client.on("error", (err) =>
  console.log("Redis Client Redis client not connected to the server:", err)
);

client.on("connect", async () => {
  console.log("Redis client connected to the server");
});

client.subscribe("holberton school channel")

client.on('message', (channel, message) => {
  if (message === "KILL_SERVER") {
    client.unsubscribe();
    client.quit();
  } else {
    console.log(message);
  }
});
