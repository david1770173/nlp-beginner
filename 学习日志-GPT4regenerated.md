model: chatGPT4(no customization)
prompt: 这是我今天的学习记录，非常的潦草，请你加入一些解释性的语言，让我的学习记录可以变成一份发布在互联网上的教程。
---

# 开始NLP学习之旅：使用Anaconda和VSCode

## Day 1: 准备工作（2月8日）

在这个NLP（自然语言处理）学习之旅的第一天，我决定从基础做起，为自己搭建一个稳定且高效的开发环境。这里是我完成的步骤，希望对你也有帮助。

### 第一步：获取代码库

首先，我从GitHub上找到了一个适合初学者的NLP项目：[FudanNLP/nlp-beginner](https://github.com/FudanNLP/nlp-beginner)。通过fork和clone这个项目，我成功地在本地创建了一个工作副本，这是开始任何项目的第一步。

### 第二步：解决编码问题

在初步检查代码时，我遇到了乱码问题。为了解决这个问题，我将我的VSCode默认编码设置改为了UTF-8。这是一个简单但有效的解决方案，可以避免在处理文件时遇到编码兼容性问题。

### 第三步：安装Anaconda

为了避免环境配置问题，我决定使用Anaconda，这是一个流行的虚拟环境管理工具。具体来说，我选择了Miniconda，因为它比完整的Anaconda更轻量，只需下载500MB，而不是几GB。后续所需的包可以随时安装，非常方便。

#### 换源提速

在Anaconda Prompt中执行以下命令，将包的下载源切换到清华大学的镜像，以加快下载速度：

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```

#### Anaconda的基本操作

- 创建虚拟环境：`conda create -n 环境名 python=版本号`
- 查看虚拟环境：`conda info --envs`
- 激活环境：`activate 环境名`
- 退出环境：`conda deactivate`（不需要指定环境名）
- 安装包：`conda install 包名`
- 使用pip：Anaconda环境中也支持pip安装
- 删除包：`conda uninstall 包名`
- 删除环境：`conda remove -n 环境名 --all`

小提示：通过`conda <子命令> --help`可以查看任何命令的帮助信息。

### 第四步：配置VSCode

尽管PyCharm是一个强大的IDE，但我选择了VSCode作为我的开发环境，因为VSCode对Markdown有更好的支持。我安装了以下扩展来优化Python开发体验：

- Python
- Python Debugger
- Python Indent
- Python Extension Packs

通过`Ctrl+Shift+P`打开命令面板，选择Python解释器时，我遇到了一个问题：Anaconda创建的环境没有立即显示出来。通过查找解决方案，我发现可以参考[Stack Overflow上的这个讨论](https://stackoverflow.com/questions/59502466/vs-code-python-interactive-window-cannot-find-conda-env)来解决问题。

注意，VSCode中“Python：python path”现在已更名为“Python：python interpreter path”。

小提示：Conda命令也可以在VSCode的终端或Powershell中输入，这让环

境管理变得非常方便。

---

通过这些步骤，我成功地为自己的NLP学习之旅搭建了一个强大且灵活的开发环境。希望这份指南能帮助你顺利开始自己的编程之旅。如果你有任何问题或建议，欢迎在下方留言交流。让我们一起学习，一起进步！