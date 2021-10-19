from microbit import *
Dice = 0
def on_pin_pressed_p0():
    global Dice
    basic.show_number(6)
    basic.clear_screen()
    if input.button_is_pressed(Button.A):
        Dice = randint(1, 6)
        if Dice == 1:
            basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
        elif Dice == 2:
              basic.show_leds("""
            . . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . .
            """)
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
            basic.pause(100)
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
        elif Dice == 3:
              basic.show_leds("""
            # . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . #
            """)
            for index in range(3):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
        elif Dice == 4:
              basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """)
            for index2 in range(4):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
        elif Dice == 5:
              basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
            for index3 in range(5):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
        elif Dice == 6:
              basic.show_leds("""
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            """)
            for index4 in range(6):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p1():
    global Dice
    basic.show_number(10)
    basic.clear_screen()
    if input.button_is_pressed(Button.A):
        Dice = randint(1, 10)
        if Dice == 1:
            basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
        elif Dice == 2:
              basic.show_leds("""
            . . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . .
            """)
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
            basic.pause(100)
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
        elif Dice == 3:
              basic.show_leds("""
            # . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . #
            """)
            for index5 in range(3):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
        elif Dice == 4:
              basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """)
            for index6 in range(4):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
        elif Dice == 5:
              basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
            for index7 in range(5):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
        elif Dice == 6:
              basic.show_leds("""
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            """)
            for index8 in range(6):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
        elif Dice == 7:
              basic.show_leds("""
            # . . . #
            . . . . .
            # . # . #
            . . . . .
            # . . . #
            """)
            for index9 in range(7):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
        elif Dice == 8:
              basic.show_leds("""
            # . . . #
            . . # . .
            # . . . #
            . . # . .
            # . . . #
            """)
            for index10 in range(8):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
        elif Dice == 9:
              basic.show_leds("""
            # . # . #
            . . . . .
            # . # . #
            . . . . .
            # . # . #
            """)
            for index11 in range(9):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
        elif Dice == 10:
              basic.show_leds("""
            # . . . #
            . # . # .
            # . . . #
            . # . # .
            # . . . #
            """)
            for index12 in range(10):
                music.play.tone(262, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)