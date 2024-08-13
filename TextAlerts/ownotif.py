import pyautogui
from PIL import Image
from time import sleep
import smtplib
from email.mime.text import MIMEText

carriers = {
	'att': '@mms.att.net',
	'tmobile':'@tmomail.net',
	'verizon': '@vtext.com',
	'sprint': '@page.nextel.com'
}

email = "@gmail.com"
passw = "gmai lapp pass word"
phonenum = '1234567890@vtext.com'

# Pixel coordinates and target color
minimzed_x = 1845
minimzed_y = 1405
minimized_hex = "B3601F"
fullscreen_x = 90
fullscreen_y = 760
fullscreen_hex = "1E253A"

tolerance = 30

# Function to send an email
def send_email():
    global email, passw, phonenum
    text = MIMEText("Game found!")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, passw)
    server.sendmail(email, phonenum, text.as_string())
    server.quit()

# Function to check if a color is within an acceptable range of the target color
def is_color_similar(actual, target):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(actual, target))

# Function to monitor a pixel for a range of similar colors
def monitor_pixel():
    minimzed_target = tuple(int(minimized_hex[i:i+2], 16) for i in (0, 2, 4))
    fullscreen_target = tuple(int(fullscreen_hex[i:i+2], 16) for i in (0, 2, 4))
    while True:
        minimzed_ss = pyautogui.screenshot(region=(minimzed_x, minimzed_y, 1, 1))
        rgb_im = minimzed_ss.convert('RGB')
        minimized_pixel = rgb_im.getpixel((0, 0))
        if is_color_similar(minimized_pixel, minimzed_target):
            send_email()
            break
        sleep(0.1)
        fullscreen_ss = pyautogui.screenshot(region=(fullscreen_x, fullscreen_y, 1, 1))
        rgb_im = fullscreen_ss.convert('RGB')
        fullscreen_pixel = rgb_im.getpixel((0, 0))
        if is_color_similar(fullscreen_pixel, fullscreen_target):
            send_email()
            break
        sleep(0.1)

# Start monitoring the pixel
monitor_pixel()
