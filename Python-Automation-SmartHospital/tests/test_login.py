from actions.LoginAction import LoginAction
import pytest

@pytest.mark.usefixtures("setup")
def test_validLogin(setup):
    driver = setup
    LogAct = LoginAction(driver)
    LogAct.validLogin()
    assert LogAct.assertHome()
    print("Test Passed")

def test_emptyfieldLogin(setup):
    driver = setup
    LogAct = LoginAction(driver)
    LogAct.emptyfieldLogin()
    assert LogAct.assertEmptyField()
    print("Test Passed")

@pytest.mark.parametrize("username",["darshan"])
def test_invalidusernameLogin(setup,username):
    driver = setup
    LogAct = LoginAction(driver)
    LogAct.invalidusername(username) 
    assert LogAct.assertinvalidusername()
    print("Test Passed")

@pytest.mark.parametrize("password",["darshan10"])
def test_invalidpasswordLogin(setup,password):
    driver = setup
    LogAct = LoginAction(driver)
    LogAct.invalidpassword(password)
    assert LogAct.assertinvalidpassword()
    print("Test Passed")
    
