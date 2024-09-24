import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const hashKey = 'HolbertonSchools';
const hashValues = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
};

for (const [field, value] of Object.entries(hashValues)) {
  client.hset(hashKey, field, value, redis.print);
}

client.hgetall(hashKey, (err, object) => {
  console.log(object);
});
