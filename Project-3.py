#!/usr/bin/env python
from html.parser import HTMLParser
import requests
import urllib.request
import re
from requests import get

def download(url, file_name):
# open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

    return()

def main():  


    #Download file
    #download("https://s3.amazonaws.com/tcmg476/http_access_log", "logfile")
    #req = requests.get("https://s3.amazonaws.com/tcmg476/http_access_log")
    #print(req.text)
    # print(str(req.text))
    #print(req.status_code)
    #print(req.text)

    #response = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
    #print(response.data)
    #print(response.read())
    #data = response.read()
    #print(data)

    #Open file
    #Parse file
    with urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log") as response:

        html = str(response.read())
        #print(html)
    
    html = html.replace("\\n", " ")
    #print(html)
    regex = r"(local?) - - \[(\d+)\/(\w+)\/(\d+)(.*?)] (.*?) (.*?) (.*?) (\d+) (\d+)" 
    #regex = re.compile("^.+- - \[(\d+)\/(\w+)\/(\d+).+] \"(\w+) (.*) .+? (.*?)")
    #print(response.read())
    
    data = re.split(regex, str(html))
    #print(data.group(15))
    #logfile = re.match(regex, str(html))
    #print(logfile)
    #if logfile:
        #print(logfile.group(1))
    #print(len(data))
    #print(data)
    Oct = 0
    Months = [Oct]
    #count = 0
    print(data[1])
    # for i in range (len(data)):
    #     print(data[i])
    #     target = re.search(regex, data[i])
    #     if target:
    #         print("Howdy")
            
    #         # if (target.group(3) == "Jan"):
    #         #     Months[Jan] += 1
    #         # if (target.group(3) == "Feb"):
    #         #     Months[Feb] += 1
    #         # if (target.group(3) == "Mar"):
    #         #     Months[Mar] += 1
    #         # if (target.group(3) == "Apr"):
    #         #     Months[Apr] += 1
    #         # if (target.group(3) == "May"):
    #         #     Months[May] += 1
    #         # if (target.group(3) == "Jun"):
    #         #     Months[Jun] += 1
    #         # if (target.group(3) == "Jul"):
    #         #     Months[Jul] += 1
    #         # if (target.group(3) == "Aug"):
    #         #     Months[Aug] += 1
    #         # if (target.group(3) == "Sep"):
    #         #     Months[Sep] += 1
    #         if (target.group(3) == "Oct"):
    #             Months[Oct] += 1
    #         # if (target.group(3) == "Nov"):
    #         #     Months[Nov] += 1
    #         # if (target.group(3) == "Dec"):
    #         #     Months[Dec] += 1


    #     #count += 1

    # #print(count)

    # #  for line in req:
    # #      matchObj = re.match( regex, req.text, re.M|re.I)
        
    # #      count += 1
    
    # print("total queries = ", len(data))
    # print("Oct queries", Months[Oct]) 
        
        
        
    # #for line in matchObj:
    #     #matchlength += 1

    # #print (matchlength)

    # #rint(matchObj)

    # #for i in matchObj:
    #     #if group3 = "Oct"
            

    # #if matchObj:

    # """class HTMLParser(HTMLParser)
    #     def handle_starttag(self, tag, attrs):
    #         print("Start tag: ", tag)
    #         for attr in attrs:
    #             print("attr:")
    #     def handle_endtag(sef, tag):
    #         print("End tag: ", tag)
    #     def handle_comment(self, data):
    #         print("Comment: ", data)"""
            
main()