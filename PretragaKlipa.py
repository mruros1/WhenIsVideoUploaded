from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import traceback
import sys


#video for search
videotosearch = ""
list0 = sys.argv[2:]
for i in range(len(list0)):
    videotosearch+=str(list0[i])+" "
videotosearch = videotosearch[0:-1]

# browser and page tab setup
driver = webdriver.Firefox()
#channelID
channelID = sys.argv[1]
driver.get("https://www.youtube.com/channel/"+str(channelID)+"/videos")

#xpath //a[@id='video-title' and contains(@class,'yt-simple-end')]

#loop for being sure page works
while(True):
    try:
        strr = driver.find_element_by_xpath("//ytd-searchbox[@id='search']")
        print("page works.")
        break
    except:
        print("error.")
        continue
names = []

while(True):
    try:
        videos = driver.find_elements_by_xpath("//a[@id='video-title' and contains(@class,'yt-simple-end')]")
        for i in range(len(videos)):
            #adding to all videos
            if videos[i].text not in names:
                names.append(str(videos[i].text))
        #searching for videos
        if videotosearch in names:
            print("video found!")
            break
        elif videotosearch not in names:
            #scroll if it isn't here
            driver.execute_script("window.scrollBy(0,100000)")

    except Exception as e:
        print(traceback.format_exc())
        continue
