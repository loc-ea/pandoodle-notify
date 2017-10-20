from slackclient import SlackClient

from . import settings


class Slack:
    """Connect to Slack and send messages"""

    def __init__(self, token, channel):
        """Initialize Slack object

        :param token str: Slack api token
        :param channel str: Slack channel name
        """
        self.token = token
        self.channel = channel
        self.slack_client = SlackClient(self.token)

    def send_message(self, message):
        """Send the message to channel

        :param message str: Message will be sent
        :raises Exeption: Cannot send the message to Slack
        """

        result = self.slack_client.api_call(
            'chat.postMessage',
            channel=self.channel,
            text=message
        )

        if not result['ok']:
            raise Exception('Cannot send the message to Slack channel')
