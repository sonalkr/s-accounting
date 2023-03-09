import os
import pprint

from tools.common_generator.sql_to_dict_g import sql_to_dict
from utility import file_to_text, get_models_array_as_string

pp = pprint.PrettyPrinter(indent=2)


class BaseAutoGen():
    def __init__(self, dir_name: str, auto_gen_dir_name: str, main_file_name: str, extension_name) -> None:
        self.dir_name = dir_name
        self.auto_gen_dir_name = auto_gen_dir_name
        self.main_file_name = main_file_name
        self.extension_name = extension_name
        self.auto_gen_path = f'{dir_name}/{auto_gen_dir_name}'
        self.model_dict = sql_to_dict()

    def gen_server_app(self):

        if (not self.exists_server_app_dir()):
            print(f'creating {self.dir_name} dir')
            os.mkdir(self.dir_name)

        if (not os.path.exists(f'./{self.dir_name}/{self.main_file_name}.{self.extension_name}')):
            with open(f'./{self.dir_name}/{self.main_file_name}.{self.extension_name}', 'w') as f:
                f.write(self.get_code(
                    f'{self.main_file_name}.code.{self.extension_name}'))
            self.create_auto_gen_dir()

    def create_auto_gen_dir(self):
        print('creating gen dir')
        if (not self.exists_auto_gen_dir()):
            os.makedirs(self.auto_gen_path)

    def exists_auto_gen_dir(self):
        return os.path.exists(self.auto_gen_path)

    def exists_server_app_dir(self):
        return os.path.exists(f'{self.dir_name}')

    def create_file(self, file_name: str, content: str):
        with open(f'{self.auto_gen_path}/{file_name}', 'w') as f:
            f.write(content)

    def clean_auto_gen_dir(self):
        if (self.exists_auto_gen_dir):
            print('cleaning auto gen')
            import shutil
            shutil.rmtree(self.auto_gen_path, ignore_errors=True)
            # os.removedirs(self.auto_gen_path)
            self.create_auto_gen_dir()
            return
        print('unable to clean : auto gen not found')

    def get_code(self, name: str):
        code_path = f'tools/{self.dir_name}_generator/cache_code/{name}'
        return file_to_text(code_path)

    def get_model_dict(self, model_name: str):
        for data in self.model_dict:
            if data[0]["model_name"] == model_name:
                return data[0]
            raise Exception(f"model_name not found{model_name}")

# tools/browser_generator/cache_code
# tools/browser_client_generator/cache_code/index.code.ts
