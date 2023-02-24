"""The functions in this project library."""


def hello_world(msg: str) -> str:
    """Uppercases a message string.

    The given message string will be uppercased and then returned.

    Args:
        msg: A message.

    Returns:
        An uppercase version of the input message.

    """
    result = msg.upper()
    return result


class Hello:
    msg: str
    msg2: str
    msg3: str
    msg4: str
    msg5: str
    msg6: str


class World:
    """Hello world."""

    def send_message(self, msg: str) -> str:
        """Uppercases a message string.

        The given message string will be uppercased and then returned.

        Args:
            msg: A message.

        Returns:
            An uppercase version of the input message.

        """
        result = msg.upper()
        return result
