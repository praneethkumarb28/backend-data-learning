from fastapi import FastAPI

app=FastAPI(title="Backend & Data Learning API")

@app.get("/")
def health_check():
    return {"status":"Backend service is running"}