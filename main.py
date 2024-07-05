from fastapi import FastAPI
from routes import router1

# Initialize the FastAPI application
try:
    app = FastAPI()

    # Include the router1 from the routes module
    app.include_router(router1)

    # Print a success message
    print("FastAPI application initialized successfully and router included.")

except ImportError as e:
    # Handle import errors, such as missing routes module
    print(f"ImportError: {str(e)}")
    raise HTTPException(status_code=500, detail="Failed to import required modules. Please check your configuration.")

except Exception as e:
    # Handle any other exceptions
    print(f"An error occurred: {str(e)}")
    raise HTTPException(status_code=500, detail="An unexpected error occurred during application initialization.")