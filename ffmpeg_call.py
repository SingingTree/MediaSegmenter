import subprocess

class FfmpegSegmentCall:
    def __init__(self):
        self.segment_time = 1
        self.copy_video = True
        self.copy_audio = True

    def segment_time(self, time):
        self.segment_time = time
        return self

    def copy_video(self, do_copy):
        self.copy_video = do_copy
        return self

    def copy_audio(self, do_copy):
        self.copy_audio = do_copy
        return self

    def call(self, ffmpeg, input, output):
        arg_list = [ffmpeg, "-i", input, "-f", "segment", "-segment_time", str(self.segment_time)]
        if self.copy_video:
            arg_list.extend(["-vcodec", "copy"])
        if self.copy_audio:
            arg_list.extend(["-acodec", "copy"])
        arg_list.append(output)
        print("Calling following: ")
        print(" ".join(arg_list))
        subprocess.call(arg_list)
