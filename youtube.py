#!/usr/bin/python
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import random
from helper import CANDIDATE_LIST

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyCIJpjZnPu50DovHlF8pQw1t5Q5JsxB_FQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(candidate, numresults):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  candidate_query = candidate.replace(" ", "+")
  search_response = youtube.search().list(
    q=candidate_query+"+speech",
    part="id,snippet",
    maxResults=numresults
  ).execute()

  videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append((search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))


  r = random.randint(0, len(videos) - 1)
  random_video = videos[r] #id
  return random_video

if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Google")
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()

  r = random.randint(0, len(CANDIDATE_LIST) - 1)
  random_candidate = CANDIDATE_LIST[r]
  numresults = 25
  try:
    youtube_search(random_candidate, numresults)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)