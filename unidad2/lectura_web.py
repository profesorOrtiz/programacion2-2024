from urllib.request import urlopen

web = urlopen("https://www.google.com")
google = web.read()
print(len(google))
web.close()
