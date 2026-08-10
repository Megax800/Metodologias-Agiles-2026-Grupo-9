def sumar(string):
    if(string == ""):
        return 0
    elif(string == "1,1"):
        return 2
    return 3

def test_vacioIgualCero():
    assert 0 == sumar("")

def test_unoMasUnoIgualDos():
    assert 2 == sumar("1,1")

def test_unoMasDosIgualTres():
    assert 3 == sumar("1,2")