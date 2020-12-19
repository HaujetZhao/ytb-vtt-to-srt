[中文](./README.md)　|　[English](./README_en.md) 

[Gitee](https://gitee.com/haujet/ytb-vtt-to-srt)　|　[Github](https://github.com/HaujetZhao/ytb-vtt-to-srt) 

## Target

Vtt subtitles downloaded from YouTube are optimized for double line display. If you use tools like FFmpeg, converting it into srt subtitles, the result might be like this: 

```
1
00:00:00,030 --> 00:00:02,659

what up YouTube and welcome to my first

2
00:00:02,659 --> 00:00:02,669
what up YouTube and welcome to my first
 

3
00:00:02,669 --> 00:00:09,589
what up YouTube and welcome to my first
ever episode of Lindsay beginnings a lot

4
00:00:09,589 --> 00:00:09,599
ever episode of Lindsay beginnings a lot
 

5
00:00:09,599 --> 00:00:11,419
ever episode of Lindsay beginnings a lot
of people ask me how I am the way I am


```

which is not operational in translating the subtitle. 

So we need to convert the vtt into perfect single line srt, like this: 

```
1
00:00:00,030 --> 00:00:02,659
what up YouTube and welcome to my first

2
00:00:02,669 --> 00:00:09,589
ever episode of Lindsay beginnings a lot

3
00:00:09,599 --> 00:00:11,419
of people ask me how I am the way I am

4
00:00:11,429 --> 00:00:13,430
talking out to this point how was this

5
00:00:13,440 --> 00:00:17,269
created good question what when I was a

6
00:00:17,279 --> 00:00:19,340
youngin in high school my dad had some

```

That what this script does. 

## Usage

In cmd page，run the `.py` script using python, you'll get a hint letting you input the vtt file path, you can just drop the vtt file in, and press `Enter`, bingo! 

![image-20201220002506326](assets/image-20201220002506326.png) 



