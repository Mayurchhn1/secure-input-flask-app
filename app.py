from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    input_text = ""
    if request.method == 'POST':
        input_text = request.form.get("user_input", "")
    return render_template_string("""
        <h2>Secure Input App</h2>
        <form method="POST">
            <input type="text" name="user_input" />
            <button type="submit">Submit</button>
        </form>
        <p>Output: {{input_text}}</p>
    """, input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)
