
i3 = i3ipc.Connection()

def on_workspace_focus(self, e):
    if e.current:
        print('Windows on this workspace:')
        for w in e.current.leaves():
            print(w.name)

def on_window_focus(i3, e):
    focused = i3.get_tree().find_focused()
    ws_name = f"{focused.workspace().num}:{focused.window_class}"
    print(f"{ws_name}")

i3.on('workspace::focus', on_workspace_focus)
i3.on('window::focus', on_window_focus)

i3.main()
