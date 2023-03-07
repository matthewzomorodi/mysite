from django.core.exceptions import ValidationError

import re

def validate_phone_number(value):
    p = re.compile('\(?\d{3}\)? ?-? ?\d{3} ?-? ?\d{4}')
    if not p.match(value):
        raise ValidationError('Phone number must be in (###)-###-#### format.')