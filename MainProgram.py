from internalData.userData import serviceCredentials as credentials
from internalData.baseExpValues import base, exp
from internalData import moneyInfo

def programFlow(session):
    indication = input('\nIngress the desired action: ').split()
    if indication[0] in session.functionsList:
        if len(indication) > 1:
            if indication[1] in session.lanes:
                action = session.functionsList[indication[0]]
                argument = indication[1]
                action(session, argument)
                programFlow(session)
            else:
                print('Invalid lane given, try again. ')
                programFlow(session)
        else:
            try:
                action = session.functionsList[indication[0]]
                action(session)
                programFlow(session)
            except TypeError:
                print('unknown syntax, please try again\n')
                programFlow(session)
    elif indication[0] in session.lanes and len(indication) == 3:
        print('Adding value ' + indication[1] + ' to lane ' + indication[0])
        session.attachData(indication[0], indication[1], indication[2])
        programFlow(session)
    else:
        print('unknown syntax, please try again\n')
        programFlow(session)

def ingressPassword(user):
    queriedPassword = str(input('Ingress your password: '))
    if credentials.getPassword(queriedPassword, user):
        print('\nWelcome ' + str(user) + '\n')
        print('Fetching resources... \n')
        session = moneyInfo.Session(user)
        programFlow(session)
    else:
        print('user and password doesn\'t match... ')
        ingressPassword(user)

def ingressUser():
    if credentials.getServiceCredentials(base, exp):
        queriedUser = str(input('Ingress your user: '))
        if credentials.getUser(queriedUser):
            ingressPassword(queriedUser)
        else:
            ingressUser()
    else:
        print('KeyError raised, review the installation and try again')

ingressUser()