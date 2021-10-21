import pandas as pd
import sqlite3
import sys

class DBImporter:
    def ___init__(self, db_name, db_table, excel_file):
        self.db_name = db_name
        self.db_table = db_table
        self.excel_file = excel_file
        self._field_list = None

    def require_field_list(self, func):
        def wrapper():
            if self._field_list is None:
                print("No fields exists, add_fields() needs to run first.")
                sys.exit(1)
            else:
                func()
        return wrapper

    def add_fields(self, field_list: dict):
        # Dictionary with name of column in excel as key and name of column in database as value.
        self._field_list = field_list

    @require_field_list
    def get_excel_columns(self):
        return self._field_list.keys()
    
    @require_field_list
    def get_db_columns(self):
        return self._field_list.values()

    def import_to_db(self):
        pass