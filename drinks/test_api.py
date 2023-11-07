import requests

# response = requests.get('http://127.0.0.1:8000/drinks')
# print(response.json())

url = 'http://127.0.0.1:8000/drinks/1'

# data = {
#     'name':'Banana Shake',
#     'description':'Fresh organic banana juice' 
# }

# response = requests.post(url, json=data)

response = requests.delete(url)


                    

