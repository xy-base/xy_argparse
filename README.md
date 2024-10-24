# xy_argparse

- [简体中文](readme/README_zh_CN.md)
- [繁体中文](readme/README_zh_TW.md)
- [English](readme/README_en.md)


# 说明
命令行参数简易工具.

## 源码仓库

- <a href="https://github.com/xy-base/xy_argparse.git" target="_blank">Github地址</a>  
- <a href="https://gitee.com/xy-base/xy_argparse.git" target="_blank">Gitee地址</a>

## 安装

```bash
pip install xy_argparse
```

## 开始

```python
# main.py
from argparse import Namespace
from xy_argparse.ArgParse import ArgParse

class Runner(ArgParse):

    @property
    def version(self):
        return "0.0.1"

    def __init__(self):
        self.prog = "xy_conda"
        self.description = "conda相关工具"

    def main(self):
        self.default_parser()
        self.add_arguments()
        self.parse_arguments()
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

##### Shell
```bash
python main.py -w backup
# output backup
```


## 许可证
xy_argparse 根据 <木兰宽松许可证, 第2版> 获得许可。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## 捐赠

如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  
  
![Pay-Total](./readme/Pay-Total.png)

## 联系方式

```
微信: yuyangiit
邮箱: 845262968@qq.com
```