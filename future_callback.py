#
# future_callback.py
#

import asyncio
import functools

def say_hi(arg):
    print("hi", arg)


def say_spam(*args):
    print("spam", args)


@asyncio.coroutine
def coro1(fut):
    yield from asyncio.sleep(1)
    print('coro!')
    fut.set_result('.')
    print('done.')


@asyncio.coroutine
def coro2(fut):
    yield from asyncio.sleep(1)
    print('coro!')
    fut.set_result('.')
    print('done.')


loop = asyncio.get_event_loop()

fut = asyncio.Future()
fut.add_done_callback(say_hi)

loop.run_until_complete(coro1(fut))

fut = asyncio.Future()
fut.add_done_callback(say_hi)
fut.add_done_callback(functools.partial(say_spam, 'woot'))

loop.run_until_complete(coro2(fut))
