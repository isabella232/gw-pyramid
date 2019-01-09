from wtforms import Form, StringField, TextAreaField, IntegerField, validators
from wtforms import HiddenField, PasswordField

# used to remove all whitespace from beginning and end of question
strip_filter = lambda x: x.strip() if x else None

# spawned question forms
class QuestionCreateForm(Form):
    question = TextAreaField('question', [validators.Length(min=1, max=255)],
                        filters=[strip_filter])
    type = TextAreaField('type', [validators.Length(min=1, max=255)],
                        filters=[strip_filter])
    description = TextAreaField('description', [validators.Length(max=500)],
                         filters=[strip_filter])


# class VoteCreateForm(Form):
#     vote = IntegerField('question', [validators.required()])


class QuestionOptionFrom(Form):
    question = TextAreaField('question_option', [validators.Length(min=1, max=255)], filters=[strip_filter]) 

class QuestionUpdateForm(QuestionCreateForm):
    id = HiddenField()


# original registrationForm
class RegistrationForm(Form):
    username = StringField('Enter a username here:', [validators.Length(min=1, max=255)],
                           filters=[strip_filter], default=u'')
    password = StringField('Password', [validators.Length(min=3)], default=u'test')
