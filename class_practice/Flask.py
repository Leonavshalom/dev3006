# import requests
# response = requests.get("http://localhost:5001/whatismyname")
# actual = response.text
# expected = "saved new car"
#
# assert actual == expected

import requests
response = requests.get("https://api.github.com/users/avielb/repos")
result = [{"name" : repo["full_name"],"tags" : repo["git_tags_url"]} for repo in response.json() if repo["private"] == False]
for a in result:
    print(a)


