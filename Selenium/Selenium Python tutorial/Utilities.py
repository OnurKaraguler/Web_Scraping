import time
from PIL import Image as I
import logging as L

def screenshot(d):
    '''Take the screenshot with the current date and time'''
    folder = "C:\\Python_Examples\\Web_Scraping\\Selenium\\Selenium Python tutorial\\screenshots\\"
    time_string = time.asctime().replace(":"," ")
    file_name = folder + time_string + ".png"
    d.save_screenshot(file_name)
    # modify_screenshot(file_name)

def modify_screenshot(f):
    picture = I.open(f)
    picture = picture.resize((1280,654))
    picture = picture.transpose(I.ROTATE_90)
    picture = picture.convert("RGB")
    f_new = f.replace ("png","jpg")
    picture.save(f_new)

def log(level, message, file):
    L.basicConfig(level=L.INFO, filename=file, filemode="a",
                  format="%(asctime)-12s %(levelname)s %(message)s",
                  datefmt="%d-%m-%Y %H:%M:%S")
    if level == "INFO":L.info(message)
    if level == "WARNING":L.warning(message)
    if level == "ERROR":L.error(message)
    if level == "CRITICAL":L.critical(message)