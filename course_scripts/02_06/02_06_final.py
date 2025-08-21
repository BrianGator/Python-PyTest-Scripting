from playwright.sync_api import Page, Playwright, sync_playwright

url = "<your url here>"


def open_gig_form(page: Page):
    page.get_by_role("button", name="Add a Gig").click()


def add_venue(page: Page):
    page.goto(f"{url}/venues")
    page.get_by_role("button", name="Add a Venue").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("My Venue")
    page.get_by_role("textbox", name="Name").press("Tab")
    page.get_by_role("textbox", name="Adress").fill("123 Main street")
    page.get_by_role("textbox", name="Adress").press("Tab")
    page.get_by_role("textbox", name="Contact Number").fill("123-456-7658")
    page.get_by_role("textbox", name="Contact Email Address").click()
    page.get_by_role("textbox", name="Contact Email Address").fill("test@test.com")
    page.get_by_role("spinbutton", name="Venue Capacity").click()
    page.get_by_role("spinbutton", name="Venue Capacity").fill("100")
    page.get_by_role("textbox", name="Notes").click()
    page.get_by_role("textbox", name="Notes").fill("notes")
    page.get_by_role("button", name="Submit").click()
    page.pause()


def add_client(page: Page):
    page.get_by_role("link", name=" Clients").click()
    page.get_by_role("button", name="Add a Client").click()
    page.get_by_role("textbox", name="Enter the Client's first name").click()
    page.get_by_role("textbox", name="Enter the Client's first name").fill("Dave")
    page.get_by_role("textbox", name="Enter the Client's first name").press("Tab")
    page.get_by_role("textbox", name="Enter the Client's last name").fill("Westerveld")
    page.get_by_role("textbox", name="Enter the Client's last name").press("Tab")
    page.locator("#client-address").fill("123 Main Street")
    page.locator("#client-address").press("Tab")
    page.locator("#client-city").fill("Somewhere")
    page.locator("#client-city").press("Tab")
    page.locator("#client-contact_number").fill("123-432-4321")
    page.locator("#client-contact_number").press("Tab")
    page.locator("#client-contact_email").fill("test@test.com")
    page.get_by_role("button", name="Submit").click()


def add_gig(page: Page):
    page.get_by_role("button", name="Add a Gig").click()
    page.get_by_role("textbox", name="Gig Name").click()
    page.get_by_role("textbox", name="Gig Name").fill("Test Gig")
    page.get_by_role("textbox", name="Gig Date").fill("2025-08-21")
    page.getByLabel("Venue").select_option("13")
    page.getByLabel("Client").select_option("11")
    page.get_by_role("button", name="Submit").click()


def run(playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    page = browser.new_page()

    page.goto(url)
    page.get_by_role("button", name="Continue", exact=True).click()

    open_gig_form(page)

    # Scenario 1: Create a gig with a new client and a new venue
    add_venue(page)

    add_client(page)

    page.get_by_role("link", name=" Home").click()

    add_gig(page)

    page.pause()

    # Scenario 2: Create a gig with a new client, but at a previously used venue
    page.goto(url)

    open_gig_form(page)
    add_client(page)

    page.get_by_role("link", name=" Home").nth(1).click()

    add_gig(page)
    page.pause()

    # Scenario 3: Create a gig for both a client and location that we worked with before
    page.goto(url)

    add_gig(page)
    page.pause()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
