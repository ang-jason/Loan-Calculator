from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import ValidationError, DataRequired, Length


class InputParamForm(FlaskForm):
    loan_amount = FloatField('Loan Amount ($)', validators=[DataRequired()])
    interest_rate = StringField('Interest Rate(s) %pa', validators=[DataRequired(), Length(min=1)])
    term_periods = StringField('Terms Period (Year)', validators=[])
    loan_tenor = IntegerField('Loan Tenor (Years)', validators=[DataRequired()])

    submit = SubmitField('Show Schedule')

    def validate_term_periods(self, term_periods):
        # print("validate_length_term_period",len(self.term_periods.data),len(self.interest_rate.data))
        if "," in self.term_periods.data or "," in self.interest_rate.data:
            print("validate_period_triggered!")
            term_periods_size = len(self.term_periods.data.split(","))
            interest_rate_size = len(self.interest_rate.data.split(","))
            # print(term_periods_size, interest_rate_size)
            if term_periods_size != interest_rate_size:
                raise ValidationError(f"Input of Interest Rate and Term Period not allowed.")

    def validate_interest_rate(self, interest_rate):
        # print("validate_length_interest_rate",len(self.term_periods.data),len(self.interest_rate.data))
        if "," in self.term_periods.data or "," in self.interest_rate.data:
            print("validate_ir_triggered!")
            term_periods_size = len(self.term_periods.data.split(","))
            interest_rate_size = len(self.interest_rate.data.split(","))
            # print(term_periods_size, interest_rate_size)
            if term_periods_size != interest_rate_size:
                raise ValidationError(f"Input of Interest Rate and Term Period not allowed.")
