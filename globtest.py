import glob

path = '../Documents/CCLab/GenreSorting/train30_sorting_complete/001'

for x in glob.glob(path + '*.mp3'):

    print(x) 
