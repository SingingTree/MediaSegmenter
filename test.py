import ffmpeg_call

ffmpeg = "E:/Patches/FFMpeg/ffmpeg-20160522-git-566be4f-win64-static/bin/ffmpeg.exe"
input = "big-buck-bunny_trailer.webm"
output = "big-buck-bunny_trailer-segment%02d.webm"

call = ffmpeg_call.FfmpegSegmentCall()

call.call(ffmpeg, input, output)