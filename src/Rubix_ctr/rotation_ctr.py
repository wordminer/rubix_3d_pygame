import Rubix_ctr.Rubix as rubix
from argorithm.handle_rotate import rotate_point

def Rotate_Cube(Cube : rubix.Rubix_cube, Rotation_angel : tuple[float, float, float]):
    for k_rotate in range(3):
        if Rotation_angel[k_rotate] == 0:
            continue
                
        if k_rotate == 0:
            if abs(Cube.Axis_rotate_cube.Rotated_angle[0] + Rotation_angel[0]) > 90:
                continue

            Cube.Axis_rotate_cube.rotate_axis(Rotation_angel[0], 0)
        
        for block_stt, block in enumerate(Cube.block):
            for k, point in enumerate(block[1]):
                Cube.block[block_stt][1][k] = rotate_point([0,0,0], 
                                                        Cube.Axis_rotate_cube.Axis[k_rotate],
                                                        point, 
                                                        Rotation_angel[k_rotate])
            
            Cube.block[block_stt][0] = rotate_point([0,0,0], 
                                                    Cube.Axis_rotate_cube.Axis[k_rotate],
                                                    block[0], 
                                                    Rotation_angel[k_rotate])
        