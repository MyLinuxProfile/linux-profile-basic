from linux_profile import (
    __version__,
    __info__
)
from linux_profile.base.error import (
    ErrorInvalidValue,
    ErrorParameterIsMissing,
    ErrorLoadSettings,
    ErrorOptionIsMissing,
    ErrorOptionIsInvalid,
    ErrorFile,
    print_warning,
    print_error
)


class Command():

    list_option = ['id', 'module', 'tag', 'item', 'sudo', 'debug', 'group']

    def __init__(self, parser, arguments) -> None:
        self.parser = parser
        self.arguments = arguments

        self.setup_options()
        self.execute()

    def setup_options(self):
        self.id = None
        self.module = None
        self.tag = None
        self.item = None
        self.sudo = None
        self.debug = None
        self.group = None

        for option in self.list_option:
            if hasattr(self.arguments, option):
                setattr(self, option, getattr(self.arguments, option))


class BaseCommand:

    list_module = ['package', 'alias', 'script', 'file']

    def __init__(self, parser):
        self.parser = parser
        self.subparsers = self.parser.add_subparsers()

        self.argument_module = {"required": True, "choices": self.list_module}

        self.parser._positionals.title = 'Commands'
        self.parser._optionals.title = 'Default Options'
        self.parser.add_argument(
            '-v',
            '--version',
            action='version',
            version=f'linuxp=={__version__}',
            help="Show program's version number and exit.")

        self.setup_config()
        self.setup_add()
        self.setup_remove()
        self.setup_execute()
        self.setup_install()
        self.setup_uninstall()
        self.setup_list()

    def setup_config(self):
        self.cmd_config = self.subparsers.add_parser(
            'config', help="Configuration of profile files and server connection.")

        self.cmd_config = self.cmd_config.add_argument_group('Usage: linuxp config [OPTIONS]')
        self.cmd_config.add_argument('--get', help="URL of your profile file to download and sync in the current project.")

    def setup_add(self):
        self.cmd_add = self.subparsers.add_parser(
            'add', help="Parameter used to add a new item to the list in your profile file.")

        self.cmd_add = self.cmd_add.add_argument_group('Usage: linuxp add [OPTIONS]')
        self.cmd_add.add_argument('-m', '--module', **self.argument_module)

    def setup_remove(self):
        self.cmd_remove = self.subparsers.add_parser(
            'remove', help="Removes items from the profile file.")

        self.cmd_remove = self.cmd_remove.add_argument_group('Usage: linuxp remove [OPTIONS]')
        self.cmd_remove.add_argument('--id', required=True, help="Reference ID of a database item.")

    def setup_execute(self):
        self.cmd_execute = self.subparsers.add_parser('execute')

        self.cmd_execute = self.cmd_execute.add_argument_group('Usage: linuxp execute [OPTIONS]')
        self.cmd_execute.add_argument('--id', required=True, help="Reference ID of a database item.")

    def setup_install(self):
        self.cmd_install = self.subparsers.add_parser(
            'install', help="This parameter is used to install the modules, package, alias and script.")

        self.cmd_install = self.cmd_install.add_argument_group('Usage: linuxp install [OPTIONS]')
        self.cmd_install.add_argument('-m', '--module', **self.argument_module)
        self.cmd_install.add_argument('-t', '--tag')
        self.cmd_install.add_argument('-i', '--item')
        self.cmd_install.add_argument('--sudo', default='of', help="Run the command with system root permissions.", choices=['on', 'of'])
        self.cmd_install.add_argument('--debug', default='of', help="Run a command in test mode. It only shows the command.", choices=['on', 'of'])
        self.cmd_install.add_argument('--group', default='of', help="Group items for executing a command.", choices=['on', 'of'])

    def setup_uninstall(self):
        self.cmd_uninstall = self.subparsers.add_parser(
            'uninstall', help="Command used to uninstall items. Be very careful when running.")

        self.cmd_uninstall = self.cmd_uninstall.add_argument_group('Usage: linuxp uninstall [OPTIONS]')
        self.cmd_uninstall.add_argument('-m', '--module', **self.argument_module)
        self.cmd_uninstall.add_argument('-t', '--tag')
        self.cmd_uninstall.add_argument('-i', '--item')
        self.cmd_uninstall.add_argument('--sudo', default='of', help="Run the command with system root permissions.", choices=['on', 'of'])
        self.cmd_uninstall.add_argument('--debug', default='of', help="Run a command in test mode. It only shows the command.", choices=['on', 'of'])
        self.cmd_uninstall.add_argument('--group', default='of', help="Group items for executing a command.", choices=['on', 'of'])

    def setup_list(self):
        self.cmd_list = self.subparsers.add_parser(
            'list', help="Lists all modules in the terminal and can also apply filters to find items.")

        self.cmd_list = self.cmd_list.add_argument_group('Usage: linuxp list [OPTIONS]')
        self.cmd_list.add_argument('-m', '--module', **self.argument_module)
        self.cmd_list.add_argument('-t', '--tag')
        self.cmd_list.add_argument('-i', '--item')

    def run(self):
        try:
            arguments = self.parser.parse_args()
            if hasattr(arguments, 'exec'):
                arguments.exec(parser=self.parser, arguments=arguments)
            else:
                print(__info__)

        except ErrorParameterIsMissing as error:
            print_warning(str(error))

        except ErrorOptionIsMissing as error:
            print_warning(str(error))

        except ErrorOptionIsInvalid as error:
            print_warning(str(error))

        except ErrorInvalidValue as error:
            print_warning(str(error))

        except ErrorLoadSettings as error:
            print_error(str(error))

        except ErrorFile as error:
            print_error(str(ErrorFile))

        except Exception as error:
            print_error(str(error))
