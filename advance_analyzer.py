import cv2
import json
import numpy as np

def read_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def color_boundaries(image):
    # Initialize the color boundaries dictionary with the first pixel RGB value and position
    boundaries = [{"start_pos": 0, "color": [int(val) for val in image[0][0]]}]

    last_color = image[0][0]
    
    # Loop through the x values (skipping the first one already examined)
    for x in range(1, image.shape[1]):
        current_color = image[0][x]
        
        # If the color changes significantly, update boundaries
        if np.sum(cv2.absdiff(last_color, current_color)) > 0.1:
            boundaries[-1]["end_pos"] = x-1
            boundaries.append({"start_pos": x, "color": [int(val) for val in current_color]})
            last_color = current_color
    
    # For the last color region, set the end_pos as the last x-coordinate
    boundaries[-1]["end_pos"] = x      
    return boundaries

def to_json(data):
    return json.dumps(data, indent=4)

image = read_image('strips/image1.jpg')
boundaries = color_boundaries(image)
boundaries_json = to_json(boundaries)

print(boundaries_json)
