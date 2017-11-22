from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    White = Professor(name='White', department='MISY')
    Gillespie = Professor(name='Gillespie', department='ACCT')
    Wang = Professor(name='Wang', department='MISY')
    MISY430 = Course(title='Systems Analysis and Implementation', number=430, description='Covers the challenges of developing and managing systems analysis and design projects.', professor=White)
    ACCT425 = Course(title='Strategic Information Systems and Accounting', number=425, description='Explores the role of accounting and information systems in accomplishing the strategic goals of the corporation.', professor=White)
    ACCT327 = Course(title='Cost Accounting', number=327, description='Process, job order and standard costing; variable and absorption costing; budgeting, decentralization, and transfer pricing; and cost analysis for managerial applications.', professor=Gillespie)
    MISY350 = Course(title='Business Application Development II', number=350, description='Covers concepts related to client side development, including cascading style sheets and JavaScript.', professor=Wang)
    db.session.add(White)
    db.session.add(Gillespie)
    db.session.add(Wang)
    db.session.add(MISY430)
    db.session.add(ACCT425)
    db.session.add(ACCT327)
    db.session.add(MISY350)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
