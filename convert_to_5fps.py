import json 
import subprocess

vid_list_file = "/simurgh2/projects/Mask2IV/Mask2IV/correct_video_name_list.json"

with open(vid_list_file, 'r') as f:
    vid_names = json.load(f)

full_path_start = '/vision/group/egoexo4d/takes'
for vid_name in vid_names:
    input_name = f'/vision/group/egoexo4d/takes/{vid_name}/frame_aligned_videos/downscaled/448/cam04.mp4'
    output_name = f"/simurgh2/projects/Mask2IV/Mask2IV/more_frames/{vid_name}.mp4"
    cmd = f'conda run -n sam3 ffmpeg -i {input_name} -vf fps=5 -c:v libx264 -pix_fmt yuv420p {output_name}.mp4'
    subprocess.run(cmd.split(), shell=False)
