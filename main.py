import time
from datetime import date
import urllib.request
import jsonimport RPi.GPIO as GPIO

# https://www.hackster.io/Tisko/rgb-led-change-color-through-python-7fa1c7 for schematic

red_pin = 18
green_pin = 23
blue_pin = 24
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.output(red_pin, False)
GPIO.output(green_pin, False)
GPIO.output(blue_pin, False)

url = "https://lichess.org/api/user/RogerWest"
response = urllib.request.urlopen(url)
encoding = response.info().get_content_charset('utf8')
data = json.loads(response.read().decode(encoding))

intial_rating = 1107 # from June 29

cr = data['perfs']['blitz']['rating'] # current rating
cprog = data['perfs']['blitz']['prog'] # current progression
rating_d = 0 #rating from cell

d = date.today().day
m = date.today().month
yr = date.today().year


d0 = date(2020,6,29)
d1 = date(yr,m,d)
delta = d1 - d0

calcd = delta.days #calc days in between
rperd = 16 #r ating per day
crperd = rperd * calcd # current increase
rating_goal = intial_rating + crperd # rating goal for the day
tmr_goal = rating_goal + rperd #tmrs goal for the day

print('CURRENT STREAK: ',calcd)
print("CURRENT RATING: ",cr)
print("CURRENT PROGRESSION: ",cprog)
print('CURRENT RATING GOAL: ', rating_goal)
print('TMR RATING GOAL: ', tmr_goal)

while True:
    if cr != rating_d or cr > rating_d: #if rating is meet turn light red on rpi
        print("all good fam...chill vibes")
        GPIO.output(green_pin, True)
    else:
        time.sleep(10)
        print("BEN FINEGOLD IS COMING FOR YOU!")
        GPIO.output(red_pin, True)
        
