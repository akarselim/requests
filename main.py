import time
import asyncio
import requests
import aiohttp
import threading


urls = ['https://postman-echo.com/delay/3'] * 10

# # Get data requests with sync
# def get_data_sync(urls):
#     st = time.time()
#     json_array = []
#     for url in urls:
#         json_array.append(requests.get(url).json())
#     et = time.time()
#     elapsed_time = et-st
#     print("Execution time:", elapsed_time, " seconds")
#     return json_array
# # get_data_sync(urls) # 37 seconds


# # Get data requests with async but as wrapper
# async def get_data_async_but_as_wrapper(urls):
#     st = time.time()
#     json_array = []
#     async with aiohttp.ClientSession() as session:
#         for url in urls:
#             async with session.get(url) as response:
#                 json_array.append(await response.json())
#     et = time.time()
#     elapsed_time = et - st
#     print("Execution time: ", elapsed_time, " seconds")
#     return json_array
# asyncio.run(get_data_async_but_as_wrapper(urls)) # 32 seconds


# # Get data requests with async but as concurrently
# async def get_data(session, url, json_array):
#     async with session.get(url) as response:
#         json_array.append(await response.json())
#
# async def get_data_async_concurrently(urls):
#     st = time.time()
#     json_array = []
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for url in urls:
#             tasks.append(asyncio.ensure_future(get_data(session, url, json_array)))
#         await asyncio.gather(*tasks)
#         et = time.time()
#         elapsed_time = et - st
#         print("Execution time: ", elapsed_time, " seconds")
#         return json_array
# asyncio.run(get_data_async_concurrently(urls)) #4 seconds

# Get data requests with threading

