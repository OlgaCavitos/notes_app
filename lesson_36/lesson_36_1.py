# import asyncio
# import aiohttp
# import time
#
# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()
#
#
# async def main():
#     urls=[
#     "https://example.com/",
#     "https://example.org/",
#     "https://example.net/"
#     ]
#
#     start_time=time.time()
#     async with aiohttp.ClientSession() as session:
#         #Create list corutine
#         tasks=[fetch (session,url) for url in urls]
#         #Launch parallel
#         responses=await asyncio.gather(*tasks)
#
#         for url, html in zip(urls, responses):
#             print(f"Got response from {url}: {len(html)} bytes")
#
#     print(f"Total time: {time.time()-start_time:.2f} seconds")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


import time
import resource

def read_file(filename):
    text_file = open(filename, 'r')
    lines=text_file.readlines()
    text_file.close()
    return lines

start = time()
data=read_file('lesson_36_1.txt')
print(time() - start)
print('Peak memory usage: ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


