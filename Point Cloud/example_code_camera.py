import Camera
import numpy as np
import cv2

image = np.zeros((1024,1024,3)) # replace
depth_map = np.zeros((1024,1024)) # replace

cam = Camera.Camera(image_size=(1024,1024),focal_length=(1024,1024),img_center=(512,512),rotation=np.eye(3),translation=np.zeros(3)) #change these values
cam.add_image(image,depth_map)
cam.point_cloud()

# Display PCD
cam.visualize()