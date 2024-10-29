# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "runner"
"""
  * @File    :   runner.py
  * @Time    :   2023/06/06 19:51:47
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, Ship of Ocean
  * @Desc    :   None
"""
# main.py
from argparse import Namespace
from xy_argparse.ArgParse import ArgParse


class Runner(ArgParse):
    work_list = [
        "backup",
        "install",
        "install_pack",
        "load",
    ]

    @property
    def version(self):
        return "0.0.1"

    def __init__(self):
        self.prog = "xy_conda"
        self.description = "conda相关工具"

    def main(self):
        self.default_parser()
        self.add_arguments()
        if self.work:
            self.run_arguments()
        else:
            self.parser.print_help()

    def add_arguments(self):
        self.add_argument(
            flag="-w",
            name="--work",
            help_text="""
                工作方式:
                "backup",
                "install",
                "install_pack",
                "load",
            """,
        )

    def on_arguments(
        self,
        name,
        value,
        arguments=None,
    ):
        # "backup",
        # "install",
        # "install_pack",
        # "load",
        if name == "work":
            if value == "backup":
                self.backup()
                return False
            elif value == "load":
                self.load()
                return False
            elif value == "install":
                self.install()
                return False
            elif value == "install_pack":
                self.install_pack()
                return False
        return True

    def backup(self):
        print("output backup")

    def load(self):
        print("output load")

    def install(self):
        print("output install")

    def install_pack(self):
        print("output install_pack")

    @property
    def work(self):
        arguments = self.arguments()
        if isinstance(arguments, Namespace):
            return arguments.work
        return None


if __name__ == "__main__":
    runner = Runner()
    runner.main()
