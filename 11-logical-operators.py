# Python logical operators
# AND -> and
# OR -> or
# NOt -> not

has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    eligible_for_loan = True
elif has_good_credit and not has_criminal_record:
    eligible_for_loan = True
elif has_high_income and not has_criminal_record:
    eligible_for_loan = True
else:
    eligible_for_loan = False

if eligible_for_loan:
    print('Eligible for loan')
else:
    print('Not eligible for loan')