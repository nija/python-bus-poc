from event import Event
from bus import Bus
from listener import WeatherBot

# 1- Register listeners on the bus
bus = Bus()
bus.register(WeatherBot(), Event.Types.message_created_event)

# 2- Let's create some events on the bus and see if our listeners pick them up

for i in range(4):
    if i % 2 == 0:
        print "throwing message_created_event"
        bus.notify(Event(Event.Types.message_created_event, {"room_id":1, "data": "pyro weather 94301", "user_id": 123}))
    else:
        print "throwing user_joins_room"
        bus.notify(Event(Event.Types.user_joins_room, {}))