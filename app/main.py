from fastapi import FastAPI

app = FastAPI(
    title="Expense Tracker Backend"
)

@app.get("/")
def home():
    return {
        "message": "Backend Running Successfully"
    }