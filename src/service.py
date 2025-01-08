import numpy as np
import bentoml
from bentoml.io import NumpyNdarray, JSON
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import jwt
from fastapi import FastAPI
import time
from datetime import datetime, timedelta, timezone

# Secret key and algorithm for JWT authentication
JWT_SECRET_KEY = "S3CR3TJWTK3Y"
JWT_ALGORITHM = "HS256"

# User credentials for authentication
USERS = {
    "admin": "psw",
    "bentoml": "bentoml"
}

# Pydantic model to validate input data
class InputModel(BaseModel):
    GRE_Score: int
    TOEFL_Score: int
    University_Rating: int
    SOP: float
    LOR: float
    CGPA: float
    Research: int

class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Secure only the predict endpoint
        if request.url.path == "/predict":
            token = request.headers.get("Authorization")
            if not token:
                return JSONResponse(status_code=401, content={"detail": "Missing authentication token"})
            try:
                token = token.split()[1]  # Remove 'Bearer ' prefix
                payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            except jwt.ExpiredSignatureError:
                return JSONResponse(status_code=401, content={"detail": "Token has expired"})
            except jwt.InvalidTokenError:
                return JSONResponse(status_code=401, content={"detail": "Invalid token"})
            
            request.state.user = payload.get("sub")

        response = await call_next(request)
        return response

# Function to create a JWT token
def create_jwt_token(user_id: str):
    expiration = datetime.utcnow() + timedelta(hours=4)
    payload = {
        "sub": user_id,
        "exp": int(expiration.timestamp()) # Convert datetime to Unix timestamp
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token

# Get the model from the Model Store
model_runner = bentoml.sklearn.get("admissions_model:latest").to_runner()

# Create a service API
service = bentoml.Service("service", runners=[model_runner])

# Add the JWTAuthMiddleware to the service
service.add_asgi_middleware(JWTAuthMiddleware)

# Login endpoint to get JWT token
@service.api(input=JSON(), output=JSON(), route='/login')
def login(credentials: dict) -> dict:
    username = credentials.get("username")
    password = credentials.get("password")

    if username in USERS and USERS[username] == password:
        token = create_jwt_token(username)
        return {"token": token}
    else:
        return JSONResponse(status_code=401, content={"detail": "Invalid credentials"})

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