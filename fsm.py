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
        
    def to_A1C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_A1C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1C1x(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" or text == "C2" or text == "A3" or text == "C3":
                return True
        return False

    def on_enter_A1C1x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C1", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C1", "B1", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1C1B3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" :
                return True
        return False

    def on_enter_A1C1B3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C1", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C1", "B1", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1C1B3x(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" or text == "C3":
                return True
        return False

    def on_enter_A1C1B3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C1", "B1", "B3", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C1", "B1", "B3", "A2", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1C1B3C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_A1C1B3C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C1", "B1", "B3", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C1", "B1", "B3", "A2", new, "C3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_A1A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_A1A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1A2x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "B1" or text == "C2" or text == "B3" or text == "C3":
                return True
        return False

    def on_enter_A1A2x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "A2", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "A2", "A3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1A2C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_A1A2C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "A2", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "A2", "A3", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1A2C1x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C2" or text == "C3":
                return True
        return False

    def on_enter_A1A2C1x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "A2", "A3", "C1", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "A2", "A3", "C1", "B1", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1A2C1B3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" :
                return True
        return False

    def on_enter_A1A2C1B3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "A2", "A3", "C1", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "A2", "A3", "C1", "B1", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_A1C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_A1C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1C2x(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" or text == "A2" or text == "A3" or text == "C3":
                return True
        return False

    def on_enter_A1C2x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C2", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C2", "B1", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1C2B3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" :
                return True
        return False

    def on_enter_A1C2B3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C2", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C2", "B1", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1C2B3x(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" or text == "C3":
                return True
        return False

    def on_enter_A1C2B3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C2", "B1", "B3", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C2", "B1", "B3", "A3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1C2B3C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_A1C2B3C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C2", "B1", "B3", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C2", "B1", "B3", "A3", new, "C3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_A1A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_A1A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1A3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "B1" or text == "C1" or text == "B3" or text == "C3":
                return True
        return False

    def on_enter_A1A3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "A3", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "A3", "A2", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1A3C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_A1A3C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "A3", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "A3", "A2", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1A3C2x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C1" or text == "C3":
                return True
        return False

    def on_enter_A1A3C2x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "A3", "A2", "C2", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "A3", "A2", "C2", "B3", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1A3C2B1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B1" :
                return True
        return False

    def on_enter_A1A3C2B1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "A3", "A2", "C2", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "A3", "A2", "C2", "B3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_A1B3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" :
                return True
        return False

    def on_enter_A1B3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1B3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "B1" or text == "C1" or text == "A3" or text == "C3":
                return True
        return False

    def on_enter_A1B3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "B3", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "B3", "A2", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1B3C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_A1B3C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "B3", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "B3", "A2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1B3C2x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "B1" or text == "C3":
                return True
        return False

    def on_enter_A1B3C2x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "B3", "A2", "C2", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "B3", "A2", "C2", "C1", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1B3C2A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_A1B3C2A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "B3", "A2", "C2", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "B3", "A2", "C2", "C1", new, "C3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_A1C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_A1C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1C3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C1" or text == "A2" or text == "C2" or text == "A3":
                return True
        return False

    def on_enter_A1C3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C3", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C3", "B1", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1C3B3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" :
                return True
        return False

    def on_enter_A1C3B3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C3", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C3", "B1", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_A1C3B3x(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" or text == "C2":
                return True
        return False

    def on_enter_A1C3B3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C3", "B1", "B3", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C3", "B1", "B3", "A3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_A1C3B3C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_A1C3B3C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["A1", "B2", "C3", "B1", "B3", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["A1", "B2", "C3", "B1", "B3", "A3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B1" :
                return True
        return False

    def on_enter_B1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image([new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image([new, "A1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B1C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", new, "B2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1C1x(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" or text == "C2" or text == "A3" or text == "B3":
                return True
        return False

    def on_enter_B1C1x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C1", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C1", "B2", new, "C3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1C1C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B1C1C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C1", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C1", "B2", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1C1C3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "A3" or text == "B3":
                return True
        return False

    def on_enter_B1C1C3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C1", "B2", "C3", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C1", "B2", "C3", "C2", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1C1C3A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B1C1C3A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C1", "B2", "C3", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C1", "B2", "C3", "C2", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B1A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", new, "B2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1A2x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C1" or text == "C2" or text == "A3" or text == "B3":
                return True
        return False

    def on_enter_B1A2x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "A2", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "A2", "B2", new, "C3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1A2C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B1A2C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "A2", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "A2", "B2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1A2C3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C2" or text == "B3":
                return True
        return False

    def on_enter_B1A2C3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "A2", "B2", "C3", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "A2", "B2", "C3", "A3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1A2C3C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B1A2C3C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "A2", "B2", "C3", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "A2", "B2", "C3", "A3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1B2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B2" :
                return True
        return False

    def on_enter_B1B2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1B2C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B1B2C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1B2C1x(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" or text == "C2":
                return True
        return False

    def on_enter_B1B2C1x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "C1", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "C1", "A3", new, "C3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1B2C1C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B1B2C1C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "C1", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "C1", "A3", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1B2A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B1B2A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1B2A2A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B1B2A2A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "A2", "C2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1B2A2C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B1B2A2C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "A2", "C2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1B2A2C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B1B2A2C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "A2", "C2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1B2C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_B1B2C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1B2C2x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C1" or text == "C3":
                return True
        return False

    def on_enter_B1B2C2x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "C2", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "C2", "A2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1B2C2A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B1B2C2A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "C2", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "C2", "A2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1B2A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B1B2A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1B2A3A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B1B2A3A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "A3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "A3", "C1", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1B2A3C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_B1B2A3C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "A3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "A3", "C1", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1B2A3C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B1B2A3C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "A3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "A3", "C1", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1B2C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B1B2C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1B2C3C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B1B2C3C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "C3", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "C3", "C2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1B2C3A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B1B2C3A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "C3", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "C3", "C2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1B2C3A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B1B2C3A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B2", "B3", "C3", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B2", "B3", "C3", "C2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_B1C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", new, "B2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1C2x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C1" or text == "A2" or text == "A3" or text == "B3":
                return True
        return False

    def on_enter_B1C2x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C2", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C2", "B2", new, "C3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1C2C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B1C2C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C2", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C2", "B2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1C2C3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "A2" or text == "B3":
                return True
        return False

    def on_enter_B1C2C3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C2", "B2", "C3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C2", "B2", "C3", "C1", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1C2C3A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B1C2C3A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C2", "B2", "C3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C2", "B2", "C3", "C1", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B1A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", new, "B2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1A3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C1" or text == "A2" or text == "C2" or text == "B3":
                return True
        return False

    def on_enter_B1A3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "A3", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "A3", "B2", new, "C3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1A3C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B1A3C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "A3", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "A3", "B2", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1A3C3C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B1A3C3C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "A3", "B2", "C3", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "A3", "B2", "C3", "B3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1A3C3A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B1A3C3A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "A3", "B2", "C3", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "A3", "B2", "C3", "B3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1B3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" :
                return True
        return False

    def on_enter_B1B3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", new, "B2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1B3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C1" or text == "A2" or text == "C2" or text == "A3":
                return True
        return False

    def on_enter_B1B3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B3", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B3", "B2", new, "C3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1B3C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B1B3C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B3", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B3", "B2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1B3C3C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B1B3C3C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B3", "B2", "C3", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B3", "B2", "C3", "A3", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1B3C3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "A2" or text == "C2":
                return True
        return False

    def on_enter_B1B3C3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "B3", "B2", "C3", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "B3", "B2", "C3", "A3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B1C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", new, "B2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1C3C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B1C3C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1C3C1x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "A3" or text == "B3":
                return True
        return False

    def on_enter_B1C3C1x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", "C1", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", "C1", "C2", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1C3C1A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B1C3C1A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", "C1", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", "C1", "C2", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1C3A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B1C3A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1C3A2x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C2" or text == "B3":
                return True
        return False

    def on_enter_B1C3A2x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", "A2", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", "A2", "C1", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1C3A2A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B1C3A2A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", "A2", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", "A2", "C1", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1C3C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_B1C3C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1C3C2x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "A2" or text == "B3":
                return True
        return False

    def on_enter_B1C3C2x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", "C2", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", "C2", "C1", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1C3C2A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B1C3C2A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", "C2", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", "C2", "C1", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1C3A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B1C3A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1C3A3C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B1C3A3C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", "A3", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", "A3", "B3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1C3A3A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B1C3A3A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", "A3", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", "A3", "B3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1C3A3C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_B1C3A3C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", "A3", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", "A3", "B3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B1C3B3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" :
                return True
        return False

    def on_enter_B1C3B3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B1C3B3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C1" or text == "C2":
                return True
        return False

    def on_enter_B1C3B3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", "B3", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", "B3", "A3", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B1C3B3A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B1C3B3A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B1", "A1", "C3", "B2", "B3", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B1", "A1", "C3", "B2", "B3", "A3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B2" :
                return True
        return False

    def on_enter_B2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image([new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image([new, "A1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2B1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B1" :
                return True
        return False

    def on_enter_B2B1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2B1C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B2B1C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2B1C1x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C2" or text == "C3":
                return True
        return False

    def on_enter_B2B1C1x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", "C1", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", "C1", "A3", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2B1C1A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B2B1C1A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", "C1", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", "C1", "A3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2B1A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B2B1A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2B1A2C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B2B1A2C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", "A2", "C2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2B1A2A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B2B1A2A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", "A2", "C2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2B1A2C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B2B1A2C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", "A2", "C2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2B1C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_B2B1C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2B1C2x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C1" or text == "C3":
                return True
        return False

    def on_enter_B2B1C2x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", "C2", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", "C2", "A2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2B1C2A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B2B1C2A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", "C2", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", "C2", "A2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2B1A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B2B1A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2B1A3e(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "A2" or text == "C3":
                return True
        return False

    def on_enter_B2B1A3e(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", "A3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", "A3", "C1", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2B1A3C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_B2B1A3C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", "A3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", "A3", "C1", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2B1C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B2B1C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2B1C3e(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C1" or text == "A2":
                return True
        return False

    def on_enter_B2B1C3e(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", "C3", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", "C3", "C2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2B1C3A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B2B1C3A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B1", "B3", "C3", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B1", "B3", "C3", "C2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B2C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2C1x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "B2" or text == "C2" or text == "B3" or text == "C3":
                return True
        return False

    def on_enter_B2C1x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "C1", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "C1", "A3", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2C1A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B2C1A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "C1", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "C1", "A3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2C1A2B1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B1" :
                return True
        return False

    def on_enter_B2C1A2B1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "C1", "A3", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "C1", "A3", "A2", "C2", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2C1A2B3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" :
                return True
        return False

    def on_enter_B2C1A2B3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "C1", "A3", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "C1", "A3", "A2", "C2", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2C1A2C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B2C1A2C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "C1", "A3", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "C1", "A3", "A2", "C2", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B2A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2A2B1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B1" :
                return True
        return False

    def on_enter_B2A2B1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2A2B1C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B2A2B1C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", "B1", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", "B1", "B3", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2A2B1e(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "A3" or text == "C3":
                return True
        return False

    def on_enter_B2A2B1e(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", "B1", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", "B1", "B3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2A2C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B2A2C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2A2C1e(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "B1" or text == "C3":
                return True
        return False

    def on_enter_B2A2C1e(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", "C1", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", "C1", "A3", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2A2C1B3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" :
                return True
        return False

    def on_enter_B2A2C1B3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", "C1", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", "C1", "A3", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2A2A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B2A2A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2A2A3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "B1" or text == "B3":
                return True
        return False

    def on_enter_B2A2A3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", "A3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", "A3", "C1", new, "C3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2A2A3C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B2A2A3C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", "A3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", "A3", "C1", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2A2B3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" :
                return True
        return False

    def on_enter_B2A2B3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2A2B3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "A3" or text == "C3":
                return True
        return False

    def on_enter_B2A2B3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", "B3", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", "B3", "B1", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2A2B3C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B2A2B3C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", "B3", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", "B3", "B1", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2A2C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B2A2C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2A2C3e(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "B1" or text == "C1":
                return True
        return False

    def on_enter_B2A2C3e(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", "C3", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", "C3", "B3", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2A2C3A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B2A2C3A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A2", "C2", "C3", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A2", "C2", "C3", "B3", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2C2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C2" :
                return True
        return False

    def on_enter_B2C2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2C2x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "B1" or text == "C1" or text == "B3" or text == "C3":
                return True
        return False

    def on_enter_B2C2x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "C2", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "C2", "A2", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2C2A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B2C2A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "C2", "A2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "C2", "A2", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2C2A3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "B3" or text == "C3":
                return True
        return False

    def on_enter_B2C2A3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "C2", "A2", "A3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "C2", "A2", "A3", "C1", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2C2A3B1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B1" :
                return True
        return False

    def on_enter_B2C2A3B1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "C2", "A2", "A3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "C2", "A2", "A3", "C1", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B2A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2A3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "A2" or text == "C2" or text == "B3" or text == "C3":
                return True
        return False

    def on_enter_B2A3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A3", "C1", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2A3B1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B1" :
                return True
        return False

    def on_enter_B2A3B1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A3", "C1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A3", "C1", new, "B3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2A3B1A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B2A3B1A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A3", "C1", "B1", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A3", "C1", "B1", "B3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2A3B1e(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C2" or text == "C3":
                return True
        return False

    def on_enter_B2A3B1e(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "A3", "C1", "B1", "B3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "A3", "C1", "B1", "B3", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()



    def to_B2B3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "B3" :
                return True
        return False

    def on_enter_B2B3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2B3x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "A2" or text == "C2" or text == "A3" or text == "C3":
                return True
        return False

    def on_enter_B2B3x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B3", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B3", "B1", new, "C1"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2B3C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B2B3C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B3", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B3", "B1", new, "A3"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2B3C1x(self, event):
        if event.get("message"):
            text = event['message']['text']
        	if text == "C2" or text == "C3":
                return True
        return False

    def on_enter_B2B3C1x(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B3", "B1", "C1", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B3", "B1", "C1", "A3", new, "A2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "You lose")
        self.go_back()



    def to_B2B3C1A2(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A2" :
                return True
        return False

    def on_enter_B2B3C1A2(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "B3", "B1", "C1", "A3", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "B3", "B1", "C1", "A3", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)
        responese = send_text_message(sender_id, "平手")
        self.go_back()


    def to_B2C3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C3" :
                return True
        return False

    def on_enter_B2C3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", new, "B1"], sender_id)
        responce = send_image_url(sender_id, new_image)



    def to_B2C3C1(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "C1" :
                return True
        return False

    def on_enter_B2C3C1(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "C3", "B1", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        new_image = bind_image(["B2", "A1", "C3", "B1", new, "C2"], sender_id)
        responce = send_image_url(sender_id, new_image)


    def to_B2C3C1A3(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == "A3" :
                return True
        return False

    def on_enter_B2C3C1A3(self, event):
        sender_id = event['sender']['id']
        new = event['message']['text']
        new_image = bind_image(["B2", "A1", "C3", "B1", "C1", "C2", new], sender_id)
        responce = send_image_url(sender_id, new_image)
        

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
