from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler

class SayHelloTo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('to.hello.say.intent')
    def  handle_say_hello_to_intent(self, message):
        response = {'name': message.data.get("name")}
        self.speak_dialog("to.hello.say", data=response)

def create_skill():
    return SayHelloTo()
