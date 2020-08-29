import requests
import time
import json
import os

from dotenv import load_dotenv
load_dotenv()

token = os.getenv('STUDENT_COMM_SLACK_TOKEN')

### Grab files older than three months - change as necessary
ts_to = int(time.time()) - 90 * 24 * 60 * 60

def list_files():

  params = {
    'token': token,
    'ts_to': ts_to,
    'count': 10 # Number of attachments to delete - change as necessary - recommend fewer than 200 at a time to avoid timeout
  }

  uri = 'https://slack.com/api/files.list'

  response = requests.get(uri, params=params)

  all_files = json.loads(response.text)['files']

  number_of_files = len(all_files)
  ### How many files did we fetch?
  print ( "%d files will be deleted." % (number_of_files))

  ### Print the whole bloody array of objects (if you want to see all the key/value pairs)
  # print(all_files)

  ### Let's have a closer look at what we got 
  for single_file in all_files:
    id = [single_file['id']]
    name = [single_file['url_private']]
    timestamp = [single_file['timestamp']]
    readableTime = time.strftime("%D %H:%M", time.localtime(timestamp[0]))
    print(id, name, readableTime)

  return json.loads(response.text)['files']

list_files()
