import { createClient, print, hset } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("error", (err) =>
	console.log("Redis Client Redis client not connected to the server:", err)
);

client.on("connect", async () => {
	console.log("Redis client connected to the server");
});

async function setNewSchool(schoolName, value) {
	client.set(schoolName, value, print);
}

const res1 = await client.hset(
	'HolbertonSchools',
	{
		'Portland': '50',
		'Seattle': '80',
		'New York': '20',
		
	}
)

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
	try {
		const value = await getAsync(schoolName);
		console.log(value);
	} catch (err) {
		console.error(err);
	}
}


