import uuid

from core.utils.text import cleaning_option
from core.base.error import ErrorOptionIsMissing


class Validator():

    def __init__(self, **kwargs):
        self.id = uuid.uuid4().hex.upper()
        
        for arg in kwargs:
            value = kwargs.get(arg) if kwargs.get(arg) else None
            setattr(self, arg, value)

            if hasattr(self, "validator_"+arg):
                call = getattr(self, "validator_"+arg)
                setattr(self, arg, call(value))


class ValidatorAddPackage(Validator):

    option_manager = [
        'apt-get',
        'apt',
        'snap',
        'deb',
        'sh',
        'py',
        'dnf',
        'pacman',
        'zypper',
        'spack',
        'brew',
        'pip'
    ]

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_type(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Package Manager')

        if not value in self.option_manager:
            raise ErrorOptionIsMissing('Package Manager')

        return cleaning_option(value).lower()

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Package name')

        return cleaning_option(value)


class ValidatorAddAlias(Validator):

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_command(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Alias Command')

        return cleaning_option(value).lower()

    def validator_content(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Alias Content')

        return value


class ValidatorAddTerminal(Validator):

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Terminal Name')

        return value


class ValidatorInitDefault(Validator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ValidatorInitConfig(Validator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
