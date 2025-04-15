# Web App Penetration Tester

A Python tool to test a web app for vulnerabilities like SQL injection. Includes a dummy app to practice safely

## How It Works
- Runs a test web app with a login form (intentionally vulnerable)
- Sends common attack payloads to check for issues
- Reports any weaknesses found

## Setup
1. Install Python 3.8+
2. Run `pip install -r requirements.txt`
3. Start the test app: `python app.py`
4. In another terminal, run `python tester.py`

## Use Case
Helps developers learn about web security by showing how attacks work and what to fix. Great for training or pentesting demos

## Future Improvements
- Test for more vulnerabilities (e.g., XSS)
- Add detailed fix guides in reports

Contact: kswierczynska21@gmail.com