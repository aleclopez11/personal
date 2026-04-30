from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from contextlib import asynccontextmanager
import stocks
import datetime
import to_do_list

async def refresh_data():
    # while True:
    print('running refresh of stock data')
    stock_info = {}
    now = datetime.datetime.now()
    weekday = now.weekday()
    time = now.time()
    start_time = datetime.time(9, 30)  # 9:30 AM
    end_time = datetime.time(16, 0)    # 4:00 PM
    if weekday < 5 and (start_time <= time <= end_time):
        print('refreshing data')
        stock_info = stocks.retrieve_stocks()
    # await asyncio.sleep(300)  # Refresh every 5 minutes (300 seconds)
    # stock_info = stocks.retrieve_stocks()

    return stock_info


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the background task when the application starts
    task = asyncio.create_task(refresh_data())
    yield
    # Cancel the background task when the application shuts down
    task.cancel()


app = FastAPI(lifespan = lifespan)

origins = [
    "http://localhost:5173",
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Allows specific origins
    allow_credentials=True,         # Allows cookies to be sent cross-origin
    allow_methods=["*"],            # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],            # Allows all headers
)


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    print('websocket connection established')
    await websocket.accept()
    while True:
        print('waiting for data from client')
        # data = await websocket.receive_text()
        data = await refresh_data()
        print(f'Received data from client: {data}')
        # if data != {}:
            # response = f'Server received: {data}'
            # await websocket.send_text(data)
        await websocket.send_json(data)
        await asyncio.sleep(300)  # Sleep for 5 minutes if no data is available
        


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
    # return stock_info

@app.get('/stocks')
def get_stocks():
    stock_info = stocks.retrieve_stocks()
    print(type(stock_info))
    print(stock_info)
    print('api hit')
    return stock_info

@app.post('/addTask')
def post_task(task: str):
    to_do_list.add_task(task)
    return f'task {task} added'

# if __name__ == '__main__':
#     app.run()