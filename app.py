import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi
from onboarding_tutorial import OnboardingTutorial

app = Flask('OSE Bot')
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events", app)

# Initialize a Web API client
client = WebClient(token=SLACK_BOT_TOKEN)

def clubCategory(user_id: str, channel: str):
    # Create a new onboarding tutorial.
    onboarding_tutorial = OnboardingTutorial(channel)

    # Get the onboarding message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)

# ================ Team Join Event =============== #
# When the user first joins a team, the type of the event will be 'team_join'.
# Here we'll link the onboarding_message callback to the 'team_join' event.
@slack_events_adapter.on("app_mention")
def select_channel(payload):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """
    # dictionary for channel
    channel_dict = {
        "President": "CTZMY1LS2",
        "Co-President": "CTZMY1LS2",
        "Vice-President": "CTZMY1LS2",
        "Financial Officer": "GU13ENXMM"
    }

    slackbotID = 'DNNLR3BMG' # slackbot ID

    event = payload.get("event", {})

    # Get the id of the Slack user associated with the incoming event
    text = event["text"]
    userid_loc = text.find("@")+1
    user_id = text[userid_loc:userid_loc+9]
    userrole_loc = text.find("bot")+5
    userrole = text[userrole_loc:].strip()


    # TESTING: post selected userrole
    response = client.chat_postMessage(
        channel=event["channel"],
         text=userrole
        )

    # VERIFIED for all users
    if userrole in channel_dict.keys():
        response = client.conversations_invite(
            channel=channel_dict[userrole],
            users = user_id
        )
    # Post the onboarding message.
    clubCategory(user_id, channel)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000)