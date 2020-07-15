from fastapi import FastAPI
import uvicorn

app = FastAPI()

#  check if websockets can do filehandling
# i have remmoved apt buildpack will need to be restored before running open cv
# API Register
@app.get("/")
async def homepage():
    return {
        "name": "shibasis"
    }

if __name__ == '__main__':
    uvicorn.run(app)
