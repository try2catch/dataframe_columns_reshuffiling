import pandas as pd


def check_duplicate_indexes(header_indexes):
    if len(header_indexes) == len(set(header_indexes)):
        return False
    else:
        return True


def get_headers(header_list, subset=None):
    size = len(header_list)
    headers = [None] * size
    for header in header_list:
        index = header.get('index')
        if index < size:
            headers[index] = header.get('name')
        else:
            break

    result = filter(lambda x: x is None, headers)
    result = list(result)
    value = ''
    try:
        value = result[0]
    except IndexError:
        pass

    if value is None:
        return 'There is indexing issue with header list. {}'.format(str(header_list))
    else:
        if subset is None:
            return headers
        else:
            index = []
            if type(subset) == int:
                index.append(subset)
            else:
                index = subset

            duplicate = check_duplicate_indexes(index)
            if duplicate:
                return 'Indexes given for headers are duplicate : ' + str(index)

            accessed_mapping = map(headers.__getitem__, index)
            try:
                accessed_list = list(accessed_mapping)
                return accessed_list
            except IndexError:
                return 'The given indexes are not matched with headers max length.'
            except TypeError:
                return 'Type of indexes parameter must me integer or list.'


header = [
    {
        "index": 1,
        "name": "country"
    },
    {
        "index": 0,
        "name": "beer_servings"
    },
    {
        "index": 2,
        "name": "spirit_servings"
    },
    {
        "index": 3,
        "name": "wine_servings"
    },
    {
        "index": 4,
        "name": "total_litres_of_pure_alcohol"
    },
    {
        "index": 5,
        "name": "continent"
    }
]

required_headers = get_headers(header)

df = pd.read_csv('files/drinks.csv')
dff = df[required_headers]
dff.to_csv('files/output.csv', index=False)
