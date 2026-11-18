from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(device_scale_factor=2)
    page.goto("http://localhost:8095/print-carla.html")
    page.wait_for_selector("#phone-screen")
    page.locator("#phone-screen").screenshot(path="assets/print-conversacion-carla.jpg", quality=90, type="jpeg")
    browser.close()
    print("Screenshot saved to assets/print-conversacion-carla.jpg")
