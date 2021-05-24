import queue
import json


class MessageAnnouncer:

    def __init__(self):
        self.listeners = dict()

    def listen(self, key):
        self.listeners[key] = queue.Queue(maxsize=5)
        return self.listeners[key]

    def announce(self, msg):
        # We go in reverse order because we might have to delete an element, which will shift the
        # indices backward
        data = list(filter(None, msg.split('\n')))
        key = data[0][7:]
        # value = data[1][6:]
        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[key].put_nowait(msg)
            except queue.Full:
                del self.listeners[key]


def format_sse(data: str, event=None) -> str:
    """Formats a string and an event name in order to follow the event stream convention.
    >>> format_sse(data=json.dumps({'abc': 123}), event='Jackson 5')
    'event: Jackson 5\\ndata: {"abc": 123}\\n\\n'
    """
    msg = f'data: {data}\n\n'
    if event is not None:
        msg = f'event: {event}\n{msg}'
    return msg
