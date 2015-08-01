#
# asyncio_examples/is_coroutine.py
#

import asyncio


@asyncio.coroutine
def coro():
    print("CORO!")


c = coro()

print("c = coro()\n----------\n")

print("coro is coroutine:", asyncio.iscoroutine(coro))
print("coro is coroutinefunction:", asyncio.iscoroutinefunction(coro))
print("")
print("c is coroutine:", asyncio.iscoroutine(c))
print("c is coroutinefunction:", asyncio.iscoroutinefunction(c))
print("")
print("asyncio.start_server is coroutine?", asyncio.iscoroutine(asyncio.start_server))


