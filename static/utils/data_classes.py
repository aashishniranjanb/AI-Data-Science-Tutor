from dataclasses import dataclass

@dataclass
class Message:
    """
    A data class for storing individual messages
    in the chat interface.
    """
    role: str      # "user" or "assistant"
    content: str   # The actual text content of the message
