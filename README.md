# CSUAutoselect

中南大学自动选课工具 V1.3

作者：[@DavidHuang](https://github.com/CrazyDaveHDY)

## 安装
### Python3
该项目需要 Python3，可以从 [Python 官网](https://www.python.org/) 下载并安装

### Repo
点击右上角的 `Clone or download` 下载该项目至本地

对于 git 命令行：
```console
$ git clone https://github.com/CrazyDaveHDY/CSUAutoSelect.git
```

### requests模块
在命令行中运行：
```console
$ pip3 install requests
```

## 运行

进入项目根目录，命令行中运行
```console
$ python3 autoselect.py
```

按照提示输入学号，教务系统密码，课程 ID 后即可开始自动选课

课程 ID 查找方法：在 [中南大学教务系统课表查询页面](http://csujwc.its.csu.edu.cn/jiaowu/pkgl/llsykb/llsykb_frm.jsp?isview=1) 中点击「按教师」按钮，输入学年学期、教师名称后点击「查询」，格子中央的 6 位数字编号即为课程 ID。

![课程 ID.png](https://i.loli.net/2021/01/13/G7mN9BUzpaHRtkw.png)

## 许可协议

CSUAutoSelect [GPL-3.0 License](https://github.com/CrazyDaveHDY/CSUAutoSelect/blob/master/LICENSE)
