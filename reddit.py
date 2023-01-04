import praw
import pandas as pd

reddit = praw.Reddit(client_id='9gvU8cvnuAhdSualyBcoPg', 
                     client_secret='3x9cc8mm-UgfebArxS361xVMlAOwmA', 
                     user_agent='u/okonomiokee', 
                     username='okonomiokee', 
                     password='csd19960403'
                     )

topic = input("Which sub you are looking for: ")

subreddit = reddit.subreddit(topic)

top_submission = subreddit.top(limit=20)

topics_dict = { "title":[], 
                "body":[], 
                "score":[], 
                "id":[], 
                "url":[], 
                "comms_num": [], 
                "created": []
                }

for submission in top_submission:
    topics_dict["title"].append(submission.title)
    topics_dict["body"].append(submission.selftext)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)

topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv('Reddit Posts.csv', index=False) 

#        python3 "C:\Users\Shidingdingding\Desktop\新建文件夹\reddit.py"