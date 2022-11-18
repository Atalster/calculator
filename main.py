#current notes/to do list:
#work on addition system



#Variables
Operator = 1
Shaked = False
num1 = 0
#Functions
def on_multiplication_selected():
    basic.show_leds("""
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    """)


def on_division_selected():
    basic.show_leds("""
    . . # . .
    . . . . .
    # # # # #
    . . . . .
    . . # . .
    """)

def on_subtraction_selected():
    basic.show_leds("""
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    . . . . .
    """)

def on_addition_selected():
    basic.show_leds("""
    . . # . .
    . . # . .
    # # # # #
    . . # . .
    . . # . .
    """)
    def on_button_pressed_b():
        global num1
        basic.show_number(num1)
        def on_num1_decrease():
            global num1
            num1 -= 1
            basic.show_number(num1)


        input.on_button_pressed(Button.A, on_num1_decrease)

        def on_num1_increase():
            global num1
            num1 += 1
            basic.show_number(num1)
        input.on_button_pressed(Button.B, on_num1_increase)

    input.on_button_pressed(Button.B, on_button_pressed_b)

#Default Functions

def on_forever():
    pass
basic.forever(on_forever)

def on_gesture_shake():
    global Operator
    global Shaked
    Shaked = True
    
    #Make sure operator doesnt go above 4
    if Operator == 5:
        Operator = 1
    # checking which Operator is currently selected
    if Operator == 4:
       
        on_multiplication_selected()
        Operator += 1
    elif Operator == 3:
        
        on_division_selected()
        Operator += 1
    elif Operator == 2:
        
        on_subtraction_selected()
        Operator += 1
    elif Operator == 1:
       
        on_addition_selected()
        Operator += 1
 #Animations
for i in range(infinity):
    if Shaked:
        break
    input.on_gesture(Gesture.SHAKE, on_gesture_shake)
      
       
    #Addition Operator
    basic.show_leds("""
                . . # . .
                . . # . .
                # # # # #
                . . # . .
                . . # . .
                """)
    pause(100)
    basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        
     #Subtraction Operator
       
    basic.show_leds("""
                    . . . . .
                    . . . . .
                    # # # # #
                    . . . . .
                    . . . . .
                    """)
    pause(100)
    basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)

        #Division Operator
       
    basic.show_leds("""
                        . . # . .
                        . . . . .
                        # # # # #
                        . . . . .
                        . . # . .
                        """)
    pause(100)
    basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
      
    
    #Multiplication Operator
    basic.show_leds("""
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    """)
    pause(100)
    basic.show_leds("""
                            . . . . .
                            . . . . .
                            . . . . .
                            . . . . .
                            . . . . .
                            """)




