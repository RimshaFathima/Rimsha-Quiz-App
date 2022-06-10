from flask import Flask,render_template,request,session,redirect
app=Flask(__name__)
app.config['SECRET_KEY']='1234'

@app.route("/")
def home():
    name='Rimsha'
    location='UAE'
    session['my_name']=name
    session['place']=location
    return '''<h1 style='color:red;'>
    Hello Everyone</h1>
    <p>This is a Paragraph<p>
    '''  
 #building route
@app.route('/aboutme')
def aboutme():
    return 'This is About Myself'

@app.route('/evenorodd',methods=['GET','POST'])
def evenorodd(): 
    if request.method=='GET':
        return render_template('evenorodd.html')
    elif request.method=='POST':    
        number=int(request.args.get("number"))
    result=""   
    if number%2==0:
            result='even'
    elif number%2!=0: 
            result='odd'
    return render_template("evenorodd.html",output=result)    
 
@app.route('/max_num',methods=['GET','POST'])
def max_num():
    #Checking wheather user is logged in or not
    if session.get('authenticated')!= True:
        return redirect('/register')
    if request.method=='GET':
       return render_template('max.html')
    elif request.method=='POST':
        n1=int(request.form.get('num1'))
        n2=int(request.form.get('num2'))
        n3=int(request.form.get('num3'))
        results=''
        if n1>n2 and n1>n3:
            result='num1 is greatest among 3'
        elif n2>n1 and n2>n3:
            result='num2 is greatest among 3'
        elif n3>n2 and n3>n2:
            result='num3 is greatest among 3'    
        return render_template('max.html',result=result) 

emails=['user1@gmail.com','user2@gmail.com','user3@gmail.com']
passwords=[123,456,789]

@app.route('/register',methods=['GET','POST'])   
def validate_register():
    if request.method=='GET':
        name=session.get('my_name' , 'user')
        message='Hello' + name + 'Welcome to Registeration Page'
        return render_template('register.html',message=message)
    elif request.methods=='POST':
        name=request.form.get('name')
        email=request.form.get('email')    
        age=int(request.forms.get('age'))
        password=request.form.get('password') 
        message=''
        #CHECK WHEATHER EMAIL IS ALREADY PRESENT IN THE LIST
        if email in emails:
            message='Email ID already exists'
        elif email not in emails:  
            if password not in passwords and age>=12:
                message= ('Hi' + name +'Registeration Succesful')
                emails.append(email)
                passwords.append(password)
                session['my_email']=email
                session['my_password']=password
        elif password in passwords:
            message='The given password is taken , please use another one'
        elif age<12:
            message='Your below 12 , Please come back when your 12 or above '
        else: 
            message='age should be more than or equal to 12'
        return render_template('register.html',ouput=message)  

@app.route('/login',methods=['GET' ,'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        email_session=session.get("my email") 
        password_session=session.get('password')
        message=''
    if email==email_session and password==password_session:
        message='Login Succcessful !'
        session['authenticated']=True
        session['authenticated']=True #session{"authenticated":True}
        return render_template('home.html' ,message=message)    
    else:
        message='Email or Password is incorrect'
        return render_template('login.html',message=message)  

#QUIZ APPLICATION

@app.route('/q1', methods=['GET', 'POST'])
def q1():
    score=session.get('score',0)
    #User is'nt logged inn
    # if session.get('authenticated') !=True:
    #     return redirect('/login')
    if request.method=="GET":
        return render_template('question_1.html')
    elif request.method=='POST':   
        correct_answer='a' 
        user_option=request.form.get('option')
        message=''
        if user_option==correct_answer:
            message='Your Correct !'
            score=score+10
            session['score']=score  #10
        else:  
            message='Incorrect !'  
        return render_template('question_2.html',message=message)

@app.route('/q2', methods=['GET', 'POST'])
def q2():
    if request.method=='GET':
        return render_template('question_2.html')
    elif request.method=='POST':
        correct_answer='c' 
        user_option=request.form.get('option')
        message=''
        if user_option==correct_answer:
            message='Your Correct !'
            score=score+10
            session['score']=score  #10
        else:  
            message='Incorrect !'  
        return render_template('question_3.html',message=message)  
@app.route('/q3', methods=['GET', 'POST'])
def q3():
    if request.method=='GET':
        return render_template('question_3.html')
    elif request.method=='POST':
        correct_answer='b'
        user_option=request.form.get('option')
        message=''
        if user_option==correct_answer:
            message='Your Correct!'
            score=score+10
            session['score']=score
        else:
            message="Incorrect !"
        return render_template('question_4.html',messsage=message)                   
@app.route('/q4', methods=['GET', 'POST'])
def q4():
    if request.method=='GET':
        return render_template('question_3.html')
    elif request.method=='POST':
        correct_answer='c'
        user_option=request.form.get('option')
        message=''
        if user_option==correct_answer:
            message='Your Correct!'
            score=score+10
            session['score']=score
        else:
            message="Incorrect !"
        return render_template('question_5.html',messsage=message)                     
@app.route('/q5', methods=['GET', 'POST'])
def q5():
    if request.method=='GET':
        return render_template('question_3.html')
    elif request.method=='POST':
        correct_answer='b'
        user_option=request.form.get('option')
        message=''
        if user_option==correct_answer:
            message='Your Correct!'
            score=score+10
            session['score']=score
        else:
            message="Incorrect !"
        return render_template('question_6.html',messsage=message)   
                  
@app.errorhandler(404)
def page_not_found(e):
    # Note that we set the 404 status explicitly
    return render_template('404.html'), 404 

leaderboard= [[1, 'test1', 'test12@gmail.com', 50],
             [2, 'test1', 'test12@gmail.com', 50],
             [3, 'test1', 'test12@gmail.com', 50],
             [4, 'test1', 'test12@gmail.com', 50],
             [5, 'test1', 'test12@gmail.com', 50]]
@app.route('/leaderboard')
def leaderboard_data():
    return render_template('leader_board.html',leaderboard=leaderboard)  
            
if __name__=='__main__':
    app.run(debug=True)        




                     



 
 

