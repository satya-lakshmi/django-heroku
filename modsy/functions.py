import os
import logging
logging.basicConfig(level=logging.DEBUG)

from slack import WebClient
from slack.errors import SlackApiError

slack_token = os.environ.get("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

try:
  response = client.chat_postMessage(
    channel="#lakshmig",
    text="Hello from your app! :tada:"
  )
except SlackApiError as e:
  # You will get a SlackApiError if "ok" is False
  assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
  log(e.response)



