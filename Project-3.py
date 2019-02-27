#!/usr/bin/env python
import urllib.request
import re

#Compare with 3XX, 4XX codes
#Calculate %
#Catch extraneous logfiles


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
        
    regex = r"(local|remote) - - \[(\d+)\/(\w+)\/(\d+)(.*?)] (.*?) (.*?) (.*?) (\d+) (\d+?)"
   
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
    print("There were", len(data), "queries in the log")
    print("Of the ", len(data), "requests, ", Success, "were successful,", Redirect, "were redirected, and", Fail, "failed due to server error")

    month = input("Choose a month (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ")
    if (month == "Jan"):
        print("There were", Jan, "queries in", month)
        day = input("Enter a day (1-31): ")
        
    if (month == "Feb"):
        print("There were", Feb, "queries in", month)
        day = input("Enter a day (1-31): ")
        
        new_feb_match.write(str(match.groups()) + "\n")
    if (month == "Mar"):
        print("There were", Mar, "queries in", month)
        day = input("Enter a day (1-31): ")
        
        new_mar_match.write(str(match.groups()) + "\n")
    if (month == "Apr"):
        print("There were", Apr, "queries in", month)
        day = input("Enter a day (1-31): ")
        
        new_apr_match.write(str(match.groups()) + "\n")
    if (month == "May"):
        print("There were", May, "queries in", month)
        day = input("Enter a day (1-31): ")
        
        new_may_match.write(str(match.groups()) + "\n")
    if (month == "Jun"):
        print("There were", Jun, "queries in", month)
        day = input("Enter a day (1-31): ")
        
        new_jun_match.write(str(match.groups()) + "\n")
    if (month == "Jul"):
        print("There were", Jul, "queries in", month)
        day = input("Enter a day (1-31): ")
        
        new_jul_match.write(str(match.groups()) + "\n")
    if (month == "Aug"):
        print("There were", Aug, "queries in", month)
        day = input("Enter a day (1-31): ")
        
        new_aug_match.write(str(match.groups()) + "\n")
    if (month == "Sep"):
        print("There were", Sep, "queries in", month)
        day = input("Enter a day (1-31): ")
        
        new_sep_match.write(str(match.groups()) + "\n")
    if (month == "Oct"):
        print("There were", Oct, "queries in", month)
        day = input("Enter a day (1-31): ")
        
        new_oct_match.write(str(match.groups()) + "\n")
    if (month == "Nov"):
        print("There were", Nov, "queries in", month)
        day = input("Enter a day (1-31): ")
        
        new_nov_match.write(str(match.groups()) + "\n")
    if (month == "Dec"):
        print("There were", Dec, "queries in", month)
        day = input("Enter a day (1-31): ")
        

    
    # print("There were", Jan, "queries in January")
    # print(Feb)
    # print(Mar)
            
main()