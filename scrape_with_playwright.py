from playwright.sync_api import sync_playwright

def save_rendered_html(url, filename):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        html = page.content()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        browser.close()
        print(f"✅ Đã lưu xong: {filename}")

save_rendered_html("https://luyenthieps.vn/", "luyenthieps.html")
save_rendered_html("https://thithu.luyenthieps.vn/", "thithu.html")
