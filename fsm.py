from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_message
from utils import send_image_url
from draw_3x3 import draw
from build_image import bind_image

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
        print("I'm entering A1")
        sender_id = event['sender']['id']
        new_image = bind_image(["A1"], sender_id)
        responce = send_image_url(sender_id, new_image)
    
        new_image = bind_image(["A1","B2"], sender_id)
        responce = send_image_url(sender_id, new_image)


        #def on_exit_A1(self, a):
        #print("Leaving A1")

    def to_A1B1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "B1"
        return False

    def on_enter_A1B1(self, event):
        print("I'm entering A1B1")
        sender_id = event['sender']['id']
        new_image = bind_image(["A1", "B2", "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)
    
        new_image = bind_image(["A1","B2", "B1", "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        #self.go_back()
    
    def to_A1B1x(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" or text == "C2" or text == "B3" or text == "C3":
                return True
        return False
    
    def on_enter_A1B1x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "B1", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
    
        new_image = bind_image(["A1","B2", "B1", "C1", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)

        responese = send_text_message(sender_id, "You lose")
        self.go_back()

    def to_A1B1A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3":
                return True
        return False

    def on_enter_A1B1A3(self, event):
        sender_id = event['sender']['id']
        new_image = bind_image(["A1", "B2", "B1", "C1", "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
    
        new_image = bind_image(["A1","B2", "B1", "C1", "A3", "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)

    def to_A1B1A3x(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" or text == "C3":
                return True
        return False

    def on_enter_A1B1A3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "B1", "C1", "A3", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
    
        new_image = bind_image(["A1","B2", "B1", "C1", "A3", "A2", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)

        responese = send_text_message(sender_id, "You lose")
        self.go_back()

        
    def to_A1B1A3C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2":
                return True
        return False

    def on_enter_A1B1A3C2(self, event):
        sender_id = event['sender']['id']
        new_image = bind_image(["A1", "B2", "B1", "C1", "A3", "A2", "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
    
        new_image = bind_image(["A1","B2", "B1", "C1", "A3", "A2", "C2", "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)

        responese = send_text_message(sender_id, "平手")

        self.go_back()
        
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
