import time

def timer(func):
    def wrapper(*args, **kwargs):
        # *args is used for the unlimited arguments..
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    # I have made a function inside a function  and defined all the parameter in the the function.
    return wrapper
@timer

def example_function(n):
    time.sleep(n)

example_function(2)    

# here inside a function function run called as decorators