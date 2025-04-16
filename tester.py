import requests
from bs4 import BeautifulSoup

def test_sql_injection(url, form_id):
    payloads = ["' OR '1'='1", "admin' --", "1; DROP TABLE users"]
    results = []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find("form", id=form_id)
    if not form:
        return ["No form found with given ID."]

    inputs = form.find_all("input")
    fields = [inp["name"] for inp in inputs if inp.get("name")]

    for payload in payloads:
        data = {field: payload for field in fields}
        try:
            response = requests.post(url, data=data, timeout=5)
            if "error" not in response.text.lower():
                results.append(f"Potential SQL injection found with: {payload}")
        except requests.RequestException as e:
            results.append(f"Error testing payload: {payload}, Exception: {e}")

    return results if results else ["No SQL injection vulnerabilities detected."]

def test_xss(url):
    payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
    results = []

    for payload in payloads:
        try:
            response = requests.get(url, params={"q": payload}, timeout=5)
            if payload in response.text:
                results.append(f"Potential XSS vulnerability found with payload: {payload}")
        except requests.RequestException as e:
            results.append(f"Error testing payload: {payload}, Exception: {e}")

    return results if results else ["No XSS vulnerabilities detected."]

def generate_report(results):
    with open("vulnerability_report.txt", "w") as report:
        report.write("Vulnerability Scan Report\n")
        report.write("=========================\n\n")
        for result in results:
            report.write(f"{result}\n")
        report.write("\nRecommended Fixes:\n")
        report.write("- For SQL Injection: Use parameterized queries or ORM.\n")
        report.write("- For XSS: Sanitize and escape user input.\n")

if __name__ == "__main__":
    test_url = "http://localhost:5000"
    form_id = "login-form"
    print("Starting vulnerability tests...")
    sql_results = test_sql_injection(test_url, form_id)
    xss_results = test_xss(test_url)
    combined_results = sql_results + xss_results
    generate_report(combined_results)
    print("Report generated: vulnerability_report.txt")
