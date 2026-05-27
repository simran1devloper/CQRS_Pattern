# infrastructure/event_bus.py

ORDER_EVENTS_TOPIC = "order-events"


class EventBus:
    def __init__(self, message_broker):
        self.message_broker = message_broker

    def subscribe(self, handler):
        self.message_broker.subscribe(ORDER_EVENTS_TOPIC, handler)

    def publish(self, event):
        self.message_broker.publish(ORDER_EVENTS_TOPIC, event)

    def get_published_events(self):
        return self.message_broker.get_messages()
