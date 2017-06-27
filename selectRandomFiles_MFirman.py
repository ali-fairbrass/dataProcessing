import shutil, os, random
random.seed(10)

src = '/media/michael/Elements2/Fieldwork_Data/2015/SE232NZ/SM2BAT+/'
dst = '/home/michael/Dropbox/engage/FairbrassFirmanetal_/data/random_SE232NZ/'

fnames = os.listdir(src)
random.shuffle(fnames)
fnames = fnames[:25]

for fname in fnames:
    shutil.copy(src + fname, dst)