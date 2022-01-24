from markupsafe import functools
import numpy as np
import time

from rich.console import Console
import rich.traceback

console = Console()
console.clear()
rich.traceback.install()

time_array = []

def decorator_timing(_func = None, index = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            for i in range(1,index+1):
                start_time = time.time()
                result = func(*args, **kwargs)
                timeE = (time.time() - start_time) * 1_000
                time_array.append(timeE)
                console.print(f'Function {func.__name__} finished the {i} in {timeE:0.08f} ms')
            avarage_time = np.mean(time_array)
            console.print(f'Avarage time of {func.__name__} : {avarage_time} ms')
            return result

        return wrap
    
    if _func is not None:
        return decorator(_func)
    else:
        return decorator


'''
@decorator_timing(index = 20)
def fibon(n = 1):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibon(n-1)+fibon(n-2)

console.print(fibon(2))
'''


@decorator_timing(index = 20)
def sequence(n = 1):
    if n == 0:
        return 1
    else:
        return (2 * sequence(n - 1) + 5 * (n - 1))

console.log(sequence())

