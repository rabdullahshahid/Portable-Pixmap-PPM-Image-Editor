# Portable Pixmap (PPM) Image Editor

This Python program is a Portable Pixmap (PPM) Image Editor designed for basic image manipulation. It allows users to apply various effects to PPM images through a simple and interactive command-line interface. The available effects include converting to greyscale, flipping horizontally, adjusting color negativity, and more.

## Features

- **Convert to Greyscale**: Convert the image to greyscale.
- **Flip Horizontally**: Flip the image horizontally.
- **Negative of Red**: Invert the red channel.
- **Negative of Green**: Invert the green channel.
- **Negative of Blue**: Invert the blue channel.
- **Just the Reds**: Keep only the red channel.
- **Just the Greens**: Keep only the green channel.
- **Just the Blues**: Keep only the blue channel.
- **Flatten Reds**: Remove the red channel.
- **Flatten Greens**: Remove the green channel.
- **Flatten Blues**: Remove the blue channel.
- **Extreme Contrast**: Apply extreme contrast to the image.

## Usage

1. Clone the repository and navigate to the project directory.
2. Run the `main.py` script using Python:
   ```bash
   python main.py
   ```
3. Follow the prompts to enter the input PPM image file and the desired output file.
4. Choose an effect from the list of available options.
5. The processed image will be saved to the specified output file.

## Example

To convert an image to greyscale:

1. Run the script:
   ```bash
   python main.py
   ```
2. Enter the name of the input image file (e.g., `input.ppm`).
3. Enter the name of the output image file (e.g., `output.ppm`).
4. Select the greyscale effect by entering `1`.
5. The processed image will be saved as `output.ppm`.

## Requirements

- Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/Portable-Pixmap-PPM-Image-Editor/ppm-image-editor.git
cd ppm-image-editor
```

Run the script:

```bash
python main.py
```

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open-source .
