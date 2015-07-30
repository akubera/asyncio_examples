#
# loop_stopper.py
#

import asyncio

loop = asyncio.get_event_loop()

@asyncio.coroutine
def spam(x):
    i = 1
    while True:
        print(x, i)
        i += 1
        yield from asyncio.sleep(1)
        if x == 'C':
            loop.stop()

loop.create_task(spam('A'))
loop.create_task(spam('B'))
loop.create_task(spam('C'))
loop.create_task(spam('D'))

loop.run_forever()
print("Done.")

loop.run_forever()
print("Really Done.")
