import state_pb2

def get_state(ID):
    my_pb_file = "state.pb"

    my_all_sender = state_pb2.all_sender()

    with open(my_pb_file, "rb") as f:
        my_all_sender.ParseFromString(f.read())

    for sender in my_all_sender.sender:
        if ID == sender.id:
            return sender.state

    return "user"

def store_state(ID, state):
    my_pb_file = "state.pb"
    
    my_all_sender = state_pb2.all_sender()

    with open(my_pb_file, "rb") as f:
        my_all_sender.ParseFromString(f.read())

    for sender in my_all_sender.sender:
        if ID == sender.id:
            sender.state = state
            with open("state.pb", "wb") as f:
                f.write(my_all_sender.SerializeToString())
            return

    # no record
    my_all_sender2 = state_pb2.all_sender()

    new = my_all_sender2.sender.add()

    new.id = ID
    new.state = state

    with open("state.pb", "ab") as f:
        f.write(my_all_sender2.SerializeToString())

def clean_state(ID):
    my_pb_file = "state.pb"
    
    my_all_sender = state_pb2.all_sender()

    with open(my_pb_file, "rb") as f:
        my_all_sender.ParseFromString(f.read())

    for sender in my_all_sender.sender:
        if ID == sender.id:
            sender.state = "user"
            with open("state.pb", "wb") as f:
                f.write(my_all_sender.SerializeToString())
            return

    return

