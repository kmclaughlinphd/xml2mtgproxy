from cxfilestruct import * 

# class for working with the config file
class syscfg():

    def __init__(self, path):
        self.fs = fs(path)
        self.xmlpath = ""
        self.searchpath = ""

    def readopts(self):

        if ( self.fs.open("r") != -1 ):
            self.fs.read()
            # get info from cfg file
            options = self.fs.text.splitlines()

            # parse each line in the file
            for i in range(0,len(options)):
                # parse out the single line
                optline = str(options[i]).split()
                # it should have exactly two elements, otherwise we ignore it
                if ( len(optline) == 2 ):
                    if ( optline[0] == "xml" ):
                        self.xmlpath = optline[1]
                    elif ( optline[0] == "search" ):
                        self.searchpath = optline[1]

            self.fs.close()
        else:
            print "warning: unable to open cfg file for read: " + os.curdir + self.fs.path

    # write options to cfg file
    def writeopts(self):

        # try to open the file for write
        if ( self.fs.open("w") != -1 ):
            if ( self.xmlpath != "" ): #write 
                self.fs.text = "xml " + self.xmlpath + "\n"
                self.fs.write()
            if ( self.searchpath != "" ):
                self.fs.text = "search " + self.searchpath + "\n"
                self.fs.write()
            self.fs.close()
        else:
            print "warning: unable to open cfg file for write: " + os.curdir + self.fs.path