from bottle import route, run, request, abort, static_file
import image_pb2
from fsm import TocMachine
import os
import sys
from utils import send_image_url 
from utils import send_text_message

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
        'B1', 'B1C1', 'B1C1x', 'B1C1C3', 'B1C1C3x', 'B1C1C3A2', 'B1A2', 'B1A2x', 'B1A2C3', 'B1A2C3x', 'B1A2C3C1', 'B1B2', 'B1B2C1', 'B1B2C1x', 'B1B2C1C3', 'B1B2A2', 'B1B2A2A3', 'B1B2A2C1', 'B1B2A2C3', 'B1B2C2', 'B1B2C2x', 'B1B2C2A3', 'B1B2A3', 'B1B2A3A2', 'B1B2A3C2', 'B1B2A3C3', 'B1B2C3', 'B1B2C3C1', 'B1B2C3A2', 'B1B2C3A3', 'B1C2', 'B1C2x', 'B1C2C3', 'B1C2C3x', 'B1C2C3A3', 'B1A3', 'B1A3x', 'B1A3C3', 'B1A3C3C1', 'B1A3C3A2', 'B1B3', 'B1B3x', 'B1B3C3', 'B1B3C3C1', 'B1B3C3x', 'B1C3', 'B1C3C1', 'B1C3C1x', 'B1C3C1A2', 'B1C3A2', 'B1C3A2x', 'B1C3A2A3', 'B1C3C2', 'B1C3C2x', 'B1C3C2A3', 'B1C3A3', 'B1C3A3C1', 'B1C3A3A2', 'B1C3A3C2', 'B1C3B3', 'B1C3B3x', 'B1C3B3A2', 
        'B2', 'B2B1', 'B2B1C1', 'B2B1C1x', 'B2B1C1A2', 'B2B1A2', 'B2B1A2C1', 'B2B1A2A3', 'B2B1A2C3', 'B2B1C2', 'B2B1C2x', 'B2B1C2A3', 'B2B1A3', 'B2B1A3e', 'B2B1A3C2', 'B2B1C3', 'B2B1C3e', 'B2B1C3A3', 'B2C1', 'B2C1x', 'B2C1A2', 'B2C1A2B1', 'B2C1A2B3', 'B2C1A2C3', 'B2A2', 'B2A2B1', 'B2A2B1C1', 'B2A2B1e', 'B2A2C1', 'B2A2C1e', 'B2A2C1B3', 'B2A2A3', 'B2A2A3x', 'B2A2A3C3', 'B2A2B3', 'B2A2B3x', 'B2A2B3C1', 'B2A2C3', 'B2A2C3e', 'B2A2C3A3', 'B2C2', 'B2C2x', 'B2C2A3', 'B2C2A3x', 'B2C2A3B1', 'B2A3', 'B2A3x', 'B2A3B1', 'B2A3B1A2', 'B2A3B1e', 'B2B3', 'B2B3x', 'B2B3C1', 'B2B3C1x', 'B2B3C1A2',
        'B2C3', 'B2C3B1', 'B2C3B1A2', 'B2C3B1e', 'B2C3x',
        'C1', 'C1C2', 'C1C2x', 'C1C2A1', 'C1C2A1x', 'C1C2A1B3', 'C1C3', 'C1C3x', 'C1C3A2', 'C1C3A2x', 'C1C3A2B3', 'C1B1', 'C1B1x', 'C1B1C3', 'C1B1C3x', 'C1B1C3A2', 'C1B3', 'C1B3x', 'C1B3A2', 'C1B3A2x', 'C1B3A2C3', 'C1A1', 'C1A1x', 'C1A1B3', 'C1A1B3x', 'C1A1B3C2', 'C1A2', 'C1A2x', 'C1A2B3', 'C1A2B3x', 'C1A2B3A1', 'C1A3', 'C1A3x', 'C1A3A2', 'C1A3A2x', 'C1A3A2C3', 
        'C2', 'C2C3', 'C2C3x', 'C2C3A3', 'C2C3A3x', 'C2C3A3B1', 'C2B1', 'C2B1x', 'C2B1A3', 'C2B1A3x', 'C2B1A3C3', 'C2B2', 'C2B2C3', 'C2B2C3x', 'C2B2C3A3', 'C2B2B1', 'C2B2B1A1', 'C2B2B1C3', 'C2B2B1A3', 'C2B2B3', 'C2B2B3x', 'C2B2B3A1', 'C2B2A1', 'C2B2A1B1', 'C2B2A1B3', 'C2B2A1A3', 'C2B2A3', 'C2B2A3C3', 'C2B2A3B1', 'C2B2A3A1', 'C2B3', 'C2B3x', 'C2B3A3', 'C2B3A3x', 'C2B3A3A1', 'C2A1', 'C2A1x', 'C2A1A3', 'C2A1A3C3', 'C2A1A3B1', 'C2A2', 'C2A2x', 'C2A2A3', 'C2A2A3C3', 'C2A2A3x', 'C2A3', 'C2A3C3', 'C2A3C3x', 'C2A3C3B1', 'C2A3B1', 'C2A3B1x', 'C2A3B1A1', 'C2A3B3', 'C2A3B3x', 'C2A3B3A1', 'C2A3A1', 'C2A3A1C3', 'C2A3A1B1', 'C2A3A1B3', 'C2A3A2', 'C2A3A2x', 'C2A3A2B1',
        'C3', 'C3B3', 'C3B3x', 'C3B3C1', 'C3B3C1x', 'C3B3C1A2', 'C3A3', 'C3A3x', 'C3A3B1', 'C3A3B1x', 'C3A3B1A2', 'C3C2', 'C3C2x', 'C3C2A3', 'C3C2A3x', 'C3C2A3B1', 'C3A2', 'C3A2x', 'C3A2B1', 'C3A2B1x', 'C3A2B1A3', 'C3C1', 'C3C1x', 'C3C1A2', 'C3C1A2x', 'C3C1A2B3', 'C3B1', 'C3B1x', 'C3B1A2', 'C3B1A2x', 'C3B1A2C1', 'C3A1', 'C3A1x', 'C3A1B1', 'C3A1B1x', 'C3A1B1A3',
        'B3', 'B3A3', 'B3A3x', 'B3A3A1', 'B3A3A1x', 'B3A3A1C2', 'B3C2', 'B3C2x', 'B3C2A1', 'B3C2A1x', 'B3C2A1A3', 'B3B2', 'B3B2A3', 'B3B2A3x', 'B3B2A3A1', 'B3B2C2', 'B3B2C2C1', 'B3B2C2A3', 'B3B2C2A1', 'B3B2A2', 'B3B2A2x', 'B3B2A2C1', 'B3B2C1', 'B3B2C1C2', 'B3B2C1A2', 'B3B2C1A1', 'B3B2A1', 'B3B2A1A3', 'B3B2A1C2', 'B3B2A1C1', 'B3A2', 'B3A2x', 'B3A2A1', 'B3A2A1x', 'B3A2A1C1', 'B3C1', 'B3C1x', 'B3C1A1', 'B3C1A1A3', 'B3C1A1C2', 'B3B1', 'B3B1x', 'B3B1A1', 'B3B1A1A3', 'B3B1A1x', 'B3A1', 'B3A1A3', 'B3A1A3x', 'B3A1A3C2', 'B3A1C2', 'B3A1C2x', 'B3A1C2C1', 'B3A1A2', 'B3A1A2x', 'B3A1A2C1', 'B3A1C1', 'B3A1C1A3', 'B3A1C1C2', 'B3A1C1A2', 'B3A1B1', 'B3A1B1x', 'B3A1B1C2', 
        'A3', 'A3A2', 'A3A2x', 'A3A2C3', 'A3A2C3x', 'A3A2C3B1', 'A3A1', 'A3A1x', 'A3A1C2', 'A3A1C2x', 'A3A1C2B1', 'A3B3', 'A3B3x', 'A3B3A1', 'A3B3A1x', 'A3B3A1C2', 'A3B1', 'A3B1x', 'A3B1C2', 'A3B1C2x', 'A3B1C2A1', 'A3C3', 'A3C3x', 'A3C3B1', 'A3C3B1x', 'A3C3B1A2', 'A3C2', 'A3C2x', 'A3C2B1', 'A3C2B1x', 'A3C2B1C3', 'A3C1', 'A3C1x', 'A3C1C2', 'A3C1C2x', 'A3C1C2A1',
        'A2', 'A2A1', 'A2A1x', 'A2A1C1', 'A2A1C1x', 'A2A1C1B3', 'A2B3', 'A2B3x', 'A2B3C1', 'A2B3C1x', 'A2B3C1A1', 'A2B2', 'A2B2A1', 'A2B2A1x', 'A2B2A1C1', 'A2B2B3', 'A2B2B3C3', 'A2B2B3A1', 'A2B2B3C1', 'A2B2B1', 'A2B2B1x', 'A2B2B1C3', 'A2B2C3', 'A2B2C3B3', 'A2B2C3B1', 'A2B2C3C1', 'A2B2C1', 'A2B2C1A1', 'A2B2C1B3', 'A2B2C1C3', 'A2B1', 'A2B1x', 'A2B1C1', 'A2B1C1x','A2B1C1C3', 'A2C3', 'A2C3x', 'A2C3C1', 'A2C3C1A1', 'A2C3C1B3', 'A2C2', 'A2C2x', 'A2C2C1', 'A2C2C1A1', 'A2C2C1x', 'A2C1', 'A2C1A1', 'A2C1A1x', 'A2C1A1B3', 'A2C1B3', 'A2C1B3x', 'A2C1B3C3', 'A2C1B1', 'A2C1B1x', 'A2C1B1C3', 'A2C1C3', 'A2C1C3A1', 'A2C1C3B3', 'A2C1C3B1', 'A2C1C2', 'A2C1C2x', 'A2C1C2B3' 
 
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
            'dest': 'B2C3B1',
            'conditions': 'to_B2C3B1'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C3B1',
            'dest': 'B2C3B1A2',
            'conditions': 'to_B2C3B1A2'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C3B1',
            'dest': 'B2C3B1e',
            'conditions': 'to_B2C3B1e'
        },

        {
            'trigger': 'b_two',
            'source': 'B2C3',
            'dest': 'B2C3x',
            'conditions': 'to_B2C3x'
        },



        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'C1',
            'conditions': 'to_C1'
        },

        {
            'trigger': 'c_one',
            'source': 'C1',
            'dest': 'C1C2',
            'conditions': 'to_C1C2'
        },

        {
            'trigger': 'c_one',
            'source': 'C1C2',
            'dest': 'C1C2x',
            'conditions': 'to_C1C2x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1C2',
            'dest': 'C1C2A1',
            'conditions': 'to_C1C2A1'
        },

        {
            'trigger': 'c_one',
            'source': 'C1C2A1',
            'dest': 'C1C2A1x',
            'conditions': 'to_C1C2A1x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1C2A1',
            'dest': 'C1C2A1B3',
            'conditions': 'to_C1C2A1B3'
        },

        {
            'trigger': 'c_one',
            'source': 'C1',
            'dest': 'C1C3',
            'conditions': 'to_C1C3'
        },

        {
            'trigger': 'c_one',
            'source': 'C1C3',
            'dest': 'C1C3x',
            'conditions': 'to_C1C3x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1C3',
            'dest': 'C1C3A2',
            'conditions': 'to_C1C3A2'
        },

        {
            'trigger': 'c_one',
            'source': 'C1C3A2',
            'dest': 'C1C3A2x',
            'conditions': 'to_C1C3A2x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1C3A2',
            'dest': 'C1C3A2B3',
            'conditions': 'to_C1C3A2B3'
        },

        {
            'trigger': 'c_one',
            'source': 'C1',
            'dest': 'C1B1',
            'conditions': 'to_C1B1'
        },

        {
            'trigger': 'c_one',
            'source': 'C1B1',
            'dest': 'C1B1x',
            'conditions': 'to_C1B1x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1B1',
            'dest': 'C1B1C3',
            'conditions': 'to_C1B1C3'
        },

        {
            'trigger': 'c_one',
            'source': 'C1B1C3',
            'dest': 'C1B1C3x',
            'conditions': 'to_C1B1C3x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1B1C3',
            'dest': 'C1B1C3A2',
            'conditions': 'to_C1B1C3A2'
        },

        {
            'trigger': 'c_one',
            'source': 'C1',
            'dest': 'C1B3',
            'conditions': 'to_C1B3'
        },

        {
            'trigger': 'c_one',
            'source': 'C1B3',
            'dest': 'C1B3x',
            'conditions': 'to_C1B3x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1B3',
            'dest': 'C1B3A2',
            'conditions': 'to_C1B3A2'
        },

        {
            'trigger': 'c_one',
            'source': 'C1B3A2',
            'dest': 'C1B3A2x',
            'conditions': 'to_C1B3A2x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1B3A2',
            'dest': 'C1B3A2C3',
            'conditions': 'to_C1B3A2C3'
        },

        {
            'trigger': 'c_one',
            'source': 'C1',
            'dest': 'C1A1',
            'conditions': 'to_C1A1'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A1',
            'dest': 'C1A1x',
            'conditions': 'to_C1A1x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A1',
            'dest': 'C1A1B3',
            'conditions': 'to_C1A1B3'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A1B3',
            'dest': 'C1A1B3x',
            'conditions': 'to_C1A1B3x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A1B3',
            'dest': 'C1A1B3C2',
            'conditions': 'to_C1A1B3C2'
        },

        {
            'trigger': 'c_one',
            'source': 'C1',
            'dest': 'C1A2',
            'conditions': 'to_C1A2'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A2',
            'dest': 'C1A2x',
            'conditions': 'to_C1A2x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A2',
            'dest': 'C1A2B3',
            'conditions': 'to_C1A2B3'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A2B3',
            'dest': 'C1A2B3x',
            'conditions': 'to_C1A2B3x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A2B3',
            'dest': 'C1A2B3A1',
            'conditions': 'to_C1A2B3A1'
        },

        {
            'trigger': 'c_one',
            'source': 'C1',
            'dest': 'C1A3',
            'conditions': 'to_C1A3'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A3',
            'dest': 'C1A3x',
            'conditions': 'to_C1A3x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A3',
            'dest': 'C1A3A2',
            'conditions': 'to_C1A3A2'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A3A2',
            'dest': 'C1A3A2x',
            'conditions': 'to_C1A3A2x'
        },

        {
            'trigger': 'c_one',
            'source': 'C1A3A2',
            'dest': 'C1A3A2C3',
            'conditions': 'to_C1A3A2C3'
        },

        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'C2',
            'conditions': 'to_C2'
        },

        {
            'trigger': 'c_two',
            'source': 'C2',
            'dest': 'C2C3',
            'conditions': 'to_C2C3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2C3',
            'dest': 'C2C3x',
            'conditions': 'to_C2C3x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2C3',
            'dest': 'C2C3A3',
            'conditions': 'to_C2C3A3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2C3A3',
            'dest': 'C2C3A3x',
            'conditions': 'to_C2C3A3x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2C3A3',
            'dest': 'C2C3A3B1',
            'conditions': 'to_C2C3A3B1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2',
            'dest': 'C2B1',
            'conditions': 'to_C2B1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B1',
            'dest': 'C2B1x',
            'conditions': 'to_C2B1x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B1',
            'dest': 'C2B1A3',
            'conditions': 'to_C2B1A3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B1A3',
            'dest': 'C2B1A3x',
            'conditions': 'to_C2B1A3x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B1A3',
            'dest': 'C2B1A3C3',
            'conditions': 'to_C2B1A3C3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2',
            'dest': 'C2B2',
            'conditions': 'to_C2B2'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2',
            'dest': 'C2B2C3',
            'conditions': 'to_C2B2C3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2C3',
            'dest': 'C2B2C3x',
            'conditions': 'to_C2B2C3x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2C3',
            'dest': 'C2B2C3A3',
            'conditions': 'to_C2B2C3A3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2',
            'dest': 'C2B2B1',
            'conditions': 'to_C2B2B1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2B1',
            'dest': 'C2B2B1A1',
            'conditions': 'to_C2B2B1A1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2B1',
            'dest': 'C2B2B1C3',
            'conditions': 'to_C2B2B1C3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2B1',
            'dest': 'C2B2B1A3',
            'conditions': 'to_C2B2B1A3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2',
            'dest': 'C2B2B3',
            'conditions': 'to_C2B2B3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2B3',
            'dest': 'C2B2B3x',
            'conditions': 'to_C2B2B3x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2B3',
            'dest': 'C2B2B3A1',
            'conditions': 'to_C2B2B3A1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2',
            'dest': 'C2B2A1',
            'conditions': 'to_C2B2A1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2A1',
            'dest': 'C2B2A1B1',
            'conditions': 'to_C2B2A1B1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2A1',
            'dest': 'C2B2A1B3',
            'conditions': 'to_C2B2A1B3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2A1',
            'dest': 'C2B2A1A3',
            'conditions': 'to_C2B2A1A3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2',
            'dest': 'C2B2A3',
            'conditions': 'to_C2B2A3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2A3',
            'dest': 'C2B2A3C3',
            'conditions': 'to_C2B2A3C3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2A3',
            'dest': 'C2B2A3B1',
            'conditions': 'to_C2B2A3B1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B2A3',
            'dest': 'C2B2A3A1',
            'conditions': 'to_C2B2A3A1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2',
            'dest': 'C2B3',
            'conditions': 'to_C2B3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B3',
            'dest': 'C2B3x',
            'conditions': 'to_C2B3x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B3',
            'dest': 'C2B3A3',
            'conditions': 'to_C2B3A3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B3A3',
            'dest': 'C2B3A3x',
            'conditions': 'to_C2B3A3x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2B3A3',
            'dest': 'C2B3A3A1',
            'conditions': 'to_C2B3A3A1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2',
            'dest': 'C2A1',
            'conditions': 'to_C2A1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A1',
            'dest': 'C2A1x',
            'conditions': 'to_C2A1x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A1',
            'dest': 'C2A1A3',
            'conditions': 'to_C2A1A3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A1A3',
            'dest': 'C2A1A3C3',
            'conditions': 'to_C2A1A3C3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A1A3',
            'dest': 'C2A1A3B1',
            'conditions': 'to_C2A1A3B1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2',
            'dest': 'C2A2',
            'conditions': 'to_C2A2'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A2',
            'dest': 'C2A2x',
            'conditions': 'to_C2A2x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A2',
            'dest': 'C2A2A3',
            'conditions': 'to_C2A2A3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A2A3',
            'dest': 'C2A2A3C3',
            'conditions': 'to_C2A2A3C3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A2A3',
            'dest': 'C2A2A3x',
            'conditions': 'to_C2A2A3x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2',
            'dest': 'C2A3',
            'conditions': 'to_C2A3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3',
            'dest': 'C2A3C3',
            'conditions': 'to_C2A3C3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3C3',
            'dest': 'C2A3C3x',
            'conditions': 'to_C2A3C3x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3C3',
            'dest': 'C2A3C3B1',
            'conditions': 'to_C2A3C3B1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3',
            'dest': 'C2A3B1',
            'conditions': 'to_C2A3B1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3B1',
            'dest': 'C2A3B1x',
            'conditions': 'to_C2A3B1x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3B1',
            'dest': 'C2A3B1A1',
            'conditions': 'to_C2A3B1A1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3',
            'dest': 'C2A3B3',
            'conditions': 'to_C2A3B3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3B3',
            'dest': 'C2A3B3x',
            'conditions': 'to_C2A3B3x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3B3',
            'dest': 'C2A3B3A1',
            'conditions': 'to_C2A3B3A1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3',
            'dest': 'C2A3A1',
            'conditions': 'to_C2A3A1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3A1',
            'dest': 'C2A3A1C3',
            'conditions': 'to_C2A3A1C3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3A1',
            'dest': 'C2A3A1B1',
            'conditions': 'to_C2A3A1B1'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3A1',
            'dest': 'C2A3A1B3',
            'conditions': 'to_C2A3A1B3'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3',
            'dest': 'C2A3A2',
            'conditions': 'to_C2A3A2'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3A2',
            'dest': 'C2A3A2x',
            'conditions': 'to_C2A3A2x'
        },

        {
            'trigger': 'c_two',
            'source': 'C2A3A2',
            'dest': 'C2A3A2B1',
            'conditions': 'to_C2A3A2B1'
        },



        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'C3',
            'conditions': 'to_C3'
        },

        {
            'trigger': 'c_three',
            'source': 'C3',
            'dest': 'C3B3',
            'conditions': 'to_C3B3'
        },

        {
            'trigger': 'c_three',
            'source': 'C3B3',
            'dest': 'C3B3x',
            'conditions': 'to_C3B3x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3B3',
            'dest': 'C3B3C1',
            'conditions': 'to_C3B3C1'
        },

        {
            'trigger': 'c_three',
            'source': 'C3B3C1',
            'dest': 'C3B3C1x',
            'conditions': 'to_C3B3C1x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3B3C1',
            'dest': 'C3B3C1A2',
            'conditions': 'to_C3B3C1A2'
        },

        {
            'trigger': 'c_three',
            'source': 'C3',
            'dest': 'C3A3',
            'conditions': 'to_C3A3'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A3',
            'dest': 'C3A3x',
            'conditions': 'to_C3A3x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A3',
            'dest': 'C3A3B1',
            'conditions': 'to_C3A3B1'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A3B1',
            'dest': 'C3A3B1x',
            'conditions': 'to_C3A3B1x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A3B1',
            'dest': 'C3A3B1A2',
            'conditions': 'to_C3A3B1A2'
        },

        {
            'trigger': 'c_three',
            'source': 'C3',
            'dest': 'C3C2',
            'conditions': 'to_C3C2'
        },

        {
            'trigger': 'c_three',
            'source': 'C3C2',
            'dest': 'C3C2x',
            'conditions': 'to_C3C2x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3C2',
            'dest': 'C3C2A3',
            'conditions': 'to_C3C2A3'
        },

        {
            'trigger': 'c_three',
            'source': 'C3C2A3',
            'dest': 'C3C2A3x',
            'conditions': 'to_C3C2A3x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3C2A3',
            'dest': 'C3C2A3B1',
            'conditions': 'to_C3C2A3B1'
        },

        {
            'trigger': 'c_three',
            'source': 'C3',
            'dest': 'C3A2',
            'conditions': 'to_C3A2'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A2',
            'dest': 'C3A2x',
            'conditions': 'to_C3A2x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A2',
            'dest': 'C3A2B1',
            'conditions': 'to_C3A2B1'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A2B1',
            'dest': 'C3A2B1x',
            'conditions': 'to_C3A2B1x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A2B1',
            'dest': 'C3A2B1A3',
            'conditions': 'to_C3A2B1A3'
        },

        {
            'trigger': 'c_three',
            'source': 'C3',
            'dest': 'C3C1',
            'conditions': 'to_C3C1'
        },

        {
            'trigger': 'c_three',
            'source': 'C3C1',
            'dest': 'C3C1x',
            'conditions': 'to_C3C1x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3C1',
            'dest': 'C3C1A2',
            'conditions': 'to_C3C1A2'
        },

        {
            'trigger': 'c_three',
            'source': 'C3C1A2',
            'dest': 'C3C1A2x',
            'conditions': 'to_C3C1A2x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3C1A2',
            'dest': 'C3C1A2B3',
            'conditions': 'to_C3C1A2B3'
        },

        {
            'trigger': 'c_three',
            'source': 'C3',
            'dest': 'C3B1',
            'conditions': 'to_C3B1'
        },

        {
            'trigger': 'c_three',
            'source': 'C3B1',
            'dest': 'C3B1x',
            'conditions': 'to_C3B1x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3B1',
            'dest': 'C3B1A2',
            'conditions': 'to_C3B1A2'
        },

        {
            'trigger': 'c_three',
            'source': 'C3B1A2',
            'dest': 'C3B1A2x',
            'conditions': 'to_C3B1A2x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3B1A2',
            'dest': 'C3B1A2C1',
            'conditions': 'to_C3B1A2C1'
        },

        {
            'trigger': 'c_three',
            'source': 'C3',
            'dest': 'C3A1',
            'conditions': 'to_C3A1'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A1',
            'dest': 'C3A1x',
            'conditions': 'to_C3A1x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A1',
            'dest': 'C3A1B1',
            'conditions': 'to_C3A1B1'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A1B1',
            'dest': 'C3A1B1x',
            'conditions': 'to_C3A1B1x'
        },

        {
            'trigger': 'c_three',
            'source': 'C3A1B1',
            'dest': 'C3A1B1A3',
            'conditions': 'to_C3A1B1A3'
        },

        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'B3',
            'conditions': 'to_B3'
        },

        {
            'trigger': 'b_three',
            'source': 'B3',
            'dest': 'B3A3',
            'conditions': 'to_B3A3'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A3',
            'dest': 'B3A3x',
            'conditions': 'to_B3A3x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A3',
            'dest': 'B3A3A1',
            'conditions': 'to_B3A3A1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A3A1',
            'dest': 'B3A3A1x',
            'conditions': 'to_B3A3A1x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A3A1',
            'dest': 'B3A3A1C2',
            'conditions': 'to_B3A3A1C2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3',
            'dest': 'B3C2',
            'conditions': 'to_B3C2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3C2',
            'dest': 'B3C2x',
            'conditions': 'to_B3C2x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3C2',
            'dest': 'B3C2A1',
            'conditions': 'to_B3C2A1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3C2A1',
            'dest': 'B3C2A1x',
            'conditions': 'to_B3C2A1x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3C2A1',
            'dest': 'B3C2A1A3',
            'conditions': 'to_B3C2A1A3'
        },

        {
            'trigger': 'b_three',
            'source': 'B3',
            'dest': 'B3B2',
            'conditions': 'to_B3B2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2',
            'dest': 'B3B2A3',
            'conditions': 'to_B3B2A3'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2A3',
            'dest': 'B3B2A3x',
            'conditions': 'to_B3B2A3x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2A3',
            'dest': 'B3B2A3A1',
            'conditions': 'to_B3B2A3A1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2',
            'dest': 'B3B2C2',
            'conditions': 'to_B3B2C2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2C2',
            'dest': 'B3B2C2C1',
            'conditions': 'to_B3B2C2C1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2C2',
            'dest': 'B3B2C2A3',
            'conditions': 'to_B3B2C2A3'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2C2',
            'dest': 'B3B2C2A1',
            'conditions': 'to_B3B2C2A1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2',
            'dest': 'B3B2A2',
            'conditions': 'to_B3B2A2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2A2',
            'dest': 'B3B2A2x',
            'conditions': 'to_B3B2A2x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2A2',
            'dest': 'B3B2A2C1',
            'conditions': 'to_B3B2A2C1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2',
            'dest': 'B3B2C1',
            'conditions': 'to_B3B2C1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2C1',
            'dest': 'B3B2C1C2',
            'conditions': 'to_B3B2C1C2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2C1',
            'dest': 'B3B2C1A2',
            'conditions': 'to_B3B2C1A2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2C1',
            'dest': 'B3B2C1A1',
            'conditions': 'to_B3B2C1A1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2',
            'dest': 'B3B2A1',
            'conditions': 'to_B3B2A1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2A1',
            'dest': 'B3B2A1A3',
            'conditions': 'to_B3B2A1A3'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2A1',
            'dest': 'B3B2A1C2',
            'conditions': 'to_B3B2A1C2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B2A1',
            'dest': 'B3B2A1C1',
            'conditions': 'to_B3B2A1C1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3',
            'dest': 'B3A2',
            'conditions': 'to_B3A2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A2',
            'dest': 'B3A2x',
            'conditions': 'to_B3A2x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A2',
            'dest': 'B3A2A1',
            'conditions': 'to_B3A2A1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A2A1',
            'dest': 'B3A2A1x',
            'conditions': 'to_B3A2A1x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A2A1',
            'dest': 'B3A2A1C1',
            'conditions': 'to_B3A2A1C1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3',
            'dest': 'B3C1',
            'conditions': 'to_B3C1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3C1',
            'dest': 'B3C1x',
            'conditions': 'to_B3C1x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3C1',
            'dest': 'B3C1A1',
            'conditions': 'to_B3C1A1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3C1A1',
            'dest': 'B3C1A1A3',
            'conditions': 'to_B3C1A1A3'
        },

        {
            'trigger': 'b_three',
            'source': 'B3C1A1',
            'dest': 'B3C1A1C2',
            'conditions': 'to_B3C1A1C2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3',
            'dest': 'B3B1',
            'conditions': 'to_B3B1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B1',
            'dest': 'B3B1x',
            'conditions': 'to_B3B1x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B1',
            'dest': 'B3B1A1',
            'conditions': 'to_B3B1A1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B1A1',
            'dest': 'B3B1A1A3',
            'conditions': 'to_B3B1A1A3'
        },

        {
            'trigger': 'b_three',
            'source': 'B3B1A1',
            'dest': 'B3B1A1x',
            'conditions': 'to_B3B1A1x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3',
            'dest': 'B3A1',
            'conditions': 'to_B3A1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1',
            'dest': 'B3A1A3',
            'conditions': 'to_B3A1A3'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1A3',
            'dest': 'B3A1A3x',
            'conditions': 'to_B3A1A3x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1A3',
            'dest': 'B3A1A3C2',
            'conditions': 'to_B3A1A3C2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1',
            'dest': 'B3A1C2',
            'conditions': 'to_B3A1C2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1C2',
            'dest': 'B3A1C2x',
            'conditions': 'to_B3A1C2x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1C2',
            'dest': 'B3A1C2C1',
            'conditions': 'to_B3A1C2C1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1',
            'dest': 'B3A1A2',
            'conditions': 'to_B3A1A2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1A2',
            'dest': 'B3A1A2x',
            'conditions': 'to_B3A1A2x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1A2',
            'dest': 'B3A1A2C1',
            'conditions': 'to_B3A1A2C1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1',
            'dest': 'B3A1C1',
            'conditions': 'to_B3A1C1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1C1',
            'dest': 'B3A1C1A3',
            'conditions': 'to_B3A1C1A3'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1C1',
            'dest': 'B3A1C1C2',
            'conditions': 'to_B3A1C1C2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1C1',
            'dest': 'B3A1C1A2',
            'conditions': 'to_B3A1C1A2'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1',
            'dest': 'B3A1B1',
            'conditions': 'to_B3A1B1'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1B1',
            'dest': 'B3A1B1x',
            'conditions': 'to_B3A1B1x'
        },

        {
            'trigger': 'b_three',
            'source': 'B3A1B1',
            'dest': 'B3A1B1C2',
            'conditions': 'to_B3A1B1C2'
        },



        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'A3',
            'conditions': 'to_A3'
        },

        {
            'trigger': 'a_three',
            'source': 'A3',
            'dest': 'A3A2',
            'conditions': 'to_A3A2'
        },

        {
            'trigger': 'a_three',
            'source': 'A3A2',
            'dest': 'A3A2x',
            'conditions': 'to_A3A2x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3A2',
            'dest': 'A3A2C3',
            'conditions': 'to_A3A2C3'
        },

        {
            'trigger': 'a_three',
            'source': 'A3A2C3',
            'dest': 'A3A2C3x',
            'conditions': 'to_A3A2C3x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3A2C3',
            'dest': 'A3A2C3B1',
            'conditions': 'to_A3A2C3B1'
        },

        {
            'trigger': 'a_three',
            'source': 'A3',
            'dest': 'A3A1',
            'conditions': 'to_A3A1'
        },

        {
            'trigger': 'a_three',
            'source': 'A3A1',
            'dest': 'A3A1x',
            'conditions': 'to_A3A1x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3A1',
            'dest': 'A3A1C2',
            'conditions': 'to_A3A1C2'
        },

        {
            'trigger': 'a_three',
            'source': 'A3A1C2',
            'dest': 'A3A1C2x',
            'conditions': 'to_A3A1C2x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3A1C2',
            'dest': 'A3A1C2B1',
            'conditions': 'to_A3A1C2B1'
        },

        {
            'trigger': 'a_three',
            'source': 'A3',
            'dest': 'A3B3',
            'conditions': 'to_A3B3'
        },

        {
            'trigger': 'a_three',
            'source': 'A3B3',
            'dest': 'A3B3x',
            'conditions': 'to_A3B3x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3B3',
            'dest': 'A3B3A1',
            'conditions': 'to_A3B3A1'
        },

        {
            'trigger': 'a_three',
            'source': 'A3B3A1',
            'dest': 'A3B3A1x',
            'conditions': 'to_A3B3A1x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3B3A1',
            'dest': 'A3B3A1C2',
            'conditions': 'to_A3B3A1C2'
        },

        {
            'trigger': 'a_three',
            'source': 'A3',
            'dest': 'A3B1',
            'conditions': 'to_A3B1'
        },

        {
            'trigger': 'a_three',
            'source': 'A3B1',
            'dest': 'A3B1x',
            'conditions': 'to_A3B1x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3B1',
            'dest': 'A3B1C2',
            'conditions': 'to_A3B1C2'
        },

        {
            'trigger': 'a_three',
            'source': 'A3B1C2',
            'dest': 'A3B1C2x',
            'conditions': 'to_A3B1C2x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3B1C2',
            'dest': 'A3B1C2A1',
            'conditions': 'to_A3B1C2A1'
        },

        {
            'trigger': 'a_three',
            'source': 'A3',
            'dest': 'A3C3',
            'conditions': 'to_A3C3'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C3',
            'dest': 'A3C3x',
            'conditions': 'to_A3C3x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C3',
            'dest': 'A3C3B1',
            'conditions': 'to_A3C3B1'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C3B1',
            'dest': 'A3C3B1x',
            'conditions': 'to_A3C3B1x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C3B1',
            'dest': 'A3C3B1A2',
            'conditions': 'to_A3C3B1A2'
        },

        {
            'trigger': 'a_three',
            'source': 'A3',
            'dest': 'A3C2',
            'conditions': 'to_A3C2'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C2',
            'dest': 'A3C2x',
            'conditions': 'to_A3C2x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C2',
            'dest': 'A3C2B1',
            'conditions': 'to_A3C2B1'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C2B1',
            'dest': 'A3C2B1x',
            'conditions': 'to_A3C2B1x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C2B1',
            'dest': 'A3C2B1C3',
            'conditions': 'to_A3C2B1C3'
        },

        {
            'trigger': 'a_three',
            'source': 'A3',
            'dest': 'A3C1',
            'conditions': 'to_A3C1'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C1',
            'dest': 'A3C1x',
            'conditions': 'to_A3C1x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C1',
            'dest': 'A3C1C2',
            'conditions': 'to_A3C1C2'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C1C2',
            'dest': 'A3C1C2x',
            'conditions': 'to_A3C1C2x'
        },

        {
            'trigger': 'a_three',
            'source': 'A3C1C2',
            'dest': 'A3C1C2A1',
            'conditions': 'to_A3C1C2A1'
        },

        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'A2',
            'conditions': 'to_A2'
        },

        {
            'trigger': 'a_two',
            'source': 'A2',
            'dest': 'A2A1',
            'conditions': 'to_A2A1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2A1',
            'dest': 'A2A1x',
            'conditions': 'to_A2A1x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2A1',
            'dest': 'A2A1C1',
            'conditions': 'to_A2A1C1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2A1C1',
            'dest': 'A2A1C1x',
            'conditions': 'to_A2A1C1x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2A1C1',
            'dest': 'A2A1C1B3',
            'conditions': 'to_A2A1C1B3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2',
            'dest': 'A2B3',
            'conditions': 'to_A2B3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B3',
            'dest': 'A2B3x',
            'conditions': 'to_A2B3x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B3',
            'dest': 'A2B3C1',
            'conditions': 'to_A2B3C1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B3C1',
            'dest': 'A2B3C1x',
            'conditions': 'to_A2B3C1x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B3C1',
            'dest': 'A2B3C1A1',
            'conditions': 'to_A2B3C1A1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2',
            'dest': 'A2B2',
            'conditions': 'to_A2B2'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2',
            'dest': 'A2B2A1',
            'conditions': 'to_A2B2A1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2A1',
            'dest': 'A2B2A1x',
            'conditions': 'to_A2B2A1x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2A1',
            'dest': 'A2B2A1C1',
            'conditions': 'to_A2B2A1C1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2',
            'dest': 'A2B2B3',
            'conditions': 'to_A2B2B3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2B3',
            'dest': 'A2B2B3C3',
            'conditions': 'to_A2B2B3C3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2B3',
            'dest': 'A2B2B3A1',
            'conditions': 'to_A2B2B3A1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2B3',
            'dest': 'A2B2B3C1',
            'conditions': 'to_A2B2B3C1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2',
            'dest': 'A2B2B1',
            'conditions': 'to_A2B2B1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2B1',
            'dest': 'A2B2B1x',
            'conditions': 'to_A2B2B1x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2B1',
            'dest': 'A2B2B1C3',
            'conditions': 'to_A2B2B1C3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2',
            'dest': 'A2B2C3',
            'conditions': 'to_A2B2C3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2C3',
            'dest': 'A2B2C3B3',
            'conditions': 'to_A2B2C3B3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2C3',
            'dest': 'A2B2C3B1',
            'conditions': 'to_A2B2C3B1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2C3',
            'dest': 'A2B2C3C1',
            'conditions': 'to_A2B2C3C1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2',
            'dest': 'A2B2C1',
            'conditions': 'to_A2B2C1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2C1',
            'dest': 'A2B2C1A1',
            'conditions': 'to_A2B2C1A1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2C1',
            'dest': 'A2B2C1B3',
            'conditions': 'to_A2B2C1B3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B2C1',
            'dest': 'A2B2C1C3',
            'conditions': 'to_A2B2C1C3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2',
            'dest': 'A2B1',
            'conditions': 'to_A2B1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B1',
            'dest': 'A2B1x',
            'conditions': 'to_A2B1x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B1',
            'dest': 'A2B1C1',
            'conditions': 'to_A2B1C1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B1C1',
            'dest': 'A2B1C1x',
            'conditions': 'to_A2B1C1x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2B1C1',
            'dest': 'A2B1C1C3',
            'conditions': 'to_A2B1C1C3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2',
            'dest': 'A2C3',
            'conditions': 'to_A2C3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C3',
            'dest': 'A2C3x',
            'conditions': 'to_A2C3x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C3',
            'dest': 'A2C3C1',
            'conditions': 'to_A2C3C1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C3C1',
            'dest': 'A2C3C1A1',
            'conditions': 'to_A2C3C1A1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C3C1',
            'dest': 'A2C3C1B3',
            'conditions': 'to_A2C3C1B3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2',
            'dest': 'A2C2',
            'conditions': 'to_A2C2'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C2',
            'dest': 'A2C2x',
            'conditions': 'to_A2C2x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C2',
            'dest': 'A2C2C1',
            'conditions': 'to_A2C2C1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C2C1',
            'dest': 'A2C2C1A1',
            'conditions': 'to_A2C2C1A1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C2C1',
            'dest': 'A2C2C1x',
            'conditions': 'to_A2C2C1x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2',
            'dest': 'A2C1',
            'conditions': 'to_A2C1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1',
            'dest': 'A2C1A1',
            'conditions': 'to_A2C1A1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1A1',
            'dest': 'A2C1A1x',
            'conditions': 'to_A2C1A1x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1A1',
            'dest': 'A2C1A1B3',
            'conditions': 'to_A2C1A1B3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1',
            'dest': 'A2C1B3',
            'conditions': 'to_A2C1B3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1B3',
            'dest': 'A2C1B3x',
            'conditions': 'to_A2C1B3x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1B3',
            'dest': 'A2C1B3C3',
            'conditions': 'to_A2C1B3C3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1',
            'dest': 'A2C1B1',
            'conditions': 'to_A2C1B1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1B1',
            'dest': 'A2C1B1x',
            'conditions': 'to_A2C1B1x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1B1',
            'dest': 'A2C1B1C3',
            'conditions': 'to_A2C1B1C3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1',
            'dest': 'A2C1C3',
            'conditions': 'to_A2C1C3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1C3',
            'dest': 'A2C1C3A1',
            'conditions': 'to_A2C1C3A1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1C3',
            'dest': 'A2C1C3B3',
            'conditions': 'to_A2C1C3B3'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1C3',
            'dest': 'A2C1C3B1',
            'conditions': 'to_A2C1C3B1'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1',
            'dest': 'A2C1C2',
            'conditions': 'to_A2C1C2'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1C2',
            'dest': 'A2C1C2x',
            'conditions': 'to_A2C1C2x'
        },

        {
            'trigger': 'a_two',
            'source': 'A2C1C2',
            'dest': 'A2C1C2B3',
            'conditions': 'to_A2C1C2B3'
        },



 



        {
            'trigger': 'go_back',
            'source': [
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
                'B1', 'B1C1', 'B1C1x', 'B1C1C3', 'B1C1C3x', 'B1C1C3A2', 'B1A2', 'B1A2x', 'B1A2C3', 'B1A2C3x', 'B1A2C3C1', 'B1B2', 'B1B2C1', 'B1B2C1x', 'B1B2C1C3', 'B1B2A2', 'B1B2A2A3', 'B1B2A2C1', 'B1B2A2C3', 'B1B2C2', 'B1B2C2x', 'B1B2C2A3', 'B1B2A3', 'B1B2A3A2', 'B1B2A3C2', 'B1B2A3C3', 'B1B2C3', 'B1B2C3C1', 'B1B2C3A2', 'B1B2C3A3', 'B1C2', 'B1C2x', 'B1C2C3', 'B1C2C3x', 'B1C2C3A3', 'B1A3', 'B1A3x', 'B1A3C3', 'B1A3C3C1', 'B1A3C3A2', 'B1B3', 'B1B3x', 'B1B3C3', 'B1B3C3C1', 'B1B3C3x', 'B1C3', 'B1C3C1', 'B1C3C1x', 'B1C3C1A2', 'B1C3A2', 'B1C3A2x', 'B1C3A2A3', 'B1C3C2', 'B1C3C2x', 'B1C3C2A3', 'B1C3A3', 'B1C3A3C1', 'B1C3A3A2', 'B1C3A3C2', 'B1C3B3', 'B1C3B3x', 'B1C3B3A2', 
                'B2', 'B2B1', 'B2B1C1', 'B2B1C1x', 'B2B1C1A2', 'B2B1A2', 'B2B1A2C1', 'B2B1A2A3', 'B2B1A2C3', 'B2B1C2', 'B2B1C2x', 'B2B1C2A3', 'B2B1A3', 'B2B1A3e', 'B2B1A3C2', 'B2B1C3', 'B2B1C3e', 'B2B1C3A3', 'B2C1', 'B2C1x', 'B2C1A2', 'B2C1A2B1', 'B2C1A2B3', 'B2C1A2C3', 'B2A2', 'B2A2B1', 'B2A2B1C1', 'B2A2B1e', 'B2A2C1', 'B2A2C1e', 'B2A2C1B3', 'B2A2A3', 'B2A2A3x', 'B2A2A3C3', 'B2A2B3', 'B2A2B3x', 'B2A2B3C1', 'B2A2C3', 'B2A2C3e', 'B2A2C3A3', 'B2C2', 'B2C2x', 'B2C2A3', 'B2C2A3x', 'B2C2A3B1', 'B2A3', 'B2A3x', 'B2A3B1', 'B2A3B1A2', 'B2A3B1e', 'B2B3', 'B2B3x', 'B2B3C1', 'B2B3C1x', 'B2B3C1A2',
                'B2C3', 'B2C3B1', 'B2C3B1A2', 'B2C3B1e', 'B2C3x',
                'C1', 'C1C2', 'C1C2x', 'C1C2A1', 'C1C2A1x', 'C1C2A1B3', 'C1C3', 'C1C3x', 'C1C3A2', 'C1C3A2x', 'C1C3A2B3', 'C1B1', 'C1B1x', 'C1B1C3', 'C1B1C3x', 'C1B1C3A2', 'C1B3', 'C1B3x', 'C1B3A2', 'C1B3A2x', 'C1B3A2C3', 'C1A1', 'C1A1x', 'C1A1B3', 'C1A1B3x', 'C1A1B3C2', 'C1A2', 'C1A2x', 'C1A2B3', 'C1A2B3x', 'C1A2B3A1', 'C1A3', 'C1A3x', 'C1A3A2', 'C1A3A2x', 'C1A3A2C3', 
                'C2', 'C2C3', 'C2C3x', 'C2C3A3', 'C2C3A3x', 'C2C3A3B1', 'C2B1', 'C2B1x', 'C2B1A3', 'C2B1A3x', 'C2B1A3C3', 'C2B2', 'C2B2C3', 'C2B2C3x', 'C2B2C3A3', 'C2B2B1', 'C2B2B1A1', 'C2B2B1C3', 'C2B2B1A3', 'C2B2B3', 'C2B2B3x', 'C2B2B3A1', 'C2B2A1', 'C2B2A1B1', 'C2B2A1B3', 'C2B2A1A3', 'C2B2A3', 'C2B2A3C3', 'C2B2A3B1', 'C2B2A3A1', 'C2B3', 'C2B3x', 'C2B3A3', 'C2B3A3x', 'C2B3A3A1', 'C2A1', 'C2A1x', 'C2A1A3', 'C2A1A3C3', 'C2A1A3B1', 'C2A2', 'C2A2x', 'C2A2A3', 'C2A2A3C3', 'C2A2A3x', 'C2A3', 'C2A3C3', 'C2A3C3x', 'C2A3C3B1', 'C2A3B1', 'C2A3B1x', 'C2A3B1A1', 'C2A3B3', 'C2A3B3x', 'C2A3B3A1', 'C2A3A1', 'C2A3A1C3', 'C2A3A1B1', 'C2A3A1B3', 'C2A3A2', 'C2A3A2x', 'C2A3A2B1',
                'C3', 'C3B3', 'C3B3x', 'C3B3C1', 'C3B3C1x', 'C3B3C1A2', 'C3A3', 'C3A3x', 'C3A3B1', 'C3A3B1x', 'C3A3B1A2', 'C3C2', 'C3C2x', 'C3C2A3', 'C3C2A3x', 'C3C2A3B1', 'C3A2', 'C3A2x', 'C3A2B1', 'C3A2B1x', 'C3A2B1A3', 'C3C1', 'C3C1x', 'C3C1A2', 'C3C1A2x', 'C3C1A2B3', 'C3B1', 'C3B1x', 'C3B1A2', 'C3B1A2x', 'C3B1A2C1', 'C3A1', 'C3A1x', 'C3A1B1', 'C3A1B1x', 'C3A1B1A3',
                'B3', 'B3A3', 'B3A3x', 'B3A3A1', 'B3A3A1x', 'B3A3A1C2', 'B3C2', 'B3C2x', 'B3C2A1', 'B3C2A1x', 'B3C2A1A3', 'B3B2', 'B3B2A3', 'B3B2A3x', 'B3B2A3A1', 'B3B2C2', 'B3B2C2C1', 'B3B2C2A3', 'B3B2C2A1', 'B3B2A2', 'B3B2A2x', 'B3B2A2C1', 'B3B2C1', 'B3B2C1C2', 'B3B2C1A2', 'B3B2C1A1', 'B3B2A1', 'B3B2A1A3', 'B3B2A1C2', 'B3B2A1C1', 'B3A2', 'B3A2x', 'B3A2A1', 'B3A2A1x', 'B3A2A1C1', 'B3C1', 'B3C1x', 'B3C1A1', 'B3C1A1A3', 'B3C1A1C2', 'B3B1', 'B3B1x', 'B3B1A1', 'B3B1A1A3', 'B3B1A1x', 'B3A1', 'B3A1A3', 'B3A1A3x', 'B3A1A3C2', 'B3A1C2', 'B3A1C2x', 'B3A1C2C1', 'B3A1A2', 'B3A1A2x', 'B3A1A2C1', 'B3A1C1', 'B3A1C1A3', 'B3A1C1C2', 'B3A1C1A2', 'B3A1B1', 'B3A1B1x', 'B3A1B1C2', 
                'A3', 'A3A2', 'A3A2x', 'A3A2C3', 'A3A2C3x', 'A3A2C3B1', 'A3A1', 'A3A1x', 'A3A1C2', 'A3A1C2x', 'A3A1C2B1', 'A3B3', 'A3B3x', 'A3B3A1', 'A3B3A1x', 'A3B3A1C2', 'A3B1', 'A3B1x', 'A3B1C2', 'A3B1C2x', 'A3B1C2A1', 'A3C3', 'A3C3x', 'A3C3B1', 'A3C3B1x', 'A3C3B1A2', 'A3C2', 'A3C2x', 'A3C2B1', 'A3C2B1x', 'A3C2B1C3', 'A3C1', 'A3C1x', 'A3C1C2', 'A3C1C2x', 'A3C1C2A1',
                'A2', 'A2A1', 'A2A1x', 'A2A1C1', 'A2A1C1x', 'A2A1C1B3', 'A2B3', 'A2B3x', 'A2B3C1', 'A2B3C1x', 'A2B3C1A1', 'A2B2', 'A2B2A1', 'A2B2A1x', 'A2B2A1C1', 'A2B2B3', 'A2B2B3C3', 'A2B2B3A1', 'A2B2B3C1', 'A2B2B1', 'A2B2B1x', 'A2B2B1C3', 'A2B2C3', 'A2B2C3B3', 'A2B2C3B1', 'A2B2C3C1', 'A2B2C1', 'A2B2C1A1', 'A2B2C1B3', 'A2B2C1C3', 'A2B1', 'A2B1x', 'A2B1C1', 'A2B1C1x','A2B1C1C3', 'A2C3', 'A2C3x', 'A2C3C1', 'A2C3C1A1', 'A2C3C1B3', 'A2C2', 'A2C2x', 'A2C2C1', 'A2C2C1A1', 'A2C2C1x', 'A2C1', 'A2C1A1', 'A2C1A1x', 'A2C1A1B3', 'A2C1B3', 'A2C1B3x', 'A2C1B3C3', 'A2C1B1', 'A2C1B1x', 'A2C1B1C3', 'A2C1C3', 'A2C1C3A1', 'A2C1C3B3', 'A2C1C3B1', 'A2C1C2', 'A2C1C2x', 'A2C1C2B3', 
 
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
        if event.get('message') and event['message'].get('text') and event['message']['text'] == "init":
            machine.go_back()
            send_image_url(event['sender']['id'], "https://i.imgur.com/T0Qd8Va.png")
        elif event.get('message') and event['message'].get('text'):
            if event['message']['text'] != "A1" or event['message']['text'] != "A2" or event['message']['text'] != "A3" or event['message']['text'] != "B1" or event['message']['text'] != "B2" or event['message']['text'] != "B3" or event['message']['text'] != "C1" or event['message']['text'] != "C2" or event['message']['text'] != "C3" or event['message']['text'] != "init":
                send_text_message(event['sender']['id'], "輸入由A~C 1~3 組成的字符")
                send_text_message(event['sender']['id'], "ex: B2")
                send_text_message(event['sender']['id'], "或是依照以下圖片來輸入字符")
                send_image_url(event['sender']['id'], "https://i.imgur.com/T0Qd8Va.png")




                   # https://i.imgur.com/5XlsDjU.png")

        if event.get('message') and event['message'].get('text'):
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



#@route('/show-fsm', methods=['GET'])
#def show_fsm():
#    machine.get_graph().draw('fsm.png', prog='dot', format='png')
#    return static_file('fsm.png', root='./', mimetype='image/png')

@route('/imgur-record', methods=['GET'])
def imgur():
    my_all_image = image_pb2.all_image()
    with open("image.pb", "rb") as f:
        my_all_image.ParseFromString(f.read())
    out = "<pre>" + "   name             url"
    for image in my_all_image.image:
        out = out + "\n" + image.name + " " + image.url
    out = out + "</pre>"

    return out

if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
    #run(host="localhost", port=5000, debug=True, reloader=True)
