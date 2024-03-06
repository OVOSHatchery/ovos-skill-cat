from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler
import requests

from ovos_workshop.decorators import resting_screen_handler


class CatSkill(OVOSSkill):

    def update_cat(self):
        r = requests.get('https://api.thecatapi.com/v1/images/search')
        if r:
            self.gui['imgLink'] = r.json()[0]['url']

    @resting_screen_handler("Cat Image")
    def idle(self, message):
        self.update_cat()
        self.gui.show_page('idle.qml')

    @intent_handler('ShowCat.intent')
    def cat_handler(self, message):
        self.log.info('SHOWING CAT')
        self.update_cat()
        self.gui.show_page('cat.qml')
        self.speak_dialog('mjau')
