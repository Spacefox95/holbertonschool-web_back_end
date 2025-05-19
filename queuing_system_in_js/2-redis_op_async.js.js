import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("error", (err) =>
  console.log("Redis Client Redis client not connected to the server:", err)
);

client.on("connect", async () => {
  console.log("Redis client connected to the server");

  await displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFrancisco", "100");
  await displaySchoolValue("HolbertonSanFrancisco");
});

async function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}
