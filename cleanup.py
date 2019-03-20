import requests
import time
import json
import os

token = os.environ['STUDENT_COMM_SLACK_TOKEN']

### Grab files older than three months - change as necessary
ts_to = int(time.time()) - 90 * 24 * 60 * 60

def list_files():

  params = {
    'token': token,
    'ts_to': ts_to,
    'count': 100 # Number of attachments to delete - change as necessary - recommend fewer than 200 at a time to avoid timeout
  }

  uri = 'https://slack.com/api/files.list'

  response = requests.get(uri, params=params)
  
  files = json.loads(response.text)['files']

  file_ids = [f['id'] for f in files]
  
  return file_ids


def delete_files(file_ids):

  count = 0

  num_files = len(file_ids)

  for file_id in file_ids:

    count += 1

    params = {
      'token': token,
      'file': file_id
      }

    uri = 'https://slack.com/api/files.delete'

    response = requests.get(uri, params=params)

    print (count, "of", num_files, "-", file_id, json.loads(response.text)['ok'])

# Files, be gone!
delete_files(list_files())
