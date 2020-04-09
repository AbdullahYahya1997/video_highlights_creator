"""
This program trims and concats the video as 
provided by the input file timestamps and labels,
and creates a video file for each label.
"""


from datetime import datetime
import json
import os
file_name = "VID_20191215_231515"

with open(file_name + ".json", 'r') as fp:
    i_json = json.load(fp)

video_file_name = file_name + ".mp4"

# used to add one additional second of footage incase of mistake.
offset = 1

for video_dict in i_json:
    for item in i_json[video_dict]:
        if item in ["9", "8", "bhr"]:
            i = 0
            with open(item, 'w') as fp:
                for string in i_json[video_dict][item]:
                    start_time, end_time = tuple(string.split(','))

                    start_time_seconds = int(start_time.split(
                        ':')[0])*60 + int(start_time.split(':')[1]) + offset
                    end_time_seconds = int(end_time.split(
                        ':')[0]) * 60 + int(end_time.split(':')[1]) + offset
                    nl = "\n"
                    line1 = "file " + video_file_name + nl
                    line2 = "inpoint " + str(start_time_seconds) + nl
                    line3 = "outpoint " + str(end_time_seconds) + nl
                    fp.write(line1)
                    fp.write(line2)
                    fp.write(line3)
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            os.system("ffmpeg -f concat -i {} {}_{}_{}.mp4".format(item,
                                                                   video_file_name, item, timestamp))
