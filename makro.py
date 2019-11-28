import mouse
import pyautogui
import win32api
import keyboard

horizontal_range = 2
min_vertical = 1
max_vertical = 2
min_firerate = 0.01
max_firerate = 0.03

print("Açma Kapama Tuşunu Seç") #select your open/close button
tuş = input("")
toggle_button = tuş

enabled = False


def is_mouse_down():
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0


print("Macro Çalıştırıldı") #macro running
if enabled:
    print("Açık") #open
else:
    print("Kapalı") #close

last_state = False
while True:
    key_down = keyboard.is_pressed(toggle_button)
    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("Açık") #open
            else:
                print("Kapalı") #close

    if is_mouse_down() and enabled:
        mouse.move(-4.40, 8.40, absolute=False, duration=0.129)
        if is_mouse_down() and enabled:
            mouse.move(-12.40, 24.00, absolute=False, duration=0.129)
            if is_mouse_down() and enabled:
                mouse.move(-15.20, 20.00, absolute=False, duration=0.129)
                if is_mouse_down() and enabled:
                    mouse.move(-14.40, 20.00, absolute=False, duration=0.129)
                    if is_mouse_down() and enabled:
                        mouse.move(-13.60, 17.60, absolute=False, duration=0.129)
                        if is_mouse_down() and enabled:
                            mouse.move(0.00, 15.60, absolute=False, duration=0.129)
                            if is_mouse_down() and enabled:
                                mouse.move(8.80, 12.40, absolute=False, duration=0.129)
                                if is_mouse_down() and enabled:
                                    mouse.move(13.20, 12.00, absolute=False, duration=0.129)
                                    if is_mouse_down() and enabled:
                                        mouse.move(20.00, 8.00, absolute=False, duration=0.129)
                                        if is_mouse_down() and enabled:
                                            mouse.move(20.00, 6.40, absolute=False, duration=0.129)
                                            if is_mouse_down() and enabled:
                                                mouse.move(19.20, 6.00, absolute=False, duration=0.129)
                                                if is_mouse_down() and enabled:
                                                    mouse.move(16.80, 7.20, absolute=False, duration=0.129)
                                                    if is_mouse_down() and enabled:
                                                        mouse.move(14.00, 8.80, absolute=False, duration=0.129)
                                                        if is_mouse_down() and enabled:
                                                            mouse.move(8.40, 13.60, absolute=False, duration=0.129)
                                                            if is_mouse_down() and enabled:
                                                                mouse.move(-4.00, 15.20, absolute=False, duration=0.129)
                                                                if is_mouse_down() and enabled:
                                                                    mouse.move(-6.00, 16.00, absolute=False,
                                                                               duration=0.129)
                                                                    if is_mouse_down() and enabled:
                                                                        mouse.move(-11.20, 15.20, absolute=False,
                                                                                   duration=0.129)
                                                                        if is_mouse_down() and enabled:
                                                                            mouse.move(-19.20, 15.20, absolute=False,
                                                                                       duration=0.129)
                                                                            if is_mouse_down() and enabled:
                                                                                mouse.move(-18.80, 13.20,
                                                                                           absolute=False,
                                                                                           duration=0.129)
                                                                                if is_mouse_down() and enabled:
                                                                                    mouse.move(-21.20, 10.00,
                                                                                               absolute=False,
                                                                                               duration=0.129)
                                                                                    if is_mouse_down() and enabled:
                                                                                        mouse.move(-20.00, 9.20,
                                                                                                   absolute=False,
                                                                                                   duration=0.129)
                                                                                        if is_mouse_down() and enabled:
                                                                                            mouse.move(-19.20, 4.00,
                                                                                                       absolute=False,
                                                                                                       duration=0.129)
                                                                                            if is_mouse_down() and enabled:
                                                                                                mouse.move(-16.00, 5.60,
                                                                                                           absolute=False,
                                                                                                           duration=0.129)
                                                                                                if is_mouse_down() and enabled:
                                                                                                    mouse.move(-11.20,
                                                                                                               8.00,
                                                                                                               absolute=False,
                                                                                                               duration=0.129)
                                                                                                    if is_mouse_down() and enabled:
                                                                                                        mouse.move(
                                                                                                            -4.00, 8.00,
                                                                                                            absolute=False,
                                                                                                            duration=0.129)
                                                                                                        if is_mouse_down() and enabled:
                                                                                                            mouse.move(
                                                                                                                4.00,
                                                                                                                10.00,
                                                                                                                absolute=False,
                                                                                                                duration=0.129)
                                                                                                            if is_mouse_down() and enabled:
                                                                                                                mouse.move(
                                                                                                                    17.60,
                                                                                                                    16.00,
                                                                                                                    absolute=False,
                                                                                                                    duration=0.129)
                                                                                                                if is_mouse_down() and enabled:
                                                                                                                    mouse.move(
                                                                                                                        20.00,
                                                                                                                        12.80,
                                                                                                                        absolute=False,
                                                                                                                        duration=0.129)
                                                                                                                    if is_mouse_down() and enabled:
                                                                                                                        mouse.move(
                                                                                                                            22.00,
                                                                                                                            14.80,
                                                                                                                            absolute=False,
                                                                                                                            duration=0.129)
                                                                                                                        if is_mouse_down() and enabled:
                                                                                                                            mouse.move(
                                                                                                                                26.00,
                                                                                                                                16.00,
                                                                                                                                absolute=False,
                                                                                                                                duration=0.129)


