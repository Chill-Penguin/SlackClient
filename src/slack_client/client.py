from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from exceptions import SlackReadMessageError, SlackSendMessageError


class SlackClientWrapper:
    def __init__(self, token: str):
        self.client = WebClient(token=token)

    def send_message(self, channel_id, text, thread_ts=None, blocks=None, attachments=None):
        try:
            response = self.client.chat_postMessage(
                channel=channel_id,
                text=text,
                thread_ts=thread_ts,
                blocks=blocks,
                attachments=attachments
            )
            return response.data
        except SlackApiError as e:
            raise SlackSendMessageError(f"Slack Send Error: {e.response['error']}") from e
        
    def get_messages(self, channel, limit=10, query=""):
        """
        Fetch the last 10 messages from a Slack channel and return those matching a query.

        :param channel: The Slack channel ID (or name) to fetch messages from.
        :param query: The query string to search for in the message content.
        :return: List of matching messages
        """
        try:
            response = self.client.conversations_history(channel=channel, limit=limit)
            messages = response['messages']
            matching_messages = [msg for msg in messages if query.lower() in msg.get('text', '').lower()]
            return matching_messages
        except SlackApiError as e:
            raise SlackReadMessageError(f"Slack Read Error: {e.response['error']}")
