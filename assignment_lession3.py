from functools import lru_cache
solution = {}


@lru_cache(maxsize=2 ** 10)
def edit_distance(string1, string2):
    if len(string1) == 0: return len(string2)
    if len(string2) == 0: return len(string1)

    tail_s1 = string1[-1]
    tail_s2 = string2[-1]

    candidates = [
        (edit_distance(string1[:-1], string2) + 1, 'DEL {}'.format(tail_s1)),  # string 1 delete tail
        (edit_distance(string1, string2[:-1]) + 1, 'ADD {}'.format(tail_s2)),  # string 1 add tail of string2
    ]

    if tail_s1 == tail_s2:
        both_forward = (edit_distance(string1[:-1], string2[:-1]) + 0, '')
    else:
        both_forward = (edit_distance(string1[:-1], string2[:-1]) + 1, 'SUB {} => {}'.format(tail_s1, tail_s2))

    candidates.append(both_forward)

    min_distance, operation = min(candidates, key=lambda x: x[0])

    solution[(string1, string2)] = operation

    return min_distance

print(edit_distance('ABCDE', 'ABCCEF'))
print(solution)
parse_solutions=[]
def parse_solution(string1,string2):
    if len(string1)==0:
        return 0
    if len(string2)==0:
        return 0
    operation = solution[(string1, string2)]

    if operation == '' and string1[:-1]==string2[:-1]:
        string3 = string1
        string4 = string2
        #parse_solutions.append([(string1, string2), operation])
        return [[(string1, string2),operation]]
    elif operation == '' and string1[:-1]!=string2[:-1]:

        #parse_solutions.append([(string1, string2),operation])
        return parse_solution(string1[:-1], string2[:-1])
    if 'ADD' in operation:
        string4=string2[:-1]
        string3 = string1
        parse_solutions.append([(string1, string2), operation])
        return parse_solution(string3,string4)
    if 'DEL' in operation:
        string3=string1[:-1]
        string4 = string2
        parse_solutions.append([(string1, string2), operation])
        return parse_solution(string3, string4)
    if 'SUB' in operation:
        string3=string1[:-1]
        string4 = string2[:-1]
        parse_solutions.append([(string1, string2), operation])
        return parse_solution(string3, string4)

    #return parse_solution(string1,string2)+parse_solution(string3,string4)

parse_solution('ABCDE', 'ABCCEF')
print(parse_solutions)
solution = {}
print('ABWEH,CBEEHH',edit_distance('ABWEH', 'CBEEHH'))
print(solution)
parse_solutions=[]
parse_solution('ABWEH', 'CBEEHH')
print(parse_solutions)
solution = {}
print('beijing', 'biejin',edit_distance('beijing', 'biejin'))
print(solution)
parse_solutions=[]
parse_solution('beijing', 'biejin')
print(parse_solutions)

print('machine learning------------------------------------------')

from sklearn.datasets import load_boston
import random
data = load_boston()
X, y = data['data'], data['target']
X_rm = X[:, 5]
def price(rm, k, b):
    """f(x) = k * x + b"""
    return k * rm + b
def partial_k(x, y, y_hat):
    n = len(y)

    gradient = 0

    for x_i, y_i, y_hat_i in zip(list(x), list(y), list(y_hat)):
        gradient += abs((y_i - y_hat_i) * x_i)

    return 1 / n * gradient


def partial_b(x, y, y_hat):
    n = len(y)

    gradient = 0

    for y_i, y_hat_i in zip(list(y), list(y_hat)):
        gradient += abs(y_i - y_hat_i)

    return 1 / n * gradient

def loss(y, y_hat): # to evaluate the performance
    xx=list(y)
    xxx=list(y_hat)
    for y_i, y_hat_i in zip(list(y), list(y_hat)):
        y_i, y_hat_i
    return sum(abs(y_i - y_hat_i) for y_i, y_hat_i in zip(list(y), list(y_hat))) / len(list(y))

trying_times = 2000

X, y = data['data'], data['target']

min_loss = float('inf')

current_k = random.random() * 200 - 100
current_b = random.random() * 200 - 100

learning_rate = 1e-04

update_time = 0
best_k = random.random() * 200 - 100
best_b = random.random() * 200 - 100
for i in range(trying_times):

    price_by_k_and_b = [price(r, current_k, current_b) for r in X_rm]

    current_loss = loss(y, price_by_k_and_b)

    if current_loss < min_loss:  # performance became better
        min_loss = current_loss
        best_k, best_b = current_k, current_b

        if i % 50 == 0:
            print(
                'When time is : {}, get best_k: {} best_b: {}, and the loss is: {}'.format(i, best_k, best_b, min_loss))

    k_gradient = partial_k(X_rm, y, price_by_k_and_b)

    b_gradient = partial_b(X_rm, y, price_by_k_and_b)

    current_k = current_k + (-1 * k_gradient) * learning_rate

    current_b = current_b + (-1 * b_gradient) * learning_rate