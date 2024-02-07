from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
import uvicorn

app = FastAPI(
    title="Customers Service",
    description="This is the Customers Service for the DineStream application",
    version="0.1.0",
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001, log_level="debug")