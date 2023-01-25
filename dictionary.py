class File:
    def __init__(self, file_type, owner_name, full_path_name, **kwargs):
        self.maps = {}
        self.maps = kwargs
        self.file_type = file_type
        self.full_path_name = full_path_name
        self.owner_name = owner_name

        if self.file_type == "sqlite":
            import sqlite3

    def openfile(self):  # open file by connecting to server
        pass

    def create(self):
        # print(self.maps)
        create_statement = "CREATE TABLE {}"
        for value in self.maps.values():
            if type(value) == str:
                print("string")
            elif type(value) == float:
                print("float")
            elif type(value) in (int, bool):  # sqlite treats bool as INT
                print("int")
            else:
                print("called")

    def closefile(self):  # close file by disconnecting to server
        pass


employee = File(file_type="sqlite", full_path_name="EMPLOYEE", owner_name="maindatabase.db", id=1, firstname="test",
                lastname=2.3, active=True)
employee.create()
