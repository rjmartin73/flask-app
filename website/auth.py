from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('logout.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email address is too short.', category='error')
        elif len(firstName) < 2:
            flash('First name must be 2 or more characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 6 characters.', category='error')
        else:
            # add user to database
            flash('Account created', category='success')

        return render_template('signup.html',
                               email=email,
                               firstName=firstName)
    else:
        return render_template('signup.html')
