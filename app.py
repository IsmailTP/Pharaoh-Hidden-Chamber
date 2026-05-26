from flask import Flask, render_template, request, redirect, url_for, session
import base64

app = Flask(__name__)
app.secret_key = 'super_secret_pharaoh_key_no_one_can_guess'

# Simulated backend database
users = {
    1: {"name": "Pharaoh", "role": "admin"},
    101: {"name": "Explorer", "role": "user"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    # Auto-login the user as Explorer
    session['user_id'] = 101
    # Base64 of '101' is 'MTAx'
    encoded_id = base64.b64encode(b'101').decode('utf-8')
    return redirect(url_for('temple', glyph=encoded_id))

@app.route('/temple')
def temple():
    glyph = request.args.get('glyph')
    
    if not glyph:
        return "The temple doors remain closed. You are missing a glyph.", 400
        
    if glyph == 'admin':
        return render_template('temple.html', fake_warning=True)

    try:
        decoded_id = base64.b64decode(glyph).decode('utf-8')
        user_id = int(decoded_id)
        
        # Fake logs structure - seen on the backend CLI
        actual_session_user = session.get('user_id', 'Unknown')
        print(f"SECURITY LOG: Session User {actual_session_user} accessing identity {user_id}")
        
        # Authorization failure (IDOR) - intentionally missing user check vs session
        if user_id in users:
            identity = users[user_id]
            is_pharaoh = user_id == 1
            return render_template('temple.html', identity=identity, is_pharaoh=is_pharaoh, glyph=glyph)
        else:
            return render_template('temple.html', dangerous_path=True)
            
    except Exception as e:
        return "The glyph is corrupted... the curse awakens.", 400

@app.route('/chamber')
def chamber():
    glyph = request.args.get('glyph')
    if not glyph:
        return "You must be Pharaoh to enter.", 403
        
    try:
        decoded_id = base64.b64decode(glyph).decode('utf-8')
        if int(decoded_id) == 1:
            return render_template('chamber.html')
        else:
            return "You are not the Pharaoh. The chamber seals itself.", 403
    except:
        return "Corrupt glyph.", 400

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
