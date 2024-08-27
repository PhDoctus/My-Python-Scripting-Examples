class User():

    def __init__(self, name, job, passphrase='password1'):

        self.name = name
        self.job = job
        self.passphrase = passphrase


        name = input('Please provide us with your full name: ')
        job = input('Please provide us with your current occupation:')


        print('Welcome', name.title() + ',', 'you will be starting a new position as', job.title(), end='!\n')

        print('\nYour password is,', passphrase)

    def updatepassword(self, new_password):

        self.new_password = new_password

        new_password = input('\nPlease enter your new passphrase: ')

        print('\nYour updated password is', new_password)

    '''def administrator(self, priveleges=[], clearance=[]):

        self.priveleges = priveleges
        self.clearance = clearance

        priveleges = ['delpassword', 'printMainOffice', 'updateWebsite', 'companyCreditCard']
        clearance = ['first', 'second', 'third', 'fourth', 'fifth']'''

class Administrator(User):

    def __init__(self, privileges='', clearance=''):
        super().__init__(privileges, clearance)

        privileges = ['clear Directory', 'update Log', 'clear Log', 'update Directory']
        clearance = ['AB', 'AAB', 'BA']

        clearance_level = (input('Your clearance level is: ', ))

        print('\nYou have', clearance_level, 'clearance!', end='\n')



        while True:
            #for x in xy: define class/list of positions and assign those positions to clearance levels

            if clearance_level == 'AB':
                print('\nYou have the following privileges:', privileges[0])

                break

            elif clearance_level == 'AAB':
                print('\nYou have the following privileges:', privileges[0:2])

                break

            elif clearance_level == 'BA':
                print('\nYou have the following privileges:', privileges[0:])

                break

            else:
                print('\nRestricted. You have not been given clearance!')

                break



Administrator().updatepassword('')
Administrator()




