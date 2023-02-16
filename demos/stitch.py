from vidpy import Text, Clip, Composition

clip1 = Clip('videos/clip1.mpeg')
clip2 = Clip('videos/hand2.mp4')
clip3 = Clip('videos/clip3.mpeg')

line1 = "Could you tell us about yourself?"
font = 'Helvetica'
color = '#ff5179'
outline_color = '#a0ff5f'
outline_size = 1
weight = '100'
style = 'normal'
boundingbox = ('10%', '10%', '80%', '80%')

text1 = Text(line1, end=1, color=color, font=font, style=style, weight=weight, olcolor=outline_color, outline=outline_size, size=70, bbox=boundingbox, pad=50)
text1.glow(1)

line2 = "What is your experience level on ReactJS? Could you please elaborate on this?"
text2 = Text(line2, end=1, color=color, font=font, style=style, weight=weight, olcolor=outline_color, outline=outline_size, size=70, bbox=boundingbox, pad=50)
text2.glow(1)

clips = [clip3, text1, clip1,text2, clip2 ]

# stitch all clips together
# stiched = Composition(clips, singletrack=True)
# stiched.save('allvids.mp4')

# stitch the first second of all clips
for clip in clips:
    clip.cut(start=0, end=5)

stiched = Composition(clips, singletrack=True)
stiched.save('firstsecond.mp4')
