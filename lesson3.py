from collections import defaultdict
called_time = defaultdict(int)
import functools


def get_call_times(f):
    result = f()
    print('function: {} called once! '.format(f.__name__))
    called_time[f.__name__] += 1
    print(f.__name__)

    return result

def some_funcion_1():
    print('I am function 1')
get_call_times(some_funcion_1)
print(called_time)
#some_funcion_1
call_time_with_arg = defaultdict(int)
#del call_time_with_arg

original_price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 25]
price = defaultdict(int)
for i, p in enumerate(original_price):
    price[i + 1] = p

solution={}
@functools.lru_cache()
def r(n):

    # fname = r.__name__
    # call_time_with_arg[(fname, n)] += 1

    print(n,[price[n]] + [r(i) + r(n - i) for i in range(1, n)])
    max_price, max_split = max(
        [(price[n], 0)] + [(r(i) + r(n - i), i) for i in range(1, n)], key=lambda x: x[0]
    )

    solution[n] = (n - max_split, max_split)


    return max_price

print(price[14])

print(r(20))
print(solution)

from functools import wraps
called_time_with_arg = defaultdict(int)
def get_call_time(f):
    """@param f is a function"""
    @wraps(f)
    def wrap(n):
        """Haha I am warp"""
        print('I can count')
        result = f(n)
        #print(33333)
        called_time_with_arg[(f.__name__, n)] += 1
        return result
    return wrap

def add_ten(n):
    return n + 10
#get_call_time(add_ten)

@get_call_time
def add_twenty(n):
    #print(44444)
    return n + 20
#add_twenty = get_call_time(add_twenty)
print(add_twenty(9))



def my_decorator(f):
    @wraps(f)
    def wrapper(*args,**kwds):
        print("Calling decorated function")
        return f(*args,**kwds)
    return wrapper

@my_decorator
def example():
    """DocString"""
    print ("Called example function")

example()
print (example.__name__)
print (example.__doc__)
'''
可以看到，最终调用函数example时，是经过 @my_decorator装饰的，装饰器的作用是接受一个被包裹的函数作为参数，对其进行加工，返回一个包裹函数，代码使用 @functools.wraps装饰将要返回的包裹函数wrapper，使得它的 __name__， __module__，和 __doc__ 属性与被装饰函数example完全相同，这样虽然最终调用的是经过装饰的example函数，但是某些属性还是得到维护。

如果在 @my_decorator的定义中不使用 @function.wraps装饰包裹函数，那么最终example.__name__ 将会变成'wrapper'，而example.__doc__ 也会丢失。

将 @wraps(f)注释掉，然后运行程序，控制台输出，
'''
called_time_with_arg = defaultdict(int)
solution = {}


def memo(f):
    memo.already_computed = {}

    @wraps(f)
    def _wrap(arg):
        result = None

        if arg in memo.already_computed:
            result = memo.already_computed[arg]
        else:
            result = f(arg)
            memo.already_computed[arg] = result

        return result

    return _wrap


@memo
def r(n):
    """
    Args: n is the iron length
    Return: the max revenue
    """
    max_price, max_split = max(
        [(price[n], 0)] + [(r(i) + r(n - i), i) for i in range(1, n)], key=lambda x: x[0]
    )


    solution[n] = (n - max_split, max_split)

    return max_price
print(r(243))
print(solution)


def parse_solution(n):
    left_split, right_split = solution[n]

    if right_split == 0: return [left_split]

    return parse_solution(left_split) + parse_solution(right_split)
print(parse_solution(242))

print('-------------------------------------------------machine learning！')
from sklearn.datasets import load_boston
data = load_boston()
X, y = data['data'], data['target']
print(X.shape,y.shape)
print(X[:,5])
import matplotlib.pyplot as plt
def draw_rm_and_price():
    plt.scatter(X[:, 5], y)
    plt.show()
draw_rm_and_price()
import random
def price(rm, k, b):
    """f(x) = k * x + b"""
    return k * rm + b
X_rm = X[:, 5]
k = random.randint(-100, 100)
b = random.randint(-100, 100)
print(k)
price_by_random_k_and_b = [price(r, k, b) for r in X_rm]

draw_rm_and_price()
plt.scatter(X_rm, price_by_random_k_and_b)
#plt.show()

trying_times = 2000

min_loss = float('inf')
best_k, best_b = None, None

def loss(y, y_hat): # to evaluate the performance
    xx=list(y)
    xxx=list(y_hat)
    for y_i, y_hat_i in zip(list(y), list(y_hat)):
        y_i, y_hat_i
    return sum((y_i - y_hat_i)**2 for y_i, y_hat_i in zip(list(y), list(y_hat))) / len(list(y))

for i in range(trying_times):
    k = random.random() * 200 - 100
    b = random.random() * 200 - 100
    price_by_random_k_and_b = [price(r, k, b) for r in X_rm]

    current_loss = loss(y, price_by_random_k_and_b)

    if current_loss < min_loss:
        min_loss = current_loss
        best_k, best_b = k, b
        print('When time is : {}, get best_k: {} best_b: {}, and the loss is: {}'.format(i, best_k, best_b, min_loss))

trying_times = 2000

min_loss = float('inf')

best_k = random.random() * 200 - 100
best_b = random.random() * 200 - 100

direction = [
    (+1, -1),  # first element: k's change direction, second element: b's change direction
    (+1, +1),
    (-1, -1),
    (-1, +1),
]

next_direction = random.choice(direction)

scalar = 0.1

update_time = 0

for i in range(trying_times):

    k_direction, b_direction = next_direction

    current_k, current_b = best_k + k_direction * scalar, best_b + b_direction * scalar

    price_by_k_and_b = [price(r, current_k, current_b) for r in X_rm]

    current_loss = loss(y, price_by_k_and_b)

    if current_loss < min_loss:  # performance became better
        min_loss = current_loss
        best_k, best_b = current_k, current_b

        next_direction = next_direction
        update_time += 1

        if update_time % 10 == 0:
            print(
                'When time is : {}, get best_k: {} best_b: {}, and the loss is: {}'.format(i, best_k, best_b, min_loss))
    else:
        next_direction = random.choice(direction)

''''
loss=1n∑(yi−yi^)2
loss=1n∑(yi−yi^)2
loss=1n∑(yi−(kxi+bi))2
loss=1n∑(yi−(kxi+bi))2
∂loss∂k=−2n∑(yi−(kxi+bi))xi
∂loss∂k=−2n∑(yi−(kxi+bi))xi
∂loss∂k=−2n∑(yi−yi^)xi
∂loss∂k=−2n∑(yi−yi^)xi
∂loss∂b=−2n∑(yi−yi^)
∂loss∂b=−2n∑(yi−yi^)
'''



def partial_k(x, y, y_hat):
    n = len(y)

    gradient = 0

    for x_i, y_i, y_hat_i in zip(list(x), list(y), list(y_hat)):
        gradient += (y_i - y_hat_i) * x_i

    return -2 / n * gradient


def partial_b(x, y, y_hat):
    n = len(y)

    gradient = 0

    for y_i, y_hat_i in zip(list(y), list(y_hat)):
        gradient += (y_i - y_hat_i)

    return -2 / n * gradient


trying_times = 2000

X, y = data['data'], data['target']

min_loss = float('inf')

current_k = random.random() * 200 - 100
current_b = random.random() * 200 - 100

learning_rate = 1e-04

update_time = 0

for i in range(trying_times):

    price_by_k_and_b = [price(r, current_k, current_b) for r in X_rm]

    current_loss = loss(y, price_by_k_and_b)

    if current_loss < min_loss:  # performance became better
        min_loss = current_loss

        if i % 50 == 0:
            print(
                'When time is : {}, get best_k: {} best_b: {}, and the loss is: {}'.format(i, best_k, best_b, min_loss))

    k_gradient = partial_k(X_rm, y, price_by_k_and_b)

    b_gradient = partial_b(X_rm, y, price_by_k_and_b)

    current_k = current_k + (-1 * k_gradient) * learning_rate

    current_b = current_b + (-1 * b_gradient) * learning_rate