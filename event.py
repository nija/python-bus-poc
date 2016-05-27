class Event():
    '''Event class'''

    class Types():
        '''Types of event classes'''
        message_created_event = "MESSAGE_CREATED_EVENT"
        user_joins_room = "USER_JOINS_ROOM_EVENT"
    
    def __init__(self, event_type, data):
        self.data = data
        self.type = event_type
        
    def get_data(self):
        return self.data
    
    def get_type(self):
        return self.type
    
    def __str__(self):
        return "{}:{}".format(self.type, self.data)