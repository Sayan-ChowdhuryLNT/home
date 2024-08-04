
import sqlite3
from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from Mainapp import app
import time
from flask_login import LoginManager
from flask_session import Session
import threading
from datetime import datetime, timedelta

auth_bp = Blueprint('auth_bp', __name__, template_folder="templates")
app.permanent_session_lifetime = timedelta(hours=8)
app.secret_key = '956956'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

admin= ["sayan.chowdhury@lntecc.com","balajirajadurai@lntecc.com","karthiga@lntecc.com","sudripta.misra@lntecc.com","prabhakaranm@lntecc.com","srb@lntecc.com","rpvenkatesh@lntecc.com","bnk@lntecc.com"]
editpradmins= ["sayan.chowdhury@lntecc.com","balajirajadurai@lntecc.com","karthiga@lntecc.com","srb@lntecc.com","rpvenkatesh@lntecc.com","prabhakaranm@lntecc.com",'bnk@lntecc.com']


login_manager = LoginManager()
login_manager.init_app(app)


class User(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
class userlogin(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000)) 
    loggedin = db.Column(db.String(1000)) 
    loggedout = db.Column(db.String(1000)) 
    timespent = db.Column(db.Float) 
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ic = db.Column(db.String(255), nullable=False)
    sbg = db.Column(db.String(255), nullable=False)
    bu = db.Column(db.String(255), nullable=False)
    emanage = db.Column(db.String(255), nullable=False)
    plead = db.Column(db.String(255), nullable=True)
    mlead = db.Column(db.String(255), nullable=True)
    elead = db.Column(db.String(255), nullable=True)
    ilead = db.Column(db.String(255), nullable=True)
    scmlead = db.Column(db.String(255), nullable=True)
    others = db.Column(db.String(255), nullable=True)
    project_name = db.Column(db.String(255), nullable=False)
    client_name = db.Column(db.String(255), nullable=False)
    job_code = db.Column(db.String(50), nullable=False)
    process_date = db.Column(db.String(50), nullable=True)
    mech_date = db.Column(db.String(50), nullable=True)
    elec_date = db.Column(db.String(50), nullable=True)
    instru_date = db.Column(db.String(50), nullable=True)
    other_date = db.Column(db.String(50), nullable=True)
    


class PR_data_Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ic = db.Column(db.String(255), nullable=True)
    sbg = db.Column(db.String(255), nullable=True)
    bu = db.Column(db.String(255), nullable=True)
    job_code = db.Column(db.String(50), nullable=True)
    project_name = db.Column(db.String(255), nullable=True)
    discipline = db.Column(db.String(255), nullable=True)
    equipment= db.Column(db.String(255), nullable=True)
    item_code = db.Column(db.String(255), nullable=True)
    item_vendor_code = db.Column(db.String(255), nullable=True)
  
    vendor_name = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    remarks = db.Column(db.String(255), nullable=True)
    pr_issue_date_pre= db.Column(db.String(255), nullable=True)
    pr_issue_date_final= db.Column(db.String(255), nullable=True)
    offer_recv_date= db.Column(db.String(255), nullable=True)
    comments_sent_pre= db.Column(db.String(255), nullable=True)
    tc_meeting_vendor_pre= db.Column(db.String(255), nullable=True)
    final_vendor_doc_pre= db.Column(db.String(255), nullable=True)
    sent_to_scm= db.Column(db.String(255), nullable=True)
    priority= db.Column(db.String(255), nullable=True)
    po_issued_date= db.Column(db.String(255), nullable=True)
    finalized_vendor=db.Column(db.String(255), nullable=True)
    post_doc_rcv_dt= db.Column(db.String(255), nullable=True)
    comments_sent_post= db.Column(db.String(255), nullable=True)
    tc_meeting_vendor_post= db.Column(db.String(255), nullable=True)
    final_vendor_doc_post= db.Column(db.String(255), nullable=True)
    mfc_issued_date= db.Column(db.String(255), nullable=True)
    target_completion_date= db.Column(db.String(255), nullable=True)
    last_modified_by= db.Column(db.String(255), nullable=True)
    
    
    

class pr_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ic = db.Column(db.String(255), nullable=False)
    sbg = db.Column(db.String(255), nullable=False)
    bu = db.Column(db.String(255), nullable=False)
    job_code = db.Column(db.String(50), nullable=False)
    project_name = db.Column(db.String(255), nullable=False)
    discipline = db.Column(db.String(255), nullable=False)
    equipment= db.Column(db.String(255), nullable=False)
    item_code = db.Column(db.String(255), nullable=False)
    item_vendor_code = db.Column(db.String(255), nullable=False)
  
    vendor_name = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    elapsed_days = db.Column(db.String(255), nullable=True)
    remarks = db.Column(db.String(255), nullable=True)
    vendor_ph = db.Column(db.String(255), nullable=True)
    vendor_mail = db.Column(db.String(255), nullable=True)
    
    
    pr_issue_date_pre= db.Column(db.Date, nullable=True)
    pr_issue_date_final= db.Column(db.Date, nullable=True)
    offer_recv_date= db.Column(db.Date, nullable=True)
    comments_sent_pre= db.Column(db.Date, nullable=True)
    offer_recv_date_2= db.Column(db.Date, nullable=True)
    comments_sent_pre_2= db.Column(db.Date, nullable=True)
    offer_recv_date_3= db.Column(db.Date, nullable=True)
    comments_sent_pre_3= db.Column(db.Date, nullable=True)
    offer_recv_date_4= db.Column(db.Date, nullable=True)
    comments_sent_pre_4= db.Column(db.Date, nullable=True)
    offer_recv_date_5= db.Column(db.Date, nullable=True)
    comments_sent_pre_5= db.Column(db.Date, nullable=True)
    tc_meeting_vendor_pre= db.Column(db.Date, nullable=True)
    final_vendor_doc_pre= db.Column(db.Date, nullable=True)
    sent_to_scm= db.Column(db.Date, nullable=True)
    priority= db.Column(db.String(255), nullable=True)
    po_issued_date= db.Column(db.Date, nullable=True)
    finalized_vendor=db.Column(db.String(255), nullable=True)
    post_doc_rcv_dt= db.Column(db.Date, nullable=True)
    comments_sent_post= db.Column(db.Date, nullable=True)
    tc_meeting_vendor_post= db.Column(db.Date, nullable=True)
    final_vendor_doc_post= db.Column(db.Date, nullable=True)
    mfc_issued_date= db.Column(db.Date, nullable=True)
    target_completion_date= db.Column(db.Date, nullable=True)
    last_modified_by= db.Column(db.String(255), nullable=True)    
    
    
class pr_data_temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ic = db.Column(db.String(255), nullable=False)
    sbg = db.Column(db.String(255), nullable=False)
    bu = db.Column(db.String(255), nullable=False)
    job_code = db.Column(db.String(50), nullable=False)
    project_name = db.Column(db.String(255), nullable=False)
    discipline = db.Column(db.String(255), nullable=False)
    equipment= db.Column(db.String(255), nullable=False)
    item_code = db.Column(db.String(255), nullable=False)
    item_vendor_code = db.Column(db.String(255), nullable=False)
  
    vendor_name = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    elapsed_days = db.Column(db.String(255), nullable=True)
    remarks = db.Column(db.String(255), nullable=True)
    vendor_ph = db.Column(db.String(255), nullable=True)
    vendor_mail = db.Column(db.String(255), nullable=True)
    
    
    pr_issue_date_pre= db.Column(db.Date, nullable=True)
    pr_issue_date_final= db.Column(db.Date, nullable=True)
    offer_recv_date= db.Column(db.Date, nullable=True)
    comments_sent_pre= db.Column(db.Date, nullable=True)
    offer_recv_date_2= db.Column(db.Date, nullable=True)
    comments_sent_pre_2= db.Column(db.Date, nullable=True)
    offer_recv_date_3= db.Column(db.Date, nullable=True)
    comments_sent_pre_3= db.Column(db.Date, nullable=True)
    offer_recv_date_4= db.Column(db.Date, nullable=True)
    comments_sent_pre_4= db.Column(db.Date, nullable=True)
    offer_recv_date_5= db.Column(db.Date, nullable=True)
    comments_sent_pre_5= db.Column(db.Date, nullable=True)
    tc_meeting_vendor_pre= db.Column(db.Date, nullable=True)
    final_vendor_doc_pre= db.Column(db.Date, nullable=True)
    sent_to_scm= db.Column(db.Date, nullable=True)
    priority= db.Column(db.String(255), nullable=True)
    po_issued_date= db.Column(db.Date, nullable=True)
    finalized_vendor=db.Column(db.String(255), nullable=True)
    post_doc_rcv_dt= db.Column(db.Date, nullable=True)
    comments_sent_post= db.Column(db.Date, nullable=True)
    tc_meeting_vendor_post= db.Column(db.Date, nullable=True)
    final_vendor_doc_post= db.Column(db.Date, nullable=True)
    mfc_issued_date= db.Column(db.Date, nullable=True)
    target_completion_date= db.Column(db.Date, nullable=True)
    target_completion_date_po= db.Column(db.Date, nullable=True)
    
    target_completion_date_post= db.Column(db.Date, nullable=True)
    
    last_modified_by= db.Column(db.String(255), nullable=True)    
    
    
        
    
        
    
    

class pr_data_backup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ic = db.Column(db.String(255), nullable=False)
    sbg = db.Column(db.String(255), nullable=False)
    bu = db.Column(db.String(255), nullable=False)
    job_code = db.Column(db.String(50), nullable=False)
    project_name = db.Column(db.String(255), nullable=False)
    discipline = db.Column(db.String(255), nullable=False)
    equipment= db.Column(db.String(255), nullable=False)
    item_code = db.Column(db.String(255), nullable=False)
    item_vendor_code = db.Column(db.String(255), nullable=False)
  
    vendor_name = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    elapsed_days = db.Column(db.String(255), nullable=True)
    remarks = db.Column(db.String(255), nullable=True)
    vendor_ph = db.Column(db.String(255), nullable=True)
    vendor_mail = db.Column(db.String(255), nullable=True)
    
    
    pr_issue_date_pre= db.Column(db.Date, nullable=True)
    pr_issue_date_final= db.Column(db.Date, nullable=True)
    offer_recv_date= db.Column(db.Date, nullable=True)
    comments_sent_pre= db.Column(db.Date, nullable=True)
    offer_recv_date_2= db.Column(db.Date, nullable=True)
    comments_sent_pre_2= db.Column(db.Date, nullable=True)
    offer_recv_date_3= db.Column(db.Date, nullable=True)
    comments_sent_pre_3= db.Column(db.Date, nullable=True)
    offer_recv_date_4= db.Column(db.Date, nullable=True)
    comments_sent_pre_4= db.Column(db.Date, nullable=True)
    offer_recv_date_5= db.Column(db.Date, nullable=True)
    comments_sent_pre_5= db.Column(db.Date, nullable=True)
    tc_meeting_vendor_pre= db.Column(db.Date, nullable=True)
    final_vendor_doc_pre= db.Column(db.Date, nullable=True)
    sent_to_scm= db.Column(db.Date, nullable=True)
    priority= db.Column(db.String(255), nullable=True)
    po_issued_date= db.Column(db.Date, nullable=True)
    finalized_vendor=db.Column(db.String(255), nullable=True)
    post_doc_rcv_dt= db.Column(db.Date, nullable=True)
    comments_sent_post= db.Column(db.Date, nullable=True)
    tc_meeting_vendor_post= db.Column(db.Date, nullable=True)
    final_vendor_doc_post= db.Column(db.Date, nullable=True)
    mfc_issued_date= db.Column(db.Date, nullable=True)
    target_completion_date= db.Column(db.Date, nullable=True)
    last_modified_by= db.Column(db.String(255), nullable=True)    
    removed_by= db.Column(db.String(255), nullable=True)    
    
    
    
    
    
    
    
    





class StatusTableData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    discipline = db.Column(db.String(255))
    equipment = db.Column(db.String(255))
    vendor_name = db.Column(db.String(255))
    offer_received = db.Column(db.String(255))
    status = db.Column(db.String(255))


class vendorDataBank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    EMI_Items = db.Column(db.String(255))
    vendor_Name = db.Column(db.String(255))
    person = db.Column(db.String(255))
    contact_no = db.Column(db.String(255))
    e_mail = db.Column(db.String(255))
    location = db.Column(db.String(255))
    designation = db.Column(db.String(255))
    scope_of_work = db.Column(db.String(255))
    address = db.Column(db.String(500))
    type_of_supplier = db.Column(db.String(255))

    def __repr__(self):
        return f"<StatusTableData {self.id}>"




with app.app_context():
    db.create_all()

def session_expired():
    """Check if the session has expired."""
    now = datetime.now()
    if 'last_activity' in session:
        last_activity = session['last_activity']
        # Define your session expiration time here, for example 4 hours
        expiration_time = timedelta(hours=8)
        return now - last_activity > expiration_time
    return False

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
@app.route('/lnt')
@auth_bp.route('/login')
def login():
    thread_count = threading.active_count()
    if thread_count > 1:
        print(f"This Flask application is running with : {thread_count} threads")

    return render_template('login.html')

@auth_bp.route('/homepage', methods=['POST'])
def login_post():
    # login code goes here
    global uname,login_time,login_timestamp
    login_time = time.time()
    login_timestamp = datetime.now()
    uname = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(name=uname).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user:
        flash('Username does not exist')
        return f"""
                <script>
                    alert('Username does not exist');
                    window.location.href = '/lnt/login';
                </script>
                """ # if the user doesn't exist or password is wrong, reload the page
    if not check_password_hash(user.password, password):
        flash('Password is incorrect')
        return f"""
                <script>
                    alert('Password is incorrect');
                    window.location.href = '/lnt/login';
                </script>
                """
        # return jsonify({'message': 'Form data received successfully'})
    else:
        conn = sqlite3.connect('C:\\Users\\Sayan\\Downloads\\Vendor_Engineering\\WETDESK2-Vendor_Engineering\\instance\\database.sqlite3')
        cursor = conn.cursor()

        cursor.execute('SELECT scmlead FROM project')
        session['scm'] = cursor.fetchall()
        transformed_emails = ['none' if email[0] is None else email[0] for email in session['scm']]
        print(transformed_emails)
        if user.email in transformed_emails:
            print("homepage SCM",uname)
            session["user"] = uname
            return render_template('homepage.html', flagscm=1)
        else:
            print("homepage ",uname)
            session["user"] = uname
            return render_template('homepage.html', flagscm=0)
    
    
@auth_bp.route('/signup')
def signup():
    return render_template('signup.html')


@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('username')
    password = request.form.get('password')
    print(email,name,password)
    email_already_exists = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    user = User.query.filter_by(name=name).first() # if this returns a user, then the username already exists in database

    
    if email_already_exists: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return f"""
                <script>
                    alert('Email address already exists');
                    window.location.href = '/lnt/signup';
                </script>
                """
    if user: # if a username is found, we want to redirect back to signup page so user can enter different username
        flash('Username already exists')
        return f"""
                <script>
                    alert('Username already exists');
                    window.location.href = '/lnt/signup';
                </script>
                """   
    if '@lntecc.com' not in email:
        flash('Please enter an official mail address')
        return f"""
                <script>
                    alert('Please enter an official mail address');
                    window.location.href = '/lnt/signup';
                </script>
                """
    if len(password)<4:
        flash('Please enter password of atleast 4 characters')
        return redirect(url_for('auth_bp.signup'))

    else:
        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth_bp.login'))

@auth_bp.route('/homepage')
def homepage():
    session_expired_flag = False
    if "user" in session:
        userr = session["user"]
        user = User.query.filter_by(name=userr).first()
        conn = sqlite3.connect('C:\\Users\\Sayan\\Downloads\\Vendor_Engineering\\WETDESK2-Vendor_Engineering\\instance\\database.sqlite3')
        cursor = conn.cursor()

        cursor.execute('SELECT scmlead FROM project')
        session['scm'] = cursor.fetchall()
        transformed_emails = ['none' if email[0] is None else email[0] for email in session['scm']]
        print(transformed_emails)
        if user.email in transformed_emails:
            print("homepage SCM",userr)
            return render_template('homepage.html', flagscm=1)
        else:
            print("homepage",userr)
            return render_template('homepage.html', flagscm=0)
    else:
        # Check if session has expired
        if session_expired():
            session_expired_flag = True
        return render_template(
            'login.html',
            title='Login',
            year=datetime.now().year,
            message='Kindly Enter User Details',
            session_expired_flag=session_expired_flag
        )

@auth_bp.route('/newproject')
def newproject():
    if "user" in session :
        userr = session["user"]
        user = User.query.filter_by(name=userr).first()
        email = user.email  # Access the email ID of the logged-in user
        if email in admin:
            print("newproject", userr, email)
            return render_template(
                    'createproject.html',
                    year=datetime.now().year,
                    title='New Project',
                    message='')
        else:
            return render_template(
        'nopermission.html',
        title='Permission Denied',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )
    else:
        return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )


@auth_bp.route('/manageproject')
def manageproject():
    if "user" in session :
        userr = session["user"]
        user = User.query.filter_by(name=userr).first()
        email = user.email  # Access the email ID of the logged-in user
        if email in admin:
            print("manageproject", userr, email)
            return render_template(
                    'manageproject.html',
                    year=datetime.now().year,
                    title='Manage Projects',
                    message='')
        else:
            return render_template(
        'nopermission.html',
        title='Permission Denied',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )
    else:
        return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )








@auth_bp.route('/project')
def project():
    if "user" in session:
        userr = session["user"]
        print("project",userr)
        return render_template(
            'projects.html',
            year=datetime.now().year,
            title='Project Details',
            message=''
            )
    else:
        return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )
    

@auth_bp.route('/newpr')
def newpr():
    if "user" in session:
        userr = session["user"]
        print("newpr",userr)
        return render_template(
            'newpr.html',
            year=datetime.now().year,title='Add PR',
            message=''
            )
    else:
        return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )
@auth_bp.route('/prstatus')
def prstatus():
    if "user" in session:
        userr = session["user"]
        print("prstatus",userr)
        return render_template(
            'prstatus.html',
            year=datetime.now().year,
            title='PR Data ',
            message=''
            )
    else:
        return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )
    

@auth_bp.route('/updatepr')
def updatepr():
    if "user" in session:
        userr = session["user"]
        print("updatepr",userr)
        return render_template(
            'updatepr.html',
            year=datetime.now().year,
            title='Update PR',
            message=''
            )
    else:
        return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )
        
        
@auth_bp.route('/editpr')
def editpr():
    if "user" in session :
        userr = session["user"]
        user = User.query.filter_by(name=userr).first()
        email = user.email  # Access the email ID of the logged-in user
        if email in editpradmins:
            print("editpr", userr, email)
            return render_template(
                    'editpr.html',
                    year=datetime.now().year,
                    title='Edit PR',
                    message='')
        else:
            return render_template(
        'nopermission.html',
        title='Permission Denied',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )
    else:
        return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )



@auth_bp.route('/dashboard')
def dashboard():
    if "user" in session:
        userr = session["user"]
        print("dashboard",userr)
        return render_template(
            'dashboard.html',
            year=datetime.now().year,
            title='Management Console',
            message=''
            )
    else:
        return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )


@auth_bp.route('/databank')
def databank():
    if "user" in session:
        userr = session["user"]
        print("databank",userr)
        return render_template(
            'databank.html',
            year=datetime.now().year,
            title='Data Bank',
            message=''
            )
    else:
        return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )
@auth_bp.route('/edit_databank')
def edit_databank():
    if "user" in session:
        userr = session["user"]
        print("edit databank",userr)
        return render_template(
            'edit_databank.html',
            year=datetime.now().year,
            title='Data Bank',
            message=''
            )
    else:
        return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Kindly Enter User Details'
        )

@auth_bp.route('/logout')
def logout():
    global login_time,logout_time,login_timestamp,logout_timestamp   
    logout_time = time.time()
    logout_timestamp = datetime.now()
    try:
        login_time
    except:
        login_time=logout_time-60
    try:
        login_timestamp
    except:
        login_timestamp=logout_timestamp
    
    username_logged = session["user"]

    time_elapsed = logout_time-login_time
    time_elapsed = round(time_elapsed,3)
    userloginobj = userlogin(name=username_logged,loggedin=login_timestamp,loggedout=logout_timestamp,timespent=time_elapsed)
    db.session.add(userloginobj)
    db.session.commit()    
    session.pop("user", None)
    return render_template ('logout.html',message="Successfully Logged Out")




def get_email():
    if "user" in session :
            userr = session["user"]
            user = User.query.filter_by(name=userr).first()
            email = user.email  # Access the email ID of the logged-in user
            return email