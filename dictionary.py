import sqlite3
import pyodbc


class File:
    def __init__(self, file_type, owner_name, full_path_name, **kwargs):
        self.maps = {}
        self.maps = kwargs
        self.file_type = file_type
        self.full_path_name = full_path_name
        self.owner_name = owner_name
        self.conn = "--connectivity settings here--"

    def openfile(self):  # open file by connecting to server
        if self.file_type == "sqlite":
            self.conn = sqlite3.connect(self.owner_name)
        elif self.file_type == "odbc":
            self.conn = pyodbc.connect(self.owner_name)

    def createfile(self):
        create_statement = "create table if not exists {}(".format(
            self.full_path_name).upper()
        for key, value in self.maps.items():
            if value.find("STRING") > 0:
                data_type = "TEXT"
            # elif value.find("REAL") > 0:
            #     data_type = "REAL"
            # elif value.find(t=d for d in ["LONG", "SHORT", "BYTE"]) > 0:
            #     data_type = "INT"
            column_str = key + " " + data_type
            create_statement = create_statement + "{},".format(column_str)
        create_statement = create_statement[:-1] + ")"
        self.openfile()
        cur = self.conn.cursor()
        cur.execute(create_statement)

    def closefile(self):  # close file by disconnecting to server
        pass


employee = File(file_type="sqlite",
                full_path_name="employee",
                owner_name="maindatabase.db",
                id="INT(12)",
                firstname="STRING(10)",
                lastname="STRING(10)",
                active="BYTE")
employee.createfile()
employee.openfile()
