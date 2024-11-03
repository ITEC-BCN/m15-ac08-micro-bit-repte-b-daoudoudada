def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.RINGTONE),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play(music.string_playable("C D E F G A B C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    music.change_tempo_by(20)
basic.forever(on_forever)
