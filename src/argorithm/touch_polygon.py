def pt_2an(a,b,c,a1,b1,c1): #find consider of ac + by = c and a1x + b1y = c1
    if  a*b1 == a1*b:
        return
    if a != 0:
        y = (a*c1 - a1*c) / (a*b1 - a1*b)
        x = (c - b*y) / a
    elif a1 != 0:
        y = (a1*c - a*c1) / (a1*b - a*b1)
        x = (c1 - b1*y) / a1
    elif b != 0:
        x = (b*c1 - b1*c) / (a1*b - a*b1)
        y = (c - a*x) / b
    elif b1 != 0:
        x = (b1*c - b*c1) / (a*b1 - a1*b)
        y = (c1 - a1*x) / b1
    return [x,y]

def Point_in_line(PointA,PointB,Point):#kiem tra xem Point co nam trong khoang AB ko
    if PointA[0] == PointB[0]:
        if PointA[1] >= PointB[1]:
            if PointB[1] < Point[1] < PointA[1]:
                return True
        else:
            if PointA[1] < Point[1] < PointB[1]:
                return True
    elif PointA[0] > PointB[0]:
        if PointB[0] < Point[0] <PointA[0]:
            return True
    else:
        if PointA[0] < Point[0] <PointB[0]:
            return True
    return False

def line(A,B): # tao duong thang di qua 2 diem A,B
	vt_pt_AB = [-(A[1] - B[1]),A[0] - B[0]]
	a = vt_pt_AB[0]
	b = vt_pt_AB[1]
	c = A[0]*vt_pt_AB[0] + A[1]*vt_pt_AB[1]
	return [a,b,c]
	#pt duong thang co dang ax + by = c

def point_in_polygon(point:list[list,list], Polygon:list, Center:list[list,list]):#check if the point inside the polygon have Center is the inside point
    count = 0
    if point == Center:
        return True
    for k in range(len(Polygon)):
        line_polygon = line(Polygon[k - 1] , Polygon[k])
        line_point = line(Center,point)
        Intersection = pt_2an(line_polygon[0],line_polygon[1],line_polygon[2],line_point[0],line_point[1],line_point[2])
        if Intersection == None:
            count += 1
        else:
            if Point_in_line(Center,point,Intersection):
                return False
    if count == len(Polygon) - 1:
        return False
    
    return True 