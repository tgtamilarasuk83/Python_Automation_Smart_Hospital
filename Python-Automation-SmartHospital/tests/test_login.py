from actions.LoginAction import LoginAction
import pytest

@pytest.mark.usefixtures("setup")
def test_validLogin(setup):
    driver = setup
    LogAct = LoginAction(driver)
    LogAct.validLogin()
    assert LogAct.assertHome()