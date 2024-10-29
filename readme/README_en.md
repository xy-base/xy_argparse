# xy_argparse

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

# Description
Simple tool for command line arguments.

## Source Code Repositories

- <a href="https://github.com/xy-base/xy_argparse.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-base/xy_argparse.git" target="_blank">Gitee</a>

## Installation

```bash
# bash
pip install xy_argparse
```

## Start

```python
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
```

```bash
# bash
python main.py -w backup
# output backup
```

## License
xy_argparse is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```