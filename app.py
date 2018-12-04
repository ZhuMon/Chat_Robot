from bottle import route, run, request, abort, static_file

from fsm import TocMachine
import os

VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'A1',
        'A1B1',
        'A1B1x',
        'A1B1A3',
        'A1B1A3x',
        'A1B1A3C2'
        
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'A1',
            'conditions': 'to_A1'
        },
        {
            'trigger': 'a_one',
            'source': 'A1',
            'dest': 'A1B1',
            'conditions': 'to_A1B1'
        },
        {
            'trigger': 'a_one',
            'source': 'A1B1',
            'dest': 'A1B1x',
            'conditions': 'to_A1B1x'
        },
        {
            'trigger': 'a_one',
            'source': 'A1B1',
            'dest': 'A1B1A3',
            'conditions': 'to_A1B1A3'
        },
        {
            'trigger': 'a_one',
            'source': 'A1B1A3',
            'dest': 'A1B1A3x',
            'conditions': 'to_A1B1A3x'
        },
        {
            'trigger': 'a_one',
            'source': 'A1B1A3',
            'dest': 'A1B1A3C2',
            'conditions': 'to_A1B1A3C2'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2', 
                'A1B1x',
                'A1B1A3x',
                'A1B1A3C2'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        if machine.state[0] == 'A' and machine.state[1] == '1':
            machine.a_one(event)
        else:
            machine.advance(event)
        print("Ok")
        return 'OK'



@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    #run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
    run(host="localhost", port=5000, debug=True, reloader=True)
