#using subprocess library for checking and installing
import importlib
import subprocess
import time
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt

def install_package(package):
    subprocess.check_call(["python", '-m', 'pip', 'install', package])

def check_and_install(package):
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"{package} is not installed. Installing...")
        install_package(package)

try:
    check_and_install('qrcode')
    check_and_install('cv2')
except subprocess.CalledProcessError:
    print(f"Error: Could not install {package}.")
import qrcode
import cv2

class QRCodeGenerator:
    def generate(self, text, filename):
        if not filename.endswith('.png'):
            filename += '.png'
        qr = qrcode.make(text)
        qr.save(filename)
        print(f"QR Code generated and saved as {filename}")

class QRCodeDecoder:
    def decode(self, image_path):
        # Loading the image
        image_path = rf"{image_path}"
        image = cv2.imread(image_path)

    # Check if image was successfully loaded
        if image is None:
            print(f"Error: Unable to load image from {image_path}")
            return
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.axis('off')  # Turn off axis numbers and ticks
        plt.show()


    # Decode QR code
        qr_codes = decode(image)

    # Loop over all detected QR codes
        for qr_code in qr_codes:
        # Extract the QR code's data (in bytes)
            qr_data_bytes = qr_code.data

        # Convert the data bytes to a string
            qr_data_str = qr_data_bytes.decode('utf-8')

        # Print the QR code's data
        print(f"QR Code Data: {qr_data_str}")

if __name__ == '__main__':
    generator = QRCodeGenerator()
    decoder = QRCodeDecoder()
    while True:
        print("\nMenu:")
        print("1. Encode text into QR code")
        print("2. Decode QR code from image")
        print("3. Encode and Decode")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            # Encode text into QR code
            text = input("Enter text to generate QR code: ")
            filename = input("Enter filename to save the QR code (without extension): ")
            generator.generate(text, filename)

        elif choice == '2':
            # Decode QR code from image
            image_path = input("Enter the path to the image containing QR code: ")
            decoder.decode(image_path)

        elif choice == '3':
            # Encode and Decode
            text = input("Enter text to generate QR code: ")
            filename = input("Enter filename to save the QR code (without extension): ")
            generator.generate(text, filename)
            
            image_path = input("Enter the path to the image containing QR code: ")
            decoder.decode(image_path)

        elif choice == '4':
            # Exit
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
