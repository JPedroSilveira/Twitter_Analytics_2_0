from Database.DBData import DBData


class BTreeInfo(DBData):
    # Id of the root
    root_id = 0

    def __init__(self):
        self.root = None
