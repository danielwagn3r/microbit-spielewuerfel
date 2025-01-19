zahl = 0

def on_gesture_shake():
    global zahl
    basic.clear_screen()
    zahl = randint(1, 6)
    if zahl == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif zahl == 2:
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . #
            . . . . .
            . . . . .
            """)
    elif zahl == 3:
        basic.show_leds("""
            . . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . .
            """)
    elif zahl == 4:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            """)
    elif zahl == 5:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
    else:
        basic.show_leds("""
            # . . . #
            . . . . .
            # . . . #
            . . . . .
            # . . . #
            """)
    basic.pause(2000)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
