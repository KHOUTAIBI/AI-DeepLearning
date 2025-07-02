def make_file_readable(filepath):
    try:
        f = open(filepath,"r")
        fileArray = f.readlines()
        return fileArray[1:]
    except:
        return None
    