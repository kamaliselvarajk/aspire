import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as a

class NumberValidator(object):
    def validate(self, password, user=None):
        if not len(re.findall('\d', password)) >= 3:
            raise ValidationError(a('Invalid password!'))
        else:
            return True

class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(a('Invalid password!'))
        else:
            return True