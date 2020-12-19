import subprocess
import srt
import os


# 这个脚本的作用是
# 将油管的双行 vtt 字幕转成 srt 字幕后，再转成单行
# 因为油管的字幕总是会有重复的 0.1 秒的字幕，将 ffmpeg 转成的 srt 字幕导入到 arctime 里
# 会在每一行都有重复


print('\n\n\n')
print('Please input the vtt subtitle file path')
输入文件 = input('请输入 vtt 字幕路径：').strip('"')
输出文件 = os.path.splitext(输入文件)[0] + '.srt'
print('\n\n\n')
command = f'ffmpeg -y -i "{输入文件}" "{输出文件}"'
print('\n\n\n')
print(f'command: {command}')
print('\n\n\n')
subprocess.call(command)

try:
    with open(输出文件, 'r', encoding='utf-8') as f:
        输入文件内容 = f.read()
except:
    with open(输出文件, 'r', encoding='gbk') as f:
        输入文件内容 = f.read()


输入字幕列表 = list(srt.parse(输入文件内容))
输出字幕列表 = []
# for index, subtitle in enumerate(输入字幕列表):
#     if index == 0:
#         subtitle.content = subtitle.content.split('\n')[1]
#         输出字幕列表.append(subtitle)
#     本句字幕内容 = subtitle.content
#     上一句字幕内容 = 输入字幕列表[index - 1].content
#     本句字幕内容分行 = 本句字幕内容.split('\n')
#     上一句字幕内容分行 = 上一句字幕内容.split('\n')
#     if 本句字幕内容分行[0] in 上一句字幕内容分行 and 本句字幕内容分行[1] == ' ':
#         输出字幕列表[-1].end = subtitle.end
#     elif 本句字幕内容分行[0] in 上一句字幕内容分行 and 本句字幕内容分行[1] != ' ':
#         subtitle.content = 本句字幕内容分行[1]
#         输出字幕列表.append(subtitle)

for index, subtitle in enumerate(输入字幕列表):
    if  subtitle.end.seconds == subtitle.start.seconds and subtitle.end.microseconds - subtitle.start.microseconds == 10000:
        continue
    subtitle.content = subtitle.content.split('\n')[1]
    输出字幕列表.append(subtitle)

输出文件内容 = srt.compose(输出字幕列表, reindex=True, start_index=1, strict=True)
with open(输出文件, 'w', encoding='utf-8') as out:
    out.write(输出文件内容)

print('\n\n\n')
print('Finished\n完成')