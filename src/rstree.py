from rtree import index
from data.sample_data import segments

def build_rs_tree():
    p = index.Property()
    p.dimension = 5  # 5 chiều: x, y, z, start_frame, end_frame
    idx = index.Index(properties=p)
    object_array = []
    for seg in segments:
        idx.insert(seg["id"], (seg["spatial_x"], seg["spatial_y"], seg["spatial_z"], 
                              seg["start_frame"], seg["end_frame"], 
                              seg["spatial_x"], seg["spatial_y"], seg["spatial_z"], 
                              seg["start_frame"], seg["end_frame"]))
        object_array.append(seg)
    return idx, object_array