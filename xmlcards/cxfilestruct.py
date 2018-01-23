# file struct
class fs:

    def __init__(self, path):
        self.path = path 
        self.ptr = ""
        self.text = ""

    def open(self,mode):
        try:
            self.ptr = open(self.path,mode)
        except IOError:
            return(-1)

    def close(self):
        try:
            self.ptr.close()
        except IOError:
            print "Unable to close file " + self.path
            sys.exit(-1)

    def read(self):
        try:
            self.text = self.ptr.read()
        except IOError:
            print "Unable to read from " + self.path
            sys.exit(-1)

    def write(self):
        try:
            self.ptr.write(self.text)
        except IOError:
            print "Unable to write to " + self.path
            sys.exit(-1)
