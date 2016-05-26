class Bus():
    
    def __init__(self):
        self.listeners = {}
        return
    
    def notify(self, event):
        print "Bus notified of event {}".format(event.get_type())
        
        if self.listeners.get(event.get_type()) is None:
            print "There are no listeners registered for event type {}".format(event.get_type())
            return
        
        for listener in self.listeners[event.get_type()]:
            listener.handle_event(event)
        
        return
    
    def register(self, listener, event_type):
        print "Listener {} registered for event {}!".format(listener, event_type)
        if event_type in self.listeners:
            self.listeners[event_type].append(listener)
        else:
            self.listeners[event_type] = [listener]
        return