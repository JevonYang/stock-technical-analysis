import configparser
import os

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


def project_dir(project_name=None):
    """
        获取当前项目根路径
        :param project_name:
        :return: 根路径
        """
    PROJECT_NAME = 'stock-technical-analysis' if project_name is None else project_name
    project_path = os.path.abspath(os.path.dirname(__file__))
    root_path = project_path[:project_path.find("{}\\".format(PROJECT_NAME)) + len("{}\\".format(PROJECT_NAME))]
    return root_path


if __name__ == '__main__':
    print(project_dir())
