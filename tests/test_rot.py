from app.rot_cipher import rot13_cipher


class TestClass:
    def test_rot13_cipher(self):
        assert rot13_cipher("foobar") == "sbbone"
        assert rot13_cipher("me llamo dani") == "zr yynzb qnav"
        assert rot13_cipher("juego a futbol") == "whrtb n shgoby" 
