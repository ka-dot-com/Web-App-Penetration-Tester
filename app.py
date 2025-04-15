from flask import Flask, request, render_template, escape

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Securely handle user input to avoid SQL Injection
        username = escape(request.form.get("username"))
        password = escape(request.form.get("password"))
        
        # Simulated secure query (do not use raw SQL in production)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        return f"Query executed securely: {query}"
    
    return render_template("login.html")

if __name__ == "__main__":
    print("Starting secure web app on http://localhost:5000")
    app.run(debug=False, host="0.0.0.0", port=5000)
