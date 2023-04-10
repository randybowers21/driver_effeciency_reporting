class QueryFailedError(Exception):
    def __init__(self, queries: list):
        self.queries = queries
        self.message = f'{len(self.queries)} query/queries failed see error message and try again'
        super().__init__(self.message)

class ItemNotInDbError(Exception):
    def __init__(self, item: tuple):
        self.item = item
        self.message = f'The item {item[0]} with the value {item[1]} you are trying to find was not found in the database'
        super().__init__(self.message)