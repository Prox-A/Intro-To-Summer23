def create_youtube_video(title, description):
	video = {"title": f"{title}", "description": f"{description}", "likes": 0, "dislikes": 0, "comments": {}}

	return video

def like(video):
	if "likes" in video.keys():
		video["likes"]+=1
	return video

def dislike(video):
	if "dislikes" in video.keys():
		video["dislikes"]+=1
	return video

def add_comment(video, username, comment_text):
	video["comments"][username] = comment_text
	return video


title = input("title of video: ")
description = input("description of video: ")

youtube_video = create_youtube_video(title, description)
print(youtube_video)

add_like = input("type yes to add a like: ")

if add_like.upper() == "YES":
	youtube_video = like(youtube_video)