import sublime, sublime_plugin


class PromptFunctionGroupHeaderCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Header text:", "", self.onDone, None, None)

    def onDone(self, text):
        if self.window.active_view():
            self.window.active_view().run_command("function_group_header", {"headerText": text} )

class FunctionGroupHeaderCommand(sublime_plugin.TextCommand):
    def run(self, edit, headerText):
        count = int((100-4-len(headerText))/2)
        spaces = " "*count
        extraSpace = " " if len(headerText) % 2 == 1 else ""

        header = _template.format(spaces, headerText, spaces, extraSpace)

        for sel in self.view.sel():
            self.view.insert(edit, sel.begin(), header)

_template = '''
/**************************************************************************************************/
/*{0}{1}{2}{3}*/
/**************************************************************************************************/
'''