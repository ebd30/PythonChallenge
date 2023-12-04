# encoding text. 암호화된 암호문
string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# decoding function : two move alphabet. 복호화시키는 함수. 2개의 알파벳을 움직이는 함수다.
def two_move_alphabet(text) : 
    doc1 = "abcdefghijklmnopqrstuvwxyz" # 기존 알파벳 순서
    doc2 = "cdefghijklmnopqrstuvwxyzab" # 알바벳을 2번 움직인 순서
    decoding = text.maketrans(doc1, doc2) # maketrans(parameter1, parameter2, parameter3) 함수는 문자열을 치환시켜주는 함수다. parameter1에 기존 문자열, parameter2에 치환할 문자열을 넣어준다. parameter3는 원래 문자열에서 제거할 문자를 넣어준다(없어도 무방하다). parameter1, parameter2 길이가 같아야한다.
    
    print(text.translate(decoding)) # translate()는 maketrans()에서 만든 값을 전달받음.

two_move_alphabet(string) # 함수 호출
