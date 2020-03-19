from internalData.userData import serviceCredentials as credentials
from internalData.baseExpValues import base, exp
from internalData import moneyInfo

'''
TODO:

Thinking of adding a separated .json for every user, and
the admin account as a validator for creating new users
and assigning the new file to the user. Then establish a
dataBase-like functionality to access each of the files
separately
'''
def programFlow():
    indication = input('\nIngress the desired action: ').split()
    if indication[0] in moneyInfo.functionsList:
        if len(indication) > 1:
            if indication[1] in moneyInfo.lanes:
                action = moneyInfo.functionsList[indication[0]]
                argument = indication[1]
                action(argument)
                programFlow()
            else:
                print('Invalid lane given, try again. ')
                programFlow()
        else:
            action = moneyInfo.functionsList[indication[0]]
            action()
            programFlow()
    elif indication[0] in moneyInfo.lanes and len(indication) == 3:
        print('Adding value ' + indication[1] + ' to lane ' + indication[0])
        moneyInfo.attachData(indication[0], indication[1], indication[2])
        programFlow()
    elif len(indication) == 1 and indication[0].lower() == 'help':
        print('help') #add help paths
        programFlow()
    elif len(indication) == 1 and indication[0].lower() == 'exit':
        print('Ending session...')
        exit()
    else:
        print('unknown syntax, please try again\n')
        programFlow()

def ingressPassword(user):
    queriedPassword = str(input('Ingress your password: '))
    if credentials.getPassword(queriedPassword, user):
        print('\nWelcome ' + str(user) + '\n')
        print('Fetching resources... \n')
        programFlow()
    else:
        print('user and password doesn\'t match... ')
        ingressPassword(user)

def ingressUser():
    if credentials.getServiceCredentials(base, exp):
        queriedUser = str(input('Ingress your user: '))
        if credentials.getUser(queriedUser):
            ingressPassword(queriedUser)
        else:
            print('no user found... ')
            ingressUser()
    else:
        print('KeyError raised, review the installation and try again')

ingressUser()