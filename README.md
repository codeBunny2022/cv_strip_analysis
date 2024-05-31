# CV Strip Analysis Web Application

## Overview

This project is a web application developed using Flask. It allows users to upload an image of some color strips which are then analyzed to extract and return the RGB values of the colors on the strips. The application uses the OpenCV library to perform image processing and analysis.

## Structure

The project is composed of two main python scripts:

- **strip_analyzer.py**: This script contains the function that handles the reading in of the image and color boundary analysis using OpenCV.

- **webnode.py**: This is the main application script. This script uses Flask to handle file uploads, calls the functions from `strip_analyzer.py` to analyze color boundaries and returns the results.

Here's what each file does:

**strip_analyzer.py**
- `read_image()`: This function reads an image file into a numpy array.
- `get_rgb_values()`: This function is responsible for extracting the color boundaries in a given image.
- `transform_to_json()`: This function transforms the color boundaries into a JSON format that is easier to work with and understand.

**webnode.py**
- Flask app configuration: The application is configured to accept certain file extensions and sets up an upload path for saving uploaded images.
- Route handling: A POST route is set up to handle incoming requests that include the image to be analyzed.
- Handling POST requests: The application receives the POST request that includes the user's name, email, and image file. It reads in the image, analyzes it and writes the results into a text file. The text file is then made available for download.

## Usage

To use the web application, the user makes a POST request containing their name, email, and the image file of color strips. The application then returns a text file that contains the RGB values of color on the strips.

## Dependencies
This project requires the following Python libraries: Flask, Werkzeug, and opencv-python-headless. These can be installed by using the `requirements.txt` file included with the project.

```bash
pip install -r requirements.txt