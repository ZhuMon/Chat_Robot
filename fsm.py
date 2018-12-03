from transitions.extensions import GraphMachine

from utils import send_text_message
from draw_3x3 import draw

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state1'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state2'
        return False

    def to_A1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == 'A1'
        return False

    def on_enter_A1(self, event):
        sender_id = event['sender']['id']
        responce = send_text_message(sender_id, draw(["A1"]))
        #responce = send_text_message(sender_id, draw(["A1", "B2"]))
        #self.go_back()

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state1")
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state2")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')
