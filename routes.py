from fastapi import APIRouter,HTTPException
from models import Records, Records_fetch
from config.db import collection
from fastapi.responses import JSONResponse
from typing import List

router1 = APIRouter()

# Helper function to convert MongoDB document to Pydantic model
def record_helper(data) -> Records:
    return Records(
        BP = data["BP"],
        Height_in_meters = data["Height_in_meters"],
        Weight_in_kg = data["Weight_in_kg"],
        Fever = data["Fever"],
        Date = data["Date"],
        Name = data["Name"],
        Gender = data["Gender"]
    )

# API to store user health record
@router1.post("/", response_model=Records)
async def add(record: Records):
    try:
        record_dict = record.dict()                     # Converts record object into dictionary
        result = collection.insert_one(record_dict)     # Insert data into database
        if result.inserted_id:
            return JSONResponse(content={'status_code':200, 'detail':"Record added successfully"})
        else:
            raise HTTPException(status_code=500, detail="Failed to store record")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


# API to fetch user health record
@router1.get("/fetch", response_model=List[Records])
async def fetch(record: Records_fetch):
    try:
        # Validate and clean the input data
        validated_data = record.model_dump()
        key_list = []
        for key in validated_data.keys():
            if validated_data[key] == None:
                key_list.append(key)
        for key in key_list:
            validated_data.pop(key)

        # Fetch records from the database
        record = list(collection.find(validated_data))
        if record:
            return [record_helper(data) for data in record]
        else:
            raise HTTPException(status_code=404, detail="No records found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    