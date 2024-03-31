from cfg_file import host, port,db_port, title, dbname, db_user, db_password
from flask import Flask, render_template, request, redirect

import database.db as postgres_db


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "C:/Users/79615/PycharmProjects/FlaskWebAppShopPython/static/images"
db = postgres_db.ConnectToDatabase(host, db_port, dbname, db_user, db_password)


@app.route("/")
@app.route("/home")
@app.route("/main")
def hello_world():
    return render_template("main_page.html", title=title, admins_lst=db.show_admins())


if __name__ == "__main__":
    app.run(debug=True,
            host=host,
            port=port)
