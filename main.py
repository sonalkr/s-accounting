from os import  getcwd, path, remove
from shutil import rmtree
from time import sleep
from sqlalchemy import create_engine
from utility import get_list_of_models_path, get_model_in_text
# from glob import glob
from tools.server_fastapi_generator.server_generator_g import server_code_gen
from tools.browser_client_generator.browser_client_generator_g import browser_code_gen


# rmdir('data.sqlite')
db_file = 'data.sqlite'
if path.isfile(path.join(getcwd(), db_file)):
    remove(path.join(getcwd(), db_file))

engine = create_engine(f'sqlite:///./{db_file}')
engine.execute('PRAGMA foreign_keys = ON;')
cursor = engine.connect()

list_of_model = get_list_of_models_path()

# list_of_model = glob(path.join(getcwd(), 'models')+"/*.sql")
sleep(1)
for model in list_of_model:
    # sleep(1)
    print('creating database' + model.split('/')[-1])
    cursor.execute(get_model_in_text(model))

cursor.close()

server_code_gen()
browser_code_gen()
