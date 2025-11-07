import asyncio
import datetime
import random

async def my_sleep_func():
    await asyncio.sleep(random.randint(0,5))


async def display_date(num, loop):
    end_time=loop.time()+50

    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() +1.0) >= end_time:  #Set time of the completion
            print("Break")
            break

        await my_sleep_func()   #Call the function pause


async def main():
    loop=asyncio.get_event_loop()

    await asyncio.gather(display_date(1,loop), display_date(2,loop))

#Receive the current event cycle
loop = asyncio.get_event_loop()


#Launch the main task and await it completion

loop.run_until_complete(main())
loop.close()