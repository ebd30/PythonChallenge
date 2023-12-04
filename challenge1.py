# encoding text
string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# decoding function : two move alphabet
def two_move_alphabet(text) :
    doc1 = "abcdefghijklmnopqrstuvwxyz" 
    doc2 = "cdefghijklmnopqrstuvwxyzab"
    decoding = text.maketrans(doc1, doc2)
    
    print(text.translate(decoding))

two_move_alphabet(string)