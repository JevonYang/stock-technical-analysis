from sqlalchemy import create_engine
from utils import config

engine = create_engine(config.databases(), encoding='utf8')


def save_to_db(dataframe, table_name, index=False):
    dataframe.to_sql(table_name, con=engine, if_exists='append', index=index)
