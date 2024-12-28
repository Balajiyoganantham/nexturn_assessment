// Import MongoClient from the mongodb module
const MongoClient = require('mongodb').MongoClient;

// Connection URL
const uri = "mongodb://127.0.0.1:27017";

// Database and Collection Name
const dbName = 'mydb';
const collectionName = 'customers';
const client = new MongoClient(uri);

console.log('Connecting to MongoDB server...');
async function connectToMongoDB() {
    try {
        // Connect to the MongoDB server
        await client.connect();
        console.log('Connected to MongoDB server');

        const db = client.db(dbName);
        const collection = db.collection(collectionName);

        // Insert a single document
        const insertResult = await collection.insertOne({ name: 'John Doe' });
        console.log('Inserted a document into the customers collection, with _id:', insertResult.insertedId);

        // Insert multiple documents
        const documents = [
            { name: 'Jane Doe' },
            { name: 'Alice' },
            { name: 'Bob' }
        ];
        const insertManyResult = await collection.insertMany(documents);
        console.log('Inserted multiple documents into the customers collection, with _ids:', insertManyResult.insertedIds);

        // Query for a single document
        const query = { name: 'John Doe' };
        const findResult = await collection.findOne(query);
        console.log('Found a document in the customers collection:', findResult);

    } catch (error) {
        console.error('Error connecting to MongoDB server:', error);
    } finally {
        await client.close();
        console.log('Closed connection to MongoDB server');
    }
}

connectToMongoDB();
