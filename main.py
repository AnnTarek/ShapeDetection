from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model

# Train the model with 1 GPU
results = model.train(data='data.yaml', epochs=30, imgsz=225, device=0)
pre = model.predict('triangle.jpeg', save=True, show=True, conf=0.8) #predict an image
print(pre)
