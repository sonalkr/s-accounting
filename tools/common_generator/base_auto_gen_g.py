from itertools import combinations
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
        self.model_dict_com = self.get_model_dict_com()

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
        raise Exception('unable to clean : auto gen not found')

    def get_code(self, name: str):
        code_path = f'tools/{self.dir_name}_generator/cache_code/{name}'
        return file_to_text(code_path)

    def get_model_dict(self, model_name: str):
        for data in self.model_dict:
            if data[0]["model_name"] == model_name:
                return data[0]
            raise Exception(f"model_name not found{model_name}")

    def get_model_dict_com(self):
        result = []
        for model in self.model_dict:
            d = []
            d.append(model[0]["model_name"])
            for r in model[0]["relationship"]:
                d.append(r["model_name"])
            for r in model[0]["ref_relationship"]:
                d.append(r["model_name"])

            for i in range(1, len(d)):
                new_dic = {}
                models = {}
                fields = []
                f_name = []

                com_list = list(combinations(d, i+1))
                for c in com_list:
                    c = list(c)
                    if not c.__contains__(model[0]["model_name"]):
                        continue

                    with_out_f = c[1:]
                    for model2 in self.model_dict:
                        if c[0] == model2[0]["model_name"]:

                            for f in model2[0]["fields"]:

                                if c.__contains__(f["name"][:-3]):
                                    continue
                                # print(f["name"])
                                if f_name.__contains__(f["name"]):
                                    continue
                                fields.append(f)
                                f_name.append(f["name"])

                        if with_out_f.__contains__(model2[0]["model_name"]):
                            for f in model2[0]["fields"]:

                                if f["name"] == model[0]["model_name"]+"_id":
                                    continue
                                if f_name.__contains__(f["name"]):
                                    continue
                                fields.append(f)
                                f_name.append(f["name"])
                            pass

                    for model2 in self.model_dict:
                        if not c.__contains__(model2[0]["model_name"]):
                            continue

                        # new_dic[model2[0]["model_name"]] = model2[0]
                        models[model2[0]["model_name"]] = model2[0]

                    new_dic["com"] = c
                    new_dic["models"] = models
                    new_dic["model_name"] = "_".join(c)
                    new_dic["fields"] = fields

                result.append(new_dic)
        return result
# tools/browser_generator/cache_code
# tools/browser_client_generator/cache_code/index.code.ts
