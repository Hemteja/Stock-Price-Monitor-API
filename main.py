from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    display = {"home" : "Development in progress"}
    return display["home"]

@app.get("/login")
def login():
    return "You're too early")
