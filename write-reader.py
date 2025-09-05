import sys

try:
    # open file stream
    file = open(file_name, "w")
except IOError:
    print ("There was an error writing to ", file_name)
    sys.exit()
 