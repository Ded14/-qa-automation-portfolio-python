from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login_cu_credentiale_valide():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")
        titlu = page.inner_text("[data-test='title']")
        assert titlu == "Products"
        
def test_login_cu_utilizator_blocat():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        login_page = LoginPage(page)
        login_page.login("locked_out_user", "secret_sauce")
        mesaj_eroare = page.inner_text("[data-test='error']")
        assert "locked out" in mesaj_eroare