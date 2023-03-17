import writechannel
# import writeSDK
import shutilSDK
'''
原神客户端B官服切换python小程序
可以将B服原神客户端转化为官服客户端，
将官服原神客户端转化为B服客户端
实现原理：
https://www.bilibili.com/video/BV16b411Q7k1/?spm_id_from=333.337.search-card.all.click&vd_source=338e2dd944c2ac6aa2f76cbb27959c74
以上链接中不是程序设计者本人
官服切换成B服
1，右键，打开属性
2，打开文件所在位置
3，找到Genshin Impact Game
4，打开config.ini，把channel中1改为14
5，打开YuanShen_Data，找到Plugins，把PCGameSDK.dll给放进来（先打开客户端）
官服换成B服反之
channel 中14改为1，把PCGameSDK.dll删除
该程序由Ealsen制作
github主页；
https://github.com/Ealsen
'''

def printmenu():
    print('---------------------------------------')
    print('-欢迎来到原神客户端B官服切换python小程序-')
    print('------------注意事项-------------------')
    print('1.请打开游戏客户端在运行此python程序----')
    print('2.使用前注意先到同级目录下的filepath.py-')
    print('指定原神的游戏目录----------------------')
    print('3.如果是官服客户端需要在YuanShen_Data的')
    print('Plugins文件夹下添加PCGameSDK文件-------')
    print('PCGameSDK文件和config文件都随游戏版本更新')
    print('config在游戏目录的Genshin Impact Game文件下')
    print('找更新了最新版B服客户端的朋友要或者上网找')
    print('注意PCGameSDK.dll文件必须备份一份在本小程序目录下')
    print('否则无法切换成功-貌似原神会在启动游戏时删除添加的SDK文件-')
    print('建议启动客户端点击开始游戏时再使用官服转B服功能')
    print('=================功能==================')
    print('-输入数字1即可将B服客户端转化为官服客户端-')
    print('-输入数字2即可将官服客户端转化为B服客户端-')
    print('-输入数字3结束python小程序--------------')
    print('----------该程序由Ealsen制作------------')
    print('---------------------------------------')


def main():
      import time
      whileSwitch = True
      while whileSwitch:
            printmenu()
            key = input('请输入对应的功能数字键：')
            if key == '1':
                 writechannel.wchannel(1)
                 shutilSDK.shssdk(2)
               #   writeSDK.wsdk(1)
                 time.sleep(2)
                 pass
            elif key == '2':
                 writechannel.wchannel(2)
                 shutilSDK.shssdk(1)
               #   writeSDK.wsdk(2)
                 time.sleep(2)
                 pass
            elif key == "3":
                 print('正在退出小程序...')
                 time.sleep(2)
                 break
            else:
                 print('不合法输入，请仔细查看提示内容')
                 time.sleep(3)
                 pass
            

if __name__ == '__main__':
    main()
    