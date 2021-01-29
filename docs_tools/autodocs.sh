#! /usr/bin/bash

# 自动构建脚本
# 文档 http://www.pythondoc.com/sphinx/tutorial.html


#安装
pip install -U Sphinx
#安装主题
#pip install sphinx_rtd_theme
#https://sphinx-book-theme.readthedocs.io/en/latest/index.html
pip install sphinx-book-theme


# https://github.com/lotharschulz/sphinx-pages
pip install sphinx-autobuild 
#markdown基础支持
#recommonmark的PyPi说明：https://pypi.org/project/sphinx-markdown-tables/
pip install recommonmark

#
#清理之前生成的文档
rm -rf ./source/res/
#扫描目录
sphinx-apidoc -o ./source/res ../src

#编译成为html
#make html
#sphinx-autobuild ./source ../docs --open-browser

#HTML 页面保存在 ../docs 目录。
sphinx-build -b html ./source ../docs 

cp ./.nojekyll ../docs

# 推送命令
cd ../
git add .
git commit -m "auto更新文档"
git pull
git push
