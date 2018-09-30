from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class SayHelloTo(MycroftSkill):
    @intent_handler(IntentBuilder("") \
            .requeire("to.hello.say.intent").require("Name"))
    def handle_say_hello_to_intent(self, message):
        name = message.data.get("Name")
        self.speak_dialog("to.hello.say", data=name)

def create_skill():
    return SayHelloTo()

