import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("url", ["/home"])
def test_get_app_button_redirects(page: Page, url):
    page.goto("https://begenuin.com" + url)
    get_app_btn = page.locator('//button[contains(text(), "Get App")]')
    expect(get_app_btn).to_be_visible()
    get_app_btn.click()
    modal = page.locator('//p[@class="text-new-h4-mobile"]')
    expect(modal).to_be_visible()
    qr_code = page.locator('//canvas[@id="react-qrcode-logo"]') 
    expect(qr_code).to_be_visible()

def test_login_invalid_credentials(page: Page):
    page.goto("https://begenuin.com")

    # Click the "Log in" button
    login_button = page.locator('//button[contains(text(),"Log in")]')
    expect(login_button).to_be_visible()
    login_button.click()

    # Wait for login modal to appear and fields to be ready
    email_input = page.locator("//input[@id='loginEmail']")
    expect(email_input).to_be_visible()

    password_input = page.locator("//input[@id='loginPassword']")
    expect(password_input).to_be_visible() 

    submit_button = page.locator("//button[contains(text(),'Log In')]")
    expect(submit_button).to_be_visible()

    email_input.fill("test@example.com")
    password_input.fill("wrongpass")
    submit_button.click()

    Optionally validate error message
    error_msg = page.locator("//div[@class='rnc__notification-message']")  
    expect(error_msg).to_be_visible()

def test_become_creator_badge(page: Page):
    page.goto("https://begenuin.com/home")
    badge = page.locator("//p[@class='w-64 overflow-hidden p-3 text-start text-body-1-bold']")
    expect(badge).to_be_visible()
