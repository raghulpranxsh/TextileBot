from fastapi import FastAPI, Depends, HTTPException, Header
from apscheduler.schedulers.background import BackgroundScheduler
from contextlib import asynccontextmanager
from tally.connector import get_stock_summary, get_outstanding, get_invoices, get_purchase_orders, get_ledger_balances
import datetime

# Hardcoded clients for demonstration (This would be in DB)
VALID_CLIENTS = {
    "client_raghul_123": {"name": "Rahul Textiles", "plan": "pro"},
    "client_demo_456": {"name": "Demo Company", "plan": "free"}
}

def verify_client(x_client_token: str = Header(...)):
    if x_client_token not in VALID_CLIENTS:
        raise HTTPException(status_code=401, detail="Invalid Client Token")
    return VALID_CLIENTS[x_client_token]

# Background Sync Task
def sync_tally_data():
    print(f"[{datetime.datetime.now()}] Running background sync for all active clients...")
    # In a real app, you would loop through clients, fetch from Tally, and write to PostgreSQL
    # Example: data = get_stock_summary() -> save_to_db(data)
    print("Sync complete.")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Start the background scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(sync_tally_data, 'interval', minutes=10) # Run every 10 mins
    scheduler.start()
    yield
    # Shutdown
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home(client: dict = Depends(verify_client)):
    return {"message": f"TextileBot Backend Running for {client['name']}"}

@app.get("/stock")
def stock(client: dict = Depends(verify_client)):
    data = get_stock_summary()
    return {"client": client['name'], "tally_response": data}

@app.get("/outstanding")
def outstanding(client: dict = Depends(verify_client)):
    data = get_outstanding()
    return {"client": client['name'], "tally_response": data}

@app.get("/invoices")
def invoices(client: dict = Depends(verify_client)):
    data = get_invoices()
    return {"client": client['name'], "tally_response": data}

@app.get("/purchase-orders")
def purchase_orders(client: dict = Depends(verify_client)):
    data = get_purchase_orders()
    return {"client": client['name'], "tally_response": data}

@app.get("/ledgers")
def ledgers(client: dict = Depends(verify_client)):
    data = get_ledger_balances()
    return {"client": client['name'], "tally_response": data}
