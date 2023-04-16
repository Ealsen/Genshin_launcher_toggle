# Genshin_launcher_toggle
## 原神客户端B官服切换python小程序

用Python实现PC端原神客户端的B服客户端与官服客户端的相互切换

### 使用说明
1. 打开Genshin_launcher_toggle文件夹,在此文件夹下用记事本打开filepath.py修改里面的head_path变量的值为你当前的原神游戏目录
2. 打开Genshin_launcher_toggle文件夹,在此文件夹下用cmd命令运行
mainrun.py即可打开该python程序
```cmd
python mainrun.py
```
3. 该程序基于python3开发,请确认您是否安装了此环境
4. 测试的原神版本为3.5.0,如果为其他版本则需更换config.ini和PCGameSDK.dll文件,详情看注意事项

### 注意事项
1. 请打开游戏客户端在运行此python程序  
2. 使用前注意先到同级目录下的filepath.py中指定原神的游戏目录  
3. 如果是官服客户端需要在YuanShen_Data的Plugins文件夹下添加PCGameSDK文件     
4. PCGameSDK.dll文件和config.ini文件都随游戏版本更新
5. config.ini在游戏目录的Genshin Impact Game文件下
找更新了最新版B服客户端的朋友要或者上网找    
6. 注意PCGameSDK.dll文件必须备份一份在本小程序目录下    
否则无法切换成功(貌似原神会在启动游戏时删除添加的SDK文件)    
7. 建议启动客户端点击开始游戏后再使用官服转B服功能
  
### 功能
+ 输入数字1即可将B服客户端转化为官服客户端 
+ 输入数字2即可将官服客户端转化为B服客户端 
+ 输入数字3结束python小程序 

### 该程序由Ealsen制作
+ 免责声明:
  您使用了该程序或者相关代码所造成的损失均与程序设计者无关。
  本人承诺该程序无任何有害代码,有疑虑请移步。
  
#### 2023年4月16日
+ 在原神3.6版本中，此程序已经不能使用
+ 要想使用请更新程序种中的PCGameSDK.dll文件
+ 暂停对此程序的维护更新
