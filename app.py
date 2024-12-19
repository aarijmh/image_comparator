import os
from flask import Flask, request, render_template, jsonify
import cv2
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def compare_images(image1_path, image2_path):
    # Read the images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)
    
    # Ensure images are the same size
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    
    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Calculate difference
    diff = cv2.absdiff(gray1, gray2)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    
    # Calculate percentage difference
    total_pixels = thresh.size
    different_pixels = np.count_nonzero(thresh)
    difference_percentage = (different_pixels / total_pixels) * 100
    
    # Create visualization
    diff_color = img1.copy()
    diff_color[thresh == 255] = [0, 0, 255]  # Mark differences in red
    
    # Convert the difference image to base64 for display
    _, buffer = cv2.imencode('.png', diff_color)
    diff_image_base64 = base64.b64encode(buffer).decode('utf-8')
    
    return diff_image_base64, round(difference_percentage, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({'error': 'Both images are required'}), 400
        
    image1 = request.files['image1']
    image2 = request.files['image2']
    
    # Save uploaded images temporarily
    image1_path = os.path.join(UPLOAD_FOLDER, 'image1.png')
    image2_path = os.path.join(UPLOAD_FOLDER, 'image2.png')
    
    image1.save(image1_path)
    image2.save(image2_path)
    
    try:
        diff_image, difference_percentage = compare_images(image1_path, image2_path)
        return jsonify({
            'difference_image': diff_image,
            'difference_percentage': difference_percentage
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Clean up temporary files
        if os.path.exists(image1_path):
            os.remove(image1_path)
        if os.path.exists(image2_path):
            os.remove(image2_path)

if __name__ == '__main__':
    app.run(debug=True)
