import requests
from playwright.sync_api import Page, Playwright, sync_playwright

base_url = "<your url here>"


def create_venue():
    venue_data = {
        "name": "Test Venue",
        "address": "123 Main St",
        "city": "Springfield",
        "contact_number": "555-555-5555",
        "contact_email": "test@test.com",
        "capacity": 100,
        "notes": "Great venue!",
    }
    response = requests.post(f"{base_url}/api/venues", json=venue_data)


def open_gig_form(page: Page):
    page.get_by_role("button", name="Add a Gig").click()
    page.get_by_label("Venue").click()


def run(playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    page = browser.new_page()

    page.goto(base_url)
    open_gig_form(page)

    page.pause()

    for i in range(3):
        create_venue()
        page.get_by_role("button", name="Cancel").click()
        open_gig_form(page)
        page.get_by_label("Venue").select_option(f"{i + 1}")
        page.pause()
    browser.close()


create_venue()
with sync_playwright() as playwright:
    run(playwright)
