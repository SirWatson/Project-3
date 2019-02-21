from html.parser import HTMLParser
import requests
import urllib.request
import re


def main():  

    #Download file
    req = requests.get("https://s3.amazonaws.com/tcmg476/http_access_log")
    print(req.status_code)
    print(req.text)

    #Open file
    #Parse file
    #with urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log") as response:
    #html = response.read()

    regex = r"(.*) - - (.*) (.*) (.*) (.*) (.*) (.*)"

    matchObj = re.match( regex, req.text, re.M|re.I)
    for line in matchObj:
        matchlength += 1

    print (matchlength)

    #rint(matchObj)

    #for i in matchObj:
        #if group3 = "Oct"
            

    #if matchObj:

    """class HTMLParser(HTMLParser)
        def handle_starttag(self, tag, attrs):
            print("Start tag: ", tag)
            for attr in attrs:
                print("attr:")
        def handle_endtag(sef, tag):
            print("End tag: ", tag)
        def handle_comment(self, data):
            print("Comment: ", data)"""
            
main()