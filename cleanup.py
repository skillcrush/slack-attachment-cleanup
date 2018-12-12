import requests

import time

import json

from secret.token.secret import token

# Grab files older than six months:
ts_to = int(time.time()) - 180 * 24 * 60 * 60

def list_files():

  params = {

    'token': token

    ,'ts_to': ts_to

    ,'count': 10 # this number is arbitrary

  }

  uri = 'https://slack.com/api/files.list'

  response = requests.get(uri, params=params)

  print(response)

  # todo - 
  payload = json.loads(response.text)['files']

  # How many do we have?
  print (len(payload))

  # Let's have a look at the names
  id = [f['id'] for f in payload]
  name = [f['url_private'] for f in payload]
  timestamp = [f['timestamp'] for f in payload]
  print(timestamp)

  # Print the whole bloody object
  # print(payload)
  return json.loads(response.text)['files']


def delete_files(file_ids):

  count = 0

  num_files = len(file_ids)

  for file_id in file_ids:

    count = count + 1

    params = {

      'token': token

      ,'file': file_id

      }

    uri = 'https://slack.com/api/files.delete'

    response = requests.get(uri, params=params)

    print (count, "of", num_files, "-", file_id, json.loads(response.text)['ok'])

files = list_files()

file_ids = [f['id'] for f in files]

delete_files(file_ids)