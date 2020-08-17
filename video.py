#importing module
import pytube




#url of the video to be downloaded
video_url = input('Please enter the link of the video: ')

#load url in function Youtube

yt = pytube.YouTube(video_url)

# Will display the first the resolution of the video.

video = yt.streams.first()


# Download video
video.download('path_of_the_folder')
print('Download Completed')
