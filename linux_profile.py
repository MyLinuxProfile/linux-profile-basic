#!/usr/bin/env python3

from setuptools import setup
from core.base.error import (
    ErrorInvalidValue,
    ErrorParameterIsMissing,
    ErrorLoadSettings,
    ErrorOptionIsMissing,
    print_warning,
    print_error
)
from core.main import (
    CommandInit,
    CommandAdd,
    CommandInstall,
    CommandUninstall,
    CommandList
)

try:
    setup(
        name="linux-profile",
        cmdclass={
            'init': CommandInit,
            'add': CommandAdd,
            'install': CommandInstall,
            'uninstall': CommandUninstall,
            'list': CommandList
        }
    )

except ErrorParameterIsMissing as error:
    print_warning(str(error))

except ErrorInvalidValue as error:
    print_warning(str(error))

except ErrorOptionIsMissing as error:
    print_warning(str(error))

except ErrorLoadSettings as error:
    print_error(str(error))

except Exception as error:
    print_error(str(error))
