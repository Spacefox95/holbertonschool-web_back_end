import { createClient, print } from "redis";

const client = createClient();

client.on("error", (err) => console.log("Redis Client Redis client not connected to the server:", err))
client.set("message", "Redis client connected to the server");
client.get('message', (err, value) => {
console.log(value)
})

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, print)
}

function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, value) => {
		console.log(value)
	})
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');