from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime, timezone
import json
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to be more restrictive in production
    allow_credentials=True,
    allow_methods=["*"],  # This allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],
)

DB_FILE = "db.json"

# Data Models
class InformationField(BaseModel):
    name: str
    field_type: str
    required: bool
    example: str = None

class RequestType(BaseModel):
    request_type: str
    purpose: str
    information_to_collect: List[InformationField]
    request_type_owner: str
    time_of_creation: datetime
    time_of_update: datetime = None

# Helper functions to read/write from/to db.json
def read_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4, default=str)

@app.get("/request-types/")
def get_request_types():
    return read_db()

@app.post("/request-types/")
def create_request_type(request_type: RequestType):
    data = read_db()
    request_type.time_of_creation = datetime.now(timezone.utc)  # Set time of creation with timezone
    data.append(request_type.model_dump())
    write_db(data)
    return {"message": "Request type created successfully."}

@app.put("/request-types/{index}")
def update_request_type(index: int, request_type: RequestType):
    data = read_db()
    if index >= len(data):
        raise HTTPException(status_code=404, detail="Request type not found")
    
    # Retrieve the existing time_of_creation
    existing_request_type = data[index]
    time_of_creation = existing_request_type.get("time_of_creation")

    # Update the request type with the existing time_of_creation
    request_type.time_of_creation = time_of_creation  # Preserve the original creation time
    request_type.time_of_update = datetime.now(timezone.utc)  # Set the time of update

    data[index] = request_type.model_dump()
    write_db(data)
    return {"message": "Request type updated successfully."}

@app.delete("/request-types/{index}")
def delete_request_type(index: int):
    data = read_db()
    if index >= len(data):
        raise HTTPException(status_code=404, detail="Request type not found")
    del data[index]
    write_db(data)
    return {"message": "Request type deleted successfully."}