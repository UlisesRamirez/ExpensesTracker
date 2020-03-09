from internalData.userData.metaInf import data

#base = 42841, exp = 541
def getServiceCredentials(base, exp):
    if hex(base ** exp) == data['keyPar']:
        return True
    else:
        return False

def getPassword(query, userIndex):
    passwordsData = data['passwords']
    try:
        if passwordsData[query] == data['users'][userIndex]:
            return True
        else:
            return False
    except KeyError:
        return False

def getUser(query):
    usersData = data['users']
    if query in usersData:
        return True
    else:
        return False