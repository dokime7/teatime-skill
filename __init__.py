from mycroft import MycroftSkill, intent_file_handler


class Teatime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('teatime.intent')
    def handle_teatime(self, message):
        self.speak_dialog('teatime')


def create_skill():
    return Teatime()

