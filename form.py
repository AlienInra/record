# -*- coding: UTF-8 -*-
# author:liujiayu

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class projectForm(FlaskForm):
    order_id = StringField(
        label="订单号",
        validators=[
            DataRequired("请输入订单号")
        ],
        description="订单号",
        render_kw={
            "class": "form-control",
            "id": "ds_host",
            "placeholder": "请输入订单号"
        }
    )

    title = StringField(
        label="资源说明",
        validators=[
            DataRequired("请输入资源名称")
        ],
        description="资源说明",
        render_kw={
            "class": "form-control",
            "id": "ds_host",
            "placeholder": "阿里云产品名，例如：ecs、rds"
        }
    )
    count = StringField(
        label="购买数量",
        validators=[
            DataRequired("请输入购买数量")
        ],
        description="购买数量",
        render_kw={
            "class": "form-control",
            "id": "ds_host",
            "placeholder": "购买数量，例如: 1"
        }
    )
    type = SelectField(
        label="消费类型",
        validators=[
            DataRequired("请输入消费类型")
        ],
        description="消费类型",
        render_kw={
            "class": "form-control",
            "id": "ds_host",
        },
        choices = [(1, '新增'), (2, '续费'), (3, '退款'),(4,'升配'),(5,'降配')],
        default = 1,
        coerce = int
    )
    system = StringField(
        label="资源归属项目/系统",
        validators=[
            DataRequired("请输入sql字段")
        ],
        description="资源归属项目/系统",
        render_kw={
            "class": "form-control",
            "id": "ds_host",
            "placeholder": "请输入具体信息"
        }
    )
    department = StringField(
        label="资源归属部门",
        validators=[
            DataRequired("请输入sql字段")
        ],
        description="资源归属部门",
        render_kw={
            "class": "form-control",
            "id": "ds_host",
            "placeholder": "请输入具体信息"
        }
    )
    owner = StringField(
        label="申请人",
        validators=[
            DataRequired("请输入sql字段")
        ],
        description="申请人",
        render_kw={
            "class": "form-control",
            "id": "ds_host",
            "placeholder": "请输入具体信息"
        }
    )
    owner_dep = StringField(
        label="申请人部门",
        validators=[
            DataRequired("请输入sql字段")
        ],
        description="申请人部门",
        render_kw={
            "class": "form-control",
            "id": "ds_host",
            "placeholder": "请输入具体信息"
        }
    )
    buyer = StringField(
        label="购买人",
        validators=[
            DataRequired("请输入sql字段")
        ],
        description="购买人",
        render_kw={
            "class": "form-control",
            "id": "ds_host",
            "placeholder": "请输入具体信息"
        }
    )
    price = StringField(
        label="消费金额",
        validators=[
            DataRequired("请输入sql字段")
        ],
        description="字段",
        render_kw={
            "class": "form-control",
            "id": "ds_host",
            "placeholder": "按量付费 计算1年金额，不满一年按实际时长计算，例如：500.25"
        }
    )

    submit = SubmitField(
        label="提交",
        render_kw={
            "class": "btn btn-primary"
        }

    )

class time_searchForm(FlaskForm):
    start_time = StringField(
        label="开始时间",
        validators=[
            DataRequired("请输入开始日期")
        ],
        render_kw={
            "class": "form-control",
            "id": "datetimepicker",
            "placeholder": "开始时间"
        }
    )
    last_time = StringField(
        label="结束时间",
        validators=[
            DataRequired("请输入结束日期")
        ],
        render_kw={
            "class": "form-control",
            "id": "datetimepicker2",
            "placeholder": "结束时间"
        }
    )

    submit = SubmitField(
        label="查询",
        render_kw={
            "class": "btn btn-default"
        }

    )