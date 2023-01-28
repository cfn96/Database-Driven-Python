class File:
    def __init__(self, file_type, owner_name, full_path_name, **kwargs):
        self.maps = {}
        self.maps = kwargs
        self.file_type = file_type
        self.full_path_name = full_path_name
        self.owner_name = owner_name


    def openfile(self):  # open file by connecting to server
        if self.file_type == "sqlite":
            import sqlite3 as sqlt
        self.conn = sqlt.connect(self.owner_name)
        print(type(self.conn))

    def create(self):
        create_statement = "create table {}(".format(
            self.full_path_name).upper()
        for key, value in self.maps.items():
            if type(value) == str:
                data_type = "TEXT"
            elif type(value) == float:
                data_type = "REAL"
            elif type(value) in (int, bool):  # sqlite treats bool as INT
                data_type = "INT"
            column_str = key + " " + data_type
            create_statement = create_statement + "{},".format(column_str)
        create_statement = create_statement[:-1] + ")"
        print(create_statement)
        # cur = self.conn.cursor()

    def closefile(self):  # close file by disconnecting to server
        pass


employee = File(file_type="sqlite",
                full_path_name="employee",
                owner_name="maindatabase.db",
                id=1,
                firstname="test",
                lastname=2.3,
                active=True)
employee.openfile()
