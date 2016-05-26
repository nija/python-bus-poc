class Event():
    
    class Types():
        message_created_event = "MESSAGE_CREATED_EVENT"
        user_joins_room = "USER_JOINS_ROOM"
    
    def __init__(self, type, data):
        self.data = data
        self.type = type
        
    def get_data(self):
        return self.data
    
    def get_type(self):
        return self.type
    
    def __str__(self):
        return "{}:{}".format(self.type, self.data)