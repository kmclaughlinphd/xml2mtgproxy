from cxsysconfig import *
from cxfilestruct import *
from cxwx import *
from cxdleven import *
import xml.etree.ElementTree as xmlet

class cardstruct:

    def __init__(self, string):

        self.db = xmlet.fromstring(string).findall("./cards/card")


        

def load_carddb(cfg):

    # load cards.xml
    while 1:
        if ( cfg.xmlpath != "" ):
            cardsxml = fs(cfg.xmlpath)
            if ( cardsxml.open("r") == -1 ):
                print "warning: could not access file: " + cardsxml.path
                ## remove the xml file path from cfg, since it was useless
                cfg.xmlpath = ""
                cfg.writeopts()
            else: #xml was loaded
                break
        else:
            # get new path, and update in cfg
            cfg.xmlpath = get_path("Select cards.xml file", cfg.searchpath, "*.xml")
            if ( cfg.xmlpath == None ):
                sys.exit(0)
            cfg.searchpath = os.path.dirname(cfg.xmlpath)
            cfg.writeopts()
            #loop

    # read the xml file, and parse into db
    cardsxml.read()
    print "loading db"
    carddb = cardstruct(cardsxml.text)

    #done, close xml and cfg file
    cardsxml.close()

    return carddb


# scan db for best match to the query qname
def find_match(qname, db):

    bestDist = 9999
    bestId = -1

    for i in range(0,len(db)):
       currDist = damerau_levenshtein_distance(db[i][0].text.lower(), qname.lower())
       if ( currDist < bestDist ):
           bestDist = currDist
           bestId = i

    return bestId



def map_cards(carddb, qlist):
   
    cards = carddb.db
    
    # for each card in qlist, find the closes damerau_levenshtein matched card from db
    for i in range(0,len(qlist.cardname)):
        qlist.id.append(find_match(qlist.cardname[i], cards))
        # match cards will be appended to the id array of qlist object

    return