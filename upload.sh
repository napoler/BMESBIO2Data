#!/bin/bash
#这里是一个自动执行上传的命令

# 安装依赖查找库
pip install pipreqs
#遇到已经存在 强制覆盖 requirements.txt
pipreqs ./ --force


#打包
python3 setup.py sdist
#python3 setup.py install
#上传
python3 setup.py sdist upload
