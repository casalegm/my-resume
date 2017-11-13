from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def get_all_courses():
    courses = [
        'MISY225 - Introduction to Programming Business Applications',
        'MISY350 - Business Application Development II',
        'MISY430 - Systems Analysis and Implementation']
    return render_template('courses.html', courses=courses)


if __name__ == '__main__':
    app.run()
