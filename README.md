# Image Comparator

A web service that compares two images and identifies the differences between them. The service highlights the areas where the images differ and provides a percentage of difference.

## Features

- Upload and compare two images
- Visual preview of uploaded images
- Highlights differences in red
- Calculates percentage difference
- Responsive web interface
- Handles images of different sizes

## Installation

### Quick Setup (Windows)
1. Clone the repository:
```bash
git clone https://github.com/yourusername/image_comparator.git
cd image_comparator
```

2. Run the setup script:
```bash
setup.bat
```
This will:
- Create a virtual environment
- Activate the virtual environment
- Install all dependencies
- Set up the project in development mode

### Manual Setup
If you prefer to set up manually or are using a different operating system:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/image_comparator.git
cd image_comparator
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Use the web interface to:
   - Upload two images using the file input fields
   - Click "Compare Images"
   - View the comparison results, including:
     - Highlighted differences in red
     - Percentage difference between the images

## Technical Details

The image comparison is performed using:
- OpenCV for image processing
- Flask for the web server
- NumPy for numerical operations
- Pillow for additional image handling

The comparison process:
1. Images are converted to grayscale
2. Absolute difference is calculated
3. Threshold is applied to identify significant differences
4. Differences are highlighted in red
5. Percentage difference is calculated based on pixel differences

## Requirements

- Python 3.8 or higher
- Dependencies listed in requirements.txt:
  - Flask
  - OpenCV-Python
  - NumPy
  - Pillow

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
