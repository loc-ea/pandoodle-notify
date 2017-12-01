import unittest
from unittest.mock import Mock

from notifyproject.app import Notify

class TestNotify(unittest.TestCase):
    def setUp(self):
        self.notify = Notify()
        self.notify.connector.hosts = ['127.0.0.1', '10.0.0.11'];
        self.notify.slack.send_message = Mock()

    def test_send_warning_message_if_one_node_alive(self):
        self.notify.connector.get_num_of_alive_nodes = Mock(return_value=1)

        is_sent = self.notify.send_message_if_dead()
        self.assertTrue(is_sent)
        self.notify.slack.send_message.assert_called_with(
            self.notify.messages['warning']
        )

    def test_send_danger_message_if_no_node_alives(self):
        self.notify.connector.get_num_of_alive_nodes = Mock(return_value=0)

        is_sent = self.notify.send_message_if_dead()
        self.assertTrue(is_sent)
        self.notify.slack.send_message.assert_called_with(
            self.notify.messages['danger']
        )

    def test_dont_sent_message_if_more_than_2_node_alive(self):
        self.notify.connector.get_num_of_alive_nodes = Mock(return_value=2)

        is_sent = self.notify.send_message_if_dead()
        self.assertFalse(is_sent)
        self.notify.slack.send_message.assert_not_called()
