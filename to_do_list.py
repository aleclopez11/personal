import json


def get_tasks():
    config = json.load(open('settings.json'))
    tasks = config['tasks']
    keys = config['task_keys']

    # output = {}
    output = []

    for task in tasks:
        print('getting info')
        # output[task] = get_task_info(task, keys)
        output.append(task)

    return output

def add_task(task):
    config = json.load(open('settings.json'))
    tasks = config['tasks']
    tasks.append(task)
    with open('settings.json', 'w') as f:
        json.dump(config, f, indent=4)

def delete_task(task):
    config = json.load(open('settings.json'))
    tasks = config['tasks']
    tasks.remove(task)
    with open('settings.json', 'w') as f:
        json.dump(config, f, indent=4)

