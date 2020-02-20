import os
import logging
import json
import requests
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi

app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)

# Initialize a Web API client
client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

# ================ Team Join Event =============== #
# When the user first joins a team, the type of the event will be 'team_join'.
# Here we'll link the onboarding_message callback to the 'team_join' event.
@slack_events_adapter.on("app_mention")
def workflow(payload):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """
    # dictionary for channel
    channel_dict = {
        "President": "CTZMY1LS2",
        "Co-President": "CTZMY1LS2",
        "Vice-President": "CTZMY1LS2",
        "Financial Officer": "GU13ENXMM",
        "Academic": "CU7L7F16K",
        "Arts-Dance":"CU7PHQR61",
        "Arts-Drama":"CU7L7QE95",
        "Arts-Music":"CTW99CUN7",
        "Arts-Other":"CU79RD684",
        "Athletic-Club Sport":"CU5QYE3TP",
        "Athletic-Martial Arts":"CU7PY8ASZ",
        "Athletic-Outdoors": "CU7A1A05S",
        "Athletic-Other":"CU7A1A05S",
        "Community Service":"CU814EUMC",
        "Ethnic/Cultural": "CU814LN5U",
        "Health and Wellness":"CU7Q40V9N",
        "International":"CU814LN5U",
        "Media/Publications":"CUA0WN38W",
        "Political":"CTV03STQA",
        "Pre-Professional": "CU7L7F16K",
        "Recreational":"CU7A1A05S", 
        "Religious": "CTUAMEZ0T",
        "Social": "CTVLNBBBK",
        "Social Awareness":"CTV03STQA"
    }
    webhook_dict = {
        "Event Planning": "https://hooks.slack.com/workflows/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",
        "Funding": "https://hooks.slack.com/workflows/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",
        "Room Reservation": "https://hooks.slack.com/workflows/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"
    }

    event = payload.get("event", {})

    # Get the id of the Slack user associated with the incoming event
    text = event["text"].split("\n*\n")
    if event["username"] == "New Member":
        user = text[1].replace('User: <@','')[0:9]
        role = text[2].replace('Role: ','').strip()
        assu = text[3].replace('ASSU: ','').strip()
        category = text[4].replace('Category: ','').strip()

        # TESTING: post selected userrole
        # response = client.chat_postMessage(
        #     channel=event["channel"],
        #     text=role + "\n" + assu + "\n" + category
        #     )

        # VERIFIED for all users
        if role in channel_dict.keys():
            response = client.conversations_invite(
                channel=channel_dict[role],
                users = user
            )

        if category in channel_dict.keys():
            response = client.conversations_invite(
                channel=channel_dict[category],
                users = user
            )
    # Post the onboarding message.
    if event["username"]=="Help Desk":
        user = text[1].replace('User: <@','')[0:9]
        category = text[2].replace('Category: ','').strip()
        priority = text[3].replace('Priority: ','').strip()
        request = text[4].replace('Request: ','').strip()
        details = text[5].replace('Details: ','').strip()
        webhook_url = webhook_dict[category]
        slackdata = {
            "Category": category,
            "User": user,
            "Priority": priority,
            "Request": request,
            "Details": details
        }
        response = requests.post(webhook_url, data=json.dumps(slackdata), headers ={'Content-Type': 'application/json'})
        
if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000)