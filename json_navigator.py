import json 


def json_reader(path):
    """
    Read a json file (path) and returns Python dict object
    """
    with open(path, mode='r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def list_info(parent: str, data: list):
    """
    Shows info about current list and proposes
    a few options (view full object, chose the element
    or go back). Calls list_info or dict_info function
    """
    print(f"This is a list of {parent}. It's length = {len(data)}")
    ans = input("Please choose a number of element (num) or go back (Q) or look at all object(ALL): ")

    while ans == 'ALL':
        print(data)
        ans = input("Please choose a key (key) or go back (Q) or look at all object(ALL): ")

    if ans == 'Q':
        return '123456789fgh'

    else:
        ans = int(ans) - 1
        if type(data[ans]) == list:
            el = list_info(parent, data[ans])

        elif type(data[ans]) == dict:
            el = dict_info(parent, data[ans])

        else:
            print(f'You reached the bottom of json-tree! The leafe is {data[ans]}')

        if el == '123456789fgh':
            list_info(parent, data)


def dict_info(parent: str, data: dict):
    """
    Shows info about current dict and proposes
    a few options (view full object, chose the key
    or go back). Calls list_info or dict_info function
    """
    print(f"This is a dict about {parent} object. It's keys = {list(data.keys())}")
    ans = input("Please choose a key (key) or go back (Q) or look at all object(ALL): ")

    while ans == 'ALL':
        print(data)
        ans = input("Please choose a key (key) or go back (Q) or look at all object(ALL): ")

    if ans == 'Q':
        return '123456789fgh'

    else:
        if type(data[ans]) == list:
            el = list_info(ans, data[ans])

        elif type(data[ans]) == dict:
            el = dict_info(ans, data[ans])

        else:
            print(f'You reached the bottom of json-tree! The leafe is {data[ans]}')

        if el == '123456789fgh':
            list_info(parent, data)


def json_navigation(json_dict: dict):
    """
    Starts json navigation and prints some info about it.
    The only argument is Python dict json object
    """
    print("You are using json Python navigator")
    print("You can go through the json-tree of objects")
    print("At any time you can choose next object (son) or go back (return to parent)")

    dict_info('root', json_dict)


if __name__ == "__main__":
    json_dict = json_reader(r'C:\Python\LABA3.3\kved.json')

    json_navigation(json_dict)