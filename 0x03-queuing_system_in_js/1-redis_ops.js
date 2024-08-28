import { print, createClient } from 'redis';

// Create a Redis client
const redisClient = createClient();

// Event listener for successful connection
redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});
redisClient.on('connect', () => console.log('Redis client connected to the server'));

console.log(redisClient.connected);

// Event listener for error during connection
function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}


function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (_error, value) => {
    if (value) console.log(value);
  });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
