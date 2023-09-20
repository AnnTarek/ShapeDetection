# ShapeDetection
This project develops a shape detection model using YOLO (v8) ,deep learning framework. YOLOv8 is the latest version of YOLO by Ultralytics. As a cutting-edge, state-of-the-art (SOTA) model, YOLOv8 builds on the success of previous versions, introducing new features and improvements for enhanced performance, flexibility, and efficiency. 
# Data Collection 
I’ve collected the data from roboflow; seperated as 1319 images as a training set, 355 valid set, and 163 test set.It's annotated and includes 9 classes which are triangle, red_cube, yellow_cube, green_cube, blue_cube, rectangle, circle, ball, and Cube_silicone. The data was suitable for figures that will be in the SUAS competition. Download the dataset as zipped file for the YOLO v8. After downloading, the yaml file will be used in the code.
Here’s the link for the dataset:
https://universe.roboflow.com/w0/3d-geom-shape-detector/browse?queryText=class%3Ayellow_cube&pageSize=50&startingIndex=0&browseQuery=true

# Training
The model was trained using ultralytics library. Ultralytics YOLOv8 is the latest version of the acclaimed real-time object detection and image segmentation model.. Download the package and import it to use it in the main.py.
Here is the documentation link:
https://docs.ultralytics.com

# Inference code:
Utalytics have predict() accepts multiple arguments that can be passed at inference time to override defaults. You must give the path of the image to the function as an argument. I also used the imgsz, write the size of the image you chose. The conf argument (object confidence threshold for detection)was set to 0.8. I also changed the save argument to True so i can see the image in the runs file created by ultratyics (It will be created automatically once the code is done execution and found in the folder of the project).
# Result
After the execution of the program, you will find the runs folder created in the project. It includes the predict folder and the training folder. The training folder will include all the histograms and details associated with the dataset.
