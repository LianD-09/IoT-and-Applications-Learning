const express = require("express");
const bodyParser = require("body-parser");
const MongoClient = require("mongodb").MongoClient;
const ObjectId = require("mongodb").ObjectId;
const URL = "mongodb://localhost/test";
const DATABASE_NAME = "person";


var app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
var database, collection;

app.listen(process.env.PORT || 3000, () => {
    MongoClient.connect(URL, { useNewUrlParser: true }, (error, client) => {
        if(error) {
            throw error;
        }
        database = client.db(DATABASE_NAME);
        collection = database.collection("personnel");
        console.log("Connected to `" + DATABASE_NAME + "`!");
    });
});

app.post("/person", async (request, response) => {
    await collection.insertOne(request.body, (error, result) => {
        if(error) {
            return response.status(500).send(error);
        }
        response.send(result.result);
    });
});

app.get("/person", async (request, response) => {
    await collection.find({}).toArray((error, result) => {
        if(error) {
            return response.status(500).send(error);
        }
        response.send(result);
    });
});

app.get("/person/:id", async (request, response) => {
    if (!ObjectId.isValid(request.params.id)){
        return response.send("Id person invalid!")
    }
    const personId = new ObjectId(request.params.id);
    await collection.findOne({ "_id": personId }, (error, result) => {
        if(error) {
            return response.status(500).send(error);
        }
        response.send(result);
    });
});

app.put("/person/:id", async (request, response) => {
    const newvalues = { $set: { 
        "firstname": request.body.firstname, 
        "lastname": request.body.lastname, 
        "age": request.body.age,
    }}
    if (!ObjectId.isValid(request.params.id)){
        return response.send("Id person invalid!")
    }
    const personId = new ObjectId(request.params.id);
    await collection.updateOne({ "_id": personId }, newvalues, (error, result) => {
        if(error) {
            return response.status(500).send(error);
        }
        response.send(result);
    });
});

app.delete("/person/:id", async (request, response) => {
    if (!ObjectId.isValid(request.params.id)){
        return response.send("Id person invalid!")
    }
    const personId = new ObjectId(request.params.id);
    await collection.deleteOne({ "_id": personId }, (error, result) => {
        if(error) {
            return response.status(500).send(error);
        }
        response.send(result);
    });
});