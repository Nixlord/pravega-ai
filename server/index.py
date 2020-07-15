from fastapi import FastAPI
import uvicorn

app = FastAPI()


# API Register
@app.get("/")
async def homepage():
    return {
        "name": "shibasis"
    }

if __name__ == '__main__':
    uvicorn.run(app)
