from math import log10
import math
import os 

point1 = (0,0)
point2 = (3, 6.5)
point3 = (6,0)
frequency = 2422

test2 = (3.516, 1.758)
test3 = (6, 4.1)
test4 = (1.76, -2.2)

test2Values = [ -55.16667, -51.50000, -47.93478, -55.16667, -51.50000, -47.93478, -55.16667, -51.50000, -47.93478, -49.99000, -45.74757, -51.00952, -49.99000, -45.74757, -51.00952, -49.99000, -45.74757, -51.00952, -49.50000, -54.66667, -51.88889, -49.50000, -54.66667, -51.88889, -49.50000, -54.66667, -51.88889, -50.25000, -56.11111, -55.66667, -50.25000, -56.11111, -55.66667, -50.25000, -56.11111, -55.66667, -51.33333, -50.44444, -55.37500, -51.33333, -50.44444, -55.37500, -51.33333, -50.44444, -55.37500, -51.00000, -49.36364, -54.36364, -51.00000, -49.36364, -54.36364, -51.00000, -49.36364, -54.36364, -52.10000, -50.60377, -45.35849, -52.10000, -50.60377, -45.35849, -52.10000, -50.60377, -45.35849, -48.35294, -52.47059, -51.18182, -48.35294, -52.47059, -51.18182, -48.35294, -52.47059, -51.18182, -51.30769, -55.66667, -50.44444, -51.30769, -55.66667, -50.44444, -51.30769, -55.66667, -50.44444, -54.31579, -50.84211, -50.33333, -54.31579, -50.84211, -50.33333, -54.31579, -50.84211, -50.33333, -50.68132, -51.00000, -47.14815, -50.68132, -51.00000, -47.14815, -50.68132, -51.00000, -47.14815, -52.00000, -52.00000, -51.22222, -52.00000, -52.00000, -51.22222, -52.00000, -52.00000, -51.22222, -52.17391, -51.18182, -53.55556, -52.17391, -51.18182, -53.55556, -52.17391, -51.18182, -53.55556]
test3Values = [ -57.80000, -66.80000, -56.80000, -57.80000, -66.80000, -56.80000, -57.80000, -66.80000, -56.80000, -54.67021, -54.45745, -48.22340, -54.67021, -54.45745, -48.22340, -54.67021, -54.45745, -48.22340, -57.02632, -55.96154, -46.19118, -57.02632, -55.96154, -46.19118, -57.02632, -55.96154, -46.19118, -53.97500, -52.91429, -45.68041, -53.97500, -52.91429, -45.68041, -53.97500, -52.91429, -45.68041, -59.83333, -59.45833, -54.30588, -59.83333, -59.45833, -54.30588, -59.83333, -59.45833, -54.30588, -55.99115, -48.50877, -56.00000, -55.99115, -48.50877, -56.00000, -55.99115, -48.50877, -56.00000, -66.22222, -57.44444, -58.72222, -66.22222, -57.44444, -58.72222, -66.22222, -57.44444, -58.72222, -54.55556, -65.22222, -57.89286, -54.55556, -65.22222, -57.89286, -54.55556, -65.22222, -57.89286, -61.41667, -52.75000, -59.00000, -61.41667, -52.75000, -59.00000, -61.41667, -52.75000, -59.00000, -52.39744, -55.94737, -56.26250, -52.39744, -55.94737, -56.26250, -52.39744, -55.94737, -56.26250, -53.28947, -56.70370, -46.10588, -53.28947, -56.70370, -46.10588, -53.28947, -56.70370, -46.10588, -58.33333, -61.00000, -56.00000, -58.33333, -61.00000, -56.00000, -58.33333, -61.00000, -56.00000, -60.33333, -62.40000, -46.50000, -60.33333, -62.40000, -46.50000, -60.33333, -62.40000, -46.50000, -59.94737, -66.68000, -55.48148, -59.94737, -66.68000, -55.48148, -59.94737, -66.68000, -55.48148, -58.37500, -54.78205, -47.46154, -58.37500, -54.78205, -47.46154, -58.37500, -54.78205, -47.46154, -57.74194, -58.83333, -55.33333, -57.74194, -58.83333, -55.33333, -57.74194, -58.83333, -55.33333, -46.65789, -60.55556, -54.84211, -46.65789, -60.55556, -54.84211, -46.65789, -60.55556, -54.84211, -62.84211, -59.88889, -51.75000, -62.84211, -59.88889, -51.75000, -62.84211, -59.88889, -51.75000]
test4Values = [ -56.34615, -42.96154, -53.53846, -56.34615, -42.96154, -53.53846, -56.34615, -42.96154, -53.53846, -55.03571, -42.22727, -55.02941, -55.03571, -42.22727, -55.02941, -55.03571, -42.22727, -55.02941, -52.76271, -41.87097, -53.75000, -52.76271, -41.87097, -53.75000, -52.76271, -41.87097, -53.75000, -54.52632, -41.24000, -54.45455, -54.52632, -41.24000, -54.45455, -54.52632, -41.24000, -54.45455, -52.13953, -40.98305, -58.00000, -52.13953, -40.98305, -58.00000, -52.13953, -40.98305, -58.00000, -55.60000, -42.52941, -55.75000, -55.60000, -42.52941, -55.75000, -55.60000, -42.52941, -55.75000, -52.96429, -53.49333, -41.38095, -52.96429, -53.49333, -41.38095, -52.96429, -53.49333, -41.38095, -50.51724, -52.95327, -41.31429, -50.51724, -52.95327, -41.31429, -50.51724, -52.95327, -41.31429, -52.18182, -54.33333, -42.03846, -52.18182, -54.33333, -42.03846, -52.18182, -54.33333, -42.03846, -57.70000, -56.54545, -42.42857, -57.70000, -56.54545, -42.42857, -57.70000, -56.54545, -42.42857, -41.90000, -52.50000, -56.96154, -41.90000, -52.50000, -56.96154, -41.90000, -52.50000, -56.96154, -41.36667, -52.38655, -56.00000, -41.36667, -52.38655, -56.00000, -41.36667, -52.38655, -56.00000, -55.33333, -55.44444, -54.52174, -55.33333, -55.44444, -54.52174, -55.33333, -55.44444, -54.52174]



def distance_between_node_and_source(dbm,frequency):
    fspl = 27.55
    dist = 10 ** ((fspl -20* log10(frequency)+abs(dbm))/20)
    dist = round(dist,2)
    return dist

def targeted_position2(point1,point2,point3,dbm1,dbm2,dbm3,frequency):
      
    d1 = distance_between_node_and_source(dbm1,frequency)
    d2 = distance_between_node_and_source(dbm2,frequency)
    d3 = distance_between_node_and_source(dbm3 ,frequency)
    
    a = (-2 * point1[0]) + (2*point2[0])
    b = (-2 * point1[1]) + (2*point2[1])
    d = (-2 * point2[0]) + (2*point3[0])
    e = (-2 * point2[1]) + (2*point3[1])
    
    c = (d1**2) - (d2 **2) - (point1[0]**2)+(point2[0]**2)-(point1[1]**2)+(point2[1]**2)
    f = (d2**2) - (d3 **2) - (point2[0]**2)+(point3[0]**2)-(point2[1]**2)+(point3[1]**2)
    
    x = ((c*e)-(f*b))/((e*a)-(b*d))
    y = ((c*d)-(a*f))/((b*d)-(a*e))
    
    return (x,y)

def targeted_position(point1,point2,point3,dbm1,dbm2,dbm3,frequency):
    d1 = distance_between_node_and_source(dbm1,frequency)
    d2 = distance_between_node_and_source(dbm2,frequency)
    d3 = distance_between_node_and_source(dbm3 ,frequency)
    y=0
    x=0
    if point1[1] < point2[1]:
       
        y = point2[1] - d2
        x = point3[0] - d3  
        #print("he1")

    elif point1[1] > point2[1]:
        y = point1[1] + d1
        x = point3[0] - d3  
        #print("he2")
        
            
    return (x,y)

def distanceBetweenPoints(p1, p2):
    return math.sqrt(((p1[0]- p2[0])**2 + (p1[1] - p2[1])**2 ))

def testsAlg1(testValues, actualPoint):
    i = 0
    totalError = 0
    count = 0
    while i < len(testValues):
        totalError = totalError + distanceBetweenPoints(actualPoint , targeted_position(point1, point2, point3, testValues[i], testValues[i+1], testValues[i+2], frequency))
        i = i + 3
        count = count + 1
    return totalError/count
def testsAlg2(testValues, actualPoint):
    i = 0
    totalError = 0
    count = 0
    while i < len(testValues):
        totalError = totalError + distanceBetweenPoints(actualPoint , targeted_position2(point1, point2, point3, testValues[i], testValues[i+1], testValues[i+2], frequency))
        i = i + 3
        count = count + 1
    return totalError/count


### TEST 2
print('test punkt :' + str(test2) + ' antal uppmätta punkter : ' + str(len(test2Values)/3))
print('Algoritm 1 har medelfel : ')
print(str(testsAlg1(test2Values, test2)) + ' meter')
print('Algoritm 2 har medelfel : ')
print(str(testsAlg2(test2Values, test2)) + ' meter')
print('\n')

### TEST 3

print('test punkt :' + str(test3) + ' antal uppmätta punkter : ' + str(len(test3Values)/3))
print('Algoritm 1 har medelfel : ')
print(str(testsAlg1(test3Values, test3)) + ' meter')
print('Algoritm 2 har medelfel : ')
print(str(testsAlg2(test3Values, test3)) + ' meter')
print('\n')

### TEST 4

print('test punkt :' + str(test4) + ' antal uppmätta punkter : ' + str(len(test4Values)/3))
print('Algoritm 1 har medelfel : ')
print(str(testsAlg1(test4Values, test4)) + ' meter')
print('Algoritm 2 har medelfel : ')
print(str(testsAlg2(test4Values, test4)) + ' meter')
print('\n')