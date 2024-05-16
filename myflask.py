# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/archive')
def archive():
    try:
        with open('static/base.txt', 'r') as file:
            content = file.read()
        return render_template('archive.html', content=content)
    except FileNotFoundError:
        return "File not found", 404

    

@app.route('/register', methods=['GET', 'POST'])
def answer():
    mypoints = 0
    if request.method == 'POST':
        # Get form data
        fullname = request.form['fullname']
        dateofbirth = request.form['dateofbirth']
        education = request.form['education']
        workinghours = request.form['workinghours']
        subjectfullname = request.form['subjectfullname']
        curriculum = request.form['curriculum']
        manuals = request.form['manuals']
        
        answers = {}
        for key in request.form:
            if key.startswith('question'):
                question_number = key.split('_')[-1]
                answer_option = request.form[key]
                answers[question_number] = answer_option
                # Calculate points
                if answer_option == 'option1':
                    mypoints += 2
                elif answer_option == 'option2':
                    mypoints += 1

        
        with open('static/base.txt', 'a', encoding='utf-8') as file:
            file.write(f'fullname: {fullname}, '
            f'Dateofbirth: {dateofbirth}, '
            f'Education: {education}, '
            f'Workinghours: {workinghours}, '
            f'Subjectfullname: {subjectfullname}, '
            f'Curriculum: {curriculum}, '
            f'Manuals: {manuals}, '
            f'Points: {mypoints}\n')
        return "Շնորհակալություն հարցմանը մասնակցելու համար!"
    return render_template('answer_form.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search_query']
        results = []

        with open('static/base.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if search_query in line:
                    results.append(line)

        return render_template('search_results.html', results=results)
    return render_template('search_form.html')

if __name__ == '__main__':
    app.run(debug=True)
