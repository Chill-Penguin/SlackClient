class NoSlackClientsRegisteredError(Exception):
    """Raised when trying to access a Slack client but none have been registered."""
    pass
class SlackClientError(Exception):
    """Base exception for Slack client issues."""
    pass

class SlackSendMessageError(SlackClientError):
    """Raised when sending a Slack message fails."""
    pass

class SlackReadMessageError(SlackClientError):
    """Raised when reading from Slack fails."""
    pass