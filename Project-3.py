#!/usr/bin/env python
from html.parser import HTMLParser
import requests
import urllib.request
import re
from requests import get

# def download(url, file_name):
# # open in binary mode
#     with open(file_name, "wb") as file:
#         # get request
#         response = get(url)
#         # write to file
#         file.write(response.content)

#     return()

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
    data = []
    count = 0
    #Open file
    #Parse file
    with urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log") as response:

        html = str(response.read())
        #print(html)
    
    #html = html.replace("\\n", " ")
    #print(html)
    regex = r"(local|remote) - - \[(\d+)\/(\w+)\/(\d+)(.*?)] (.*?) (.*?) (.*?) (\d+) (\d+)"
    regex2 = r"(.*?)\'(local|remote) - - \[(\d+)\/(\w+)\/(\d+)(.*?)] (.*?) (.*?) (.*?) (\d+) (\d+)"
    #re.compile(regex) 
    #regex = re.compile("^.+- - \[(\d+)\/(\w+)\/(\d+).+] \"(\w+) (.*) .+? (.*?)")
    #print(response.read())
    Jan = 0
    Feb = 0
    Mar = 0
    Apr = 0
    May = 0
    Jun = 0
    Jul = 0
    Aug = 0
    Sep = 0
    Oct = 0
    Nov = 0
    Dec = 0 
    Months = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]

    for match in re.finditer(regex, html):
        data.append(match)
        if (match.group(3) == "Jan"):
            Jan += 1
        if (match.group(3) == "Feb"):
            Feb += 1
        if (match.group(3) == "Mar"):
            Mar += 1
        if (match.group(3) == "Apr"):
            Apr += 1
        if (match.group(3) == "May"):
            Months[May] += 1
        if (match.group(3) == "Jun"):
            Months[Jun] += 1
        if (match.group(3) == "Jul"):
            Months[Jul] += 1
        if (match.group(3) == "Aug"):
            Months[Aug] += 1
        if (match.group(3) == "Sep"):
            Months[Sep] += 1
        if (match.group(3) == "Oct"):
            Months[Oct] += 1
        if (match.group(3) == "Nov"):
            Months[Nov] += 1
        if (match.group(3) == "Dec"):
            Months[Dec] += 1
        #print(match)
    print(Jan)
    print(Feb)
    print(Mar)
    # print("okay")

    # for i in range(len(data)):
    #     look = re.search(regex2, str(data[i]))
    #     print(data[i])
    #     #print(look)
    #     if look:
    #         print(data[i].group(4))
            
    #print(data[2])
    #data = re.split(regex, str(html))
    #print(data.group(15))
    #logfile = re.match(regex, str(html))
    #print(logfile)
    #if logfile:
        #print(logfile.group(1))
    #print(len(data))
    #print(data)
    
    #count = 0
    #print(data[1])
    #for i in range (len(data)):
        #print(data[i])
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