from actions.LoginAction import LoginAction

def test_validLogin(self):
    LogAct = LoginAction(self.driver)
    LogAct.validLogin()
    assert LogAct.assertHome()