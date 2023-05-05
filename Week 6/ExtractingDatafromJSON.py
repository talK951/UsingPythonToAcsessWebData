import json
import urllib.request, urllib.parse, urllib.error

url = "http://py4e-data.dr-chuck.net/comments_1809423.json"
uh = urllib.request.urlopen(url)
data = json.loads(uh.read().decode())
list_of_comments = data['comments']
sum = 0

for comment in list_of_comments:
    sum += int(comment['count'])
print(sum)
