# -*- coding: utf-8 -*-

class BMESBIO2Data:
    """[将bio和bmes格式数据转换为格式化数据
    也可以处理为对应的标注格式]
    """

    def __init__(self, markType="BMES"):
        """实例化时可以选择对应的文本格式，这里支持BMES和BIO


        >>> BMESBIO2Data("BIO")
        >>>

        """
        self.markType = markType

        pass

    def toData(self, file):
        """[将标记数据转换为格式化数据]

        Args:
            file ([type]): [对应格式的文本文件]
        """
        pre_tag = ''
        words = []
        items = []
        text = []
        item = {"type": '', "word": []}
        for line in open(file):
            if line == "\n":
                print(text)
                print(items)
                items = []
                text = []
            l = line.split(" ")
            if len(l) == 2:
                word = l[0]
                tag = l[1].replace("\n", '')

                text.append(word)
                # print (word,"ee",tag)
                if self.markType == "BIO":

                    if tag.startswith("B-"):
                        item = {"type": '', "word": []}
                        item["word"].append(word)
                        item["type"] = tag.replace("B-", '')
                        # print(item)
                    elif len(item["word"]) > 0 and tag.startswith("I-"):
                        item["word"].append(word)
                    else:
                        # print("dd")
                        if len(item["word"]) > 0:
                            items.append(item)

                    pre_tag = tag
                elif self.markType == "BMES":
                    if tag.startswith("B-"):
                        # 处理开头
                        item = {"type": '', "word": []}
                        item["word"].append(word)
                        item["type"] = tag.replace("B-", '')
                        # print(item)
                    elif len(item["word"]) > 0 and tag.startswith("M-"):
                        # 处理中间
                        item["word"].append(word)
                    elif len(item["word"]) > 0 and tag.startswith("E-"):
                        # 处理结尾
                        item["word"].append(word)
                        item = {"type": '', "word": []}
                    elif tag.startswith("S-"):
                        # 处理单个
                        item = {"type": '', "word": []}
                        item["word"].append(word)
                        item["type"] = tag.replace("S-", '')
                        items.append(item)
                        item = {"type": '', "word": []}
                    else:
                        # print("dd")
                        if len(item["word"]) > 0 and pre_tag.startswith("E-"):
                            items.append(item)

                    pre_tag = tag
            print(items)

    def fun(self):
        """[summary]
        """
        pass
