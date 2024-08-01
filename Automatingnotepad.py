import subprocess
import importlib
def install_package(package):
    subprocess.check_call(["python", '-m', 'pip', 'install', package])


def check_and_install(package):
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"{package} is not installed. Installing...")
        install_package(package)


try:
    check_and_install('pyautogui')
    check_and_install('easyocr')
    check_and_install('time')
except subprocess.CalledProcessError:
    print(f"Error: Could not install {package}.")
import pyautogui
import easyocr
from PIL import ImageGrab
import time

#description about libraries
'''
using pyautogui for opening notepad and writting the command
using easyocr for extracting the text from image
using Imagegrab for taking the screenshot
using time for sleep
using subprocess to run the sample5.bat externally
using file handling for saving the sample5.bat file
used exception handling for checking the libraries
used generators for printing final statement
'''
class notepadautomation:
    
    def open_notepad(self):
        time.sleep(2)
        pyautogui.press('win')
        pyautogui.write('notepad', interval=2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write('query session', interval=0.1)
        pyautogui.press('enter')

    def screenshot_and_extract_text_from_screenshot(self):
        reader = easyocr.Reader(['en'])
        screenshots = pyautogui.screenshot()
        screenshots.save('picture.png')
        output = reader.readtext('picture.png')
        return output
    def saving_notepad(self):
        extracted_text = self.screenshot_and_extract_text_from_screenshot()
        for text in extracted_text:
            if text[1] == 'File':
                pyautogui.click(text[0][0])
                time.sleep(2)
                break
        saving_output = self.screenshot_and_extract_text_from_screenshot()
        for text in saving_output:
            if text[1] == 'Save':
                pyautogui.doubleClick(text[0][0])
                time.sleep(1)
                pyautogui.write('sample8.bat', interval=0.2)
                break
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('alt', 'f4')
    def printingfinalstatement(self):
        q='successfully output is printed'
        yield q
    def execute(self):
        try:
            save_directory = input("enter the path for storing screenshot and also for saving bat file named sample5.bat")
            formatting_directory=rf"{save_directory}"
            self.open_notepad()
            time.sleep(1)
            self.saving_notepad()
            file_path=f"{formatting_directory}/sample8.bat"
            output=subprocess.run([file_path],capture_output=True,text=True)
            print("output:")
            print(output.stdout)
        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    automation = notepadautomation()
    automation.execute()
    r=automation.printingfinalstatement()
    print(r.__next__())

