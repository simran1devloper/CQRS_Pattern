# infrastructure/message_broker.py

from collections import defaultdict
from dataclasses import asdict, is_dataclass


class InMemoryMessageBroker:
    def __init__(self):
        self.subscribers = defaultdict(list)
        self.messages = []

    def subscribe(self, topic: str, handler):
        self.subscribers[topic].append(handler)

    def publish(self, topic: str, event):
        message = {
            "topic": topic,
            "event_type": event.__class__.__name__,
            "payload": asdict(event) if is_dataclass(event) else event
        }
        self.messages.append(message)

        for handler in self.subscribers[topic]:
            handler(event)

    def get_messages(self):
        return self.messages
