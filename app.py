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
        'A1B1A3C2',
        'A1C1', 'A1C1x', 'A1C1B3', 'A1C1B3x', 'A1C1B3C2', 'A1A2', 'A1A2x', 'A1A2C1', 'A1A2C1x', 'A1A2C1B3', 'A1C2', 'A1C2x', 'A1C2B3', 'A1C2B3x', 'A1C2B3C1', 'A1A3', 'A1A3x', 'A1A3C2', 'A1A3C2x', 'A1A3C2B1', 'A1B3', 'A1B3x', 'A1B3C2', 'A1B3C2x', 'A1B3C2A3', 'A1C3', 'A1C3x', 'A1C3B3', 'A1C3B3x', 'A1C3B3C1', 
        'B1', 'B1C1', 'B1C1x', 'B1C1C3', 'B1C1C3x', 'B1C1C3A2', 'B1A2', 'B1A2x', 'B1A2C3', 'B1A2C3x', 'B1A2C3C1', 'B1B2', 'B1B2C1', 'B1B2C1x', 'B1B2C1C3', 'B1B2A2', 'B1B2A2A3', 'B1B2A2C1', 'B1B2A2C3', 'B1B2C2', 'B1B2C2x', 'B1B2C2A3', 'B1B2A3', 'B1B2A3A2', 'B1B2A3C2', 'B1B2A3C3', 'B1B2C3', 'B1B2C3C1', 'B1B2C3A2', 'B1B2C3A3', 'B1C2', 'B1C2x', 'B1C2C3', 'B1C2C3x', 'B1C2C3A3', 'B1A3', 'B1A3x', 'B1A3C3', 'B1A3C3C1', 'B1A3C3A2', 'B1B3', 'B1B3x', 'B1B3C3', 'B1B3C3C1', 'B1B3C3x', 'B1C3', 'B1C3C1', 'B1C3C1x', 'B1C3C1A2', 'B1C3A2', 'B1C3A2x', 'B1C3A2A3', 'B1C3C2', 'B1C3C2x', 'B1C3C2A3', 'B1C3A3', 'B1C3A3C1', 'B1C3A3A2', 'B1C3A3C2', 'B1C3B3', 'B1C3B3x', 'B1C3B3A2', 'B2', 'B2B1', 'B2B1C1', 'B2B1C1x', 'B2B1C1A2', 'B2B1A2', 'B2B1A2C1', 'B2B1A2A3', 'B2B1A2C3', 'B2B1C2', 'B2B1C2x', 'B2B1C2A3', 'B2B1A3', 'B2B1A3e', 'B2B1A3C2', 'B2B1C3', 'B2B1C3e', 'B2B1C3A3', 'B2C1', 'B2C1x', 'B2C1A2', 'B2C1A2B1', 'B2C1A2B3', 'B2C1A2C3', 'B2A2', 'B2A2B1', 'B2A2B1C1', 'B2A2B1e', 'B2A2C1', 'B2A2C1e', 'B2A2C1B3', 'B2A2A3', 'B2A2A3x', 'B2A2A3C3', 'B2A2B3', 'B2A2B3x', 'B2A2B3C1', 'B2A2C3', 'B2A2C3e', 'B2A2C3A3', 'B2C2', 'B2C2x', 'B2C2A3', 'B2C2A3x', 'B2C2A3B1', 'B2A3', 'B2A3x', 'B2A3B1', 'B2A3B1A2', 'B2A3B1e', 'B2B3', 'B2B3x', 'B2B3C1', 'B2B3C1x', 'B2B3C1A2',
        'B2C3', 'B2C3C1', 'B2C3C1e', 'B2C3x',
        'B2C3C1A3'
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
            'trigger': 'a_one',
            'source': 'A1',
            'dest': 'A1C1',
            'conditions': 'to_A1C1'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C1',
            'dest': 'A1C1x',
            'conditions': 'to_A1C1x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C1',
            'dest': 'A1C1B3',
            'conditions': 'to_A1C1B3'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C1B3',
            'dest': 'A1C1B3x',
            'conditions': 'to_A1C1B3x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C1B3',
            'dest': 'A1C1B3C2',
            'conditions': 'to_A1C1B3C2'
        },

        {
            'trigger': 'a_one',
            'source': 'A1',
            'dest': 'A1A2',
            'conditions': 'to_A1A2'
        },

        {
            'trigger': 'a_one',
            'source': 'A1A2',
            'dest': 'A1A2x',
            'conditions': 'to_A1A2x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1A2',
            'dest': 'A1A2C1',
            'conditions': 'to_A1A2C1'
        },

        {
            'trigger': 'a_one',
            'source': 'A1A2C1',
            'dest': 'A1A2C1x',
            'conditions': 'to_A1A2C1x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1A2C1',
            'dest': 'A1A2C1B3',
            'conditions': 'to_A1A2C1B3'
        },

        {
            'trigger': 'a_one',
            'source': 'A1',
            'dest': 'A1C2',
            'conditions': 'to_A1C2'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C2',
            'dest': 'A1C2x',
            'conditions': 'to_A1C2x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C2',
            'dest': 'A1C2B3',
            'conditions': 'to_A1C2B3'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C2B3',
            'dest': 'A1C2B3x',
            'conditions': 'to_A1C2B3x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C2B3',
            'dest': 'A1C2B3C1',
            'conditions': 'to_A1C2B3C1'
        },

        {
            'trigger': 'a_one',
            'source': 'A1',
            'dest': 'A1A3',
            'conditions': 'to_A1A3'
        },

        {
            'trigger': 'a_one',
            'source': 'A1A3',
            'dest': 'A1A3x',
            'conditions': 'to_A1A3x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1A3',
            'dest': 'A1A3C2',
            'conditions': 'to_A1A3C2'
        },

        {
            'trigger': 'a_one',
            'source': 'A1A3C2',
            'dest': 'A1A3C2x',
            'conditions': 'to_A1A3C2x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1A3C2',
            'dest': 'A1A3C2B1',
            'conditions': 'to_A1A3C2B1'
        },

        {
            'trigger': 'a_one',
            'source': 'A1',
            'dest': 'A1B3',
            'conditions': 'to_A1B3'
        },

        {
            'trigger': 'a_one',
            'source': 'A1B3',
            'dest': 'A1B3x',
            'conditions': 'to_A1B3x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1B3',
            'dest': 'A1B3C2',
            'conditions': 'to_A1B3C2'
        },

        {
            'trigger': 'a_one',
            'source': 'A1B3C2',
            'dest': 'A1B3C2x',
            'conditions': 'to_A1B3C2x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1B3C2',
            'dest': 'A1B3C2A3',
            'conditions': 'to_A1B3C2A3'
        },

        {
            'trigger': 'a_one',
            'source': 'A1',
            'dest': 'A1C3',
            'conditions': 'to_A1C3'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C3',
            'dest': 'A1C3x',
            'conditions': 'to_A1C3x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C3',
            'dest': 'A1C3B3',
            'conditions': 'to_A1C3B3'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C3B3',
            'dest': 'A1C3B3x',
            'conditions': 'to_A1C3B3x'
        },

        {
            'trigger': 'a_one',
            'source': 'A1C3B3',
            'dest': 'A1C3B3C1',
            'conditions': 'to_A1C3B3C1'
        },

        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'B1',
            'conditions': 'to_B1'
        },

        {
            'trigger': 'b_one',
            'source': 'B1',
            'dest': 'B1C1',
            'conditions': 'to_B1C1'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C1',
            'dest': 'B1C1x',
            'conditions': 'to_B1C1x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C1',
            'dest': 'B1C1C3',
            'conditions': 'to_B1C1C3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C1C3',
            'dest': 'B1C1C3x',
            'conditions': 'to_B1C1C3x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C1C3',
            'dest': 'B1C1C3A2',
            'conditions': 'to_B1C1C3A2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1',
            'dest': 'B1A2',
            'conditions': 'to_B1A2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1A2',
            'dest': 'B1A2x',
            'conditions': 'to_B1A2x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1A2',
            'dest': 'B1A2C3',
            'conditions': 'to_B1A2C3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1A2C3',
            'dest': 'B1A2C3x',
            'conditions': 'to_B1A2C3x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1A2C3',
            'dest': 'B1A2C3C1',
            'conditions': 'to_B1A2C3C1'
        },

        {
            'trigger': 'b_one',
            'source': 'B1',
            'dest': 'B1B2',
            'conditions': 'to_B1B2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2',
            'dest': 'B1B2C1',
            'conditions': 'to_B1B2C1'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2C1',
            'dest': 'B1B2C1x',
            'conditions': 'to_B1B2C1x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2C1',
            'dest': 'B1B2C1C3',
            'conditions': 'to_B1B2C1C3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2',
            'dest': 'B1B2A2',
            'conditions': 'to_B1B2A2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2A2',
            'dest': 'B1B2A2A3',
            'conditions': 'to_B1B2A2A3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2A2',
            'dest': 'B1B2A2C1',
            'conditions': 'to_B1B2A2C1'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2A2',
            'dest': 'B1B2A2C3',
            'conditions': 'to_B1B2A2C3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2',
            'dest': 'B1B2C2',
            'conditions': 'to_B1B2C2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2C2',
            'dest': 'B1B2C2x',
            'conditions': 'to_B1B2C2x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2C2',
            'dest': 'B1B2C2A3',
            'conditions': 'to_B1B2C2A3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2',
            'dest': 'B1B2A3',
            'conditions': 'to_B1B2A3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2A3',
            'dest': 'B1B2A3A2',
            'conditions': 'to_B1B2A3A2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2A3',
            'dest': 'B1B2A3C2',
            'conditions': 'to_B1B2A3C2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2A3',
            'dest': 'B1B2A3C3',
            'conditions': 'to_B1B2A3C3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2',
            'dest': 'B1B2C3',
            'conditions': 'to_B1B2C3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2C3',
            'dest': 'B1B2C3C1',
            'conditions': 'to_B1B2C3C1'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2C3',
            'dest': 'B1B2C3A2',
            'conditions': 'to_B1B2C3A2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B2C3',
            'dest': 'B1B2C3A3',
            'conditions': 'to_B1B2C3A3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1',
            'dest': 'B1C2',
            'conditions': 'to_B1C2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C2',
            'dest': 'B1C2x',
            'conditions': 'to_B1C2x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C2',
            'dest': 'B1C2C3',
            'conditions': 'to_B1C2C3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C2C3',
            'dest': 'B1C2C3x',
            'conditions': 'to_B1C2C3x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C2C3',
            'dest': 'B1C2C3A3',
            'conditions': 'to_B1C2C3A3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1',
            'dest': 'B1A3',
            'conditions': 'to_B1A3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1A3',
            'dest': 'B1A3x',
            'conditions': 'to_B1A3x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1A3',
            'dest': 'B1A3C3',
            'conditions': 'to_B1A3C3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1A3C3',
            'dest': 'B1A3C3C1',
            'conditions': 'to_B1A3C3C1'
        },

        {
            'trigger': 'b_one',
            'source': 'B1A3C3',
            'dest': 'B1A3C3A2',
            'conditions': 'to_B1A3C3A2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1',
            'dest': 'B1B3',
            'conditions': 'to_B1B3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B3',
            'dest': 'B1B3x',
            'conditions': 'to_B1B3x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B3',
            'dest': 'B1B3C3',
            'conditions': 'to_B1B3C3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B3C3',
            'dest': 'B1B3C3C1',
            'conditions': 'to_B1B3C3C1'
        },

        {
            'trigger': 'b_one',
            'source': 'B1B3C3',
            'dest': 'B1B3C3x',
            'conditions': 'to_B1B3C3x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1',
            'dest': 'B1C3',
            'conditions': 'to_B1C3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3',
            'dest': 'B1C3C1',
            'conditions': 'to_B1C3C1'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3C1',
            'dest': 'B1C3C1x',
            'conditions': 'to_B1C3C1x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3C1',
            'dest': 'B1C3C1A2',
            'conditions': 'to_B1C3C1A2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3',
            'dest': 'B1C3A2',
            'conditions': 'to_B1C3A2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3A2',
            'dest': 'B1C3A2x',
            'conditions': 'to_B1C3A2x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3A2',
            'dest': 'B1C3A2A3',
            'conditions': 'to_B1C3A2A3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3',
            'dest': 'B1C3C2',
            'conditions': 'to_B1C3C2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3C2',
            'dest': 'B1C3C2x',
            'conditions': 'to_B1C3C2x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3C2',
            'dest': 'B1C3C2A3',
            'conditions': 'to_B1C3C2A3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3',
            'dest': 'B1C3A3',
            'conditions': 'to_B1C3A3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3A3',
            'dest': 'B1C3A3C1',
            'conditions': 'to_B1C3A3C1'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3A3',
            'dest': 'B1C3A3A2',
            'conditions': 'to_B1C3A3A2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3A3',
            'dest': 'B1C3A3C2',
            'conditions': 'to_B1C3A3C2'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3',
            'dest': 'B1C3B3',
            'conditions': 'to_B1C3B3'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3B3',
            'dest': 'B1C3B3x',
            'conditions': 'to_B1C3B3x'
        },

        {
            'trigger': 'b_one',
            'source': 'B1C3B3',
            'dest': 'B1C3B3A2',
            'conditions': 'to_B1C3B3A2'
        },

        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'B2',
            'conditions': 'to_B2'
        },

        {
            'trigger': 'b_two',
            'source': 'B2',
            'dest': 'B2B1',
            'conditions': 'to_B2B1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1',
            'dest': 'B2B1C1',
            'conditions': 'to_B2B1C1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1C1',
            'dest': 'B2B1C1x',
            'conditions': 'to_B2B1C1x'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1C1',
            'dest': 'B2B1C1A2',
            'conditions': 'to_B2B1C1A2'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1',
            'dest': 'B2B1A2',
            'conditions': 'to_B2B1A2'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1A2',
            'dest': 'B2B1A2C1',
            'conditions': 'to_B2B1A2C1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1A2',
            'dest': 'B2B1A2A3',
            'conditions': 'to_B2B1A2A3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1A2',
            'dest': 'B2B1A2C3',
            'conditions': 'to_B2B1A2C3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1',
            'dest': 'B2B1C2',
            'conditions': 'to_B2B1C2'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1C2',
            'dest': 'B2B1C2x',
            'conditions': 'to_B2B1C2x'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1C2',
            'dest': 'B2B1C2A3',
            'conditions': 'to_B2B1C2A3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1',
            'dest': 'B2B1A3',
            'conditions': 'to_B2B1A3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1A3',
            'dest': 'B2B1A3e',
            'conditions': 'to_B2B1A3e'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1A3',
            'dest': 'B2B1A3C2',
            'conditions': 'to_B2B1A3C2'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1',
            'dest': 'B2B1C3',
            'conditions': 'to_B2B1C3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1C3',
            'dest': 'B2B1C3e',
            'conditions': 'to_B2B1C3e'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B1C3',
            'dest': 'B2B1C3A3',
            'conditions': 'to_B2B1C3A3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2',
            'dest': 'B2C1',
            'conditions': 'to_B2C1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C1',
            'dest': 'B2C1x',
            'conditions': 'to_B2C1x'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C1',
            'dest': 'B2C1A2',
            'conditions': 'to_B2C1A2'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C1A2',
            'dest': 'B2C1A2B1',
            'conditions': 'to_B2C1A2B1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C1A2',
            'dest': 'B2C1A2B3',
            'conditions': 'to_B2C1A2B3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C1A2',
            'dest': 'B2C1A2C3',
            'conditions': 'to_B2C1A2C3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2',
            'dest': 'B2A2',
            'conditions': 'to_B2A2'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2',
            'dest': 'B2A2B1',
            'conditions': 'to_B2A2B1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2B1',
            'dest': 'B2A2B1C1',
            'conditions': 'to_B2A2B1C1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2B1',
            'dest': 'B2A2B1e',
            'conditions': 'to_B2A2B1e'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2',
            'dest': 'B2A2C1',
            'conditions': 'to_B2A2C1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2C1',
            'dest': 'B2A2C1e',
            'conditions': 'to_B2A2C1e'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2C1',
            'dest': 'B2A2C1B3',
            'conditions': 'to_B2A2C1B3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2',
            'dest': 'B2A2A3',
            'conditions': 'to_B2A2A3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2A3',
            'dest': 'B2A2A3x',
            'conditions': 'to_B2A2A3x'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2A3',
            'dest': 'B2A2A3C3',
            'conditions': 'to_B2A2A3C3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2',
            'dest': 'B2A2B3',
            'conditions': 'to_B2A2B3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2B3',
            'dest': 'B2A2B3x',
            'conditions': 'to_B2A2B3x'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2B3',
            'dest': 'B2A2B3C1',
            'conditions': 'to_B2A2B3C1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2',
            'dest': 'B2A2C3',
            'conditions': 'to_B2A2C3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2C3',
            'dest': 'B2A2C3e',
            'conditions': 'to_B2A2C3e'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A2C3',
            'dest': 'B2A2C3A3',
            'conditions': 'to_B2A2C3A3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2',
            'dest': 'B2C2',
            'conditions': 'to_B2C2'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C2',
            'dest': 'B2C2x',
            'conditions': 'to_B2C2x'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C2',
            'dest': 'B2C2A3',
            'conditions': 'to_B2C2A3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C2A3',
            'dest': 'B2C2A3x',
            'conditions': 'to_B2C2A3x'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C2A3',
            'dest': 'B2C2A3B1',
            'conditions': 'to_B2C2A3B1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2',
            'dest': 'B2A3',
            'conditions': 'to_B2A3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A3',
            'dest': 'B2A3x',
            'conditions': 'to_B2A3x'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A3',
            'dest': 'B2A3B1',
            'conditions': 'to_B2A3B1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A3B1',
            'dest': 'B2A3B1A2',
            'conditions': 'to_B2A3B1A2'
        },

        {
            'trigger': 'b_two',
            'source': 'B2A3B1',
            'dest': 'B2A3B1e',
            'conditions': 'to_B2A3B1e'
        },

        {
            'trigger': 'b_two',
            'source': 'B2',
            'dest': 'B2B3',
            'conditions': 'to_B2B3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B3',
            'dest': 'B2B3x',
            'conditions': 'to_B2B3x'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B3',
            'dest': 'B2B3C1',
            'conditions': 'to_B2B3C1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B3C1',
            'dest': 'B2B3C1x',
            'conditions': 'to_B2B3C1x'
        },

        {
            'trigger': 'b_two',
            'source': 'B2B3C1',
            'dest': 'B2B3C1A2',
            'conditions': 'to_B2B3C1A2'
        },

        {
            'trigger': 'b_two',
            'source': 'B2',
            'dest': 'B2C3',
            'conditions': 'to_B2C3'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C3',
            'dest': 'B2C3C1',
            'conditions': 'to_B2C3C1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C3C1',
            'dest': 'B2C3C1e',
            'conditions': 'to_B2C3C1e'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C3C1',
            'dest': 'B2C3C1A3',
            'conditions': 'to_B2C3C1A3'
        }
        {
            'trigger': 'b_two',
            'source': 'B2C3',
            'dest': 'B2C3x',
            'conditions': 'to_B2C3x'
        },

        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2', 
                'A1B1x',
                'A1B1A3x',
                'A1B1A3C2',
                'A1C1', 'A1C1x', 'A1C1B3', 'A1C1B3x', 'A1C1B3C2', 'A1A2', 'A1A2x', 'A1A2C1', 'A1A2C1x', 'A1A2C1B3', 'A1C2', 'A1C2x', 'A1C2B3', 'A1C2B3x', 'A1C2B3C1', 'A1A3', 'A1A3x', 'A1A3C2', 'A1A3C2x', 'A1A3C2B1', 'A1B3', 'A1B3x', 'A1B3C2', 'A1B3C2x', 'A1B3C2A3', 'A1C3', 'A1C3x', 'A1C3B3', 'A1C3B3x', 'A1C3B3C1', 'B1', 'B1C1', 'B1C1x', 'B1C1C3', 'B1C1C3x', 'B1C1C3A2', 'B1A2', 'B1A2x', 'B1A2C3', 'B1A2C3x', 'B1A2C3C1', 'B1B2', 'B1B2C1', 'B1B2C1x', 'B1B2C1C3', 'B1B2A2', 'B1B2A2A3', 'B1B2A2C1', 'B1B2A2C3', 'B1B2C2', 'B1B2C2x', 'B1B2C2A3', 'B1B2A3', 'B1B2A3A2', 'B1B2A3C2', 'B1B2A3C3', 'B1B2C3', 'B1B2C3C1', 'B1B2C3A2', 'B1B2C3A3', 'B1C2', 'B1C2x', 'B1C2C3', 'B1C2C3x', 'B1C2C3A3', 'B1A3', 'B1A3x', 'B1A3C3', 'B1A3C3C1', 'B1A3C3A2', 'B1B3', 'B1B3x', 'B1B3C3', 'B1B3C3C1', 'B1B3C3x', 'B1C3', 'B1C3C1', 'B1C3C1x', 'B1C3C1A2', 'B1C3A2', 'B1C3A2x', 'B1C3A2A3', 'B1C3C2', 'B1C3C2x', 'B1C3C2A3', 'B1C3A3', 'B1C3A3C1', 'B1C3A3A2', 'B1C3A3C2', 'B1C3B3', 'B1C3B3x', 'B1C3B3A2', 'B2', 'B2B1', 'B2B1C1', 'B2B1C1x', 'B2B1C1A2', 'B2B1A2', 'B2B1A2C1', 'B2B1A2A3', 'B2B1A2C3', 'B2B1C2', 'B2B1C2x', 'B2B1C2A3', 'B2B1A3', 'B2B1A3e', 'B2B1A3C2', 'B2B1C3', 'B2B1C3e', 'B2B1C3A3', 'B2C1', 'B2C1x', 'B2C1A2', 'B2C1A2B1', 'B2C1A2B3', 'B2C1A2C3', 'B2A2', 'B2A2B1', 'B2A2B1C1', 'B2A2B1e', 'B2A2C1', 'B2A2C1e', 'B2A2C1B3', 'B2A2A3', 'B2A2A3x', 'B2A2A3C3', 'B2A2B3', 'B2A2B3x', 'B2A2B3C1', 'B2A2C3', 'B2A2C3e', 'B2A2C3A3', 'B2C2', 'B2C2x', 'B2C2A3', 'B2C2A3x', 'B2C2A3B1', 'B2A3', 'B2A3x', 'B2A3B1', 'B2A3B1A2', 'B2A3B1e', 'B2B3', 'B2B3x', 'B2B3C1', 'B2B3C1x', 'B2B3C1A2',
                'B2C3', 'B2C3C1', 'B2C3C1e', 'B2C3x',
                'B2C3C1A3'
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
        if machine.state[0:2] == "A1":
            machine.a_one(event)
        elif machine.state[0:2] == "A2":
            machine.a_two(event)
        elif machine.state[0:2] == "A3":
            machine.a_three(event)
        elif machine.state[0:2] == "B1":
            machine.b_one(event)
        elif machine.state[0:2] == "B2":
            machine.b_two(event) 
        elif machine.state[0:2] == "B3":
            machine.b_three(event)
        elif machine.state[0:2] == "C1":
            machine.c_one(event)
        elif machine.state[0:2] == "C2":
            machine.c_two(event) 
        elif machine.state[0:2] == "C3":
            machine.c_three(event)
        else:
            machine.advance(event)
        #print("Ok")
        return 'OK'



@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    #run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
    run(host="localhost", port=5000, debug=True, reloader=True)
