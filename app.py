from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the toolkit page
@app.route('/toolkit')
def toolkit():
    return render_template('toolkit.html')

# Route for the community post page
@app.route('/community_post', methods=['GET', 'POST'])
def community_post():
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        if name and post:
            save_post(name, post)
            return redirect(url_for('community_post'))
    posts = read_posts()
    return render_template('community_post.html', posts=posts)

# Function to save the post to a text file
def save_post(name, post):
    with open('community_posts.txt', 'a') as file:
        file.write(f"Name: {name}\nPost: {post}\n\n")

# Function to read all posts from the text file
def read_posts():
    if os.path.exists('community_posts.txt'):
        with open('community_posts.txt', 'r') as file:
            return file.read()
    return ""

# Function to run subprocesses for external tools
@app.route('/run_tool/<tool_name>')
def run_tool(tool_name):
    if tool_name == 'password_manager':
        subprocess.Popen(["python", "password_manager.py"])
    elif tool_name == 'password_generator':
        subprocess.Popen(["python", "password_generator.py"])
    # Add other tools here
    return redirect(url_for('toolkit'))

if __name__ == '__main__':
    app.run(debug=True)
