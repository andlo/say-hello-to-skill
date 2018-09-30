from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler


class SayHelloTo(MycroftSkill):
    @intent_handler(IntentBuilder("") \
            .requeire("SayHelloToKeyword").require("Name"))
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('to.hello.say.intent')
    def handle_to_hello_say(self, message):
        self.speak_dialog('to.hello.say')


def create_skill():
    return SayHelloTo()

