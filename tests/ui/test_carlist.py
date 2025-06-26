import pytest
from playwright.sync_api import expect

BASE_URL = "https://community.carlist.my/home"

def test_homepage_load(page):
    page.goto(BASE_URL)
    expect(page.locator("//p[contains(text(),'Popular')]")).to_be_visible()

def test_comment_feature(page):
    page.goto(BASE_URL)
    comment_icon = page.locator("//p[contains(text(),'Add a Comment')]").click()
    modal = page.locator("//h3[contains(text(),'Log in or sign up')]")
    expect(modal).to_be_visible()

def test_like_button(page):
    page.goto(BASE_URL)
    like_btn = page.locator('//img[@alt="reaction"]').first
    like_btn.click()
    modal = page.locator("//h3[contains(text(),'Log in or sign up')]")
    expect(modal).to_be_visible()

def test_search_community(page):
    page.goto(BASE_URL)
    search = page.locator('//input[@id="search-input"]')
    expect(search).to_be_visible()
    search.fill("audi")
    page.locator("//p[contains(text(),'@audil4960')]").click()
    page.wait_for_timeout(2000)
    assert "search" in page.url or "audil4960" in page.url

def test_filter_categories(page):
    page.goto(BASE_URL)
    expect(page.locator("//p[contains(text(),'Categories')]")).to_be_visible()

def test_user_login(page):
    page.goto(BASE_URL)
    page.locator("//div[contains(@class, 'hover:bg-monochrome-6')]/p[text()='Log in']").click()
    modal = page.locator("//h3[contains(text(),'Log in or sign up')]")
    expect(modal).to_be_visible()