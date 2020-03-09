from internalData.userData import serviceCredentials as credentials
from internalData.baseExpValues import base, exp
from internalData.moneyInfo import outgoData

# --------------------- AP 2 -------------------------
def programFlow(ingressedUser):
    print('Fetching resources... ')

# --------------------- AP 1 -------------------------
# User checking steps, for differentiation of the bases
# imports the verification steps from internal folders
# together with a unique key access to the users file
def ingressPassword(user):
    queriedPassword = str(input('Ingress your password: '))

    if credentials.getPassword(queriedPassword, user):
        print('Welcome ' + str(user))
        programFlow(user)
    else:
        print('user and password doesn\'t match... ')
        ingressPassword(user)

def ingressUser():
    queriedUser = str(input('Ingress your user: '))

    if credentials.getServiceCredentials(base, exp):
        if credentials.getUser(queriedUser):
            ingressPassword(queriedUser)
        else:
            print('no user found... ')
            ingressUser()
    else:
        print('KeyError raised, review the installation and try again')

ingressUser()