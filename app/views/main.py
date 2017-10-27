from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import PostsForm
from flask_login import current_user
from app.models import Posts
from app.extensions import db


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostsForm()
    if form.validate_on_submit():
        # 判断用户是否是登录状态
        if current_user.is_authenticated:
            user = current_user._get_current_object()
            posts = Posts(content=form.content.data, user=user)
            db.session.add(posts)
            return redirect(url_for('main.index'))
        else:
            flash('登录后才能发表')
            return redirect(url_for('user.login'))
    # 分页读取数据，然后展示
    # 从请求的参数中获取当前页码，没有page参数默认为第一页
    page = request.args.get('page', 1, type=int)
    # paginate参数介绍p
    # page：唯一的必须参数，表示当前的页码
    # per_page：可选参数，表示每页显示的记录数，默认20条
    # error_out：可选参数，页码超出范围时是否显示404错误，默认为True
    pagination = Posts.query.filter_by(rid=0).order_by(Posts.timestamp.desc()).paginate(page, per_page=5, error_out=False)
    # 获取当前页的记录
    posts = pagination.items
    return render_template('main/index.html', form=form, posts=posts, pagination=pagination)

