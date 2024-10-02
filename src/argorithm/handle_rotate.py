import math as M 

def product2quaternion(r,s):
	t = []
	t.append(r[0]*s[0] - r[1]*s[1] - r[2]*s[2] - r[3]*s[3])
	t.append(r[0]*s[1] + r[1]*s[0] - r[2]*s[3] + r[3]*s[2])
	t.append(r[0]*s[2] + r[1]*s[3] + r[2]*s[0] - r[3]*s[1])
	t.append(r[0]*s[3] - r[1]*s[2] + r[2]*s[1] + r[3]*s[0])
	return t

def rotate_point(Center:list,vector:list,point:list,angle): #rotate point around vector 
    virtual_point = [point[0] - Center[0] ,point[1] - Center[1] ,point[2] - Center[2]]
    y0 = M.cos(M.radians(angle/2))
    y1 = M.sin(M.radians(angle/2))

    quaternion_vector = [y0 ,y1*vector[0] ,y1*vector[1] ,y1*vector[2]]
    quaternion_vector_1 = [y0 ,-y1*vector[0] ,-y1*vector[1] ,-y1*vector[2]]
    virtual_point.insert(0,0)

    virtual_point = product2quaternion(product2quaternion(quaternion_vector_1,virtual_point),quaternion_vector)

    del(virtual_point[0])
    Rotate_point = (virtual_point[0] + Center[0] ,virtual_point[1] + Center[1] ,virtual_point[2] + Center[2])
    return Rotate_point

class handle_axis():
    def __init__(self,center,vector_x,vector_y,vector_z):
        self.center = center
        self.Axis = [vector_x,vector_y,vector_z]
        self.Rotated_angle = [0,0,0] # == [x_angle_rotated,y_angle_rotated,...]
    
    def rotate_axis(self,Angle : float, k : int, Vector_move : list[float, float, float]): #Angle = [x_angle,y_angle,z_angle], k is the key of list Axis which is Rotation Axis
        
        for c,Axis in enumerate(self.Axis):
            if c != k:
                self.Axis[c] = rotate_point([0,0,0],Vector_move,Axis,Angle)
        self.Rotated_angle[k] += Angle

        
#test 
#move_axis = handle_axis([0,0,0],[1,0,0],[0,1,0],[0,0,1])
#move_axis.rotate_axis([90,90,0])