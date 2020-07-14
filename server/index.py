from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

# from server.api.cv.ClockDetector import clock_detector
# from server.api.samples.Sample import samples

app = FastAPI()

# API Register
# app.register_blueprint(clock_detector, url_prefix='/api')
# app.register_blueprint(samples, url_prefix='/sample-api')
app.mount("/static", StaticFiles(directory="server/build"), name="static")

#
# @app.get("/api/.*", status_code=404, include_in_schema=False)
# def invalid_api():
#     return None


# UI
@app.get("/.*")
@app.get("/{file_path:path}")
async def read_file(file_path: str = "home"):
    return HTMLResponse(open("./build/static/index.html").read())

if __name__ == '__main__':
    uvicorn.run(app)
