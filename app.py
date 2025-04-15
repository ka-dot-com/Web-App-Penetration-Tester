from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Simulate a vulnerable login form for testing
        username = request.form.get("username")
        password = request.form.get("password")
        # Note: This is insecure by design for demo purposes
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        return f"Query executed: {query}"
    return render_template("login.html")

if __name__ == "__main__":
    print("Starting test web app on http://localhost:5000")
    app.run(debug=False, host="0.0.0.0", port=5000)