import queue
import json


class MessageAnnouncer:

    def __init__(self):
        # maintains which keys are being subscribed to
        self.listeners = dict()

    def listen(self, key):
        # new queue created per subscriber
        self.listeners[key] = queue.Queue(maxsize=5)
        return self.listeners[key]

    def announce(self, msg):
        data = list(filter(None, msg.split('\n')))
        key = data[0][7:]

        # puts data in queue under given key
        try:
            self.listeners[key].put_nowait(msg)
        except queue.Full:
            del self.listeners[key]


def format_sse(data: str, event=None):
    # Formats string to match sse standard as per installed client
    msg = f'data: {data}\n\n'
    if event is not None:
        msg = f'event: {event}\n{msg}'
    return msg
