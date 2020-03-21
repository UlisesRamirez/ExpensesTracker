from internalData.userData.metaInf import data, addNewUser

def getServiceCredentials(base, exp):
    if hex(base ** exp) == data['keyPar']:
        return True
    else:
        return False

def getPassword(query, userIndex):
    passwordsData = data['passwords']
    try:
        if passwordsData[query] == data['users'][userIndex]['index']:
            return True
        else:
            return False
    except KeyError:
        return False

def setPassword(user):
    password1 = str(input('Set your password {}: '.format(user)))
    password2 = str(input('Confirm your password: '))
    if password1 == password2:
        print('Adding new user... ')
        index = len(data['users'])
        data['users'][user] = {"privileges": "user", "index": index}
        data['passwords'][password1] = index
        addNewUser(data)
    else:
        print('Passwords doesn\'t match.')
        setPassword(user)

def createNewUser():
    newUser = str(input('How do you want to be named: '))
    if newUser not in data['users']:
        setPassword(newUser)
    else:
        print('That name is already being used. Please try again.')
        createNewUser()

def getAdminAccount(attempts = 0):
    admUser = str(input('Ingress a valid admin account to get editing privileges: '))
    if admUser in data['users'] and data['users'][admUser]['privileges'] == 'admin':
        admPass = str(input('Ingress the password for {}: '.format(admUser)))
        try:
            if data['passwords'][admPass] == data['users'][admUser]['index']:
                createNewUser()
            else:
                if attempts < 5:
                    print('Wrong password.')
                    attempts += 1
                    getAdminAccount(attempts)
                else:
                    print('too many wrong attempts.')
                    exit()
        except KeyError:
            if attempts < 5:
                print('Wrong password.')
                attempts += 1
                getAdminAccount(attempts)
            else:
                print('too many wrong attempts.')
                exit()
    else:
        if attempts < 5:
            print('Admin account not valid...')
            print('try again.')
            attempts += 1
            getAdminAccount(attempts)
        else:
            print('too many wrong attemps.')
            exit()

def getUser(query):
    usersData = data['users']
    if query in usersData:
        return True
    else:
        prompt = str(input('No user {} found, do you want to create a new user? '.format(query))).lower()
        if prompt == 'yes':
            getAdminAccount()
            return False
        else:
            return False