import json
file = open("alphabet.json")
file2 = open("binary.json")
def encode(string):
    jsonveri = json.loads(file.read())
    jsonveri2 = json.loads(file2.read())
    ascii=""
    jsonveri["ı"] = "11"
    jsonveri["ö"] = "19"
    jsonveri["ğ"] = "09"
    jsonveri["ç"] = "04"
    jsonveri["ü"] = "27"
    for i in string:
        ascii+=jsonveri[i]
    b1 = bin(int(ascii)).replace("0b", "")
    b2 = bin(int(ascii)).replace("0b", "")
    b1 = b1
    b2 = b2[::-1]
    last = ""
    sayi = 0
    for a in str(b1):
        if a == "0" and b2[sayi] == "0":
            last+="0"
        elif a == "1" and b2[sayi] == "0":
            last+="1"
        elif a == "0" and b2[sayi] == "1":
            last+="1"
        elif a == "1" and b2[sayi] == "1":
            last+="0"
        elif a == " " and b2[sayi] == " ":
            last+=" "
        sayi+=1
    donusturme = 0
    var = 6
    lar = 0
    sonvalla = ""
    while lar<=len(last):
        sonvalla+=last[lar:var]+" "
        var+=6
        lar+=6
    sonvalla=sonvalla.strip()
    if len(sonvalla.split(" ")[-1::]) < 6:
        haha = len(sonvalla.split(" ")[-1::][0])
        while haha < 6:
            sonvalla+="0"
            haha = len(sonvalla.split(" ")[-1::][0])
    yenibirson=""
    liste = sonvalla.split(" ")
    for i in liste:
        yenibirson+=jsonveri2[i]
    print(yenibirson)
encode("kr208")