import re
from cxwx import *
from cxfilestruct import *

class qlists:

    def __init__(self):
        self.N = 0
        self.qty = []
        self.cardname = []
        self.id = []

    def add_card(self, qty, cardid):        
        self.qty.append(qty)
        self.cardname.append(cardid)

    def find_match(self, card, carddb): 
        print ''






#load input file (card query list)
def load_qlist(cfg):

    path = get_path("Select input file", cfg.searchpath, "*")
    if path == None:
        sys.exit(-1)
    qlistfs = fs(path)

    qlistfs.open("r")

    # initialize card list
    qlist = qlists()

    # loop through file; grab one line at a time
    qlistfs.read()
    qlistfsline = qlistfs.text.splitlines()
    for i in range(0,len(qlistfsline)):
        linetok = qlistfsline[i].split()
        if re.match("[0-9]+x?",linetok[0]): #check for a quantity modifier "[0-9]" or "[0-9]x"
            qty = re.search("[0-9]+",linetok[0]).group()
            qlist.add_card(int(qty), " ".join(linetok[1:len(linetok)])) # add a quantity of cards
        else:
            qlist.add_card(int(1), " ".join(linetok[0:len(linetok)])) # add a single card

    
    qlistfs.close()
    return(qlist)