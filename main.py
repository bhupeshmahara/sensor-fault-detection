# check if connection is made successfully from mongodb atlas

from sensor.configuration.mongodb_connections import MongoDBClient

if __name__ == "__main__":
    mongodb_client = MongoDBClient()
    print(mongodb_client.database.list_collection_names())
