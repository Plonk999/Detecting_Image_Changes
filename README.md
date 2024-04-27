
## Overview

The Image Difference Detector is a Python program that detects differences between two grayscale images and generates a new image highlighting those differences. It utilizes the Python Imaging Library (PIL) to perform image processing tasks.

---

## Features

- Compares two grayscale images and identifies areas of difference.
- Generates a new image that highlights the differences between the input images.
- Thresholds the difference image to make the differences more visible.
- Saves the resulting difference image to the specified output path.
- Displays the difference image using the default image viewer.

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your-username/image-difference-detector.git
    ```

2. Install the required dependencies:

    ```
    pip install pillow
    ```

## Usage

1. Place the grayscale images you want to compare in the specified input paths (`image1_path` and `image2_path`).
2. Specify the output path where the difference image will be saved (`output_path`).
3. Run the program:

    ```
    python detect_differences.py
    ```

4. The difference image will be generated and saved to the specified output path.
5. The difference image will also be displayed using the default image viewer.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the (LICENSE) file for details.

---

You can customize this README template to include specific details about your program, such as usage examples, additional features, or contribution guidelines. Make sure to replace placeholders like `your-username` with appropriate values for your project.
