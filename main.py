import datetime
import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    result = {
        "project": "api",
        "version": "0.0.1",
        "time": datetime.datetime.now().strftime("%H:%M:%S")
    }
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
