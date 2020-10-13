#-*- coding:utf-8 -*-
import sys
import os
import pathlib
import json
import base64
import subprocess
import shutil
import io
from uiutil.globaltool import *

'''
   环境变量
'''
class CFEnv(object):
    '''
        初始化配置及环境变量
    '''
    def initEnvData():
        #初始化配置对象
        CFEnv.configObj = {}
        #初始化基础目录结构
        CFEnv.rootDir = pathlib.Path(os.getcwd()).parent
        CFEnv.binDir = os.path.join(CFEnv.rootDir,'bin')
        CFEnv.dataDir = os.path.join(CFEnv.rootDir,'data')
        CFEnv.pluginDir = os.path.join(CFEnv.dataDir,'plugins')
        CFEnv.scriptDir = os.path.join(CFEnv.dataDir,'scripts')
        try:
            os.makedirs(CFEnv.binDir)
        except Exception as ex1:
            pass
        try:
            os.makedirs(CFEnv.dataDir)
        except Exception as ex1:
            pass
        try:
            os.makedirs(CFEnv.pluginDir)
        except Exception as ex1:
            pass
        try:
            os.makedirs(CFEnv.scriptDir)
        except Exception as ex1:
            pass
        
        #初始化配置文件路径
        CFEnv.configFilePath = os.path.join(CFEnv.rootDir,'config.json')
        CFEnv.backupConfigFilePath = os.path.join(CFEnv.rootDir,'config.json.backup')
        #CFEnv.templeteScriptFile = os.path.join(CFEnv.rootDir,'templete.js')

        #载入配置
        CFEnv.loadConfig()

        #取环境变量名称
        #CFEnv.switchScriptEnv()

    '''
        载入配置文件
    '''
    def loadConfig():
        #载入配置
        if pathlib.Path(CFEnv.configFilePath).exists():
            #读入数据
            try:
                jsonStr = IOTool.readAllText(CFEnv.configFilePath)
                CFEnv.configObj = json.loads(jsonStr)
            except Exception as exx:
                CFEnv.initConfig()
        else:
            CFEnv.initConfig()

    '''
        初始化配置文件,如果存在备份则使用，否则输出一个新的
    '''
    def initConfig():
        if pathlib.Path(CFEnv.backupConfigFilePath).exists():
            shutil.copyfile(CFEnv.backupConfigFilePath, CFEnv.configFilePath)
        else:
            CFEnv.writeNewConfig()
    
    '''
        保存配置
    '''
    def saveConfig():
        IOTool.writeAllText(CFEnv.configFilePath, json.dumps(CFEnv.configObj, indent=4))

    '''
        输出标准配置文件
    '''
    def writeNewConfig():
        #初始化的例子
        CFEnv.configObj['downloadDir'] = '~/PDownloaderDir'
        #保存配置
        CFEnv.saveConfig()
