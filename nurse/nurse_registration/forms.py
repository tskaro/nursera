from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, length, Email


class registration_form(FlaskForm):
    email = StringField("ელექტრონული ფოსტა", [DataRequired(), length(min=4), Email()])
    first_name = StringField("სახელი", [DataRequired()])
    last_name = StringField("გვარი", [DataRequired()])
    submit = SubmitField("Done")


class registration_form2(FlaskForm):
    address = StringField("მისამართი", [DataRequired()])
    department = StringField("დეპარტამენტი", [DataRequired()])
    shift = SelectField("მორიგეობის განრიგი:",
                        choices=[
                            (16, "16 საათიანი მორიგეობა"),
                            (24, "24 საათიანი მორიგეობა"),
                            {8, "დღის სამსახური"}
                        ])
    submit = SubmitField("Done")


class final_save_to_db(FlaskForm):
    submit = SubmitField("Save")
