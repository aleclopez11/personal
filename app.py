from fastapi import FastAPI
import stocks
import to_do_list


app = FastAPI()



@app.get('/')
def home():
    print('refreshing data')
    stock_info = stocks.retrieve_stocks()

    tasks = to_do_list.get_tasks()

    output = ''
    for key in stock_info:
        output += f'<br>${key}:<br>' 
        for values in stock_info[key]:
            output += f'{values}: {stock_info[key][values]}<br>'

    for task in tasks:
        output += f'<br>{task}'
    return(f'app homepage <br>{output}')

@app.post('/addTask')
def post_task(task: str):
    to_do_list.add_task(task)
    return f'task {task} added'

# if __name__ == '__main__':
#     app.run()