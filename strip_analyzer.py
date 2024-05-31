import cv2
import json

def read_image(file_path):
    # Read the image
    image = cv2.imread(file_path)
    # Convert BGR image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def get_rgb_values(image, x_values, y_value):
    rgb_values = {}
    # Loop through given x_values
    for x in x_values:
        # Get RGB values and convert them to regular integers
        r, g, b = [int(val) for val in image[y_value][x]]
        # Append RGB values to the list
        rgb_values[f"pixel_{x}_{y_value}"] = {"r": r, "g": g, "b": b}
    return rgb_values

def transform_to_json(data):
    # Convert dict to JSON
    return json.dumps(data, indent=4)
        
# Define the x coordinates of the color strips on the image
# Here, you need to replace with your real x and y
x_values = [i * 10 for i in range(10)]  
y_value = 0 

# Read image
image = read_image('strips/image1.jpg')

# Get RGB values
rgb_values = get_rgb_values(image, x_values, y_value)

# Convert to JSON
rgb_values_json = transform_to_json(rgb_values)

print(rgb_values_json)
