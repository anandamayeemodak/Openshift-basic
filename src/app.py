from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/")
async def baseRoute():
    print("Request to baseRoute(home)")
    id = random.randint(1,100)
    return "Base Request ID: {}".format(str(id))

if __name__=="__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
