import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine(
  "mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")

db_connection_string = "mysql+pymysql://mr2zs3g0h9aow47fzcw0:pscale_pw_FajGQTNyYkihzwpENroelI5djE3I4mX17ndtfDMxCe5@ap-south.connect.psdb.cloud/joviancareers?charset=utf8mb4"
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})
with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  result_all = result.all()
  print("type(result.all) : ", type(result.all()))
  print(type(result_all[0]))
  first_result_dict = result_all[0][0]
  print("type of first result", type(first_result_dict))
  print(first_result_dict)
  result_dict = {}
  result_ld = []
  i = 0
  for result in result_all:
    result_dict['id'] = result[0]
    result_dict['title'] = result[1]
    result_dict['location'] = result[2]
    result_dict["salary"] = result[3]
    result_dict['currency'] = result[4]
    result_dict['responsibilities'] = result[5]
    result_dict['requirements'] = result[6]
    print(result_dict)
    result_ld.append(result_dict.copy())
  print(result_ld)
