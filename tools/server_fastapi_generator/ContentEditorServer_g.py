from tools.common_generator.base_content_editor_g import BaseContentEditor
class ContentEditorServer(BaseContentEditor):
    def __init__(self, auto_gen) -> None:
        super().__init__(auto_gen)

    # adding dependency
    def add_dependency_FastApi_Router_BaseModel(self, router_name = 'default_api'):
        self.add_to_content_nl('from fastapi import APIRouter, Depends, HTTPException')
        self.add_to_content_nl('from pydantic import BaseModel')
        self.add_to_content_nl('from sqlalchemy.orm import Session')
        # self.add_to_content_nl('from itertools import chain')
        self.add_nl()
        self.add_to_content_nl('from server_fastapi.auto_gen.database import get_db')
        self.add_nl()
        self.add_to_content_nl(f'{router_name} = APIRouter()')
        
        self.add_nl()



    def add_model(self, model: dict):
        data: list = model['fields']
        self.add_to_content_nl(f'class {model["model_name"].capitalize()}(BaseModel):')

        for i in data:
            null_value = ""
            datatype = ""
            if i['null'] == True:
                null_value = " | None = None"
            if i['type'] == 'TEXT':
                datatype = "str"
            if i['type'] == 'INTEGER':
                datatype = "int"
            if i['type'] == 'DECIMAL':
                datatype = "float"
            if i['type'] == "BOOLEAN":
                datatype = 'bool'
            
            # if i['name'].endswith('_id'):
            #     datatype = "str"
            self.add_tab()
            self.add_to_content_nl(f'{i["name"]}: {datatype}{null_value}')
    
        self.add_nl()

    def add_api(self, model, router_name = 'default_api'):
        self.add_create_api(model=model, router_name=router_name)
        self.add_get_api(model=model, router_name=router_name)
        self.add_delete_api(model=model, router_name=router_name)
        self.add_update_api(model=model, router_name=router_name)

    def add_create_api(self,model, router_name = 'default_api'):
        self._add_api_function_head_create(model, router_name, function_name='create', method='post')

        model_name = model["model_name"]

        self.add_tab()
        self.add_to_content_nl("data = "+model_name+".dict()")
        self.add_tab()
        self.add_to_content_nl("del data['id']")
        self.add_tab()
        self.add_to_content_nl("columns = ', '.join(data.keys())")
        self.add_tab()
        self.add_to_content_nl("placeholders = ':'+', :'.join(data.keys())")
        self.add_tab()
        self.add_to_content_nl( "query = f'INSERT INTO "+model_name+ "({columns}) VALUES ({placeholders});'")
        # self.add_tab()
        # self.add_to_content_nl("print(query)")
    
        self.add_tab()
        self.add_to_content_nl('db.execute(query, data)')
        self.add_tab()
        self.add_to_content_nl('db.commit()')
        self.add_tab()
        self.add_to_content_nl('return "ok"')
        
        self.add_nl()
        self.add_nl()


    def add_update_api(self,model, router_name = 'default_api'):
        self._add_api_function_head_create(model, router_name, function_name='update', method='put')

        model_name = model["model_name"]

        self.add_tab()
        self.add_to_content_nl("data = "+model_name+".dict()")
        self.add_tab()
        self.add_to_content_nl("id = data['id']")
        self.add_tab()
        self.add_to_content_nl("del data['id']")
        self.add_tab()

        # self.add_to_content_nl("list_of_data = list(chain.from_iterable([list(i) for i in zip(data.keys(), data.values())]))")
        self.add_to_content_nl("list_of_data = [i for i in zip(data.keys(), data.values())]")
        self.add_tab().add_to_content_nl("print(list_of_data)")

        # self.add_tab().add_to_content_nl("query = 'UPDATE "+ model_name+" SET {}'.format(', '.join('{}=%s'.format(k) for k in list_of_data))")
        self.add_tab().add_to_content_nl("query = 'UPDATE "+ model_name+" SET {}'.format(', '.join(\"%s='%s'\" % (k) for k in list_of_data))")
        self.add_tab().add_to_content_nl("query = query + ' WHERE id = ' + str(id) + ';'")
        self.add_tab().add_to_content_nl("print(query)")




        # self.add_to_content_nl("columns = ', '.join(data.keys())")
        # self.add_tab()
        # self.add_to_content_nl("placeholders = ':'+', :'.join(data.keys())")
        # self.add_tab()
        # self.add_to_content_nl( "query = f'INSERT INTO "+model_name+ "({columns}) VALUES ({placeholders});'")
        # self.add_tab()
        # self.add_to_content_nl("print(query)")
    
        self.add_tab()
        self.add_to_content_nl('db.execute(query)')
        self.add_tab()
        self.add_to_content_nl('db.commit()')
        self.add_tab()
        self.add_to_content_nl('return "ok"')
        
        self.add_nl()
        self.add_nl()


    def add_get_api(self,model, router_name = 'default_api'):
        self._add_api_function_head_get(model, router_name, function_name='get', method='get')
        model_name = model["model_name"]
        self.add_tab()
        self.add_to_content_nl(f'rs = db.execute("SELECT * FROM {model_name};").all()')
        self.add_tab()
        self.add_to_content_nl("return rs")
    
        self.add_nl()

    def _add_api_function_head_create(self, model, router_name, function_name, method):
        self.add_to_content_nl(f'@{router_name}.{method}("/{model["model_name"]}/{function_name}/")')
        self.add_to_content_nl(f'async def {function_name}_{model["model_name"]}({model["model_name"]}: {model["model_name"].capitalize()}, db: Session = Depends(get_db)):')

    def _add_api_function_head_get(self, model, router_name, function_name, method):
        self.add_to_content_nl(f'@{router_name}.{method}("/{model["model_name"]}/{function_name}/")')
        self.add_to_content_nl(f'async def {function_name}_{model["model_name"]}(db: Session = Depends(get_db)):')



    def add_delete_api(self,model, router_name = 'default_api'):
        self._add_api_function_head_delete(model, router_name, function_name='delete', method='delete')
        model_name = model["model_name"]
        self.add_tab()

        self.add_to_content_nl('for id in ids:')
        self.add_tab().add_tab()
        self.add_to_content_nl(f'rs = db.execute(f"SELECT * FROM {model_name} WHERE id = '+ '{str(id)}' +';").all()')
        self.add_tab().add_tab()
        self.add_to_content_nl('if len(rs) == 0:')
        self.add_tab().add_tab().add_tab()
        self.add_to_content_nl('raise HTTPException(status_code=404, detail=f"\'{str(id)}\'")')


        self.add_tab().add_tab()
        self.add_to_content_nl(f'db.execute(f"DELETE FROM {model_name} WHERE id = ' + '{str(id)}' + ';")')
        self.add_tab()
        self.add_to_content_nl('db.commit()')
        self.add_tab()
        self.add_to_content_nl('return "ok"')
        self.add_nl()


    def _add_api_function_head_delete(self, model, router_name, function_name, method):
        self.add_to_content_nl(f'@{router_name}.{method}("/{model["model_name"]}/{function_name}/")')
        self.add_to_content_nl(f'async def {function_name}_{model["model_name"]}(ids: list[int], db: Session = Depends(get_db)):')
