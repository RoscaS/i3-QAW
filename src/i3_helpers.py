
class I3(object):

    @classmethod
    def current_wp(cls, i3):
        return i3.get_tree().find_focused().workspace()

    @classmethod
    def marked_list(cls, i3):
        return i3.get_tree().find_marked('quaked')
