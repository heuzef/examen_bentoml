import numpy as np
import bentoml
from bentoml.io import NumpyNdarray, JSON
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import base64
import time
from datetime import datetime, timedelta, timezone

security = HTTPBasic()

# User credentials for authentication
USERS = {
    "admin": "psw",
    "bentoml": "bentoml"
}

app = FastAPI()
security = HTTPBasic()

# Pydantic model to validate input data
class InputModel(BaseModel):
    GRE_Score: int
    TOEFL_Score: int
    University_Rating: int
    SOP: float
    LOR: float
    CGPA: float
    Research: int

# Get the model from the Model Store
model_runner = bentoml.sklearn.get("admissions_model:latest").to_runner()

# Create a service API
service = bentoml.Service("service", runners=[model_runner])

# Login endpoint
@service.api(input=JSON(), output=JSON(), route='/login')
async def login(credentials: dict) -> dict:
    username = credentials.get("username")
    password = credentials.get("password")

    if username in USERS and USERS[username] == password:
        return {"message": f"Hello, {username}!"}
    else:
        return JSONResponse(status_code=401)

# Create an API endpoint for the service
@service.api(
    input=JSON(pydantic_model=InputModel),
    output=JSON(),
    route='/predict'
)
async def predict(input_data: InputModel, ctx: bentoml.Context) -> dict:
    request = ctx.request

    # Convert the input data to a numpy array
    input_series = np.array([
        input_data.GRE_Score, 
        input_data.TOEFL_Score, 
        input_data.University_Rating, 
        input_data.SOP, input_data.LOR, 
        input_data.CGPA, 
        input_data.Research
        ])

    prediction = await model_runner.predict.async_run(input_series.reshape(1, -1))

    return {
        "Chance of Admit": float(prediction[0])
        }