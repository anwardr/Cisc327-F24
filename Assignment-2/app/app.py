from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Samhith will handle moving this into another directory
# ================================================================================

# Mock database to hold registered users and Google users
users = [{'username': 'user_01', 'email': 'user_01@gmail.com', 'password': '123', 'user_type': 'Landlord'}]
google_users = []  # Store all Google users separately

# Helper function to check if a username or email exists in both user lists
def is_user_exists(username, email):
    return any(user['username'] == username or user['email'] == email for user in users) or \
           any(google_user['username'] == username or google_user['email'] == email for google_user in google_users)

# Helper function to create and append a new user (either regular or Google user)
def create_user(username, email, password, user_type, is_google_user=False):
    new_user = {'username': username, 'email': email, 'password': password, 'user_type': user_type}
    if is_google_user:
        google_users.append(new_user)
    else:
        users.append(new_user)

def find_google_user(email):
    return next((user for user in google_users if user['email'] == email), None)

# ================================================================================


# Route for user registration (Starting Page)
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user_type = request.form.get('user_type', 'Tenant')

        # Check if the email or username already exists in both users and google_users
        if is_user_exists(username, email):
            return redirect(url_for('register_failure', reason='user_exists'))

        # Save the new user and redirect to success page
        create_user(username, email, password, user_type, is_google_user=False)

        return redirect(url_for('register_success', username=username))

    return render_template('register/register.html')

# Route to simulate Google user registration
@app.route('/google_redirect')
def google_redirect():
    base_username = 'google_user_'
    password = '123'
    user_type = 'Landlord'

    # Find the next available username and email for Google users
    user_count = len(google_users) + 1
    while True:
        new_username = f'{base_username}{user_count:02d}'
        new_email = f'user_{user_count:02d}@gmail.com'
        
        # Check if the username or email already exists
        if not is_user_exists(new_username, new_email):
            break
        
        # Increment the counter and try the next available username/email
        user_count += 1

    # Create and append the new Google user
    create_user(new_username, new_email, password, user_type, is_google_user=True)

    # Redirect to the register_success route with the username
    return redirect(url_for('register_success', username=new_username))

# Route for successful registration
@app.route('/register_success')
def register_success():
    username = request.args.get('username')
    return render_template('register/register_success.html', username=username)

# Route for registration failure
@app.route('/register_failure')
def register_failure():
    reason = request.args.get('reason')
    return render_template('register/register_failure.html', reason=reason)

# Route to go back to the registration page
@app.route('/go_back')
def go_back():
    return redirect(url_for('register'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the email and password match a user in the users list
        user = next((u for u in users if u['username'] == username and u['email'] == email and u['password'] == password), None)

        if user:
            # If the credentials match, redirect to login success page
            return redirect(url_for('login_success', username=user['username']))
        else:
            # If credentials do not match, redirect to login failure page
            return redirect(url_for('login_failure'))

    return render_template('login/login.html')

# Route to login with a Google account
@app.route('/choose_google_account')
def choose_google_account():
    error = request.args.get('error')
    return render_template('login/auth.html', error=error)

# Route for Google sign in using email verification
@app.route('/google_signin', methods=['POST'])
def google_signin():
    email = request.form['email']
    user = find_google_user(email)

    if user:
        # Email recognized, redirect to password entry page
        return redirect(url_for('password_entry', email=email))
    else:
        # Email not recognized, redirect back with error parameter
        return redirect(url_for('choose_google_account', error=1))

# Route for Google sign in password page
@app.route('/password_entry/<email>')
def password_entry(email):
    error = request.args.get('error')
    return render_template('login/auth_pass.html', email=email, error=error)

# Direct user to a success message if correct password, else show failure message
@app.route('/password_verify/<email>', methods=['POST'])
def password_verify(email):
    password = request.form['password']
    user = find_google_user(email)

    if user and user['password'] == password:
        # Password is correct, redirect to login success page
        return redirect(url_for('login_success', username=user['username']))
    else:
        # Password is incorrect, redirect back to the password page with an error
        return redirect(url_for('password_entry', email=email, error=1))

# Route for login success page
@app.route('/login_success')
def login_success():
    username = request.args.get('username')
    return render_template('login/login_success.html', username=username)

# Route for login failure page
@app.route('/login_failure')
def login_failure():
    return render_template('login/login_failure.html')

# Route for forgot password functionality
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Simulate password reset functionality
        return redirect(url_for('forgot_password_success'))
    return render_template('login/forgot_password.html')

# Route for successful password reset
@app.route('/forgot_password_success')
def forgot_password_success():
    return render_template('login/forgot_password_success.html')

@app.route('/tenants')
def tenants():
    return render_template('tenants/tenants.html')


if __name__ == '__main__':
    app.run(debug=True)
