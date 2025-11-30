# Reindeer - Python 快速启动项目管理器

[English](README-EN.md)

目前众多项目每次启动不同项目的时候需要避免项目冲突创建虚拟环境然后安装依赖后，启动项目，这不利于我们快速开发，这同样在我做项目的时候遇到的一些问题，为了避免重复工作，作者因此才制作了该项目。
Reindeer - Python 虚拟环境管理器 是一个图形化工具，旨在简化 Python 项目的设置和管理，快速启动虚拟环境然后启动项目。通过简洁美观的界面，它可以轻松创建虚拟环境、管理依赖项并执行自动化启动项目脚本。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)

## 功能特点

- 自动检测安装`uv`项目
- 使用 `uv` 工具创建 Python 虚拟环境
- 自动从 `requirements.txt` 安装依赖
- 可以自动写入默认启动的项目入口 py 文件
- 可配置自定义包索引镜像源用于快速下载不同依赖包
- 生成 Windows 批处理文件，启动虚拟环境快速启动项目，避免每次需要启动虚拟环境然后再启动项目。
- 美观、现代化的彩色图形界面

## 环境要求

- Python 3.7+
- [uv](https://github.com/astral-sh/uv) - 极速的 Python 包安装和解析工具

## 安装方法

以下方法是对于想研究源代码的成员所需，对于新手可以用我这边编译好的包即可。

1. 确保预定义环境存在
   ```
   uv venv [项目名称]
   ```
2. 克隆或下载此仓库
3. 安装所需依赖（如果环境中还没有）：
   ```
   uv pip install -r requirements.txt
   ```

## 使用方法

运行应用程序：

1. 激活虚拟环境
2. 运行应用程序：
   ```
   python run.py
   ```

## 应用功能说明

在图形界面中：

- 选择项目目录
- 配置虚拟环境选项
- 点击"执行配置"设置环境
- 可选生成批处理文件用于快速启动

### 环境配置选项卡

- **项目路径**：选择 Python 项目的根目录
- **虚拟环境名称**：虚拟环境的名称（默认为"venv"）
- **自动安装 UV**：如果 uv 不存在则自动安装
- **安装 requirements.txt**：如果存在则安装其中的依赖项
- **镜像源**：指定自定义包索引 URL
- **执行脚本**：环境设置完成后运行的 Python 脚本

### 批处理文件生成选项卡

- **生成批处理文件**：创建一个 Windows 批处理文件，该文件将：
  1. 激活预定义环境
  2. 激活项目虚拟环境
  3. 导航回项目目录
  4. 执行指定的 Python 脚本（如有）
  5. 保持命令提示符窗口开启

## 工作原理

Reindeer - Python 虚拟环境管理器利用超快的 [uv](https://github.com/astral-sh/uv) 工具来创建虚拟环境和管理包，通过一系列的配置环境的指令达到快速启动项目的目的。生成的批处理文件允许一致地激活环境和执行脚本。

所有操作都会在预定义的 Python 环境中执行，确保使用正确的 Python 版本和依赖。

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

该项目基于 MIT 许可证 - 详见 LICENSE 文件了解详情。
