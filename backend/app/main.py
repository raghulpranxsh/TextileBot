from fastapi import FastAPI
from tally.connector import get_stock_summary

app = FastAPI()

@app.get("/")
def home():
    return {"message": "TextileBot Backend Running"}

@app.get("/stock")
def stock():
    data = get_stock_summary()
    return {"tally_response": data}
