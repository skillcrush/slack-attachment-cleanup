import time
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

token = os.getenv('STUDENT_COMM_SLACK_TOKEN')

### Grab files older than three months - change as necessary
ts_to = int(time.time()) - 90 * 24 * 60 * 60

def list_file_ids():

  params = {
    'token': token,
    'ts_to': ts_to,
    'count': 100 # Max number of attachments to delete - change as necessary - recommend fewer than 200 at a time to avoid timeout
  }

  uri = 'https://slack.com/api/files.list'

  response = requests.get(uri, params=params)
  files = json.loads(response.text)['files']

  # Have a look at the keys of the first dictionnary entry in the files list
  print([f.keys() for f in files[0:1]])

  file_ids = [f['id'] for f in files]
  
  return file_ids


def delete_files(file_ids):

  for count, file_id in enumerate(file_ids, 1):

    params = {
      'token': token,
      'file': file_id
      }

    uri = 'https://slack.com/api/files.delete'

    response = requests.get(uri, params=params)

    print (f'{count} of {len(file_ids)}, -, {file_id} {json.loads(response.text)["ok"]}')


# Files, be gone!
if __name__ == '__main__':
  delete_files(list_file_ids())