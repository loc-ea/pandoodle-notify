import threading

from notifyproject.connector import Connector
from notifyproject.slack import Slack

from . import settings


class Notify:

    def __init__(self):
        self.connector = Connector(settings.HOSTS)
        self.slack = Slack(
            settings.SLACK_API_TOKEN,
            settings.SLACK_CHANNEL
        )
        self.messages = {
            'warning': ':warning:There is only one node alive:warning:',
            'danger': ':exclamation:All nodes are dead:exclamation:',
        }
        self.interval = 5

    def send_message_if_dead(self):
        """Send warning message if there is only 1 node alive
        and send danger message if there is no nodes alive

        :returns bool: return True if a warning or danger message is sent
        """

        is_sent = True
        alive_nodes = self.connector.get_num_of_alive_nodes()
        if alive_nodes == 1:
            self.slack.send_message(self.messages['warning'])
        elif alive_nodes == 0:
            self.slack.send_message(self.messages['danger'])
        else:
            is_sent = False

        return is_sent

    def run(self):
        """Check if all Cassandra nodes are dead, send a message via Slack
        at specified intervals (in seconds).

        If a warning or danger message is already sent, the next check will
        be in 1 minute. Otherwise the next check will be in 5 seconds. It
        is used to prevent spaming too much.
        """

        is_sent = self.send_message_if_dead()
        self.interval = 60 if is_sent else 5
        threading.Timer(self.interval, self.run).start()
