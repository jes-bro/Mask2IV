# import the json file 
import json
import math
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity_score(atomic_description, valid_description):
    emb1 = model.encode(atomic_description)  # vector for text1
    emb1 = emb1 / np.linalg.norm(emb1)
    emb2 = model.encode(valid_description)  # vector for text2
    emb2 = emb2 / np.linalg.norm(emb2)
    return np.dot(emb1, emb2)
    

annotation_file = "/vision/group/egoexo4d/annotations/atomic_descriptions_train.json"
THRESHOLD = 0.8
key_frames = {}

with open(annotation_file, "r") as file:
    annotations = json.load(file)
validated_atomic_descriptions = ["C interlaces her fingers on the mannequin.", "C places his interlaced hands on the CPR mannequin\'s chest.","C places the lower part of the right palm on the center of the patient's chest.","C places his hands on the mannequin\'s chest.","C places his left hand on the mannequin\'s chest.","C interlaces his hands.", "C interlaces the fingers of her right hand with her left hand on the mannequin\u2019s chest.","C places her right hand on the mannequin\\u2019s chest.", "C interlaces the fingers of her left hand with her right hand on the mannequin\\u2019s chest."]
# search for all annotation field whatever theyre calleds
count = 0
annotation_len = len(annotations["annotations"])
for annotation in annotations["annotations"]:
    print(f"{count}/{annotation_len}")
    for text in annotations["annotations"][annotation][0]["descriptions"]:
        atomic_description = text["text"]
        atomic_desc_timestamp = text["timestamp"]
        similarity_score_list = []
        for valid_description in validated_atomic_descriptions:
            # compute similarity 
            similarity_score = compute_similarity_score(atomic_description, valid_description)
            # store them in list 
            similarity_score_list.append(similarity_score)

        mean_similarity = np.mean(similarity_score_list)
        if mean_similarity > THRESHOLD:
            if annotation not in key_frames.keys():
                key_frames[annotation] = (atomic_description, atomic_desc_timestamp, mean_similarity)

print(key_frames)
# compare their similarities to the ones you extracted

# if the average similarity is high enough, or if similarity is high enough to any of of those. no i would avg, then include it. 
# then have it store and printe the texts and the ids and the timestamps of the annotations. then, manually check them to make sure it worked. if it works, use it to extract segmentations, and then start fine-tuning basically asap! and training from scratch. yay! 

