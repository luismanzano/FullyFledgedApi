from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "HI!! THIS IS MY FIRST API WITH FASTAPI"}

@app.get("/posts")
async def root():
    return {"post": "Congratulations on your first Post!!"}

@app.post("/createpost")
async def root():
    return {"data": "Post Succesfully Created"}
# TESTING THAT MY DYNAMIC SSH IS WORKING