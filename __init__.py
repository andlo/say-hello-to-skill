from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class SayHelloTo(MycroftSkill):
   
    @intent_handler(IntentBuilder("").require("say").optionally("hello").optionally("to"))

    def  handle_say_hello_to_intent(self, message):
        #response = {'name': message.data.get("Name")}
        response = {'name': message.utterance_remainder()}
        #response = message.utterance_remainder()
        self.speak_dialog("to.hello.say", data=response)

def create_skill():
    return SayHelloTo()
