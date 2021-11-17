# Face Recognition

Face recognition using python and mysql.

*******

## Useage

### Environment

Create virtual environment using Anaconda.
```
conda create -n face python=3.x
conda activate face
pip install -r requirements.txt
```

### MySQL Install

[Mac](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/macos-installation.html)

[Ubuntu](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/linux-installation.html)

[Windows](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/windows-installation.html)

You'll obtain an account and password after installation, then you should modify the `faces.py`, with the corresponding
`user` and `passwd`:
```
# create database connection
myconn = mysql.connector.connect(host="localhost", user="root", passwd="xxxxx", database="facerecognition")
```

*******

## Run

### Once the dependencies are installed, please remember to cd into GUI folder and then run login_GUI.py 


```
cd GUI/

python3 login_GUI.py
 
```

After successful login or registration, all other screens should load automatically on click.

It is vital to only run the code from inside the GUI folder. The code will not run otherwise.


### Also update the mysql connectors in the files listed below. Change the username and password of the connecter to that which runs on your local server.

accounts.py
credit_transactions.py
dashboard.py
login_GUI.py
loginhistory.py
transactions.py



### 2. Database Design

## Load SQL table data from database.sql. 

You can copy paste the contents of database.sql file into your sql command line.

## Load SQL test data from testData.sql

Similar to how you set up the test tables, you can add the test data by copy pasting the code from testData.sql into your sql command line.

