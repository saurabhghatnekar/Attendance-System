import datetime

class AttendanceSystem:

    def __init__(self):
        self.input_handler = InputHandler()
        self.database_handler = DatabaseHandler()
        self.report_generator = ReportGenerator()

    def mark_attendance(self, name):
        if  self.database_handler.check_attendance(name):
            name, time= self.input_handler.mark_attendance(name)

            self.database_handler.mark_attend(name,time)

        else:
            print("User not found")
class InputHandler:

    def __init__(self):
        pass
    def mark_attendance(self,name):
        current_time = datetime.datetime.today()
        return name, current_time

class DatabaseHandler:

    def __init__(self):
        self.db = {}
        '''
        db = {"name":[timestamps]}
        '''

    def add_user(self, name ):
        if name in self.db.keys():
            print("user already exists")
        else:
            self.db[name] = []

    def check_attendance(self, name):
        if name in self.db.keys():
            return True
        else:
            return False

    def mark_attend(self,name,time):
        self.db[name].append(time)
        print('entry marked')


    def update_user(self):
        pass

    def delete_user(self):
        pass

    def get_data(self):
        pass

class ReportGenerator:

    def __init__(self):
        pass



if __name__ == '__main__':
    system = AttendanceSystem()
    system.database_handler.add_user("Saurabh")
    system.database_handler.add_user("Pavan")
    print(system.database_handler.db)
    system.mark_attendance("Saurabh")
    system.mark_attendance("Saurab")
    system.mark_attendance("saurabh")
    system.mark_attendance("Pavan")
    system.mark_attendance("Pavan")
    print(system.database_handler.db)
