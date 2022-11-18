// current notes/to do list:
// work on addition system
// Variables
let Operator = 1
let Shaked = false
let num1 = 0
// Functions
function on_multiplication_selected() {
    basic.showLeds(`
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    `)
}

function on_division_selected() {
    basic.showLeds(`
    . . # . .
    . . . . .
    # # # # #
    . . . . .
    . . # . .
    `)
}

function on_subtraction_selected() {
    basic.showLeds(`
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    . . . . .
    `)
}

function on_addition_selected() {
    basic.showLeds(`
    . . # . .
    . . # . .
    # # # # #
    . . # . .
    . . # . .
    `)
    input.onButtonPressed(Button.B, function on_button_pressed_b() {
        
        basic.showNumber(num1)
        input.onButtonPressed(Button.A, function on_num1_decrease() {
            
            num1 -= 1
            basic.showNumber(num1)
        })
        input.onButtonPressed(Button.B, function on_num1_increase() {
            
            num1 += 1
            basic.showNumber(num1)
        })
    })
}

// Default Functions
basic.forever(function on_forever() {
    
})
// Animations
for (let i = 0; i < Infinity; i++) {
    if (Shaked) {
        break
    }
    
    input.onGesture(Gesture.Shake, function on_gesture_shake() {
        
        
        Shaked = true
        // Make sure operator doesnt go above 4
        if (Operator == 5) {
            Operator = 1
        }
        
        //  checking which Operator is currently selected
        if (Operator == 4) {
            on_multiplication_selected()
            Operator += 1
        } else if (Operator == 3) {
            on_division_selected()
            Operator += 1
        } else if (Operator == 2) {
            on_subtraction_selected()
            Operator += 1
        } else if (Operator == 1) {
            on_addition_selected()
            Operator += 1
        }
        
    })
    // Addition Operator
    basic.showLeds(`
                . . # . .
                . . # . .
                # # # # #
                . . # . .
                . . # . .
                `)
    pause(100)
    basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    // Subtraction Operator
    basic.showLeds(`
                    . . . . .
                    . . . . .
                    # # # # #
                    . . . . .
                    . . . . .
                    `)
    pause(100)
    basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
    // Division Operator
    basic.showLeds(`
                        . . # . .
                        . . . . .
                        # # # # #
                        . . . . .
                        . . # . .
                        `)
    pause(100)
    basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
    // Multiplication Operator
    basic.showLeds(`
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    `)
    pause(100)
    basic.showLeds(`
                            . . . . .
                            . . . . .
                            . . . . .
                            . . . . .
                            . . . . .
                            `)
}
