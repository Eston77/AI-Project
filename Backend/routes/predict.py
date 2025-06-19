from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from pathlib import Path
import uuid
import shutil

router = APIRouter

@router.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    try:
        extension = file.filename.split(".")[-1]
        filename = f"{uuid.uuid4()}.{extension}"
        save_path = Path("static") / filename

        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        prediction = {
            "class": "T-shirt",
            "confidence": 0.87,
            "image_url": f"/static/{filename}"
        }

        return JSONResponse(content={"prediction": prediction})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)