class Task:
    def __init__(self, title, due_date, status, project):
        self.title = title
        self.due_date = due_date
        self.status = status
        self.project = project

    def get_title(self):
        return self.title

    def get_due_date(self):
        return self.due_date

    def get_status(self):
        return self.status

    def get_project(self):
        return self.project

    def set_title(self, new_title):
        self.title = new_title
        print(self.title)

    def set_due_date(self, new_due_date):
        self.due_date = new_due_date
        print(self.due_date)

    def set_status(self, new_status):
        self.status = new_status
        print(self.status)

    def set_project(self, new_project):
        self.project = new_project
        print(self.project)

    def to_string(self):
        return "".join(self.title + "**" + str(self.due_date) + "**" + self.status + "**" + self.project + "\n")
                                # appending \n so that each task is printed on each new line