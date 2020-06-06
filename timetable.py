class Subjects:
    """Class of university subjects"""
    def __init__(self, dictionary):
        self.subjects = dictionary['subjects']

    def __str__(self):
        return self.subjects

    def __repr__(self):
        return self.__str__()


class Timetable:
    """ Class of university schedule"""
    def __init__(self, lst_subjects):
        self.para1 = lst_subjects[0]
        self.para2 = lst_subjects[1]
        self.para3 = lst_subjects[2]
        self.para4 = lst_subjects[3]

    def __str__(self):
        return '|{:^15}|{:^15}|{:^15}|{:^15}|'.format(self.para1, self.para2, self.para3, self.para4)

    def __repr__(self):
        return self.__str__()
