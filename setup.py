from setuptools import setup, find_packages

setup(
    name="image_comparator",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask==3.0.0',
        'opencv-python==4.8.1.78',
        'numpy==1.26.2',
        'Pillow==10.1.0',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A web service to compare two images and identify differences",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords="image comparison, opencv, flask, web service",
    url="https://github.com/yourusername/image_comparator",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
)
