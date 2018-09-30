from i3_helpers import I3
from settings import has_launcher
import i3ipc


class Quake(object):
    def __init__(self, class_name, launcher_name):
        self.i3 = i3ipc.Connection()
        self.class_name = class_name
        self.app_name = launcher_name
        self.con = self.is_app_running()
        if (self.con):
            self.toggle_app()
        else:
            self.start_new_instance()

    def is_app_running(self):
        for con in I3().marked_list(self.i3):
            if con.window_class == self.class_name:
                return con
        return None

    def toggle_app(self):
        current_wp = I3().current_wp(self.i3)
        con_wp = self.con.workspace()

        if I3().current_wp(self.i3).id == con_wp.id:
            self.con.command('move workspace -1')
            self.con.command(f'sticky disable')
        else:
            self.con.command(f'move workspace {current_wp.name}')
            self.con.command(f'sticky enable')
            self.set_geometry()

    def start_new_instance(self):
        timeout = 10 if self.app_name in [i.lower() for i in has_launcher] else 2
        self.i3.on('window::new', quake_app)
        self.i3.command(f'exec {self.app_name}')
        self.i3.main(timeout=timeout)
        exit(0)

    def set_geometry(self):
        self.con.command(self.resize())
        self.con.command(self.move_top())

    def resize(self):
        current_wp = I3().current_wp(self.i3)
        self.width = int(current_wp.rect.width)
        self.height = int(current_wp.rect.height / 2.5)
        return f'resize set {self.width} {self.height}'

    def move_top(self):
        current_wp = I3().current_wp(self.i3)
        height_to_move = int(current_wp.rect.height / 2 - self.height / 2)
        return f"move position center, move up {height_to_move}"


def quake_app(self, event):
    rect = self.get_tree().find_focused().workspace().rect
    width = int(rect.width + 2)
    height = int(rect.height / 2.5)
    height_to_move = int(rect.height / 2 - height / 2)
    con = event.container
    con.command('sticky enable')
    con.command('floating enable')
    con.command('mark quaked')
    con.command(f'resize set {width} {height}')
    con.command(f'move position center, move up {height_to_move}')
