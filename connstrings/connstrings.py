# this exists so only one point of change in event connstring needs to change
# may need to change the driver depending on your machine
# same again for trusted_connection (windows credentials for MSSQL Server login)
# this function does not have functionality to change either


def msss_connstring(host, database_name):
    return f"mssql+pyodbc://{host}/{database_name}?driver=SQL+Server+Native+Client+11.0?trusted_connection=yes"
