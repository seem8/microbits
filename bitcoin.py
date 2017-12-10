from microbit import *
import random

#################################
#       INWESTOR BITCOINA       #
#################################

class Bitcoin():
    '''All Bitcoin in the world'''
    def __init__(self):
        '''init for Bitcoin'''
        self.val = 10   # in 1000$
        self.hype = 1   # between -10 and 10
        self.flunct = 0
    
    def value_flunct(self):
        '''changing value randomly,
        based on current hype'''
        roll = (-2, -1, 0, 1, 2)
        self.flunct = (self.val / 10) * self.hype + random.choice(roll)
        self.val += self.flunct
        if self.flunct > 0:
            display.show(Image.HAPPY)
        elif self.flunct == 0:
            display.show(Image.SLEEP)
        elif self.flunct < 0:
            display.show(Image.SAD)

bitcoin = Bitcoin()

while True:
    display.show('?')
    
    if button_a.is_pressed():
        if bitcoin.hype > -9:
            bitcoin.hype -= 1
            display.clear()
            display.show(str(bitcoin.hype))
            sleep(1000)
    
    elif button_b.is_pressed():
        if bitcoin.hype < 10:
            bitcoin.hype += 1
            display.clear()
            display.show(str(bitcoin.hype))
            sleep(1000)
    
    elif pin0.is_touched():
        display.scroll(str(bitcoin.val * 1000))

    elif pin1.is_touched():
        bitcoin.value_flunct()
        sleep(1000)
        
        

    sleep(5)
