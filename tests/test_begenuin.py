import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("url", ["/home"])
def test_get_app_button_redirects(page: Page, url):
    page.goto("https://begenuin.com" + url)
    get_app_btn = page.get_by_role("link", name="Get App")
    expect(get_app_btn).to_be_visible()
    with page.expect_popup() as popup_info:
        get_app_btn.click()
    new_page = popup_info.value
    assert "play.google" in new_page.url or "apps.apple" in new_page.url

def test_login_invalid_credentials(page: Page):
    page.goto("https://begenuin.com/login")
    page.get_by_placeholder("Email").fill("test@example.com")
    page.get_by_placeholder("Password").fill("wrongpass")
    page.get_by_role("button", name="Login").click()
    expect(page.locator(".error-message")).to_contain_text("Invalid credentials")

def test_become_creator_badge(page: Page):
    page.goto("https://begenuin.com/home")
    badge = page.get_by_text("Become a Creator")
    expect(badge).to_be_visible()
