import re
from weather_api import WeatherApi

class Listener():
    
    def __init__(self):
        return
    
    def handle_event(self, event):
        return

class WeatherBot(Listener):

    def say_weather(self, location):
        WeatherApi.get_weather(location)
        
    def handle_event(self, event):
        print "WeatherBot is handling event {}".format(event)
        msg_data = event.data.get("data")
        pattern = "^(.*)\s(.*)\s(\d*)\s"
        
        # functions = ["weather", "zombie", "lyft"]
        
        # if msg_data.startswith("pytro"):
        #     for function in functions:
        #         if function in msg_data.contains(function):
        #             eval(function, )
                    
                
        if msg_data.startswith("pyro"):
            if "weather" in msg_data:
                pattern = "^(.*)\s(.*)\s(\d*)"
                groups = re.findall(pattern, msg_data)
                location = groups[0][2]
                self.say_weather(location)
        else:
            return
        
        
        return
        
