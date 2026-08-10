def sumar(string):
    if string == "":
        return 0
    return sum(int(n) for n in string.split(","))

def test_vacioIgualCero():
    assert 0 == sumar("")

def test_unoMasUnoIgualDos():
    assert 2 == sumar("1,1")

def test_unoMasDosIgualTres():
    assert 3 == sumar("1,2")

def test_tresSumandos():
    assert 6 == sumar("1,2,3")

def test_cincoSumandos():
    assert 15 == sumar("1,2,3,4,5")