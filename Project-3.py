#!/usr/bin/env python
import urllib.request
import re

def main():

    new_jan_match = open("January.txt",'w')
    new_feb_match = open("February.txt",'w')
    new_mar_match = open("March.txt",'w')
    new_apr_match = open("April.txt",'w')
    new_may_match = open("May.txt",'w')
    new_jun_match = open("June.txt",'w')
    new_jul_match = open("July.txt",'w')
    new_aug_match = open("August.txt",'w')
    new_sep_match = open("September.txt",'w')
    new_oct_match = open("October.txt",'w')
    new_nov_match = open("November.txt",'w')
    new_dec_match = open("December.txt",'w')
    
    data = []
  
    with urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log") as response:

        html = str(response.readlines())
        
    regex = r"(local|remote) - - \[(\d+)\/(\w+)\/(\d+)(.*?)] (.*?) (.*?) (.*?) (\d+) (\d+)?"
   
    htmlcount=0
    jpgcount=0
    xbmcount=0
    txtcount=0
    gifcount=0
    rgbcount=0
    pscount=0
    execount=0
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
    Success = 0
    Fail = 0
    Redirect = 0

    for match in re.finditer(regex, html):
        data.append(match)
        if (((match.group(7)).split('.'))[1] == "html"):
            htmlcount += 1
        if (((match.group(7)).split('.'))[1] == "jpg"):
            jpgcount += 1
        if (((match.group(7)).split('.'))[1] == "xbm"):
            xbmcount += 1
        if (((match.group(7)).split('.'))[1] == "txt"):
            txtcount += 1
        if (((match.group(7)).split('.'))[1] == "gif"):
            gifcount += 1
        if (((match.group(7)).split('.'))[1] == "rgb"):
            rgbcount += 1
        if (((match.group(7)).split('.'))[1] == "ps"):
            pscount += 1
        if (((match.group(7)).split('.'))[1] == "exe"):
            execount += 1
        if (match.group(3) == "Jan"):
            Jan += 1
            new_jan_match.write(str(match.groups()) + "\n")
        elif (match.group(3) == "Feb"):
            Feb += 1
            new_feb_match.write(str(match.groups()) + "\n")
        elif (match.group(3) == "Mar"):
            Mar += 1
            new_mar_match.write(str(match.groups()) + "\n")
        elif (match.group(3) == "Apr"):
            Apr += 1
            new_apr_match.write(str(match.groups()) + "\n")
        elif (match.group(3) == "May"):
            May += 1
            new_may_match.write(str(match.groups()) + "\n")
        elif (match.group(3) == "Jun"):
            Jun += 1
            new_jun_match.write(str(match.groups()) + "\n")
        elif (match.group(3) == "Jul"):
            Jul += 1
            new_jul_match.write(str(match.groups()) + "\n")
        elif (match.group(3) == "Aug"):
            Aug += 1
            new_aug_match.write(str(match.groups()) + "\n")
        elif (match.group(3) == "Sep"):
            Sep += 1
            new_sep_match.write(str(match.groups()) + "\n")
        elif (match.group(3) == "Oct"):
            Oct += 1
            new_oct_match.write(str(match.groups()) + "\n")
        elif (match.group(3) == "Nov"):
            Nov += 1
            new_nov_match.write(str(match.groups()) + "\n")
        elif (match.group(3) == "Dec"):
            Dec += 1
            new_dec_match.write(str(match.groups()) + "\n")
        if (match.group(9)[0] == "2"):
            Success += 1
        if (str(match.group(9))[0] == "3"):
            Redirect += 1
        if (str(match.group(9))[0] == "4"):
            Fail += 1
    
    
    total = len(data)
    dailyaverage = int((total/365))
    weeklyaverage = int((total/52))
    monthlyaverage = int((total/12))
    failpercent = int((Fail/total)*100)
    Sucpercent = int((Success/total)*100)
    Redpercent = int((Redirect/total)*100)
    print("There were", total, "queries in the log")
    print("Of the ", total, "requests, ", Success, "(", Sucpercent,"%) were successful,", Redirect, "(", Redpercent, "%) were redirected, and", Fail, "(", failpercent, "%) failed due to server error")

    print("On average, there were", dailyaverage," queries a day, ", weeklyaverage," queries a week and ", monthlyaverage," queries per month")

    #use min to count most frequent files
    files = (htmlcount, jpgcount, xbmcount, txtcount, gifcount, rgbcount, pscount, execount)

    #use min to count least frequent files
    if htmlcount == min(files):
        print('html is least requested file with', min(files), "requests")

    elif jpgcount == min(files):
        print('jpg is least requested file with', min(files), "requests")
    elif xbmcount == min(files):
        print('xbm is least requested file with', min(files), "requests")
    elif txtcount == min(files):
        print('txt is least requested file with', min(files), "requests")
    elif gifcount == min(files):
        print('gif is least requested file with', min(files), "requests")
    elif rgbcount == min(files):
        print('rgb is least requested file with', min(files), "requests")  
    elif pscount == min(files):
        print('ps is least requested file with', min(files), "requests") 
    elif execount == min(files):
        print('exe is least requested file with', min(files), "requests")

    if htmlcount == max(files):
        print('html is most requested file with', max(files), "requests")

    elif jpgcount == max(files):
        print('jpg is most requested file with', max(files), "requests")
    elif xbmcount == max(files):
        print('xbm is most requested file with', max(files), "requests")
    elif txtcount == max(files):
        print('txt is most requested file with', max(files), "requests")
    elif gifcount == max(files):
        print('gif is most requested file with', max(files), "requests")
    elif rgbcount == max(files):
        print('rgb is most requested file with', max(files), "requests")  
    elif pscount == max(files):
        print('ps is most requested file with', max(files), "requests") 
    elif execount == max(files):
        print('exe is most requested file with', max(files), "requests")  
            
main()