from playwright.sync_api import Playwright, sync_playwright

url = "your url here"


def run(playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.pause()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
