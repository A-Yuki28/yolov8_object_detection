from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Define current screenshot as source
source = "screen"

# Run inference on the source
results = model(source,show=True,stream=True)  # list of Results objects