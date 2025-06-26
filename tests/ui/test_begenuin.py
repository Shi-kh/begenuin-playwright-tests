import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://begenuin.com"

@pytest.mark.parametrize("url", ["/home"])
def test_homepage_load(page: Page, url):
    """Verify that homepage loads with key navigation items."""
    page.goto(BASE_URL + url)
    expect(page.locator("//p[contains(text(),'Popular')]")).to_be_visible()
    expect(page.locator("//p[contains(text(),'Explore')]")).to_be_visible()

def test_get_app_button_opens_modal(page: Page):
    """Verify that clicking 'Get App' opens the app modal."""
    page.goto(f"{BASE_URL}/home")
    btn = page.locator('//button[contains(text(), "Get App")]')
    expect(btn).to_be_visible()
    btn.click()
    modal = page.locator("//p[contains(text(), 'Get the ')]")
    expect(modal).to_be_visible()

def test_navigation_tabs(page: Page):
    """Verify that Popular, Latest, and Explore tabs are clickable."""
    page.goto(f"{BASE_URL}/home")
    for tab in ["Popular", "Latest", "Explore"]:
        tab_locator = page.locator(f"text={tab}")
        tab_locator.click()
        expect(tab_locator).to_be_visible()

def test_video_is_visible_in_feed(page: Page):
    """Ensure video element appears in feed (basic playback test)."""
    page.goto(f"{BASE_URL}/home")
    video = page.locator("video").first
    expect(video).to_be_visible()

def test_keyboard_tab_navigation(page: Page):
    """Check if keyboard tab navigation works on homepage."""
    page.goto(f"{BASE_URL}/home")
    for _ in range(5):
        page.keyboard.press("Tab")
    expect(page).to_have_url(f"{BASE_URL}/home")
