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

        # Check if the email or username already exists
        if any(user['email'] == email or user['username'] == username for user in users):
            # Redirect to failure page with a query parameter indicating user exists
            return redirect(url_for('register_failure', reason='user_exists'))

        # Otherwise, handle successful registration
        else:
            # Mock backend logic to 'save' the user
            new_user = {
            'username': username,
            'email': email,
            'password': password,
            'user_type': user_type
            }
            users.append(new_user)
            
            # Print the users list to the console
            # print(users)

            return redirect(url_for('register_success', username=username))

    return render_template('register/register.html')

@app.route('/register_success')
def register_success():
    username = request.args.get('username')
    # Convert google param to a boolean
    google = request.args.get('google', 'False') == 'True'
    
    # Pass username and google flag to the template
    return render_template('register/register_success.html', username=username, google=google)

@app.route('/register_failure')
def register_failure():
    reason = request.args.get('reason')
    return render_template('register/register_failure.html', reason=reason)

# Route for Google button redirection
@app.route('/google_redirect')
def google_redirect():
    # Simulate Google login success
    return redirect(url_for('register_success', google='True'))

@app.route('/go_back')
def go_back():
    return redirect(url_for('register'))  # Redirects to the register page

if __name__ == '__main__':
    app.run(debug=True)
