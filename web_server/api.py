import requests


def get_categories():
  result = requests.get('https://api.escuelajs.co/api/v1/categories')

  if result.status_code == 200:
    for category in result.json():
      print('Category: ', category['name'])
  else:
    print('There was an error! :C')
