import glob

def find_files(directory):
    return glob.glob(f"{directory}/*")

# Example usage:
directory = "/path/to/directory"
files = find_files(directory)
print(files)