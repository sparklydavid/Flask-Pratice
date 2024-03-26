from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")
# ("login.html", myText="Testing")
# in base.html {myText}

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='err')
        elif len(firstName) <2:
            flash('First Name must be greater than 2 characters', category='err')
        elif len(password1)<7:
            flash('Password must be at least 7 characters', category='err')
        elif password1 != password2:
            flash('Password don\'t match ', category='err')
        else:
            flash('Account Created!', category='succ')

    return render_template("sign_up.html")
