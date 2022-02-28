from importer import DBImporter

def main():
    db_importer = DBImporter("test.db", "test_table", "tests/test_excel.xlsx")
    db_importer.add_fields({
        "Serial number": "Serial"
    })
    print(db_importer.get_excel_columns())
    print(db_importer.get_db_columns())

if __name__ == "__main__":
    main()