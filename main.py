from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from typing import List, Optional
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
    example: Optional[str] = None

class RequestType(BaseModel):
    type_name: str
    purpose: str
    information_to_collect: List[InformationField]
    request_type_owner: Optional[str] = None
    time_of_creation: Optional[datetime] = None
    time_of_update: Optional[datetime] = None

# Helper functions to read/write from/to db.json
def read_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4, default=str)

# Helper function to validate the email in headers
def validate_email(x_user_email: Optional[str] = Header(None)):
    if not x_user_email:
        raise HTTPException(status_code=400, detail="Email header is missing")
    return x_user_email

@app.get("/request-types/")
def get_request_types(x_user_email: str = Depends(validate_email)):
    data = read_db()
    filtered_data = [rt for rt in data if rt.get("request_type_owner") == x_user_email]
    return filtered_data

@app.post("/request-types/")
def create_request_type(request_type: RequestType, x_user_email: str = Depends(validate_email)):
    data = read_db()
    request_type.time_of_creation = datetime.now(timezone.utc)  # Set time of creation with timezone
    request_type.request_type_owner = x_user_email  # Set the request type owner from the header
    data.append(request_type.model_dump())
    write_db(data)
    return {"message": "Request type created successfully."}

@app.put("/request-types/{index}")
def update_request_type(index: int, request_type: RequestType, x_user_email: str = Depends(validate_email)):
    data = read_db()
    if index >= len(data):
        raise HTTPException(status_code=404, detail="Request type not found")
    
    # Retrieve the existing request type
    existing_request_type = data[index]

    # Check if the logged-in user is the owner
    if existing_request_type.get("request_type_owner") != x_user_email:
        raise HTTPException(status_code=403, detail="You do not have permission to update this request type")

    # Preserve the original creation time and set the update time
    request_type.time_of_creation = existing_request_type.get("time_of_creation")
    request_type.time_of_update = datetime.now(timezone.utc)
    request_type.request_type_owner = x_user_email  # Ensure the owner remains the same

    data[index] = request_type.model_dump()
    write_db(data)
    return {"message": "Request type updated successfully."}

@app.delete("/request-types/{index}")
def delete_request_type(index: int, x_user_email: str = Depends(validate_email)):
    data = read_db()
    if index >= len(data):
        raise HTTPException(status_code=404, detail="Request type not found")
    
    # Retrieve the existing request type
    existing_request_type = data[index]

    # Check if the logged-in user is the owner
    if existing_request_type.get("request_type_owner") != x_user_email:
        raise HTTPException(status_code=403, detail="You do not have permission to delete this request type")

    del data[index]
    write_db(data)
    return {"message": "Request type deleted successfully."}