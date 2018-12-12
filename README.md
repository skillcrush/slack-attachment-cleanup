# Remove Stale Slack Attachments - Create More Space!

### This script will delete X number of Slack attachments from the Slack space that the token is connected to, before a specified point in time.

### Steps:


1- Get a Slack token and create an environmental variable for it

2- Open `test-first.py` and edit the `ts_to` and `count` variables to suit your current needs.

3- Run the `test-first.py` file in the Terminal and output the data to data.txt:

`python test-first.py > data.txt`

4- `data.txt` now contains the ids, names and timestamps of all the files that are slated for deletion. If you want to view timestamps in a human readable way, use [www.unixtimestamp.com](https://www.unixtimestamp.com/index.php) or similar.

5- If you are happy with the result, open `cleanup.py` and modify the `ts_to` and `count` variable to match those in the `test-first.py` file.

6- Run the `cleanup.py` file:

`python cleanup.py`

Rejoice, for lo, stale attachments no longer burden your Slack space.


![](https://media3.giphy.com/media/2yuS0kxvPq7FJxEYl1/200w.gif?cid=c94812d05c0f04a8324d306d2e987def)