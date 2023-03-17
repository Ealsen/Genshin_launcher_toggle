def shssdk(shsmode):
    import os
    import shutil
    import filepath

    last_path = '\Genshin Impact Game\YuanShen_Data\Plugins\PCGameSDK.dll'
    filepath2 = filepath.head_path + last_path
    copypath = filepath2.replace('\PCGameSDK.dll','')

    print('查找并修改SDK文件中...')


    if shsmode == 1:
        if not os.path.exists(filepath2):
            shutil.copy('PCGameSDK.dll', copypath)
            print('SDK文件添加成功，现在为B服客户端')
        elif os.path.exists(filepath2):
            print('已经存在SDK文件，现在为B服客户端')
        else:
            print('未知错误:401！\n请检查程序源码，然后联系开发者\n或者上GitHub')
    
    if shsmode == 2:
        removefile = 'PCGameSDK.dll'
        if os.path.exists(copypath + '\\' + removefile):
            os.remove(copypath + '\\' + removefile)
            print('SDK文件删除成功，现在为官方服客户端')
        elif not os.path.exists(copypath + '\\' + removefile):
            print(removefile + '文件不存在！\n 现在为官服客户端')
        else:
            print('未知错误:401！\n请检查程序源码，然后联系开发者\n或者上GitHub')





if __name__ == '__main__':
    shssdk(1)