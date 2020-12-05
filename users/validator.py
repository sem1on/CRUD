import re
from django.core.exceptions import ValidationError


class CustomPasswortValidator(object):

    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        pattern = r"^((?=.*[A-Z])(?=.*\d).{8,})$"
        result = re.findall(pattern, password)
        if not (result):
            raise ValidationError("Password not valid")


    def get_help_text(self):
        return "Your Password must contain at least 1 capital letter and 1 digit."
