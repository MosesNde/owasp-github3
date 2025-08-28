 import json
 import cv2
 import torch
 import matplotlib.pyplot as plt
 import matplotlib.patches as patches
 
from fastapi import FastAPI, Depends
 from fastapi.middleware.cors import CORSMiddleware
 from sqlalchemy.ext.asyncio import AsyncSession
 
 )
 
 # Параметры
NUM_CLASSES = cfg.num_classes
 WIDTH = cfg.width_image
 HEIGHT = cfg.height_image
 MODEL_PATH = cfg.model_path
     return final_prediction
 
 
def transform_tensor_to_image(image):
    return T.ToPILImage()(image)
 
 
 # Функция для инференса
 def detect_objects(image_path, model, iou_thresh=0.3):
     # Подготовка изображения
    image = preprocess_image(image_path)
    image = image.unsqueeze(0).to(DEVICE)
 
     # Инференс
     model.eval()
     with torch.no_grad():
        predictions = model(image)[0]
 
     # Применение NMS
     predictions = apply_nms(predictions, iou_thresh)
 
    return transform_tensor_to_image(image), predictions
 
 
 def pixel_to_geo(image_path, box):
     with rasterio.open(image_path) as src:
        # Получаем трансформацию (преобразование пикселей в географические координаты)
         transform = src.transform
        # Преобразуем [xmin, ymin, xmax, ymax] в географические координаты
        xmin, ymin = transform * (box[0], box[1])  # Левый верхний угол
        xmax, ymax = transform * (box[2], box[3])  # Правый нижний угол
        return [xmin, ymin, xmax, ymax]  # [lon_min, lat_min, lon_max, lat_max]
 
 
def create_geometry(geo_coords):
    # geo_coords: [lon_min, lat_min, lon_max, lat_max]
    geom = box(geo_coords[0], geo_coords[1], geo_coords[2], geo_coords[3])
    return geom  # Объект POLYGON в WGS84
 
 
# Инициализация модели
model = get_object_detection_model(NUM_CLASSES + 1)
model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
model.to(DEVICE)
 
 
 @app.post(
     tags=['analysis']
 )
 async def analysis_images(
     analysis_in: AnalysisIn,
     db: AsyncSession = Depends(get_async_session)
 ):
     results = []
     for image_id, image_path in zip(analysis_in.images_ids, analysis_in.images_paths):
         image, prediction = detect_objects(image_path, model)
         for object_type in objects_type:
             await crud.object_type.upsert_object_type(
                 session, ObjectTypeUpsert(**object_type)
            )
\ No newline at end of file
\ No newline at end of file