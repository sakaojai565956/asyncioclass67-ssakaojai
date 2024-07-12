# example of waiting for the first task to complete
from random import random
import asyncio
from time import sleep


# coroutine to execute in a new |task
async def task_coro(food):
    # generate a random value between 0 and 1
    waitfor = 1 + random()
    # block for a moment
    sleep(waitfor)
    # report the value
    print(f'microwave ({food}): cooking for {waitfor} seconds')
    await asyncio.sleep(waitfor)
    print(f'microwave ({food}): Finished cooking')
    return food, waitfor
# main coroutine
async def main():
    # create many tasks
    
    tasks = [
    asyncio.create_task(task_coro('rice'), name='rice'),
    asyncio.create_task(task_coro('noodle'), name='noodle'),
    asyncio.create_task(task_coro('curry'), name='curry')
    ]
    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, timeout=10, return_when=asyncio.FIRST_COMPLETED)
    
    print(f"Complete task : {len(done)} tasks")
    for task in done:
        food, time = task.result()
        print(f" - {food} is completed in {time} seconds")
    
    print(f"Uncompleted task : {len(pending)} tasks")
    for task in pending:
        print(f" - {task.get_name()}")

asyncio.run(main())