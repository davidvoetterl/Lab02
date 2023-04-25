import glob

path = "/Users/davidvoetterl/Documents/Gitarrenoten/*.*"

results = glob.glob(path)

for file in glob.glob(path, recursive=True):

    print(results)

