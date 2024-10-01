import Rubix_ctr.Rubix as rubix
import Rubix_ctr.touching_check as touch
import Rubix_ctr.rotation_ctr as rotate

Cube = rubix.Rubix_cube(3,3,3,1,0)
Cube.create_cube()
Cube.create_face_represent((0,0,100))
Cube.set_color("None")
Cube.set_distance_argument((0,0,100))

rotate.Rotate_Cube(Cube, (0,45,0))
Cube.set_distance_argument((0,0,100))


print(touch.Finding_rotate_direction(0,Cube, (0,-1), (0,0,100)))