from flask_wtf import FlaskForm
# 导入表单字段类型
from wtforms import TextAreaField, SubmitField
# 导入字段验证器
from wtforms.validators import DataRequired, Length


# 发表博客表单
class PostsForm(FlaskForm):
    content = TextAreaField('这一刻的想法...', validators=[DataRequired(), Length(1, 128)])
    submit = SubmitField('发表')
