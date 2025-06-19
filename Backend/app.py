from fastapi import FastAPI, UploadFile, File 
from routes import predict
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import numpy as np
from PIL import Image 
import io

app = FastAPI()
app.include_router(predict.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


model = None

@app.get("/")
def read_root():
    return{"status": "Backend is running"}

class PredictionRequest(BaseModel):
    input: list

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    contents =await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    image = image.resize((224, 224))
    array = np.array(image) / 255.0
    array = array.reshape(1, 224, 224, 3)


    prediction = [0.2, 0.8]

    return {"prediction": prediction}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



