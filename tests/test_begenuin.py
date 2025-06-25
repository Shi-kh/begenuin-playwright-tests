import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("url", ["/home"])
def test_homepage_load(page, url):
    page.goto("https://begenuin.com" + url)
    expect(page.locator("//p[contains(text(),'Popular')]")).to_be_visible()
    expect(page.locator("//p[contains(text(),'Explore')]")).to_be_visible()

def test_get_app_button(page):
    page.goto("https://begenuin.com/home")
    btn = page.locator('//button[contains(text(), "Get App")]')
    expect(btn).to_be_visible()
    btn.click()
    modal = page.locator("//p[contains(text(), 'Get the ')]")
    expect(modal).to_be_visible()

def test_tab_navigation(page):
    page.goto("https://begenuin.com/home")
    for tab in ["Popular", "Latest", "Explore"]:
        page.locator(f"text={tab}").click()
        expect(page.locator(f"text={tab}")).to_be_visible()

def test_video_feed_playback(page):
    page.goto("https://begenuin.com/home")
    video = page.locator("video").first
    expect(video).to_be_visible()

def test_claim_brand_cta(page):
    page.goto("https://begenuin.com/home")
    cta = page.locator("text=Claim Brand Profile")
    expect(cta).to_be_visible()
    cta.click()
    expect(page).to_have_url(lambda url: "login" in url or "creator" in url)

def test_accessibility_keyboard_nav(page):
    page.goto("https://begenuin.com/home")
    page.keyboard.press("Tab")
    expect(page).to_have_url("https://begenuin.com/home")