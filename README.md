# Image Processor

This project provides Python scripts for applying various image filters using two different methods: a custom implementation with `matplotlib` and `numpy`, and a version using `OpenCV`. It allows users to apply grayscale, blur, reflection, and edge detection filters to images. 

## Table of Contents

1. [Overview](#overview)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Image Kernels](#image-kernels)
6. [License](#license)

## Overview

The project consists of three main files:

- **filters.py**: Implements custom functions for applying image filters, such as grayscale, reflection, and kernel-based filtering (blurring and edge detection).
- **cv-version.py**: Uses `OpenCV` to apply the same filters in a more efficient manner.
- **image-processor.py**: A custom implementation using `matplotlib` and `numpy` to achieve similar results as `cv-version.py`.

### File Descriptions

- **filters.py**
  - `grayscale`: Converts an image to grayscale.
  - `reflect`: Reflects the image horizontally.
  - `calc_kernel`: Helper function for applying a 3x3 kernel to a pixel.
  - `apply_kernel`: Applies a 3x3 kernel filter to the entire image.

- **cv-version.py**
  - Uses `OpenCV` for efficient filtering.
  - Supports grayscale conversion, reflection, blur, and edge detection.
  
- **image-processor.py**
  - Uses `matplotlib` and `numpy` to implement image filtering.
  - Supports grayscale conversion, reflection, blur, and edge detection.
  
## Technologies Used

The project utilizes the following technologies:

- **Python**: Main programming language for the scripts.
- **OpenCV**: Library for computer vision tasks, used in `cv-version.py`.
- **Matplotlib**: Library for plotting and image display, used in `image-processor.py`.
- **NumPy**: Library for numerical operations, used for image manipulation.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/image-processor.git
   ```
2. Install the required Python packages:
   ```
   pip install numpy matplotlib opencv-python
   ```
   
## Usage

To run the scripts, use the command line with the following syntax:

```
python <script-name> <filter> <image-path>
```

Where:
- `<script-name>` can be either `image-processor.py` or `cv-version.py`.
- `<filter>` is one of the following:
  - `-g`: Grayscale
  - `-r`: Reflect
  - `-b`: Blur
  - `-e`: Edge Detection
- `<image-path>` is the path to the image file (must be `.png` or `.jpg`).

Example:
```
python image-processor.py -g sample.jpg
```

The modified image will be displayed and saved with a filename indicating the applied filter.

## Image Kernels

An image kernel is a matrix used to apply effects such as blurring, sharpening, or edge detection to images. Each element of the kernel specifies how much the neighboring pixels contribute to the final result for each pixel. For more details, refer to this [interactive visualization of image kernels](https://setosa.io/ev/image-kernels/).

### Example Kernels
- **Blur Kernel**:
  ```
  [ 
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9] 
  ]
  ```
  
- **Edge Detection Kernel**:
  ```
  [ 
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1] 
  ]
  ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

```
MIT License

Copyright 2024 Bhavya Patel

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
