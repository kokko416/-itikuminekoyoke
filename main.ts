input.onSound(DetectedSound.Loud, function () {
    if (input.buttonIsPressed(Button.AB)) {
        pins.digitalWritePin(DigitalPin.P1, 1)
        pins.digitalWritePin(DigitalPin.P2, 0)
        basic.pause(5000)
        pins.digitalWritePin(DigitalPin.P1, 0)
        pins.digitalWritePin(DigitalPin.P2, 1)
        basic.pause(5000)
    } else {
        basic.pause(10000)
    }
})
pins.analogWritePin(AnalogPin.P0, 1023)
