import gi
import uinput
import time
import os
os.environ['GDK_BACKEND'] = 'x11'

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

key_mapping = {uinput.KEY_ESC: "Esc", uinput.KEY_1: "1", uinput.KEY_2: "2", uinput.KEY_3: "3", uinput.KEY_4: "4", uinput.KEY_5: "5", uinput.KEY_6: "6",
    uinput.KEY_7: "7", uinput.KEY_8: "8", uinput.KEY_9: "9", uinput.KEY_0: "0", uinput.KEY_MINUS: "-", uinput.KEY_EQUAL: "=",
    uinput.KEY_BACKSPACE: "Backspace", uinput.KEY_TAB: "Tab", uinput.KEY_Q: "Q", uinput.KEY_W: "W", uinput.KEY_E: "E", uinput.KEY_R: "R",
    uinput.KEY_T: "T", uinput.KEY_Y: "Y", uinput.KEY_U: "U", uinput.KEY_I: "I", uinput.KEY_O: "O", uinput.KEY_P: "P",
    uinput.KEY_LEFTBRACE: "[", uinput.KEY_RIGHTBRACE: "]", uinput.KEY_ENTER: "Enter", uinput.KEY_LEFTCTRL: "Ctrl", uinput.KEY_A: "A",
    uinput.KEY_S: "S", uinput.KEY_D: "D", uinput.KEY_F: "F", uinput.KEY_G: "G", uinput.KEY_H: "H", uinput.KEY_J: "J", uinput.KEY_K: "K",
    uinput.KEY_L: "L", uinput.KEY_SEMICOLON: ";", uinput.KEY_APOSTROPHE: "'", uinput.KEY_GRAVE: "`", uinput.KEY_LEFTSHIFT: "Shift",
    uinput.KEY_BACKSLASH: "\\", uinput.KEY_Z: "Z", uinput.KEY_X: "X", uinput.KEY_C: "C", uinput.KEY_V: "V", uinput.KEY_B: "B",
    uinput.KEY_N: "N", uinput.KEY_M: "M", uinput.KEY_COMMA: ",", uinput.KEY_DOT: ".", uinput.KEY_SLASH: "/", uinput.KEY_RIGHTSHIFT: "Shift",
    uinput.KEY_KPENTER: "Enter", uinput.KEY_LEFTALT: "Alt", uinput.KEY_SPACE: "Space", uinput.KEY_CAPSLOCK: "CapsLock",
    uinput.KEY_F1: "F1", uinput.KEY_F2: "F2", uinput.KEY_F3: "F3", uinput.KEY_F4: "F4", uinput.KEY_F5: "F5", uinput.KEY_F6: "F6",
    uinput.KEY_F7: "F7", uinput.KEY_F8: "F8", uinput.KEY_F9: "F9", uinput.KEY_F10: "F10", uinput.KEY_F11: "F11", uinput.KEY_F12: "F12",
    uinput.KEY_SCROLLLOCK: "ScrollLock", uinput.KEY_PAUSE: "Pause", uinput.KEY_INSERT: "Insert", uinput.KEY_HOME: "Home",
    uinput.KEY_PAGEUP: "PageUp", uinput.KEY_DELETE: "Delete", uinput.KEY_END: "End", uinput.KEY_PAGEDOWN: "PageDown",
    uinput.KEY_RIGHT: "→", uinput.KEY_LEFT: "←", uinput.KEY_DOWN: "↓", uinput.KEY_UP: "↑", uinput.KEY_NUMLOCK: "NumLock",
    uinput.KEY_RIGHTCTRL: "Ctrl"}

class VirtualKeyboard(Gtk.Window):
    def __init__(self):
        super().__init__(title="Virtual Keyboard")
        self.set_border_width(10)
        self.set_resizable(True)
        self.set_keep_above(True)
        self.set_modal(False)
        self.set_focus_on_map(False)
        self.set_can_focus(False)
        self.set_accept_focus(False)
        self.same_mod = False
        self.Last_event = ''

        grid = Gtk.Grid()  # Use Grid for layout
        grid.set_row_homogeneous(True)  # Allow rows to resize based on content
        grid.set_column_homogeneous(True)  # Columns are homogeneous

        self.add(grid)

        self.device = uinput.Device(list(key_mapping.keys()))

        # Define rows for keys
        rows = [
            ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "Backspace" ],
            ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"],
            ["CapsLock", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "Enter"],
            ["Shift", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "Shift", "↑"],
            ["Ctrl", "Alt", "Space", "Alt", "Ctrl", "←", "→", "↓"]
        ]

        # Create each row and add it to the grid
        for row_index, keys in enumerate(rows):
            self.create_row(grid, row_index, keys)


    def create_row(self, grid, row_index, keys):
        col = 0  # Start from the first column
        width=0
        shift_bool=False

        for key_label in keys:
            key_event = next((key for key, label in key_mapping.items() if label == key_label), None)
            if key_event:
                button = Gtk.Button(label=key_label)
                button.connect("clicked", self.on_button_click, key_event)

              # if key_label == "Tab": width=3
                if key_label == "Space": width=14
                #elif key_label == "CapsLock": width=4
                elif key_label == "Shift" and shift_bool: width=4
                elif key_label == "Enter": width=4
                else: width=2

                grid.attach(button, col, row_index, width, 1)
                col += width  # Skip 4 columns for the space button
                if key_label == "Shift": shift_bool=True

    def on_button_click(self, widget, key_event):
        if (key_event == self.Last_event):
            self.same_mod = True
        # For Shift, Ctrl, and Alt, only simulate the key press
        if any(modifier in widget.get_label() for modifier in ["Shift", "Ctrl", "Alt"]) and not self.same_mod:
            self.device.emit(key_event, 1)  # Key press (1)
            self.Last_event = key_event
            print(self.Last_event)
        else:
            self.device.emit(key_event, 1)  # Key press (1)
            time.sleep(0.1)
            self.device.emit(key_event, 0)  # Key release (0)
            # Unpress Shift, Ctrl, and Alt after a normal key press
            self.device.emit(uinput.KEY_LEFTSHIFT, 0)  # Release Left Shift
            self.device.emit(uinput.KEY_RIGHTSHIFT, 0)  # Release Right Shift
            self.device.emit(uinput.KEY_LEFTCTRL, 0)   # Release Left Ctrl
            self.device.emit(uinput.KEY_RIGHTCTRL, 0)  # Release Right Ctrl
            self.device.emit(uinput.KEY_LEFTALT, 0)    # Release Left Alt
            self.device.emit(uinput.KEY_RIGHTALT, 0)   # Release Right Alt
            self.same_mod = False
            self.Last_event = ''

if __name__ == "__main__":
    win = VirtualKeyboard()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
