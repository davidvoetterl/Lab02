import glob
import hashlib

directory = "./image/*"
files = glob.glob(directory)

def get_file_hash(filename):
    with open(filename, 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    return file_hash


def find_duplicates(files):
    hashes = []
    duplicate_files = []
    for x in files:
        hashedFile = get_file_hash(x)
        if hashedFile in hashes:
            duplicate_files.append(x)
            # print(f"duplicate files:{duplicate_files}")
        else:
            hashes.append(hashedFile)
            # print(f"hashes:{hashes}")
    return duplicate_files


# for x in files:
# print(get_file_hash(x))
# print(get_file_hash("./image/oak.jpeg"))

duplicates = find_duplicates(files)
print(f"In folder {directory}, this script has found {len(duplicates)} duplicates.")
if len(duplicates)>0:
    print("Paths of those are:")
    for x in duplicates:
        print(x)

