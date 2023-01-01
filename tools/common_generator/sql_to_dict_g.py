import pprint
from pandas import DataFrame
from utility import get_models_array_as_string

pp = pprint.PrettyPrinter(indent=2)

def sql_to_dict():
    models = get_models_array_as_string()
    result = []
    for model in models:
        new_array = []
        model_dict = {}
        model_dict['fields'] = []
        model_dict['relationship'] = []
        model_dict['ref_relationship'] = []

        split_d = model.split('\n')
        for s in split_d:
            s = s.strip()
            s = ' '.join(s.split())
            if s.endswith(","):
                s = s[:-1]
            if len(s) == 0 or len(s.split()) < 2:
                continue
            if s.startswith('CREATE') or s.startswith('create'):
                model_dict['model_name']  = s.split(' ')[-2]
                new_array.append(model_dict)
                continue
                
            if s.split()[1].split("(")[0].split(',')[0] in ["INTEGER", "TEXT", "BOOLEAN", "DECIMAL"]:
                is_null = "NOT NULL" in s
                field = {
                    'name' : s.split()[0],
                    'type' : s.split()[1].split('(')[0].split(',')[0],
                    'null' : not is_null,
                    'raw' : s
                }
                if s.__contains__('CHECK'):
                    field['options'] = s.split('(')[-1].replace(' ','').replace(')','').replace("'","").replace('"',"").split(',')
                model_dict['fields'].append(field)
                continue
            if s.split()[0] in ["FOREIGN"]:
                relationship = {
                    'field' : s.split()[1].split("(")[1][:-1],
                    'model_name' : s.split()[-1].split('(')[0],
                    'raw' : s
                }
                model_dict['relationship'].append(relationship)
                continue
                

            pp.pprint(s)
            # new_array.append(s)
            
        for r in result:
            for t in r[0]['relationship']:
                # print(t['model_name'], r[0]['model_name'])
                model_name = r[0]['model_name']
                f = t['field']
                for i, _ in enumerate(result):
                    # print(result[i][0]['model_name'])
                    ref_relationship_list = DataFrame(result[i][0]['ref_relationship'])['model_name'].tolist() if len(result[i][0]['ref_relationship']) else list()
                    if t['model_name'] == result[i][0]['model_name'] and not model_name in ref_relationship_list:
                        # print('ok')
                        # print(result[i][0]['model_name'], model_name)
                        result[i][0]['ref_relationship'].append({'model_name':model_name, 'field': f})

        result.append(new_array)

    # pp.pprint(result)
    return result
