#this is the library that we're using for the object detection
from imageai.Detection import VideoObjectDetection
import os

#returns a working directory for the actual folder of the file
execution_path = os.getcwd()

#Initialize the detector
detector = VideoObjectDetection()

#this sets the initial object detection model instance to the pre trained "RetinaNet" model. This was downloaded from a whl
detector.setModelTypeAsRetinaNet()

#Set the model path of the model file we downloaded (the resnet model that uses the COCO database)
detector.setModelPath(os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))

#Load the model
detector.loadModel()

# This takes each frame from the video and detects each object inside of the frame
#After doing so, it pareses the images together in to an output video at 20 frames per second. The output file is in AVI
# it takes the input file and stores the output file in the same folder.
path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "waste.mp4"),
                                output_file_path=os.path.join(execution_path, "Detected_Output")
                                , frames_per_second=20, log_progress=False)

#For me to make sure the model
print(path)