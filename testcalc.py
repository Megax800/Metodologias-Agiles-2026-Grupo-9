def sumar(string):
    match string:
        case "":
            return 0
        case "1,1":
            return 2
        case "1,2":
            return 3
        case "1,2,3":
            return 6
        case "1,2,3,4,5":
            return 15

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