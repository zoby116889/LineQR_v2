import requests, json

### FROM https://wall.alphacoders.com/ ###

token_key= "INSERT TOKEN KEY HERE"
## GET API KEY FROM https://api.boteater.us/get_token ###

def search():
    search = input("Search query: ") #example naruto
    result = json.loads(requests.get("https://api.boteater.us/alphacoders?search="+search+"&auth="+token_key).text)
    for img in result["result"]:
        print("")
        print("Image Name: "+img["name"])
        print("Link Image: "+img["url"])

search()