import pywhatkit as kit
from pytbangla import computer as cp
def text_to_hand(var):
    kit.text_to_handwriting(var, rgb=[0,0,0])

text_to_hand(cp.shuno())