from flask import Flask, render_template, jsonify

app = Flask(__name__)

from database import engine,text


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()
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
    return result_ld


JOBS = load_jobs_from_db()


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
