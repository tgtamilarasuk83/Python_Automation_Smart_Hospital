from actions.ContactUsAction import ContactUsAction


def test_contact_us(setup):

    driver = setup
    contact = ContactUsAction(driver)
   

    contact.submit_form(
        "Tamil",
        "tamilarasu@test.com",
        "Automation Issue",
        "This is a test message from automation script"
    )
    assert contact.is_success_message_displayed()

  