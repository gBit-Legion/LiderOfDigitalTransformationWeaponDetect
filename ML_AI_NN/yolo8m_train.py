from ultralytics import YOLO

model = YOLO('yolov8m.pt') 
results = model.train(data='config.yaml', 
                      epochs=100, 
                      batch=4, 
                      imgsz=1024, 
                      device=0, 
                      name="yolo8m_V0", 
                      optimizer='Adam', 
                      amp=False, 
                      dropout=0.3,
                      lr0=0.001,
                      lrf=1e-12,
                      augment=True,
                      save_period=2,
                      workers=1)
