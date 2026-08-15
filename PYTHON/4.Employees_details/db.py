import oracledb

oracledb.init_oracle_client(
    lib_dir=r"C:\oracle\instantclient_19_31"
)

def get_connection():
    try:
        connection = oracledb.connect(
            user = "system",
            password = "system@123",
            dsn = "localhost:1521/XE"
        )
        print("Oracle Connected........")
        return connection
    
    except oracledb.Error as e:
        print("Connection failed...........")
        print("Error: ",e)
        
        return None