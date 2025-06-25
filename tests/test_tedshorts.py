import pytest
from playwright.sync_api import expect

BASE_URL = "https://shorts.ted.com/home"

def test_homepage_load(page):
    page.goto(BASE_URL)
    expect(page.locator("//p[contains(text(),'Popular')]")).to_be_visible()
    expect(page.locator("header")).to_be_visible()

def test_video_playback(page):
    page.goto(BASE_URL)
    thumbnail = page.locator("video").first
    expect(thumbnail).to_be_visible()

def test_navigation_tabs(page):
    page.goto(BASE_URL)
    for tab in ["Popular", "Latest"]:
        page.locator(f"//p[contains(text(),{tab})]").click()
        expect(page.locator(f"//p[contains(text(),{tab})]")).to_be_visible()

def test_search_feature(page):
    page.goto(BASE_URL)
    search = page.locator('//input[@id="search-input"]')
    expect(search).to_be_visible()
    search.fill("education")
    search.press("Enter")
    page.wait_for_timeout(1000)
    expect(page).to_have_url(lambda url: "search" in url or "education" in url)

def test_get_app_link(page):
    page.goto(BASE_URL)
    logo = page.locator('//button[contains(text(), "Get App")]')
    expect(logo).to_be_visible()
    logo.click()
    expect(page).not_to_have_url(BASE_URL)

def test_keyboard_navigation(page):
    page.goto(BASE_URL)
    for _ in range(10):
        page.keyboard.press("Tab")
    expect(page).to_have_url(BASE_URL)

def test_performance_scroll(page):
    page.goto(BASE_URL)
    for _ in range(10):
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(500)
    expect(page.locator("video")).nth(5).is_visible()