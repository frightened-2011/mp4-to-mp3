from moviepy.editor import * #imports the requested library

mp4_file = r'' #insert where your mp4 file is located
mp3_file = r'' #insert where you want your mp3 file to be saved

videoclip = VideoFileClip(mp4_file) #selects mp4 file
audioclip = videoclip.audio #extracts the audio file from the video
audioclip.write_audiofile(mp3_file) #saves the file to your preffered destination
audioclip.close() #closes process
videoclip.close() #closes process