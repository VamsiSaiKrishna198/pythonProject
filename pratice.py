#Dictionary mapping
def switch():
    s="aRTificialINTELLIgence"
    chioce=3
    def uppercase():
        print(s.toupper())
    def lowercase():
        print(s.lower())
    def isuppercase():
        print(s.isupper())
    def islowercase():
        print(s.islower())
    def replace():
        print(s.replace("INTELLgence","Neural Network"))
    def start():
        print(s.startwith("T"))
    def ends():
        print(s.endswith("e"))
    def convertup():
        print(s[0].upper())
    def convertlo():
        print(s[len(s)-1])
    dictionary ={
        1:uppercase,
        2:lowercase,
        3:isuppercase,
        4:islowercase,
        5:replace,
        6:start,
        7:ends,
        8:convertup,
        9:convertlo,
        10:exit}
    dictionary.get(chioce)()
