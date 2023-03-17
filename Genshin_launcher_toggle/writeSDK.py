def wsdk(wsmod):
    import os
    import filepath

    last_path = '\Genshin Impact Game\YuanShen_Data\Plugins'
    filepath2 = filepath.head_path + last_path
    
    print('查找并修改SDK文件中...')

    if wsmod == 1:
        try:
            os.rename(filepath2 + '/PCGameSDK.dll',filepath2 + '/PCGameSDK.dll0')
            print('修改完成，现在是官服客户端')
        except Exception as e:
            print(f'修改SDk文件名失败，原因是：{e}')
            print('请检查文件是否存在或者已经完成改名')

    if wsmod == 2:
        try:
            os.rename(filepath2 + '/PCGameSDK.dll0',filepath2 + '/PCGameSDK.dll')
            print('修改完成，现在是B服客户端')
        except Exception as e:
            print(f'修改SDk文件名失败，原因是：{e}')
            print('请检查文件是否存在或者已经完成改名')

if __name__ == '__main__':
    wsdk(1)