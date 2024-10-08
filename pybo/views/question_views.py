from crypt import methods

from flask import Blueprint, render_template, request, url_for, g, flash
from datetime import datetime
from pybo.models import Question
from ..forms import QuestionForm, AnswerForm
from werkzeug.utils import redirect
from .. import db
from pybo.views.auth_views import login_required

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list():
    # Page
    page = request.args.get('page', type=int, default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template(
        'question/question_list.html',
        question_list=question_list
    )

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template(
        'question/question_detail.html', question=question, form=form
    )

@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(
            subject=form.subject.data,
            content=form.content.data,
            create_date=datetime.now(),
            user=g.user
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template(
        'question/question_form.html',
        form=form
    )

@bp.route('/modify/<int:question_id>', methods=("GET", "POST"))
@login_required
def modify(question_id):
    question = Question.query.get_or_404(question_id)

    if g.user != question.user:
        flash("No Modify Permission")
        return redirect(url_for('question.detail', question_id=question_id))

    if request.method == 'POST':
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(question)
            question.modify_date = datetime.now() #Update modify date
            db.session.commit()
            return redirect(url_for('question.detail', question_id=question_id))
    else: #IF method is GET
        form = QuestionForm(obj=question)
    return render_template('question/question_form.html', form=form)
