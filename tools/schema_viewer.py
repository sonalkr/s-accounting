"""
how to run 
uvicorn tools.schema_viewer:app --reload

"""


from os import getcwd, path
import sqlite3
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, inspect, MetaData
from eralchemy import render_er
import matplotlib.pyplot as plt
import matplotlib.image as mimg
import uvicorn

db_file = 'data.sqlite'


app = FastAPI()
print(getcwd())
@app.get('/get_schema')
def getSchema():
    engine = create_engine(f'sqlite:///./{db_file}')
    # cursor = engine.connect()
    ins = inspect(engine)
    # file_name = 'models.png'
    # render_er(metadata, file_name)
    # implot = plt.imshow(mimg.imread())
    metadata = MetaData(bind=engine)
    # print(metadata.tables('main'))

    value = {}
    value["get_table_names"] = ins.get_table_names()
    for table_name in value.get('get_table_names'):
        value[table_name] = {}

    for table_name in value.get('get_table_names'):
        print(table_name)


        value[table_name]["default_schema_name"] = ins.default_schema_name
        # value[table_name]["from_engine"] = ins.from_engine()
        value[table_name]["get_check_constraints"] = ins.get_check_constraints(table_name)
        value[table_name]["get_columns"] = ins.get_columns(table_name)
        value[table_name]["get_foreign_keys"] = ins.get_foreign_keys(table_name)
        value[table_name]["get_indexes"] = ins.get_indexes(table_name)
        value[table_name]["get_pk_constraint"] = ins.get_pk_constraint(table_name)
        value[table_name]["get_schema_names"] = ins.get_schema_names()
        # value[table_name]["get_sequence_names"] = ins.get_sequence_names()
        value[table_name]["get_sorted_table_and_fkc_names"] = ins.get_sorted_table_and_fkc_names()
        # value[table_name]["get_table_comment"] = ins.get_table_comment(table_name)
        # value[table_name]["get_table_options"] = ins.get_table_options()
        # value[table_name]["get_temp_table_names"] = ins.get_temp_table_names()
        # value[table_name]["get_temp_view_names"] = ins.get_temp_view_names()
        # value[table_name]["get_unique_constraints"] = ins.get_unique_constraints()
        # value[table_name]["get_view_definition"] = ins.get_view_definition()
        # value[table_name]["get_view_names"] = ins.get_view_names()
        # value[table_name]["has_sequence"] = ins.has_sequence()
        # value[table_name]["has_table"] = ins.has_table()
        # value[table_name]["reflect_table"] = ins.reflect_table()
        # value[table_name]["reflecttable"] = ins.reflecttable()
        # value[table_name]["default_schema_name"] = ins.default_schema_name
        # value[table_name]["from_engine"] = ins.from_engine()
        # value[table_name]["get_check_constraints"] = ins.get_check_constraints()
        # value[table_name]["get_columns"] = ins.get_columns()
        # value[table_name]["get_foreign_keys"] = ins.get_foreign_keys()
        # value[table_name]["get_indexes"] = ins.get_indexes()
        # value[table_name]["get_pk_constraint"] = ins.get_pk_constraint()
        value[table_name]["get_schema_names"] = ins.get_schema_names()
        # value[table_name]["get_sequence_names"] = ins.get_sequence_names()
        # value[table_name]["get_sorted_table_and_fkc_names"] = ins.get_sorted_table_and_fkc_names()
        # value[table_name]["get_table_comment"] = ins.get_table_comment()
        # value[table_name]["get_table_names"] = ins.get_table_names()
        # value[table_name]["get_table_options"] = ins.get_table_options()
        # value[table_name]["get_temp_table_names"] = ins.get_temp_table_names()
        value[table_name]["get_temp_view_names"] = ins.get_temp_view_names()
        # value[table_name]["get_unique_constraints"] = ins.get_unique_constraints()
        # value[table_name]["get_view_definition"] = ins.get_view_definition()
        value[table_name]["get_view_names"] = ins.get_view_names()
        # value[table_name]["has_sequence"] = ins.has_sequence()
        # value[table_name]["has_table"] = ins.has_table()
        # value[table_name]["reflect_table"] = ins.reflect_table()
        # value[table_name]["reflecttable"] = ins.reflecttable()
    # cursor.close()
    return value
    # return {'table_name': ins.get_table_names()}


# @app.get('/')
# def index():
#     f = ""
#     with open('index.html') as f:
#         html = f.read()
#     return FileResponse(html)


app.mount('/', StaticFiles(directory='tools/static'), name='root')



# if __name__=="__main__":
#     uvicorn.run("app.app:app",host='0.0.0.0', port=4557, reload=True, debug=True, workers=3)