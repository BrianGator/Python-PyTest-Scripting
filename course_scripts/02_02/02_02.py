from playwright.sync_api import Playwright, sync_playwright

url = "<your url here>"


def run(playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.get_by_role("button", name="Continue", exact=True).click()
    page.get_by_role("link", name=" Gigs").click()
    page.pause()
    page.go_back()
    page.pause()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
