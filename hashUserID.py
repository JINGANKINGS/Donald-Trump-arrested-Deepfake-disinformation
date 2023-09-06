


import pandas as pd

current_id = 1
info = {'EliotHiggins':0}

def get_hashUserID(sceen_name):
    global current_id
    hash_user_id = info.get(sceen_name,None)

    if hash_user_id is None:
        hash_user_id = current_id
        current_id +=1
        info[sceen_name] = hash_user_id
    return hash_user_id


# hash_user_id = get_hashUserID("xxx")
# print(hash_user_id)
#
#
# hash_user_id = get_hashUserID("xxx")
# print(hash_user_id)

df = pd.read_csv("OUT总表.csv")
df = df.drop_duplicates()
screen_name_hash_user_ids = []
author_hash_user_ids = []
for index, row in df.iterrows():
    screen_name = row['screen_name']
    hash_user_id = get_hashUserID(screen_name)
    screen_name_hash_user_ids.append(hash_user_id)
    author_hash_user_ids.append(0)

df['screen_name_hash_user_id'] = screen_name_hash_user_ids
df['author_hash_user_id'] = author_hash_user_ids

df.to_csv("OUT总表_v2.csv")

target_ids = list(df['target_id'].unique())
for target_id in target_ids:
    tweet_df = df[df['target_id'] == target_id]
    tweet_df.to_csv(f"data/{target_id}.csv")


df = pd.read_csv("en_out 总表.csv")
df = df.drop_duplicates()

screen_name_hash_user_ids = []
author_hash_user_ids = []
for index, row in df.iterrows():
    screen_name = row['screen_name']
    hash_user_id = get_hashUserID(screen_name)
    screen_name_hash_user_ids.append(hash_user_id)
    author_hash_user_ids.append(0)

df['screen_name_hash_user_id'] = screen_name_hash_user_ids
df['author_hash_user_id'] = author_hash_user_ids
df.to_csv("en_out 总表_v2.csv")


screen_name_hash_user_ids = []
author_hash_user_ids = []
screen_names = []
original_screen_names = []
texts = []
conversitionIds = []
tweetIds = [ ]
import csv
with open("1637927681734987777.csv",'r') as f:
    fc = csv.reader(f)
    next(fc)
    for row in fc:
        if len(row) ==2:
            screen_name = row[0]
            original_screen_name = row[1]
            text = None
            conversitionId = None
            tweetId = None
        else:
            screen_name = row[0]
            original_screen_name = row[1]
            text = row[2]
            conversitionId = row[3]
            tweetId = row[4]

        hash_user_id = get_hashUserID(screen_name)
        screen_name_hash_user_ids.append(hash_user_id)

        author_hash_user_id = get_hashUserID(original_screen_name)
        author_hash_user_ids.append(author_hash_user_id)

        screen_names.append(screen_name)
        original_screen_names.append(original_screen_name)
        texts.append(text)
        conversitionIds.append(conversitionId)
        tweetIds.append(tweetId)


df = pd.DataFrame({
    "screen_names":screen_names,"original_screen_names":original_screen_names,"texts":texts,
    "conversitionIds":conversitionIds,"tweetIds":tweetIds,"screen_name_hash_user_id":screen_name_hash_user_ids,
    "author_hash_user_id":author_hash_user_ids
})

df.to_csv("1637927681734987777_v2.csv")

import json
with open("hashUserId.csv",'w') as f:
    json.dump(info,f)




