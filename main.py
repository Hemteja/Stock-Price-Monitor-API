from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    display = {"home" : "Development in progress"}
    return display["home"]
