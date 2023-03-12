
from tools.common_generator.base_auto_gen_g import BaseAutoGen


class BaseContentEditor():
    newline = "\n"
    tab = "    "
    content = ""

    def add_to_content(self, s: str):
        self.content = self.content + s
        return self

    def add_to_content_nl(self, s: str):
        self.content = self.content + s + '\n'
        return self

    def add_nl(self):
        self.add_to_content(self.newline)
        return self

    def add_tab(self):
        self.add_to_content(self.tab)
        return self

    def str_proper_convertor(self, s: str):
        return "".join([i.capitalize() for i in s.split("_")])

    def str_proper_heading_convertor(self, s: str):
        return " ".join([i.capitalize() for i in s.split("_")])

    def __init__(self, auto_gen: BaseAutoGen):
        self.get_code = auto_gen.get_code
        self.create_file = auto_gen.create_file
        self.model_dect = auto_gen.model_dict
