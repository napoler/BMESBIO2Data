# -*- coding: utf-8 -*-
"""[用于将类打包发布时候的配置信息]
    """
import time
from os import path as os_path

from setuptools import find_packages, setup

this_directory = os_path.abspath(os_path.dirname(__file__))

# 读取文件内容


def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

# 获取依赖


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]
# long_description="""

# 这里是说明
# 一个创建库的demo
# http://www.terrychan.org/python_libs_demo/
# """


long_description = read_file("README.md")
setup(
    name='BMESBIO2Data',  # 修改包名字
    version='0.0.0.3',
    description='Terry toolkit BMESBIO2Data',
    author='Terry Chan',
    author_email='napoler2008@gmail.com',
    url='https://www.terrychan.org/BMESBIO2Data/',
    install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
    long_description="""
    
    BMESBIO2Data
    一个用于将命名实体任务中输出的BIO、BMES数据转换为格式化数据的包。
    
    [项目地址](https://github.com/napoler/BMESBIO2Data)
    [查看文档](http://www.terrychan.org/BMESBIO2Data/)
    
    
    
    """,
    long_description_content_type="text/markdown",
    # install_requires=[
    #     # 'beautifulsoup4==4.7.1',


    # ],
    packages=['BMESBIO2Data'])

"""
pip freeze > requirements.txt

python3 setup.py sdist
#python3 setup.py install
python3 setup.py sdist upload
"""
