from tools.server_fastapi_generator.ContentEditorServer_g import ContentEditorServer
from tools.common_generator.base_auto_gen_g import BaseAutoGen



class AutoGenServer(BaseAutoGen):
    def __init__(self, dir_name: str, auto_gen_dir_name: str, main_file_name: str, extension_name: str) -> None:
        super().__init__(dir_name, auto_gen_dir_name, main_file_name, extension_name)
    
    def gen_template_api(self):
        content = """

        """
        self.create_file('__init__.py',self.get_code('default_api.code.py'))
        self.create_file('database.py',self.get_code('database.code.py'))


    def gen_api(self):
        self.create_file('database.py',self.get_code('database.code.py'))
        # data = self.model_dict[6][0]
        # pp.pprint(self.model_dict)
        contentEditor = ContentEditorServer(self)
        contentEditor.add_dependency_FastApi_Router_BaseModel()
        for data in self.model_dict:
            data = data[0]
            contentEditor.add_model(data)
            contentEditor.add_api(model = data)

        self.create_file('__init__.py',contentEditor.content)
        pass


def server_code_gen():
    print('generating')
    auto_gen = AutoGenServer( dir_name='server_fastapi', auto_gen_dir_name='auto_gen', main_file_name="server", extension_name="py")
    auto_gen.gen_server_app()
    auto_gen.clean_auto_gen_dir()
    auto_gen.gen_api()
    # auto_gen.gen_template_api()
    # print(auto_gen.sql_to_dict())
    # auto_gen.sql_to_dict()
    # pp.pprint(auto_gen.model_dict)
    print('run : uvicorn server_fastapi.server:server')
