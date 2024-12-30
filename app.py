from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key' 


def get_db_connection():
    dbfile = sqlite3.connect('users.db')
    dbfile.row_factory = sqlite3.Row
    return dbfile


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tree')
def tree():
    return render_template('tree.html')

@app.route('/tree/<family>')
def bird_family(family):
    valid_families = ['waterbirds', 'birdsofprey', 'songbirds', 'gamebirds', 'shorebirds']
    if family.lower() in valid_families:
        return render_template(f'{family}.html')
    else:
        flash('Invalid bird family selected.', 'error')
        return redirect(url_for('tree'))

@app.route('/tree/<family>/<member>')
def bird_family_member(family, member):
    valid_members = {
        'birdsofprey': ['eagles', 'owls'],
        'waterbirds': ['ducks', 'gulls'],
        'songbirds': ['robins', 'hummingbirds'],
        'gamebirds': ['turkeys', 'pheasants'],
        'shorebirds': ['sandpipers', 'plovers']
    }

    if family in valid_members and member in valid_members[family]:
        return render_template(f'{member}.html')
    else:
        flash('Invalid bird family member selected.', 'error')
        return redirect(url_for('tree'))

@app.route('/tree/birdsofprey')
def birds_of_prey():
    return render_template('birdsofprey.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not username or not password or not confirm_password:
            flash('All fields are required!', 'error')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))

        dbfile = get_db_connection()
        cursor = dbfile.cursor()

        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            dbfile.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists. Please choose a different one.', 'error')
        finally:
            dbfile.close()
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        dbfile = get_db_connection()
        cursor = dbfile.cursor()
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        dbfile.close()

        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password.', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        flash('You must be logged in to access your profile.', 'error')
        return redirect(url_for('login'))

    dbfile = get_db_connection()
    cursor = dbfile.cursor()
    user = cursor.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()

    if request.method == 'POST':
        bio = request.form['bio']
        favorites = request.form['favorites']

        cursor.execute('UPDATE users SET bio = ?, favorites = ? WHERE id = ?', (bio, favorites, session['user_id']))
        dbfile.commit()
        flash('Profile updated successfully!', 'success')

    user = cursor.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    dbfile.close()
    return render_template('profile.html', user=user)


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
