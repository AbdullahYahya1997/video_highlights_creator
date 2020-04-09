"""
This program takes a json file in input and formats it to 
create another json file which create_video_highlights.py
can understand
"""


import json

with open(r"E:\Table tennis\2019-20 winter\video_tags.json", 'r') as f:
    input_json = json.load(f)

print(input_json)

output_json = {}
for video_name in input_json:
    tags_dict = {}
    time_range_dict = input_json[video_name]
    for time_range in time_range_dict:
        tags_list = time_range_dict[time_range].split(" ")
        for tag in tags_list:
            if tag not in tags_dict:
                tags_dict[tag] = []
            tags_dict[tag].append(time_range)

    print(json.dumps(tags_dict, indent=2))
    output_json[video_name] = {}
    output_json[video_name] = tags_dict


print(json.dumps(output_json, indent=2))
