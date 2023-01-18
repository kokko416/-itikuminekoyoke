def on_sound_loud():
    if input.button_is_pressed(Button.AB):
        pins.digital_write_pin(DigitalPin.P1, 1)
        pins.digital_write_pin(DigitalPin.P2, 0)
        basic.pause(5000)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.pause(5000)
    else:
        basic.pause(10000)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

pins.analog_write_pin(AnalogPin.P0, 1023)