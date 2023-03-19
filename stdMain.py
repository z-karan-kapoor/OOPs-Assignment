from Student import Student
from Validate import Validate

class Test():

    stu1 = Student()
    val1 = Validate()


    def set_name(self):
        """It sets the name after validation"""
        name = input('\n--------------Enter your Name:--------------\n')
        if self.val1.valid_name(name) == 1:
            self.stu1.Name = name
        else:
            self.stu1.register_fail()


    def search_str(self,file_path, word, cnt, tar):
        """It searches in the text file for given string"""
        flag = 0
        with open(r"stuRegistered.txt", 'r') as fp:
            for l_no, line in enumerate(fp):
                # search string
                if word in line:
                    # print('string found in a file')
                    if (cnt < tar):
                        self.stu1.Enroll(cnt, tar)
                        file1 = open(file_path, "a")
                        file1.write(f'ENROLLED-{self.stu1.Email}\n')
                        flag = 1
                        break
                    else:
                        self.stu1.c_board()
        if flag == 0:
            self.stu1.enroll_fail()


    def set_mail(self,sub, file_name):
        """It sets the mail after validation"""
        self.stu1.Email = input('\n-------------Enter your mail-------------\n')
        if self.val1.check(self.stu1.Email) == 1:
            if self.val1.search_str('stuRegistered.txt', f'REGISTERED-{self.stu1.Email}') == 0:
                file1 = open(file_name, "a")
                file1.write(f'REGISTERED-{self.stu1.Email}\n')
                self.stu1.register_success()
                # file1.close()
            else:
                self.stu1.already_register()
                self.enroll_process()
                exit()
        else:
            self.stu1.register_fail()


    def check_handicap(self):
        """Checks if the person is handicap"""
        hcap = input('\n--------------Are you Handicap?   Y/N--------------\n')
        if (hcap == 'Y') or (hcap == 'y'):
            self.stu1._is_handicap = 1
        elif (hcap == 'N') or (hcap == 'n'):
            self.stu1._is_handicap = 0
        else:
            self.stu1.register_fail()


    def set_subject(self):
        """It sets the subject to enroll"""
        sub = input(
            '\n-------Enter the subject you want to enroll: Math | Bio | Commerce-------\n')
        if (sub == 'Bio') or (sub == 'bio') or (sub == 'Math') or (sub == 'math') or (sub == 'Commerce') or (sub == 'commerce'):
            self.stu1.Subject = sub
        else:
            self.stu1.register_fail()


    def cnt_values(self,file_name):
        """It counts the number of lines in the text file"""
        file = open(file_name, "r")
        Counter = 0

        # Reading from file
        Content = file.read()
        CoList = Content.split("\n")

        for i in CoList:
            if i:
                Counter += 1
        return Counter


    def enroll_process(self):
        """Enroll the student to desired subject"""
        print('\n---------------ENROLLMENT PROCESS--------------\n')
        en = input(
            f'\n---------------Press Y to Enrollment for {self.stu1.Subject} else N--------------\n')
        if en == 'Y' or en == 'y':
            str = self.stu1.Subject
            tmp = f'{str.lower()}Data.txt'
            if self.val1.search_str(tmp, f'ENROLLED-{self.stu1.Email}') == 1:
                self.stu1.already_enroll()
            else:
                if self.stu1.Subject == 'Bio' or self.stu1.Subject == 'bio' or self.stu1.Subject == 'Math' or stu1.Subject == 'math':
                    tar = 30
                    cnt = self.cnt_values(tmp)
                    tmp = self.search_str(tmp, self.stu1.Email, cnt, tar)
                elif self.stu1.Subject == 'Commerce' or self.stu1.Subject == 'commerce':
                    tar = 0
                    cnt = self.cnt_values('commerceData.txt')
                    tmp = self.search_str('commerceData.txt', self.stu1.Email, cnt, tar)
                else:
                    self.stu1.c_board()
        elif en == 'N' or en == 'n':
            exit()
        else:
            self.stu1.enroll_fail()

if __name__=="__main__":
    obj=Test()
    print('\n---------------REGISTERATION PROCESS--------------\n')
    obj.set_name()
    obj.set_subject()
    obj.check_handicap()
    obj.set_mail(obj.stu1.Subject, 'stuRegistered.txt')
    obj.enroll_process()
