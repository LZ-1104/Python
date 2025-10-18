import cx_Freeze##导入cx_Freeze模块,用于打包,打包后的文件可以在没有安装python的电脑上运行
from cx_Freeze import setup, Executable##导入cx_Freeze模块中的setup和Executable方法,用于打包

setup(
    name="Beating_heart",
    version="1.0",
    description="A simple beating heart animation",
    executables=[Executable("D:\\vscode\\Python\\Test\\Heart.py")]
)