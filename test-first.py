import requests
import time
import json
import os

token = os.environ['STUDENT_COMM_SLACK_TOKEN']

### Grab files older than six months - change as necessary
ts_to = int(time.time()) - 100 * 24 * 60 * 60

def list_files():

  params = {
    'token': token,
    'ts_to': ts_to,
    'count': 10 # Number of attachments to delete - change as necessary - recommend fewer than 200 at a time to avoid timeout
  }

  uri = 'https://slack.com/api/files.list'

  response = requests.get(uri, params=params)

  all_files = json.loads(response.text)['files']

  ### How many files did we fetch?
  print (len(all_files))

  ### Print the whole bloody array of objects (if you want to see all the key/value pairs)
  # print(all_files)

  ### Let's have a closer look at what we got 
  for single_file in all_files:
    id = [single_file['id']]
    name = [single_file['url_private']]
    timestamp = [single_file['timestamp']]
    print(id, name, timestamp)

  return json.loads(response.text)['files']

list_files()
