

MENU = ["борщ","вареники","салат","деруни","кава","чай","узвар"]
import time
import asyncio
import random

def create_order(order_id):
    items = random.sample(MENU,random.randint(1,3))
    return {"order_id": order_id, "items": items}

async def customer(queue):
    start = time.time()
    order_id = 1
    while (time.time() -start)<=5:
        order=create_order(order_id)
        await queue.put(order)
        print(f"Created order {order_id} order {order['items']}")
        order_id += 1
        await asyncio.sleep(random.uniform(0.5,1.5))
    print(f"The order part is finished")


async def waiter(queue, name):
    try:
        while True:
            order = asyncio.wait_for(queue.get(), timeout=2)
            print(f"Waiter{name} order {order['items']}")
            await asyncio.sleep(random.uniform(0.5,1.5))
            queue.task_done()
    except asyncio.TimeoutError:
        print(f"Waiter {name} wait too long, go home")


async def main():
    queue = asyncio.Queue()
    producer_task=asyncio.create_task(customer(queue))
    waiters = [asyncio.create_task(waiter(queue, i)) for i in range(2)]
    await producer_task
    await queue.join()
    await asyncio.sleep(3)
    for waiter1 in waiters:
        waiter1.cancel()
    print(f"Cafe is closed")


if __name__ == "__main__":
    asyncio.run(main())

