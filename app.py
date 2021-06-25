import pandas as pd
from flask import Flask
from flask import request, render_template, flash
import pickle
app = Flask(__name__)

# secret key to use flash
app.secret_key = 'epsilonpiclubvbit'


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/assignment')
def assignment():
    return render_template('assignment.html')


@app.route('/coding_challenge')
def coding_challenges():
    return render_template('coding_challenge.html')


@app.route('/mentor')
def mentor():
    return render_template('mentor_review.html')


@app.route('/mentor_login', methods=['POST'])
def mentor_login():
    if request.method == 'POST':
        key = request.form['key']
        review_type = request.form['review_type']
        with open('pickle_files/key_validation_file.pkl', 'rb') as file:
            key_ = pickle.load(file)
        if key_ == key:
            if review_type == 'assignment':
                return render_template('assignment.html')
            else:
                return render_template('coding_challenge.html')
        else:
            flash('Login Key is incorrect')
            return render_template('mentor_review.html', flag=1, msg='Login Key is incorrect. Try again!')



@app.route('/add_assignment', methods=['POST'])
def add_assignment_progress():
    df = pd.read_csv('assignments.csv')
    usernames_df = pd.read_csv('usernames_data.csv')
    if request.method == 'POST':
        mentee_name = request.form['name']
        mentee_score = int(request.form['score'])
        assigment_no = int(request.form['assign_no'])
        no_of_problems = int(request.form['total_problems'])
        solved_problems = int(request.form['solved_problems'])
        remark = request.form['remark']
        if mentee_name in list(usernames_df['user_name']):
            if mentee_name not in list(df['user_name']):
                score_t = 0
            else:
                filt = df[df['user_name'] == mentee_name]
                score_t = filt.tail(1)['total_score']
            total_score = int(score_t) + mentee_score
            total_score = int(total_score/10)
            add_row = {'user_name': mentee_name,
                       'assignment_no': assigment_no,
                       'no_of_problems': no_of_problems,
                       'no_of_solved_problems': solved_problems,
                       'score': mentee_score,
                       'total_score': total_score,
                       'remarks': remark
                       }
            df = df.append(add_row, ignore_index=True)
            df.to_csv('assignments.csv', index=False)
            flash("Added Successfully")
            return render_template('assignment.html', flag=1)
        else:
            flash('Entered wrong username')
            return render_template('assignment.html', flag=0)




@app.route('/add_coding_challenge', methods=['POST'])
def add_coding_challenges_progress():
    df = pd.read_csv('coding_challenges.csv')
    usernames_df = pd.read_csv('usernames_data.csv')
    if request.method == 'POST':
        mentee_name = request.form['name']
        mentee_score = int(request.form['score'])
        coding_challenge_no = int(request.form['assign_no'])
        no_of_problems = int(request.form['total_problems'])
        solved_problems = int(request.form['solved_problems'])
        remark = request.form['remark']
        if mentee_name in list(usernames_df['user_name']):
            if mentee_name not in list(df['user_name']):
                score_t = 0
            else:
                filt = df[df['user_name'] == mentee_name]
                score_t = filt.tail(1)['total_score']
            total_score = int(score_t) + mentee_score
            total_score = int(total_score / 10)
            add_row = {
                'user_name': mentee_name,
                'coding_challenge_no': coding_challenge_no,
                'no_of_problems': no_of_problems,
                'no_of_solved_problems': solved_problems,
                'score': mentee_score,
                'total_score': total_score,
                'remarks': remark
            }
            df = df.append(add_row, ignore_index=True)
            df.to_csv('coding_challenges.csv', index=False)
            flash("Added Successfully")
            return render_template('coding_challenge.html', flag=1)
        else:
            flash('Entered wrong username')
            return render_template('coding_challenge.html', flag=0)


@app.route('/dashboard', methods=['POST'])
def dashboard():
    if request.method == 'POST':
        assignment_df = pd.read_csv('assignments.csv')
        code_df = pd.read_csv('coding_challenges.csv')
        usernames_df = pd.read_csv('usernames_data.csv')
        hacker_rank_id = request.form['name']
        if hacker_rank_id in list(usernames_df['user_name']):
            assign_filter = assignment_df[assignment_df['user_name'] == hacker_rank_id]
            code_filter = code_df[code_df['user_name'] == hacker_rank_id]

            if (hacker_rank_id in list(assignment_df['user_name'])) and (hacker_rank_id in list(code_df['user_name'])):
                perc_ass = int(((assign_filter['no_of_solved_problems'].sum())/(assign_filter['no_of_problems'].sum()))*100)
                perc_code = int(((code_filter['no_of_solved_problems'].sum())/(code_filter['no_of_problems'].sum()))*100)
                return render_template('dashboard.html', name=hacker_rank_id, max_bar=100, max_line=20,  values_assign=list(assign_filter['score']),
                                       assign_problem_list=[assign_filter['no_of_problems'].sum(), assign_filter['no_of_solved_problems'].sum(), perc_ass],
                                       labels_assign=list(assign_filter['assignment_no']), tot_score_assign=list(assign_filter['total_score']),
                                       values_code=list(code_filter['score']), labels_code=list(code_filter['coding_challenge_no']),
                                       code_problem_list=[code_filter['no_of_problems'].sum(), code_filter['no_of_solved_problems'].sum(), perc_code],
                                       tot_score_code=list(code_filter['total_score'])
                                       )

            elif hacker_rank_id in list(assignment_df['user_name']):
                perc_ass = int(((assign_filter['no_of_solved_problems'].sum())/(assign_filter['no_of_problems'].sum()))*100)
                return render_template('dashboard.html', name=hacker_rank_id, max_bar=100, max_line=20,  values_assign=list(assign_filter['score']),
                                       assign_problem_list=[assign_filter['no_of_problems'].sum(), assign_filter['no_of_solved_problems'].sum(), perc_ass],
                                       labels_assign=list(assign_filter['assignment_no']), tot_score_assign=list(assign_filter['total_score']),
                                       values_code=[0], labels_code=[0],
                                       code_problem_list=[0, 0, 0],
                                       tot_score_code=[0]
                                       )
            elif hacker_rank_id in list(code_df['user_name']):
                perc_code = int(((code_filter['no_of_solved_problems'].sum()) / (code_filter['no_of_problems'].sum())) * 100)
                return render_template('dashboard.html', name=hacker_rank_id, max_bar=100, max_line=20,  values_assign=[0],
                                       assign_problem_list=[0, 0, 0], labels_assign=[0], tot_score_assign=[0],
                                       values_code=list(code_filter['score']), labels_code=list(code_filter['coding_challenge_no']),
                                       code_problem_list=[code_filter['no_of_problems'].sum(), code_filter['no_of_solved_problems'].sum(), perc_code],
                                       tot_score_code=list(code_filter['total_score'])
                                       )
            else:
                flash("Profile not added!")
                return render_template('login.html', flag=1, msg=" we didn't add your profile to Dashboard. We'll let you know, once it is added.", name=hacker_rank_id)
        else:
            flash("We couldn't recognize your Username.")
            return render_template('login.html', flag=0, msg="We couldn't recognize your ID.")


if __name__ == '__main__':
    app.run(debug=True)
