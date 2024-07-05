from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError


# Initialize MongoDB connection
try:
    # Establish a connection to the MongoDB server
    client = MongoClient('''Enter your connection string''')

    # Access the specific database
    db = client.proj1

    # Access the specific collection within the database
    collection = db.health_data

    # Verify the connection to the database
    # This will raise a ConnectionFailure if the server is not reachable
    client.admin.command('ping')
    print("Connected to MongoDB successfully")

except ConnectionFailure:
    # Handle connection failure exception
    print("Failed to connect to MongoDB. Please ensure that the MongoDB server is running and accessible.")
    raise

except ConfigurationError:
    # Handle configuration error exception
    print("MongoDB configuration error. Please check the connection URI and configuration settings.")
    raise

except Exception as e:
    # Handle any other exceptions that may occur
    print(f"An error occurred: {str(e)}")
    raise

