# -*- coding: UTF-8 -*-
# author:liujiayu

from datetime import datetime
from db import db


class Consume(db.Model):
    __tablename__="ali_record"
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.String(100),comment="订单号")
    title = db.Column(db.String(255),comment="阿里云产品名 如ecs、rds")
    count = db.Column(db.Integer,comment="申请数量")
    type = db.Column(db.String(255),comment="新增、续费、退款")
    system = db.Column(db.String(255),comment="资源归属项目")
    department = db.Column(db.String(255),comment="资源归属部门")
    owner = db.Column(db.String(100),comment="申请人")
    owner_dep = db.Column(db.String(255),comment="申请人部门")
    buyer =db.Column(db.String(255),comment="购买人")
    price = db.Column(db.Numeric(precision=10,scale=4),comment="消费金额")
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)
    change_time = db.Column(db.DateTime, index=True, default=datetime.now,onupdate=datetime.now, comment="更改时间")
