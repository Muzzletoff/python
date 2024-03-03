import pytesseract
from PIL import Image

# path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def convert():
    # Ask the user for the image file path
    image_path = input("Enter the path to the image: ")

    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        print("Extracted Text:")
        print(text)
    except Exception as e:
        print("Error:", e)

convert()
