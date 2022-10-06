#!/usr/bin/env python3

from core.base.storage import Storage
from core.base.log import run_profile
from core.base.config import BaseConfig
from core.base.validator import (
    ValidatorAddPackage,
    ValidatorAddAlias,
    ValidatorAddTerminal
)


class Add(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_config()
        self.load_profile()

        self.log = run_profile(name_log=self.__class__.__name__)
        self.data = Storage(database=self.file_profile)

        call_add = getattr(self, "add_"+self.module)
        call_add()

    def add_package(self):
        fields = ValidatorAddPackage(**{
                "category": input("Package Category [default]: "),
                "manager": input("Package Manager [apt-get, snap, deb]: "),
                "name": input("Package Name: "),
                "url": input("Package URL: "),
                "file": input("Package File: ")
            }
        )

        if not fields.is_valid:
            return

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content={
                "type": fields.manager,
                "name": fields.name,
                "url": fields.url,
                "file": fields.file
            },
            key='name'
        )

    def add_alias(self):
        fields = ValidatorAddAlias(**{
                "category": input("Alias Category [default]: "),
                "command": input("Alias Command: "),
                "content": input("Alias Content: ")
            }
        )

        if not fields.is_valid:
            return

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content={
                "content": fields.content,
                "command": fields.command,
            },
            key='command'
        )

    def add_terminal(self):
        fields = ValidatorAddTerminal(**{
                "category": input("Terminal Category [default]: "),
                "name": input("Terminal Name: ")
            }
        )

        if not fields.is_valid:
            return

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
