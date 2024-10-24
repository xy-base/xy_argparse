# xy_argparse

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

# 說明
簡單Python控制台輸入輸出工具封裝.

## 程式碼庫

- <a href="https://github.com/xy-base/xy_argparse.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-base/xy_argparse.git" target="_blank">Gitee位址</a>

## 安裝
```bash
pip install xy_argparse
```

## 開始

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
        self.description = "conda相關工具"

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

##### Shell
```bash
python main.py -w backup
# output backup
```

## 許可證
xy_argparse 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: 845262968@qq.com
```