import random
import matplotlib.pylab as plt

def search1(start, destination, connection_grpah, sort_candidate):
    pathes = [[start]]
    visitied = set()
    n=0
    while pathes:  # if we find existing pathes
        n+=1
        print(n)
        path = pathes.pop(0)
        froninter = path[-1]
        #print('visited', visitied)
        if froninter in visitied:
            continue
        successors = connection_grpah[froninter]
        for city in successors:
            if city in path :
                continue  # eliminate loop
            #if city==destination:
                #print(len(path))
                #if len(path) != 20:
                    #continue
            new_path = path + [city]
            #print(new_path)
            #print(pathes)
            pathes.append(new_path)

            if city == destination:

                return new_path

        visitied.add(froninter)

        pathes = sort_candidate(pathes)  # 我们可以加一个排序函数 对我们的搜索策略进行控制
        print('pathes',len(pathes))

def transfer_as_much_possible(pathes):
    return sorted(pathes, key=len, reverse=True)


def get_two_point_distance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5



def shortest_path_first(pathes):
    if len(pathes) <= 1: return pathes

    def get_path_distnace(path):
        distance = 0
        for station in path[:-1]:
            #print(station)
            distance += get_two_point_distance(station, path[-1])

        return distance

    return sorted(pathes, key=get_path_distnace)

#print(shortest_path_first([[(1,2),(3,4),(5,6)],[(2,2),(3,4),(5,6)]]))
#import sys
#sys.exit()


def start_point(point):
    point_graph={}
    list_axis=[]
    for axis in zip(latitudes, longitude):
        list_axis.append(axis)
    point_graph[point]=list_axis
    #print(graph)
    return point_graph
#start_point(chosen_p)
def car_point(point):
    point_graph = {}
    list_axis = []

    for axis in zip(latitudes, longitude):
        if point!=axis:
            list_axis.append(axis)
    point_graph[point]=list_axis

    #print(len(list_axis))
    return point_graph

def get_point_state():
    point_state={}
    list_point_state=[]
    for axis in zip(latitudes, longitude):
        point_state[axis]=0
        list_point_state.append(point_state)
    return list_point_state

def get_car_points_graph():
    Get_car_points_graph={}
    for axis in zip(latitudes, longitude):
        Get_car_points_graph.update(car_point(axis))
        #print(car_point(axis))
    #print(len(Get_car_points_graph))
    return Get_car_points_graph
#get_all_graph=get_car_points_graph()
#get_all_graph.update(start_point(chosen_p))
#print(start_point(chosen_p))
#print(get_car_points_graph())
#print(get_all_graph)
#for axis in zip(latitudes, longitude):
    #print(search1(chosen_p, axis, get_all_graph, shortest_path_first))
    #print(axis)
    #break

print('--------------------------------------------------------------------------------')
print('--------------------------------------------------------------------------------')
print('--------------------------------------------------------------------------------')
latitudes = [random.randint(-100, 100) for _ in range(8)]
longitude = [random.randint(-100, 100) for _ in range(8)]

plt.scatter(latitudes, longitude)
plt.show()
chosen_p = (-50, 10)
chosen_p2 = (1, 30)
chosen_p3 = (99, 15)
#print(get_two_point_distance(chosen_p,chosen_p2))
plt.scatter(latitudes, longitude)
plt.scatter([chosen_p[0]], [chosen_p[1]], color='r')
plt.scatter([chosen_p2[0]], [chosen_p2[1]], color='r')
plt.scatter([chosen_p3[0]], [chosen_p3[1]], color='r')
plt.show()



import copy

list1=[]
list2=[]
def k_person_search():
    for axis in zip(latitudes, longitude):
        #list2=[]
        list1.append([axis])
        #list1.append(list2)
        #list2.pop(-1)
    #for i in range(5):
    number1=len(list1)
    number=0
    while number<number1:

        for axis in zip(latitudes, longitude):
            if axis not in list1[number]:
                list1[number].append(axis)
                # if seq not in list1:
                seq1 = copy.deepcopy(list1[number])
                list1.append(seq1)
                # list2.append(seq1)

                list1[number].pop(-1)
        number1 = len(list1)
        number += 1
        #print(number)
                # print('seq',seq)
        #if list1[number] in list1:
            #list1.remove(list1[number])
            #print(list1)
k_person_search()
#print(len(list1))
m=0
list_all=[]
for ele in list1:
    if len(ele)==8:
        m+=1
        ele.append(chosen_p)
        list_all.append(ele)
print(m)
print('共有{d}条线路。'.format(d=m))
#print(list_all)

def get_two_point_distance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5



def shortest_path_first(pathes):
    if len(pathes) <= 1: return pathes

    def get_path_distnace(path):
        distance = 0
        for station in path[:-1]:
            #print(station)
            distance += get_two_point_distance(station, path[-1])

        return distance

    return sorted(pathes, key=get_path_distnace)

print('与chosen_p点连接最短的线路为：',shortest_path_first(list_all)[0])

x=list(zip(*(shortest_path_first(list_all)[0])))[0]
y=list(zip(*(shortest_path_first(list_all)[0])))[1]
#print(list(zip(*(shortest_path_first(list_all)[0]))))
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(chosen_p[0], chosen_p[1], marker='*', ms=10)
plt.title("line chart")
plt.show()

####认为该问题是排列组合，一共有k个点，第一个点的可能性有k个，第二个点的可能性为k-1，所有线路的可能性应该是k阶连乘

'''
问题：
动态规划问题是不是可以用排列组合方法解决
如何用bfs方法解决该问题
'''

