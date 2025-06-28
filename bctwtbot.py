import tweepy
import os
import datetime
import cv2
import pytesseract
import webbrowser
import time
import pyautogui

#download issues : Image movees page up : need to click clear on images RIGHT BEFORE CODE INPUT
#pytesseract initialisation
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


#keys for api
api_key = os.environ['apikey']
api_key_s = os.environ['apikeysecret']
access_token = os.environ['accesstoken']
access_token_s = os.environ['accesstokensecret']
bearer_token = os.environ['bearertoken']

#start and end time for the script (must also edit shutdown script)
start_time = '00:00'
end_time = '06:00'


#start_time = '09:40'
#end_time = '10:00'

#directory where images are saved - to be added to a cleared simultaneously
directory = 'images'


def api_query():
    #API intialisiation : sets tokens and such
    auth = tweepy.OAuth1UserHandler(
    api_key,api_key_s, access_token, access_token_s)
    api = tweepy.API(auth)
    client = tweepy.Client(bearer_token=bearer_token,
                           consumer_key=api_key,
                           consumer_secret=api_key_s,
                           access_token=access_token,
                           )
    # parameter initialisation : sets parameters ; name of acc, how many tweets etc.
    id = 1211632574587498496
    tweetCount = 15
    name = 'TWITTER ACCOUNT NAME'
    query = f'from:{name}'
    #gets actual tweets
    tweets = client.search_recent_tweets(query=query,max_results=tweetCount,tweet_fields=['author_id', 'created_at'])
    tdata = tweets.data
    #function that adds each tweet to bctwts.txt
    with open('bctwts.txt','r') as f:
        content = f.read().split('\n')
        counter = 0
        for line in content:
            if line == tdata[counter]:
                pass
            else:
                content[counter] = str(tdata[counter])
            counter +=1
        with open('bctwts.txt','w') as f:
            joincontent = '\n'.join(content)
            f.write(joincontent)
            f.close()
    print("Tweets retrieved...")

# clears specified folder (directory) of every file inside that directory
def clear_folder():
    for file in os.listdir(directory):
        file = os.path.join(directory,file)
        os.remove(file)
    print('Folder Cleared...')

#MACRO - saves the image - opens the url every interval - saves image etc.
# BCTWTS will not be emptied - replacement file always
# does not need emptying - rewrites over existing content
def save_image():
    clear_folder()
    with open('bctwts.txt') as f:
        for tweet in f:
            tweet = tweet.strip()
            if len(tweet) == 23:
                webbrowser.open(tweet)
                time.sleep(10)
                pyautogui.click(845,472,button='right')
                time.sleep(2)
                pyautogui.click(927,731,button='left')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.click(1895, 994, button='Left')
                pyautogui.hotkey('ctrl','w')
                time.sleep(2)
    print("Images Saved...")


#save_image()

#converts the image into code - pytesseract + cv2 stuff - returns the END VALUE (built exclusively for the codes)
# Will always return the LAST value in the image - ALWAYS RETURN WHAT IT EXPECTS TO BE THE CODE
# If no words are detected, does not return
def img_to_code(img):
    cvimg = cv2.imread(img)
    text = pytesseract.image_to_string(cvimg)
    if text:
        code = text.split()[-1]
        return code
    else:
        #list is empty ; cannot read the image
        pass

#The macro - theoretically given a code that it uses - opens the browser

def input_code(code):
    print(f"INPUT CODE EXECUTED FOR {code}")
    url = 'https://INPUT YOUR URL HERE/'
    webbrowser.open(url)
    #loading time - change based on average time (given no interuptions)
    time.sleep(10)
    pyautogui.click(1805, 486, button='left')
    time.sleep(1)
    pyautogui.press('pagedown')
    time.sleep(1)
    pyautogui.press('pageup')
    time.sleep(1)
    pyautogui.press('pageup')
    time.sleep(1)
    pyautogui.click(1209,554, button='left')
    time.sleep(1)
    pyautogui.click(923, 645, button='left')
    time.sleep(1)
    pyautogui.write(code)
    time.sleep(1)
    pyautogui.click(955, 717, button='left')
    time.sleep(1)
    pyautogui.hotkey('ctrl','w')
    print(f"Code Input : {code}")
    with open('logs.txt', 'a') as f:
        f.write(f"Code Input : {code}\n")
    f.close()





# Gets all the images in the specified directory (images) and converts them into codes
#for each new code added to the text file - calls on input code
# for every image, adds the last text (code) to the file codes.txt
# if code already in codes, doesn't add
# if not in codes, adds and calls on input code
def dir_to_code():
    codelist = []
    codesappend = []
    for file in os.listdir(directory):
        code = img_to_code(os.path.join(directory,file))
        if code:
            codelist.append(code)
    with open('codes.txt','r') as f:
        existingcodes = []
        for line in f:
            line = line.strip()
            if line not in existingcodes:
                existingcodes.append(line)

        for code in codelist:
            if code in existingcodes:
                pass
            else:
                #FUNCTION MACRO
                codesappend.append(code)
                existingcodes.append(code)
        f.close()
    for code in codesappend:
        with open('codes.txt', 'a') as f:
            joincode = code + '\n'
            f.write(joincode)
            f.close()
            #macro for website - inputs the actual codes into the site
            # Internal to save time (otherwise need to return list to main, iterate in main)
            input_code(code)
        print("Codes retrieved...")




#time script - gets the current time now
def get_time():
    timenow = datetime.datetime.now()
    date_time = timenow.strftime("%H:%M")
    return date_time

date_time = get_time()

#main - runs everything - function to be called multiple times throughout the night
# get time of main to run - base the sleep time off that

def main():
    date_time = get_time()
    print(f"Start time for main : {date_time}")
    api_query()
    save_image()
    time.sleep(1)
    pyautogui.click(1861, 45, button='left')
    time.sleep(1)
    dir_to_code()
    end_time = get_time()
    print(f"End time for main : {end_time}")

#script that runs on timer - change time of runnign - might also need to change start time
# starts at specified start time - runs until the first digits of the current time is equal
# to the first digits of the end time (e.g. 5:01am and 5:00 am - the script will stop even though it has passed its run time.)
def timed_script():
    stop = 0
    while stop != 1:
        date_time = get_time()
        if date_time == start_time:
            while int(date_time.split(':')[0]) != int(end_time.split(':')[0]):
                print("WHILE LOOP")
                date_time = get_time()
                main()
                print("Sleeping for 5 minutes...")
                date_time = get_time()

                time.sleep(300)
            stop = 1
    else:
        pass
    exit()

timed_script()