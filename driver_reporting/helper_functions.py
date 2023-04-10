from datetime import datetime

class DbMessages:
    def create_save_message(data:str,) -> str:
        return f'New {data} data has been saved to database'
    
    def create_be_sure_to_commit_message(data:str) -> str:
        return f'New {data} data ready but not saved. Ensure "commit" is set to true to save to database'

    def create_deleted_message():
        pass

def get_first_day_of_current_year() -> datetime:
    """ Returns first day of current year """
    current_year = datetime.today().year
    return datetime(current_year, 1, 1)

   