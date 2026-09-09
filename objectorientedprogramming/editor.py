class Editor:
    def open(self):
        print("editor open method")
    def execute(self):
        print("execute traditional way python module_name.py ")

class VsCode(Editor):
    def open(self):
        print("open with code .")

vscode_instance = VsCode()
vscode_instance.open()

