import sqlalchemy
from sqlalchemy import create_engine,text
engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")


db_connection_string = "mysql+pymysql://mr2zs3g0h9aow47fzcw0:pscale_pw_FajGQTNyYkihzwpENroelI5djE3I4mX17ndtfDMxCe5@ap-south.connect.psdb.cloud/joviancareers?charset=utf8mb4"
engine=create_engine(db_connection_string,
                    connect_args={"ssl":{"ssl_ca": "/etc/ssl/cert.pem"}})
with engine.connect() as conn:
  result=conn.execute(text("select * from jobs"))
  print(result.all())