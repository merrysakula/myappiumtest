#coding=utf-8
#https://www.cnblogs.com/yoyoketang/p/9037558.html
import yaml,os

#当前脚本路径
basepath = os.path.dirname(__file__)
# basepath = os.path.realpath(__file__)
# basepath = os.path.dirname(os.path.realpath(__file__))
print(basepath)
yamlpath = os.path.join(os.path.dirname(__file__),'element')
print(yamlpath)
def parseyaml():
    pageElement = {}
    #遍历
    for fpath,dirname,fnames in os.walk(yamlpath):
        for name in fnames:
            #yaml绝对路径
            yam_file_path = os.path.join(fpath,name)
            print(yam_file_path)
            #排除非.yaml文件
            if '.yaml' in str(yam_file_path):
                with open(yam_file_path,'r') as f:
                    page = yaml.full_load(f)
                    pageElement.update(page)#有相同的键会直接替换成 update 的值
    return pageElement
if __name__ == '__main__':
    a = parseyaml()
    print(a)