import romain as m

def test_conversion_caractere_en_int():
    assert m.conversion_caractere_en_int ('I') == 1
    assert m.conversion_caractere_en_int ('V') == 5
    assert m.conversion_caractere_en_int (0) == 0
    assert m.conversion_caractere_en_int (-1) == 0
    assert m.conversion_caractere_en_int ('a') == 0
    assert m.conversion_caractere_en_int (' ') == 0
    assert m.conversion_caractere_en_int ('ab') == 0
    assert m.conversion_caractere_en_int ('IV') == 0

def test_romain_en_nombre_int():
    assert m.romain_en_nombre_int ('MMVI') == 2006
    assert m.romain_en_nombre_int ('MCMXLIV') == 1944
    assert m.romain_en_nombre_int (' ') == 0
    assert m.romain_en_nombre_int ('1') == 0
    assert m.romain_en_nombre_int ('a') == 0

def test_somme_de_nombres_romains():
    assert m.calculatrice ('+','MMVI','MCMXLIV') == 3950
    assert m.calculatrice ('-','MMVI','MCMXLIV') == 62
    assert m.calculatrice ('-','MCMXLIV','MMVI') == -62
    assert m.calculatrice ('*','MMVI','MCMXLIV') == 3899664
    assert m.calculatrice ('/','IV','II') == 2

def test_int_en_nombre_romain():
    assert m.int_en_nombre_romain(123) == "CXXIII"
    assert m.int_en_nombre_romain(103) == "CIII"
    assert m.int_en_nombre_romain(0) == ""
    assert m.int_en_nombre_romain(993) == "CMXCIII"
    assert m.int_en_nombre_romain(2625) == "MMDCXXV"
    assert m.int_en_nombre_romain(26) == "XXVI"
    assert m.int_en_nombre_romain(5) == "V"
    assert m.int_en_nombre_romain(4000) == "Le nombre à transformer ne doit être compris entre 0 et 3000"
    assert m.int_en_nombre_romain(-321) == "Le nombre à transformer ne doit être compris entre 0 et 3000"

    