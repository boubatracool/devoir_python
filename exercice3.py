import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///missing_number.db', echo=False)


def find_missing_number(list_int):
    x = min(list_int)
    y = max(list_int)

    for i in range(x, y + 1):
        if i not in list_int:
            missing_number = i
    
    df = pd.DataFrame({'missing_number': [missing_number]})
    df.to_sql('missing_number.db', con=engine)

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    find_missing_number(list1)
