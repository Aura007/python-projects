import pyshorteners 

url=input("Enter URL for shortening: \n")

print ("Url after shortening : ",pyshorteners.Shortener().tinyurl.short(url))