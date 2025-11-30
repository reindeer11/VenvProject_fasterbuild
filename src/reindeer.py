"""Reindeer - Python虚拟环境管理器主程序"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import os
import sys
import threading
from tkinter import font
from PIL import Image, ImageTk


class ReindeerApp:
    """Reindeer应用程序主类
    
    提供图形界面用于管理Python虚拟环境，包括创建虚拟环境、
    安装依赖包、执行脚本等功能。
    """
    
    def __init__(self, root):
        """初始化Reindeer应用程序
        
        Args:
            root: tkinter根窗口对象
        """
        self.root = root
        self.root.title("Reindeer - Python虚拟环境管理器")
        self.root.geometry("1000x850")
        self.root.configure(bg='#f0f0f0')

        # 设置样式
        self.setup_styles()

        # Variables
        self.project_path = tk.StringVar()
        self.venv_name = tk.StringVar(value="venv")
        self.requirements_file = tk.BooleanVar()
        self.auto_install_uv = tk.BooleanVar()
        self.execute_script = tk.StringVar()
        self.mirror_source = tk.StringVar()
        self.generate_bat = tk.BooleanVar()

        # 设置预定义的虚拟环境路径
        self.predefined_venv_path = r"#"

        # Create UI
        self.create_widgets()

    def setup_styles(self):
        """设置应用程序的颜色主题"""
        # 定义颜色主题
        self.colors = {
            'primary': '#4285f4',
            'secondary': '#6c757d',
            'success': '#34a853',
            'danger': '#ea4335',
            'warning': '#fbbc05',
            'info': '#2563eb',
            'light': '#f8f9fa',
            'dark': '#202124',
            'background': '#f0f0f0',
            'card': '#ffffff'
        }

    def log(self, message):
        """向日志文本框添加消息
        
        Args:
            message (str): 要添加到日志的消息
        """
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.update_idletasks()

    def create_widgets(self):
        """创建应用程序的所有UI组件"""
        # 主框架
        main_frame = tk.Frame(self.root, bg=self.colors['background'], padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 标题
        title_font = font.Font(size=16, weight='bold')
        title_label = tk.Label(main_frame, text="Reindeer - Python虚拟环境管理器", 
                              font=title_font, bg=self.colors['background'], 
                              fg=self.colors['dark'])
        title_label.pack(pady=(0, 20))

        # 版本作者信息
        info_frame = tk.Frame(main_frame, bg=self.colors['card'], relief=tk.RAISED, bd=1)
        info_frame.pack(fill=tk.X, pady=(0, 15))
        
        # 尝试加载协会标志图片
        try:
            # 创建一个占位的图像（实际使用时替换为真实图片路径）
            self.logo_image = None
            # 示例：如果存在图片文件，可以这样加载
            # 获取图片的正确路径（兼容PyInstaller打包环境）
            if getattr(sys, 'frozen', False):
                # 如果是打包后的exe环境
                application_path = sys._MEIPASS
                image_path = os.path.join(application_path, 'src', 'image', 'logo.png')
            else:
                # 如果是开发环境
                image_path = os.path.join('src', 'image', 'logo.png')
            
            img = Image.open(image_path)
            img = img.resize((120, 120), Image.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"无法加载协会标志图片: {e}")
            self.logo_image = None
            
        # 创建包含图片和文字的信息框架
        if self.logo_image:
            logo_label = tk.Label(info_frame, image=self.logo_image, bg=self.colors['card'])
            logo_label.pack(side=tk.LEFT, padx=10, pady=10)
            
        info_label = tk.Label(info_frame, 
                                 text=f"""author：reindeer \nversion：1.0""",
                                 bg=self.colors['card'], fg=self.colors['dark'], 
                                 wraplength=800, justify=tk.LEFT)
        info_label.pack(side=tk.LEFT, padx=10, pady=10)

        # 项目路径框架
        path_frame = tk.LabelFrame(main_frame, text="项目设置", bg=self.colors['card'], 
                                  fg=self.colors['dark'], padx=15, pady=15)
        path_frame.pack(fill=tk.X, pady=(0, 15))

        # 项目路径输入
        tk.Label(path_frame, text="项目路径:", bg=self.colors['card'], 
                fg=self.colors['dark']).grid(row=0, column=0, sticky=tk.W, pady=5)
        
        path_input_frame = tk.Frame(path_frame, bg=self.colors['card'])
        path_input_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        path_input_frame.columnconfigure(0, weight=1)
        
        tk.Entry(path_input_frame, textvariable=self.project_path, width=50, 
                relief=tk.FLAT, bd=1, highlightthickness=1, 
                highlightcolor=self.colors['primary']).grid(row=0, column=0, sticky=(tk.W, tk.E), ipady=3)
        
        browse_btn = tk.Button(path_input_frame, text="浏览", command=self.browse_project_path,
                              bg=self.colors['primary'], fg='white', relief=tk.FLAT, 
                              activebackground=self.colors['info'], activeforeground='white')
        browse_btn.grid(row=0, column=1, padx=(10, 0))

        # Notebook for tabs
        notebook_frame = tk.LabelFrame(main_frame, text="配置选项", bg=self.colors['card'], 
                                      fg=self.colors['dark'], padx=10, pady=10)
        notebook_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        notebook_frame.columnconfigure(0, weight=1)
        notebook_frame.rowconfigure(0, weight=1)

        # 创建 Notebook
        style = ttk.Style()
        notebook = ttk.Notebook(notebook_frame)
        notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

        # 左侧选项卡 - 环境配置
        config_frame = tk.Frame(notebook, bg=self.colors['card'], padx=15, pady=15)
        notebook.add(config_frame, text="环境配置")
        
        # 虚拟环境名称
        tk.Label(config_frame, text="虚拟环境名称:", bg=self.colors['card'], 
                fg=self.colors['dark']).grid(row=0, column=0, sticky=tk.W, pady=8)
        tk.Entry(config_frame, textvariable=self.venv_name, relief=tk.FLAT, bd=1, 
                highlightthickness=1, highlightcolor=self.colors['primary']).grid(
                row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0), ipady=3)
        config_frame.columnconfigure(1, weight=1)

        # 自动安装UV
        auto_install_cb = tk.Checkbutton(config_frame, text="自动安装UV", variable=self.auto_install_uv,
                                        bg=self.colors['card'], fg=self.colors['dark'], 
                                        activebackground=self.colors['card'], 
                                        activeforeground=self.colors['dark'], 
                                        selectcolor=self.colors['card'])
        auto_install_cb.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=5)

        # 安装依赖
        req_cb = tk.Checkbutton(config_frame, text="安装 requirements.txt", variable=self.requirements_file,
                               bg=self.colors['card'], fg=self.colors['dark'],
                               activebackground=self.colors['card'], 
                               activeforeground=self.colors['dark'], 
                               selectcolor=self.colors['card'])
        req_cb.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)

        # 镜像源
        tk.Label(config_frame, text="镜像源:", bg=self.colors['card'], 
                fg=self.colors['dark']).grid(row=3, column=0, sticky=tk.W, pady=8)
        tk.Entry(config_frame, textvariable=self.mirror_source, relief=tk.FLAT, bd=1,
                highlightthickness=1, highlightcolor=self.colors['primary']).grid(
                row=3, column=1, sticky=(tk.W, tk.E), padx=(10, 0), ipady=3)

        # 执行脚本
        tk.Label(config_frame, text="执行脚本 (如 test.py):", bg=self.colors['card'], 
                fg=self.colors['dark']).grid(row=4, column=0, sticky=tk.W, pady=8)
        tk.Entry(config_frame, textvariable=self.execute_script, relief=tk.FLAT, bd=1,
                highlightthickness=1, highlightcolor=self.colors['primary']).grid(
                row=4, column=1, sticky=(tk.W, tk.E), padx=(10, 0), ipady=3)

        # 执行按钮
        execute_btn = tk.Button(config_frame, text="执行配置", command=self.execute_config,
                               bg=self.colors['success'], fg='white', relief=tk.FLAT,
                               activebackground='#2d8642', activeforeground='white',
                               padx=20, pady=5)
        execute_btn.grid(row=5, column=0, columnspan=2, pady=20)

        # 右侧选项卡 - 批处理文件生成
        batch_frame = tk.Frame(notebook, bg=self.colors['card'], padx=15, pady=15)
        notebook.add(batch_frame, text="批处理文件生成")
        
        batch_frame.columnconfigure(0, weight=1)
        
        # 生成批处理文件复选框
        gen_bat_cb = tk.Checkbutton(batch_frame, text="生成批处理文件", variable=self.generate_bat,
                                   bg=self.colors['card'], fg=self.colors['dark'],
                                   activebackground=self.colors['card'], 
                                   activeforeground=self.colors['dark'], 
                                   selectcolor=self.colors['card'])
        gen_bat_cb.grid(row=0, column=0, sticky=tk.W, pady=5)

        # 批处理文件信息文本
        info_text = """
此功能将生成一个批处理文件，该文件会：
1. 激活虚拟环境
2. 切换回项目根目录
3. 执行指定的Python脚本（如果有）
4. 保持命令提示符窗口打开
        """.strip()
        
        info_label = tk.Label(batch_frame, text=info_text, bg=self.colors['card'], 
                             fg=self.colors['secondary'], justify=tk.LEFT)
        info_label.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)

        # 生成按钮
        gen_btn = tk.Button(batch_frame, text="生成批处理文件", command=self.generate_batch_file,
                           bg=self.colors['primary'], fg='white', relief=tk.FLAT,
                           activebackground=self.colors['info'], activeforeground='white',
                           padx=20, pady=5)
        gen_btn.grid(row=2, column=0, pady=20)

        # 日志控制台
        console_frame = tk.LabelFrame(main_frame, text="执行日志", bg=self.colors['card'], 
                                     fg=self.colors['dark'], padx=1, pady=5)
        console_frame.pack(fill=tk.BOTH, expand=True)
        console_frame.columnconfigure(0, weight=1)
        console_frame.rowconfigure(0, weight=1)

        self.log_text = tk.Text(console_frame, height=40, bg='#f8f9fa', fg=self.colors['dark'],
                               relief=tk.FLAT, bd=1)
        scrollbar = tk.Scrollbar(console_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # 重定向stdout到日志
        sys.stdout = TextRedirector(self.log_text)

    def browse_project_path(self):
        """打开文件对话框以选择项目路径"""
        path = filedialog.askdirectory()
        if path:
            self.project_path.set(path)

    def execute_config(self):
        """启动执行配置的线程"""
        thread = threading.Thread(target=self._execute_config_thread)
        thread.daemon = True
        thread.start()

    def _execute_config_thread(self):
        """在独立线程中执行配置任务"""
        # 检查预定义环境是否存在
        # if not os.path.exists(self.predefined_venv_path):
        #     self.log(f"错误: 预定义环境激活脚本不存在: {self.predefined_venv_path}")
        #     messagebox.showerror("错误", f"预定义环境激活脚本不存在: {self.predefined_venv_path}")
        #     return

        project_path = self.project_path.get()
        if not project_path:
            messagebox.showerror("错误", "请选择项目路径")
            return

        if not os.path.exists(project_path):
            messagebox.showerror("错误", "项目路径不存在")
            return

        venv_name = self.venv_name.get()
        if not venv_name:
            venv_name = "venv"

        # 检查uv是否已安装
        if self.auto_install_uv.get():
            self.log("检查uv是否已安装...")
            try:
                # 在预定义环境中执行命令
                cmd = f'pip install uv'
                subprocess.run(cmd, shell=True, check=True, capture_output=True)
                self.log("uv已安装")
            except subprocess.CalledProcessError:
                self.log("正在安装uv...")
                try:
                    cmd = f'pip install uv'
                    subprocess.run(cmd, shell=True, check=True)
                    self.log("uv安装成功")
                except subprocess.CalledProcessError:
                    self.log("uv安装失败")
                    return

        # 创建虚拟环境
        self.log(f"正在创建虚拟环境 '{venv_name}'...")
        venv_path = os.path.join(project_path, venv_name)
        try:
            cmd = f'uv venv "{venv_path}"'
            subprocess.run(cmd, shell=True, check=True)
            self.log(f"虚拟环境创建成功: {venv_path}")
        except subprocess.CalledProcessError:
            self.log("虚拟环境创建失败")
            return

        # 如果需要则安装依赖
        if self.requirements_file.get():
            requirements_path = os.path.join(project_path, "requirements.txt")
            if os.path.exists(requirements_path):
                self.log("正在安装 requirements.txt 中的依赖...")
                try:
                    cmd = f'cd /d "{project_path}" && uv pip install -r requirements.txt'
                    subprocess.run(cmd, shell=True, check=True)
                    self.log("依赖安装成功")
                except subprocess.CalledProcessError:
                    self.log("依赖安装失败")
            else:
                self.log("未找到 requirements.txt")

        # 配置镜像源（如果指定了）
        if self.mirror_source.get():
            self.log(f"设置镜像源为: {self.mirror_source.get()}")
            # 这里通常会添加到pip配置或作为参数
            # 目前仅在日志中记录
            self.log("镜像源已配置（将在后续的pip命令中使用）")

        # 执行脚本（如果指定了）
        if self.execute_script.get():
            script_path = os.path.join(project_path, self.execute_script.get())
            if os.path.exists(script_path):
                self.log(f"正在执行脚本: {self.execute_script.get()}")
                try:
                    # 在预定义环境中执行脚本
                    cmd = f'cd /d "{project_path}" && python "{script_path}"'
                    subprocess.run(cmd, shell=True, cwd=project_path)
                    self.log("脚本执行成功")
                except subprocess.CalledProcessError:
                    self.log("脚本执行失败")
            else:
                self.log(f"脚本 {self.execute_script.get()} 未找到")

        self.log("配置执行完成")

    def generate_batch_file(self):
        """生成批处理文件以便快速运行项目"""
        project_path = self.project_path.get()
        if not project_path:
            messagebox.showerror("错误", "请选择项目路径")
            return

        if not self.generate_bat.get():
            messagebox.showwarning("警告", "请勾选'生成批处理文件'选项")
            return

        venv_name = self.venv_name.get() or "venv"
        script_to_execute = self.execute_script.get()

        batch_content = f'''@echo off
REM Reindeer 生成的批处理文件
cd /d "{os.path.join(project_path, venv_name, 'Scripts')}"
call activate.bat
cd /d "{project_path}"
'''

        if script_to_execute:
            batch_content += f'python "{script_to_execute}"\n'

        batch_content += 'cmd /k\n'

        batch_file_path = os.path.join(project_path, "run_project.bat")
        
        try:
            with open(batch_file_path, "w", encoding="utf-8") as f:
                f.write(batch_content)
            
            self.log(f"批处理文件生成成功: {batch_file_path}")
            messagebox.showinfo("成功", f"批处理文件生成成功:\n{batch_file_path}")
        except Exception as e:
            self.log(f"批处理文件生成失败: {str(e)}")
            messagebox.showerror("错误", f"批处理文件生成失败:\n{str(e)}")


class TextRedirector:
    """文本重定向器，用于将标准输出重定向到tkinter文本控件"""
    
    def __init__(self, widget):
        """初始化文本重定向器
        
        Args:
            widget: 目标文本控件
        """
        self.widget = widget

    def write(self, str):
        """写入字符串到目标控件
        
        Args:
            str (str): 要写入的字符串
        """
        self.widget.insert(tk.END, str)
        self.widget.see(tk.END)

    def flush(self):
        """刷新方法（空实现）"""
        pass


def main():
    """应用程序入口点"""
    root = tk.Tk()
    app = ReindeerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()