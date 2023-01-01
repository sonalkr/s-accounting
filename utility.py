from os import getcwd, path
from glob import glob


def file_to_text(path):
    text = ""
    try:
    
        with open(path, 'r') as f :
            text = f.read()
            return text
    except:
        print(f"unable to find {path}")



def contact(*args : list[str]):
    all_text : str = ""
    for t in args:
        all_text = all_text + t
    
    return t
    

def get_list_of_models_path():
    return glob(path.join(getcwd(), 'models')+"/*.sql")


def get_model_in_text(model_file_name: str):
    return file_to_text("./models/"+ model_file_name.split('/')[-1])


def get_models_array_as_string() -> list[str]:
    list_of_model = get_list_of_models_path()
    models = []
    for model in list_of_model:
        model_file_name: str = model.split('/')[-1]
        models.append(get_model_in_text(model_file_name))
    
    return models


