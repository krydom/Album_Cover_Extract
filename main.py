import os
import sys
from mutagen import File

music_dir = sys.path[0] + '\\music\\'
cover_dir = sys.path[0] + '\\cover\\'
sum = 0
for root, dirs, files in os.walk(music_dir):
    for f in files:
        sum = sum + 1
        audio=File(root + f)
        name = f[:f.rfind('.')]
        find_pic = 0
        for tag in audio.tags:  #防止某些歌曲有奇怪的ID3 tag
            if tag[:4] == 'APIC':
                mArtwork = audio.tags[tag].data
                find_pic = 1
        if find_pic == 1:
            with open(cover_dir + name + '.png', 'wb') as img:  
                img.write(mArtwork)
        else:
            print(f)
print(sum)
