# -*- coding: UTF-8 -*-
# author:liujiayu

from flask import Flask, render_template,flash, redirect, url_for, request
from form import  projectForm, time_searchForm
from model import Consume
from db import db
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csrd_key'
app.config['SQLALCHEMY_DATABASE_URI'] = "xxxxxx" #mysql+pymysql://user:password@ip:port/db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PAGE_SET']=50
db.init_app(app)


@app.route('/add',methods=['GET','POST'])
def hello_world():
    form = projectForm()
    try:
        if form.validate_on_submit():
            data=form.data
            type_dict = {1: "新增", 2: "续费", 3: "退款", 4: "升配", 5: "降配"}
            type_data = {}
            for ty in type_dict:
                if data["type"] == ty:
                    type_data[data["type"]] = type_dict[data["type"]]
            ali_info = Consume(
                title=data["title"],
                count=data["count"],
                type=type_data[data["type"]],
                system=data["system"],
                department=data["department"],
                owner=data["owner"],
                owner_dep=data["owner_dep"],
                buyer=data["buyer"],
                price=data["price"],
                order_id=data["order_id"]

            )
            db.session.add(ali_info)
            db.session.commit()
            flash("提交消费记录成功","ok")
            return redirect(url_for("table"))
    except Exception as e:
        logger.exception(str(e))
        e_data=str(e).split("[")
        flash("ERROR:{}".format(e_data[0]),"err")

    return render_template("add.html", form=form)


@app.route('/',methods=['GET','POST'])
def table():


    page = int(request.args['page']) if request.args.get('page') else 1
    form = time_searchForm()
    page_data = Consume.query.order_by(Consume.create_time.asc()).paginate(page=int(page), per_page=app.config['PAGE_SET'])

    if request.method=="GET":
        if request.args.get('title'):
            page_data = Consume.query.filter(Consume.title.like('%'+request.args.get('title')+'%'),).order_by(
                Consume.create_time.asc()).paginate(page=page, per_page=app.config['PAGE_SET'])

        if request.args.get('owner'):
            page_data = Consume.query.filter(Consume.owner == request.args.get('owner')).order_by(
                Consume.create_time.asc()).paginate(page=page, per_page=app.config['PAGE_SET'])

    if form.validate_on_submit():
        data = form.data
        start_time = data['start_time']
        last_time = data['last_time']
        page_data=Consume.query.filter(Consume.create_time >= start_time).filter(Consume.create_time <= last_time).order_by(
            Consume.create_time.asc()).paginate(page=int(page),per_page=app.config['PAGE_SET'])


    return render_template("index.html", form=form,page_data=page_data)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5001,debug=True)