这是自用的一个基于Python+PYQT的界面应该程序的模板，为方便于日后开发类似程序方便，所以特此整理，以后会不断的迭代的，有需要的可以拿去！开发环境为 VSCode+Python+PYQT Integration
proot.py 这个是Python程序的启动文件，一般不用修改,负责初始化目录结构和载入配置文件以及调用programs.py中的Program.main启动程序
programs.py 主要负责进行程序的初始化工作(创建QApplication对象，显示主窗体等)
uiDefines 窗体描述文件和描述类
uiEvents 窗体的基类和MainWindow的实现类
uiUtil一些常用函数,其中的cfenv是环境变量,负责初始化配置文件和目录结构
目录结构如下： 
bin (用于存放主程序) 
data (用于存放数据)
plugins (用于存放插件数据) 
scripts (用于存放脚本数据) 
config.json (用于存放配置数据) 
config.json.backup (用于存放配置数据的备份，当config.json解析失败时恢复用！)
