from microbit import *
import random

# ----------------------------- #
#    Skaney is Tamagochi toy    #
#     for a Microbit board.     #
# ----------------------------- #

class Snakey:
    '''bunny killer'''
    def __init__(self):
        '''init for Snakey'''
        self.happy = 9      # happiness in scale:
                            # 0 = death
                            # 10 is super happy
        self.stuffed = 5    # amount of food in the stomach:
                            # 0 = happy=-1
                            # 5 = happy+=1
                            # 10 = happy=-1 
        self.dead = False   # better to be sure
        self.health = 5     # health in scale
                            # 0 = death
                            # 10 is super happy
        self.petted = 1     # it's boring after awhile

    
    def feed(self):
        '''add food to stomach'''
        if self.stuffed <= 9:
            # we're good
            self.stuffed += 1
        elif self.stuffed > 9:
            # overstuffed
            self.health -= 1
            if self.happy > 0:
                self.happy -= 1
            # and we're sad
            if self.petted > 0:
                self.petted -= 1

    
    def heal(self):
        '''improve health'''
        if self.health <= 9:
            # we're good
            self.health += 1
        elif self.health > 9:
            # too much health is bad for heatlh
            if self.happy > 0:
                self.happy -= 1
            # and we're sad
            if self.petted > 0:
                self.petted -= 1

    
    def pet(self):
        '''adding happiness'''
        if self.petted <= 3:
            # good snakey
            self.petted += 1
            if self.happy <= 9:
                self.happy += 1            
        elif self.petted > 3:
            # you already told me this 4 times
            if self.happy > 0:
                self.happy -= 1
    
    
    def play(self):
        '''random silly things'''
        roll = random.randint(0,9)
        if roll > 0:
            # Bark!
            if self.happy <= 9:
                self.happy =+ 1
            return True
        elif roll == 0:
            # Play dead!
            self.happy = 0
            self.dead = True
            return False
    
    
    def wait(self):
        '''adjusting happiness and random stat changes'''
        # adjusting happiness

        if self.stuffed < 1 or self.stuffed > 9:
            if self.happy > 0:
                self.happy -= 1
        
        if self.health < 1 or self.health > 9:
           if self.happy > 0:
               self.happy -= 1

        if self.petted < 1 or self.petted > 3:
            if self.happy > 0:
                self.happy -= 1
        
        # random stat changes
        # self.stats[random.randint(0,3)] -= 1
        roll = (0, 0, 0, 1)
        self.happy -= random.choice(roll)
        self.stuffed -= random.choice(roll)
        self.health -= random.choice(roll)
        self.petted -= random.choice(roll)
        

snakey = Snakey()
# -------------------------------------

# start of the game
display.scroll(' Hi ! ')


# ---------------
# main magic loop
# ---------------

while snakey.dead == False:
    # ----------------------
    # user interface section
    # ----------------------
    
    
    # heal
    if button_a.is_pressed():
        snakey.heal()
        if snakey.health <= 9:
            display.show(Image.HAPPY)
            sleep(1)
        if snakey.health > 9:
            display.scroll('Ouch ! ')
    
    # feed
    elif button_b.is_pressed():
        snakey.feed()
        if snakey.stuffed <= 9:
            display.show(Image.HAPPY)
            sleep(1)
        if snakey.stuffed > 9:
            display.scroll('Burp ! ')

    # pet
    elif pin0.is_touched():
        snakey.pet()
        if snakey.petted <= 3:
            display.show(Image.HEART)
            sleep(1)
        elif snakey.petted > 3:
            display.scroll('meh ... ')
    
    # play
    elif pin1.is_touched():
        if snakey.play() == True:
            display.scroll('Bark ! ')
            display.show(Image.SILLY)
            sleep(1)
        elif snakey.play() == False:
            display.scroll('Play  dead ! ')
    
    else:
        display.show(Image.SNAKE)
    
    sleep(500)
    snakey.wait()
    
    if snakey.happy < 1:
        snakey.dead == True
        display.scroll(' unhappy ')
        display.show(Image.SKULL)
        sleep(97654321)
    
    if snakey.health < 1:
        snakey.dead == True
        display.scroll(' sick ')
        display.show(Image.SKULL)
        sleep(97654321)
    
# game over
