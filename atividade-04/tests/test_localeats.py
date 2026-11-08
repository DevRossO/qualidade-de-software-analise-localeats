from playwright.sync_api import expect, sync_playwright

def test_abrir_formulario_de_cadastro_no_localeats():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto(
            "https://local-eats-unisenac.vercel.app/",
            wait_until="domcontentloaded",
        )

        page.locator("#showRegisterBtn").click()

        expect(page.locator("#registerForm")).to_be_visible()
        expect(page.locator("#regName")).to_be_visible()
        browser.close()
