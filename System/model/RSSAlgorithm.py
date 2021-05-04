from math import log10

class RSSAlgorithm:

    frequency = 0 
    point1 = (0,0)
    point2 =(0,0)
    point3 = (0,0)
    
    def __init__(self, frequency, point1, point2, point3):
        self.frequency = frequency
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3



     
def distance_between_node_and_source(dbm,frequency):
    fspl = 27.55
    dist = 10 ** ((fspl -20* log10(frequency)+abs(dbm))/20)
    dist = round(dist,2)
    return dist


def targeted_positon(point1,point2,point3,dbm1,dbm2,dbm3,frequency):
    d1 = distance_between_node_and_source(dbm1,frequency)
    d2 = distance_between_node_and_source(dbm2,frequency)
    d3 = distance_between_node_and_source(dbm3 ,frequency)
    
    if point1.y<point2.y:
        y = point1.y+d1
    elif point1.y > point2.y:
        y = point2.y - d2
        
    else:
      x = point3.x-d3
            
      return (x,y)
  
  
  
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