from cxcarddb import * 
from cxfilestruct import *
from cxsysconfig import *
from cxwx import *

import string, re

def make_output(carddb, qlist, cfg):

    # prepare output file
    outfs = fs(get_path_new("Select output file", cfg.searchpath, "*.html"))
    if ( outfs.path == None ) :
        sys.exit(0)
    outfs.open("w")

    
    # print each card from qlist
    for i in range(0,len(qlist.cardname)):

        # print multiple copies if qty < 1        
        for count in range(0,qlist.qty[i]):

            # card name with proper capitalization
            outfs.text = string.capwords(qlist.cardname[i])
            outfs.write()

            # mana cost
            if ( carddb.db[qlist.id[i]].find('manacost') is not None ):
                outfs.text = carddb.db[qlist.id[i]].find('manacost').text
                outfs.write()

            # card types
            if ( carddb.db[qlist.id[i]].find('type') is not None ):
                outfs.text = carddb.db[qlist.id[i]].find('type').text
                outfs.write()

            # card text (removing the flavor text)
            if ( carddb.db[qlist.id[i]].find('text') is not None):
                textstr = carddb.db[qlist.id[i]].find('text').text
                outfs.text = re.sub(r"\(.*\)", "", textstr)
                outfs.write()
                
            # card p/t if applicable
            if ( carddb.db[qlist.id[i]].find('pt') is not None ):
                outfs.text = carddb.db[qlist.id[i]].find('pt').text
                outfs.write()

            # card loyalty if applicable
            if ( carddb.db[qlist.id[i]].find('loyalty') is not None ):
                outfs.text = carddb.db[qlist.id[i]].find('loyalty').text
                outfs.write()

    outfs.close()

    return
