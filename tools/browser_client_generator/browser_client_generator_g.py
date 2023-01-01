from tools.common_generator.base_auto_gen_g import BaseAutoGen
from tools.browser_client_generator.ContentEditorBrowser_client_g import ContentEditorBrowser_client
class AutoGenBrowser(BaseAutoGen):
    def __init__(self, dir_name: str, auto_gen_dir_name: str, main_file_name: str, extension_name) -> None:
        super().__init__(dir_name, auto_gen_dir_name, main_file_name, extension_name)

    def gen_table(self):
        self.create_file('test.ts', 'console.log("ok")')
        # self.create_file('index.html', self.get_code('index.code.html'))

        contentEditor = ContentEditorBrowser_client(self)
        # contentEditor.add_link(self)
        for data in self.model_dict:

            contentEditor.create_table(data[0])

        self.create_file('script.js', contentEditor.content)

def browser_code_gen():
    
    print('running broswer generator')
    auto_gen = AutoGenBrowser( dir_name='browser_client', auto_gen_dir_name='auto_gen', main_file_name="index", extension_name="html")
    auto_gen.gen_server_app()
    auto_gen.clean_auto_gen_dir()
    auto_gen.gen_table()