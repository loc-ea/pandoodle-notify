# Project settings

import os

# Database connections for Cassandra
# Sample HOSTS='127.0.01, 10.0.0.1'
HOSTS = [h.strip() for h in os.environ['HOSTS'].split(',')]

# Slack api token
SLACK_API_TOKEN = os.environ['SLACK_API_TOKEN']
# Slack channel
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
