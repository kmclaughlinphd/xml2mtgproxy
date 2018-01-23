import sys, os
from cxfilestruct import * 
from cxsysconfig import * 
from cxcarddb import * 
from cxqlist import *
from cxdump import *



def main():

    # load cfg file (saves paths, etc.)
    
    # read cards.xml path, and maybe some other options
    cfg = syscfg("xmlcards.cfg")
    cfg.readopts()
        
    # try to load XML
    carddb = load_carddb(cfg)

    # try to load input file (card query list)
    qlist = load_qlist(cfg)

    # map cards from qlist to db; card ids stored in qlist.id array
    map_cards(carddb, qlist)

    # dump output file
    make_output(carddb, qlist, cfg)





if __name__ == "__main__":

    main()


