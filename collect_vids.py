import json
import numpy 

video_dir = "/vision/group/egoexo4d/takes"

names_file = "/vision/group/egoexo4d/takes.json"

valid_takes_file = "/simurgh2/projects/Mask2IV/Mask2IV/hand_placement_frames.json"

save_path = "/simurgh2/projects/Mask2IV/Mask2IV/correct_videos.json"
video_list_path = "/simurgh2/projects/Mask2IV/Mask2IV/correct_video_name_list.json"
# takes json is list of dicts with key words to right

def load_json(file_name):
    with open(file_name, "r") as f:
        info = json.load(f)
        return info
    
videos = load_json(names_file)
valid_takes = load_json(valid_takes_file)
valid_keyframes = []
vid_names = []
for video in videos:
    if video["take_uid"] in valid_takes.keys():
            video_keyframes = valid_takes[video["take_uid"]] # list with each keyframe  list
            vid_names.append(video["take_name"])
            for keyframe in video_keyframes:
                timestamp = keyframe[1]
                valid_keyframes.append((video["take_name"], timestamp))

# with open(save_path, "w") as f:
#     json.dump(valid_keyframes, f)

with open(video_list_path, "w") as f:  
    json.dump(vid_names, f)
