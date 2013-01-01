import sublime, sublime_plugin

# class ExampleCommand(sublime_plugin.TextCommand):
#     def run(self, edit):
#         self.view.insert(edit, 0, "Hello, World!")

class ToggleWhiteSpaceCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        settings = sublime.load_settings("Preferences.sublime-settings")
        white_space = "selection" if settings.get("draw_white_space", "selection") != "selection" else "all"
        settings.set("draw_white_space", white_space)
        sublime.save_settings("Preferences.sublime-settings")
