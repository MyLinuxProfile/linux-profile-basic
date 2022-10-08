#!/usr/bin/env python3

from core.base.storage import Storage
from core.base.config import BaseConfig
from core.base.validator import (
    ValidatorAddPackage,
    ValidatorAddAlias,
    ValidatorAddTerminal
)
from core.utils.text import asterisk


class Add(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_config()
        self.load_profile()

        self.data = Storage(database=self.file_profile)

        func = f"{self.__class__.__name__}_{self.module}".lower()
        call_add = getattr(self, func)
        call_add()

    def add_package(self):
        fields = ValidatorAddPackage(**{
                "category": input("Package Category [default]: "),
                "type": input(asterisk() + "Package Manager: "),
                "name": input(asterisk() + "Package Name: "),
                "url": input("Package URL: "),
                "file": input("Package File: ")
            }
        )

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content=fields.__dict__,
            key='name'
        )

    def add_alias(self):
        fields = ValidatorAddAlias(**{
                "category": input("Alias Category [default]: "),
                "command": input(asterisk() + "Alias Command: "),
                "content": input(asterisk() + "Alias Content: "),
                "type": "exec"
            }
        )

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content=fields.__dict__,
            key='command'
        )

    def add_terminal(self):
        fields = ValidatorAddTerminal(**{
                "category": input("Terminal Category [default]: "),
                "name": input(asterisk() + "Terminal Name: ")
            }
        )

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content={
                "name": fields.name,
                "colorscheme": {},
                "profile": {
                    "Appearance": {
                        "ColorScheme": None
                    },
                    "General": {
                        "Name": None,
                        "Parent": None
                    }
                }
            },
            key='name'
        )
