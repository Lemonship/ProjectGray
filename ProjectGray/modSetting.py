import os
import clsMSSQL

ProjectPath = os.path.dirname(os.path.realpath(__file__))
SQLHost = "localhost"
SQLUser = "Development"
SQLPwd = "Development"
SQLDB = "Development"
MainDB = clsMSSQL.MSSQL(SQLHost,SQLUser,SQLPwd,SQLDB)
