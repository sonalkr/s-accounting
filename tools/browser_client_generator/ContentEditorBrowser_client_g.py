
from tools.common_generator.base_content_editor_g import BaseContentEditor


class ContentEditorBrowser_client(BaseContentEditor):

    def __init__(self, auto_gen) -> None:
        self.parrent_auto_gen = auto_gen
        super().__init__(auto_gen)

    def create_table(self, model):
        self.add_html(model)
        # print(model)

    def add_html(self, model):
        code = self.get_code('form.code.js')
        model_name = model["model_name"]
        action = "create"
        element = "form"
        heading = self.str_proper_heading_convertor(model_name)
        html = self.add_form_html(model)
        style = ""

        code = code.replace("$name$", model_name)
        code = code.replace("$action$", action)
        code = code.replace("$element$", element)
        code = code.replace("$heading$", heading)

        code = code.replace(
            "$proper_name$", self.str_proper_convertor(model_name))
        code = code.replace("$proper_action$",
                            self.str_proper_convertor(action))
        code = code.replace("$proper_element$",
                            self.str_proper_convertor(element))
        code = code.replace("$dash_name$", model_name.replace("_", "-"))

        code = code.replace("$html$", html)
        code = code.replace("$style$", style)

        self.add_to_content_nl(code)

        self.add_nl()

    def add_form_html(self, model):
        data: list = model['fields']
        model_name = model["model_name"]
        editor = BaseContentEditor(self.parrent_auto_gen)
        editor.add_to_content_nl(
            f'<form action="/{model_name}/create/" method="post">')
        for i in data:

            null_value = ""
            datatype = ""
            hidden = ""
            options = False

            if i['type'] == 'TEXT':
                datatype = "text"
            if i['type'] == 'INTEGER':
                datatype = "number"
            if i['type'] == 'DECIMAL':
                datatype = "number"
            if i['type'] == "BOOLEAN":
                datatype = 'checkbox'

            if i['null'] != True:
                null_value = "required"

            if i['name'] == 'id':
                hidden = "hidden"

            if str(i['name']).endswith("id"):
                options = True

            editor.add_to_content_nl(f"<div {hidden}>")
            editor.add_to_content_nl(
                f'<label for="{i["name"]}">{self.str_proper_heading_convertor(i["name"])}</label>')

            editor.add_to_content_nl(
                f'<input type="{datatype}" id="{i["name"]}" name="{i["name"]}" {null_value}>')

            editor.add_to_content_nl(f'</div>')

        editor.add_to_content_nl(f'<input type="submit" value="Create">')
        editor.add_to_content_nl(f'</form>')

        return editor.content
