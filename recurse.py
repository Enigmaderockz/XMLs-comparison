import os
import re

def find_files(path, pattern):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if re.search(pattern, file):
                result.append(os.path.join(root, file))
    return result
  
  grep_filenames('/path/to/directory', r'^.*\.txt$')
  
  
  import os
import re

def recursive_grep_filenames(root_dir, filename_pattern):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if re.match(filename_pattern, filename):
                print(os.path.join(dirpath, filename))
   
  root_dir = '/path/to/root/dir'
filename_pattern = r'^.*\.txt$'
recursive_grep_filenames(root_dir, filename_pattern)


import os
import re

def find_filenames(filename, pattern):
    matches = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if os.path.isdir(line):
                for root, dirnames, filenames in os.walk(line):
                    for filename in filenames:
                        if re.match(pattern, filename):
                            matches.append(os.path.join(root, filename))
            elif os.path.isfile(line):
                if re.match(pattern, line):
                    matches.append(line)
    return matches
  
  
  import os
import fnmatch

def recursive_search(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(root, filename)

# example usage
for file in recursive_search('/path/to/directory', '*.txt'):
    print(file)





