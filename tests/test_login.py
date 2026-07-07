from playwright.sync_api import sync_playwright


def test_login_cu_credentiale_valide():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.fill("[data-test='username']", "standard_user")
        page.fill("[data-test='password']", "secret_sauce")
        page.click("[data-test='login-button']")
        titlu = page.inner_text("[data-test='title']")
        assert titlu == "Products"