import configparser

cf = configparser.ConfigParser()
cf.read("../config.ini")


def tushare_token():
    return cf.get("tushare", "token")


def databases():
    db_type = cf.get("database", "type")
    host = cf.get("database", "host")
    port = cf.get("database", "port")
    user = cf.get("database", "user")
    password = cf.get("database", "password")
    db = cf.get("database", "db")
    charset = cf.get("database", "charset")
    return '%s://%s:%s@%s:%s/%s?charset=%s' % (db_type, user, password, host, port, db, charset)
