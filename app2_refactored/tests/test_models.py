# importowac tylko klase User i ja, np czy deafultowe pola sa odpowiednio wpisane, sprawdzac typy np PESEL jako string
# najwazniejsze sa testy dla routerow

from app2_refactored.src.models import User

def test_user_model():
    test_user = User(pesel = "11111", address = "Marszalkowska 12/15")
    assert test_user.pesel == "11111"
    assert test_user.address == "Marszalkowska 12/15"
    assert test_user.diseases == []
    assert test_user.tel_number == None