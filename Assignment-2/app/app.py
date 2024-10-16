from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database to hold registered users
users = []

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']  # Either 'Tenant' or 'Landlord'
        
        # Mock backend logic to 'save' the user
        new_user = {
            'username': username,
            'email': email,
            'password': password,
            'user_type': user_type
        }
        users.append(new_user)
        
        # After successful registration, redirect to a new page or a success message
        return redirect(url_for('success', username=username))
    
    return render_template('index.html')

@app.route('/success/<username>')
def success(username):
    return f"Welcome {username}, you have successfully registered!"

if __name__ == '__main__':
    app.run(debug=True)
