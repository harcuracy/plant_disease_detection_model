from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "🚀 FastAPI is working!",
        "status": "success"
    }

@app.get("/health")
def health():
    return {"status": "OK"}