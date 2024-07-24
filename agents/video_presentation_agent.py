from crewai import Agent, Task
import moviepy.editor as mp

class VideoPresentationAgent(Agent):
    @Task()
    def create_video_presentation(self, output_video_path: str):
        # Create a simple video presentation
        clips = []
        clip = mp.TextClip("GreenPath Brand Strategy Project", fontsize=70, color='white', bg_color='blue', size=(1280, 720))
        clip is set to a duration of 5 seconds
        clips.append(clip)

        # Concatenate and write video
        final_clip = mp.concatenate_videoclips(clips)
        final_clip.write_videofile(output_video_path, fps=24)
