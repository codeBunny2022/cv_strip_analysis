from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from strip_analyzer import get_rgb_values as color_boundaries, read_image, transform_to_json as to_json
import os
import json

# Create the application.
app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.jpeg']
app.config['UPLOAD_PATH'] = 'uploads'

# Create the uploads directory if it doesn't exist.
if not os.path.exists(app.config['UPLOAD_PATH']):
    os.makedirs(app.config['UPLOAD_PATH'])

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        # Get user input
        name = request.form['name']
        email = request.form['email']

        # Get uploaded file
        uploaded_file = request.files['image']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            image_path = os.path.join(app.config['UPLOAD_PATH'], filename)
            uploaded_file.save(image_path)

            # Perform image processing
            image = read_image(image_path)
            
            # Define the x coordinates of the color strips on the image
            x_values = [i * 10 for i in range(10)]  # replace with your real x coordinates
            y_value = 0  # replace with your real y coordinate 
            
            boundaries = color_boundaries(image, x_values, y_value)
            
            # Save to a text file
            with open('boundaries.txt', 'w') as f:
                f.write(json.dumps(boundaries, indent=4))
        
            return send_file('boundaries.txt', as_attachment=True)
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)