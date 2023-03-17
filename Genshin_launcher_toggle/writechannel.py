def wchannel(wfmod):
    import filepath

    last_path = '\Genshin Impact Game\config.ini'
    filepath1 = filepath.head_path + last_path

    if wfmod == 1:
        print('官服客户端配置文件写入中...')
        with open(filepath1, "r") as f:
            content1 = f.read()
            content1 = content1.replace("14", "1")

        with open(filepath1, "w") as f:
            f.write(content1)
            print("写入完毕！")
            print(f'打印写入完成后的配置文件：\n\n{content1}\n\n')
            print('切换为官服客户端配置文件完成！')

    elif wfmod == 2:
        print('B服客户端配置文件写入中...')
        with open(filepath1, "r") as f:
            content1 = f.read()
            if '14' not in content1:
                content1 = content1.replace("1", "14")
            elif '14' in content1:
                print('客户端配置文件已修改为B服客户端配置文件！\n请不要重复修改！\n')

        with open(filepath1, "w") as f:
            f.write(content1)
            print("写入完毕！")
            print(f'打印写入完成后的配置文件：\n\n{content1}\n')
            print('切换为B服客户端配置文件完成！')



if __name__ == '__main__':
    wchannel(2)