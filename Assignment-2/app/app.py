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

        # Check for existing users with the same username
        if any(user['username'] == username for user in users):
            return redirect(url_for('register_failure'))
        
        # Mock backend logic to 'save' the user
        new_user = {
            'username': username,
            'email': email,
            'password': password,
            'user_type': user_type
        }
        users.append(new_user)

        # Redirect to the success page
        return redirect(url_for('register_success', username=username))
    
    return render_template('index.html')

@app.route('/register_success/<username>')
def register_success(username):
    return render_template('register_success.html', username=username)

@app.route('/register_failure')
def register_failure():
    return render_template('register_failure.html')

if __name__ == '__main__':
    app.run(debug=True)
