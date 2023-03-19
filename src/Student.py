dic = {'math': 30, 'bio': 30, 'commerce': 0}
res = 10


class Student:

    _is_handicap = 0
    _is_enrolled = 0

    @property               # Getter for Name
    def Name(self):
        return self._name

    @Name.setter            # Setter for Name
    def Name(self, new_name):
        self._name = new_name

    @property               # Getter for Email
    def Email(self):
        return self._email

    @Email.setter           # Setter for Email
    def Email(self, new_mail):
        self._email = new_mail

    @property               # Getter for Subject
    def Subject(self):
        return self._subject

    @Subject.setter         # Setter for Subject
    def Subject(self, new_subject):
        self._subject = new_subject

    @staticmethod
    def c_board():
        print("\n\n CAPACITY FULL......ENROLLMENT UNSUCCESSFUL \n\n\n----------------------------\n\n\n-------CAPACITY BOARD-------\n\n")
        print(
            '\n       Math     -- 30\n       Bio      -- 30\n       Commerce -- 00\n')
        print(
            '\n----Reservation for Handicap: 10%----\n\n\n----------------------------\n\n')
        exit()

    @staticmethod
    def enroll_fail():
        print('\n-----------------ENROLLMENT UNSUCCESSFUL-----------------\n\n\n--------------Try Again After Registeration--------------\n\n')
        exit()

    @staticmethod
    def register_fail():
        print('\n-----------------REGISTERATION UNSUCCESSFUL-----------------\n\n\n--------------Try Again to Register--------------\n\n')
        exit()

    @staticmethod
    def already_enroll():
        print("\n--------------------YOU ARE ALREADY ENROLLED---------------------\n")
        exit()

    @staticmethod
    def already_register():
        print("\n--------------------EMAIL ALREADY REGISTERED---------------------\n")

    @staticmethod
    def register_success():
        print('\n--------------REGISTERATION SUCCESSFUL--------------\n')


    def enroll_success():
        print('\n--------------ENROLLMENT SUCCESSFUL--------------\n')

    def Enroll(self, cnt, tar):
        if (self._is_handicap == 0) and (tar > 0):
            val = f'{self.Subject}'
            tmp = val.lower()
            tar = tar-int(dic[tmp]/res)
        if cnt < tar:
            self._is_enrolled = 1
            Student.enroll_success()
        else:
            Student.c_board()
