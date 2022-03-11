from app.operaciones import resta, suma, cociente, division, multiplicacion, resto 


class TestClass:
    def test_suma(self):
        assert suma(4, 5) == 9
        assert suma(-1, -2) == -3
        assert suma(-7, 5) == -2
        assert suma(-7, 9) == 2
        
    def test_resta(self):
        assert resta(4, 5) == -1
        assert resta(-1, -2) == 1
        assert resta(-7, 5) == -12
        assert resta(-7, 9) == -16

    def test_cociente(self):
        assert cociente(10, 5) == 2
        assert cociente(20, 4) == 5
        assert cociente(10, 1) == 10
        assert cociente(18, 9) == 2

    def test_division(self):
        assert division(20, 5) == 4
        assert division(8, 2) == 4
        assert division(10, 5) == 2
        assert division(9, 9) == 1

    def test_multiplicacion(self):
        assert multiplicacion(4, 5) == 20
        assert multiplicacion(1, 2) == 2
        assert multiplicacion(7, 5) == 35
        assert multiplicacion(7, 9) == 63

    def test_resto(self):
        assert resto(21, 5) == 1
        assert resto(8, 2) == 0
