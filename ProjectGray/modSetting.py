import os
import clsMSSQL

ProjectPath = os.path.dirname(os.path.realpath(__file__))
SQLHost = "localhost"
SQLUser = "sa"
SQLPwd = "edshk"
SQLDB = "Development"
MainDB = clsMSSQL.MSSQL(SQLHost,SQLUser,SQLPwd,SQLDB)
