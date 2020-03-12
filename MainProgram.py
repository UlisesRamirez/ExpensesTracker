from internalData.userData import serviceCredentials as credentials
from internalData.baseExpValues import base, exp
from internalData import moneyInfo

# --------------------- AP 2 -------------------------
# Default flow of the program, manages the files in the
# moneyInfo folder, has 4 funtions: clear: empties the 
# called lane
#                                   current: sums the
# total of the seleceted lane
#                                   exit: terminates
# the program after user confirmation
#                       *lane, amount*: adds the ingressed
# amount to the selected lane if existent, if not: raise
# KeyError
#
# if none of the valid functions is ingressed prompt error
# then recursion
def programFlow():
    indication = input('Ingress the desired action: ').split()
    if indication[0] in moneyInfo.functionsList and len(indication) == 2:
        if indication[1] in moneyInfo.lanes:
            action = moneyInfo.functionsList[indication[0]]
            argument = indication[1]
            action(argument)
        else:
            print('Invalid lane given, try again. ')
            programFlow()
    elif indication[0] in moneyInfo.lanes and len(indication) == 3:
        print('Adding value ' + indication[1] + ' to lane ' + indication[0])
        moneyInfo.updateData(indication[0], indication[1], indication[2])
        programFlow()
    else:
        print('unknown syntax, please try again\n')
        programFlow()

# --------------------- AP 1 -------------------------
# User checking steps, for differentiation of the bases
# imports the verification steps from internal folders
# together with a unique key access to the users file
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