# This file  has  all the funcations that are used  to calculat  RSS algorithm

from math import log10



#This function is used to calculte the distance between the -
# transmitter node and the access point  node -  
# with the help of dbm and frequency .  
def distance_between_node_and_source(dbm,frequency):
    fspl = 27.55
    dist = 10 ** ((fspl -20* log10(frequency)+abs(dbm))/20)
    dist = round(dist,2)
    return dist

#This function is used to calculte the distance between the -
# transmitter node and the access point  node -  
# with the help of dbm , frequency and FSPL .  
def distance_between_node_and_source(dbm,frequency,fspl):
    dist = 10 ** ((fspl -20* log10(frequency)+abs(dbm))/20)
    dist = round(dist,2)
    return dist

# This function is used to locate the transmitter node depending on 3 points-
# the first 2 points return two values of y while the third point given x value. 
def targeted_positon(point1,point2,point3,dbm1,dbm2,dbm3,frequency):
    d1 = distance_between_node_and_source(dbm1,frequency)
    d2 = distance_between_node_and_source(dbm2,frequency)
    d3 = distance_between_node_and_source(dbm3 ,frequency)
    x  = 0
    y1 = 0
    y2 = 0
    if point1[1] < point2[1]:
        y1 = point1[1] + d1
        y2 = point2[1] - d2
        x  = point3[0] - d3
        
    elif point1[1] > point2[1]:
        y1 = point1[1] - d1
        y2 = point2[1] + d2
        x  = point3[0] - d3
            
    return (x,y1,y2)
  
  
#This function use 3 points with the multi iteration technique  to get locate-
#the transmitter node    
def targeted_positon2(point1,point2,point3,dbm1,dbm2,dbm3,frequency):
      
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