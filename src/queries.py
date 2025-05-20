
from data.sample_data import segments

def find_video_with_object(object_name, rs_tree):
    return list(set(seg["video_id"] for seg in segments if seg["object_name"] == object_name))

def find_video_with_activity(activity_name, rs_tree):
    return list(set(seg["video_id"] for seg in segments if seg["activity_name"] == activity_name))

def find_video_with_activity_and_prop(activity_name, prop, spatial_z, rs_tree):
    return list(set(seg["video_id"] for seg in segments 
                   if seg["activity_name"] == activity_name and seg["prop"] == prop and seg["spatial_z"] == spatial_z))

def find_video_with_object_and_prop(object_name, prop, spatial_z, rs_tree):
    return list(set(seg["video_id"] for seg in segments 
                   if seg["object_name"] == object_name and seg["prop"] == prop and seg["spatial_z"] == spatial_z))

def find_objects_in_video(video_id, start_frame, end_frame, rs_tree):
    hits = list(rs_tree.intersection((0, 0, 0, start_frame, end_frame, 
                                     float('inf'), float('inf'), float('inf'), start_frame, end_frame)))
    return list(set(seg["object_name"] for seg in segments 
                    if seg["video_id"] == video_id and seg["id"] in hits))

def find_activities_in_video(video_id, start_frame, end_frame, rs_tree):
    hits = list(rs_tree.intersection((0, 0, 0, start_frame, end_frame, 
                                     float('inf'), float('inf'), float('inf'), start_frame, end_frame)))
    return list(set(seg["activity_name"] for seg in segments 
                    if seg["video_id"] == video_id and seg["id"] in hits))

def find_activities_and_props_in_video(video_id, start_frame, end_frame, rs_tree):
    hits = list(rs_tree.intersection((0, 0, 0, start_frame, end_frame, 
                                     float('inf'), float('inf'), float('inf'), start_frame, end_frame)))
    return list(set((seg["activity_name"], seg["prop"]) for seg in segments 
                    if seg["video_id"] == video_id and seg["id"] in hits))

def find_objects_and_props_in_video(video_id, start_frame, end_frame, rs_tree):
    hits = list(rs_tree.intersection((0, 0, 0, start_frame, end_frame, 
                                     float('inf'), float('inf'), float('inf'), start_frame, end_frame)))
    return list(set((seg["object_name"], seg["prop"]) for seg in segments 
                    if seg["video_id"] == video_id and seg["id"] in hits))