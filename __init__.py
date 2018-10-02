from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class SayHelloTo(MycroftSkill):
   
    @intent_handler(IntentBuilder("").require("thisis"))
    
    def  handle_say_hello_to_intent(self, message):
        response = {'name': message.data.get("Name")}
        self.speak_dialog("to.hello.say", data=response)

def create_skill():
    return SayHelloTo()
