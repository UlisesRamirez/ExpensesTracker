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
    print('Fetching resources... \n')
    action = input('ingress the desired action: ').split()
    if action[0] == 'clear':
        print('ask for yes or no, if yes: clear all expenses from lane if existent, if not existent: recursion, if no: recursion')
    elif action[0] == 'current':
        print('ask for desired type to calculate, if existent: pass to moneyInfo module to make the calculation, if not existent: raise KeyError then recursion')
    elif action[0] == 'exit':
        print('ask for confirmation, if yes: exit program, if no: recursion')
    elif type(action[0]) == str and type(action[1]) == int:
        print('')
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