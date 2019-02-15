from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')

class PitchFormI(FlaskForm):
    pitch = TextAreaField('Pitch Comment', validators=[Required()])
    my_category = SelectField('Category', choices=[('Interview','Interview')])
    submit = SubmitField('Submit')

class PitchFormL(FlaskForm):
    pitch = TextAreaField('Pitch Comment', validators=[Required()])
    my_category = SelectField('Category', choices=[('PickupLine','PickupLine')])
    submit = SubmitField('Submit')

class PitchFormP(FlaskForm):
    pitch = TextAreaField('Pitch Comment', validators=[Required()])
    my_category = SelectField('Category', choices=[('Promotion','Promotion')])
    submit = SubmitField('Submit')
