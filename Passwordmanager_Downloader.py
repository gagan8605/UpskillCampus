from pytube import YouTube
import json
from datetime import date
from datetime import datetime
import sys
import time
while(True):
    ip=input("Press 1 if you have URL or Press 2 if you have video ID or Press 3 if you have pasted Debug Info in ToRead.txt file : ")
    if(ip=="1"):
        url=input("Please Enter Video URL : ")
        myVideo=YouTube(url)
        surl=url
        break
    elif(ip=="2"):
        videoid=input("Please Enter Video ID : ")
        myVideo=YouTube("www.youtube.com/watch?v="+videoid)
        surl="www.youtube.com/watch?v="+videoid
        break
    elif(ip=="3"):
        text_file =open("To Read.txt","r")
        word='"addebug_videoId":'
        s=" "
        count=1
        
        while(s):
            s=text_file.readline()
            L=s.split()
            ##print("reading")
            if word in L:
                ##print("Line Number : ",count," : ",s)
                vid=s
                break
            count+=1                
        ##print("End")
        ##print(vid)
        try:
            evid=vid.split(":")
        except:
            print("Data in 'To Read.txt' File in incorrect")
            time.sleep(5)
            sys.exit()
        ##print(len(evid))
        videoid=evid[1].replace(",","")
        videoid=videoid.replace(" ","")
        videoid=videoid.replace('"',"")
        ##print("replace")
        print(videoid)
        myVideo=YouTube("www.youtube.com/watch?v="+videoid)
        ##print("here here Here")
        surl="www.youtube.com/watch?v="+videoid
        ##time.sleep(5)
        text_file.close()
        break       
    else:
        print("\nEnter valid option\n")

##myVideo=YouTube(url)


##Title
print("\n")
print("**********Title**********")
print("Video Title : "+myVideo.title)
title=myVideo.title
##Thumbnail Image
print("\n")
print("**********Thumbnail Image**********")
print("Thumbnail Image : "+myVideo.thumbnail_url)
thum=myVideo.thumbnail_url
##Download Video
print("\n")
print("**********Download Video**********")
print("**********Wait until download is finished**********")

myVideo.streams.get_highest_resolution().download()
print("**********Video Downloaded**********")



##############################################################
##Adding to JSON File
print("**********Updating Json File Data**********")


def write_json(data , filename="Json File.json"):
     with open(filename,"w") as f :
          ##print("in write json")
          json.dump(data, f, indent=4)
with open ("Json File.json") as json_file:
     data=json.load(json_file)
     ##print("load")
     temp=data["YouTube"]
     adt=datetime.now()
     fdt=adt.strftime("%m/%d/%Y, %H:%M:%S")
     ##title="mewaacc"
     ##thumqq="newaacc"
     ##qqsurl="erwaacc"
     y={"AD Name":title,"Thumbnail":thum,"Source URL":surl,"Date":fdt}
     temp.append(y)
write_json(data)          



##Cleaning File
print("\nCleaning 'To Read.txt' File\n")
text_file=open("To Read.txt","w")
text_file.write("")
text_file.close()




time.sleep(3)
























