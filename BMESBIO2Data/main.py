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
    def autoLang(self,word):
        """[自动检查文本语言，如果为英文则添加空格 unk 前后加入空格] 

        Args:
            word ([type]): [description]

        Returns:
            [type]: [description]
        """
        if (u'\u0041'<= word <= u'\u005a') or (u'\u0061'<= word <= u'\u007a'):
            return word+" "
        elif word=="[UNK]":
            return " "+word+" "
        else:
            return word
                        
    def toData(self, markList=[]):
        """[将标记数据转换为格式化数据]
        返回数据为标记数据
        返回数据集如下 (['【', '不', '良', '反', '应', '】', '⑴', '可', '见', '胃', '肠', '道', '不', '良', '反', '应', '，', '如', '恶', '心', '、', '呕', '吐', '、', '上', '腹', '疼', '痛', '、', '便', '秘', '。'], [{'type': '不良反应', 'word': ['恶', '心'], 'start': 18, 'end': 19}, {'type': '不良反应', 'word': ['呕', '吐'], 'start': 21, 'end': 22}, {'type': '不良反应', 'word': ['上', '腹', '疼', '痛'], 'start': 24, 'end': 27}, {'type': '不良反应', 'word': ['便', '秘'], 'start': 29, 'end': 30}])

        Args:
            markList (list, optional): [标记数据列表如“['常 O']”]. Defaults to [].
        """

        pre_tag = ''
        words = []
        items = []
        text = []
        item = {"type": '', "word": [], 'start': None, 'end': None}
        # for i, line in enumerate(open(file)):
        for i, line in enumerate(markList):
            # print(line)
            if i >= 1000:
                print("items", items[:10])
                break

            if line == "\n":
                # print(text)
                # print(items)
                items = []
                text = []
                continue

            l = line.split(" ")

            # 处理合乎规则的数据
            if len(l) == 2:
                # 自动对英文添加空格处理
                word = self.autoLang(l[0])
                
                words.append(word)
                tag = l[1].replace("\n", '')
                text.append(word)
                # print(word, "//", tag)
                if self.markType == "BIO":

                    if tag.startswith("B-"):
                        item = {"type": '', "word": [],
                                'start': None, 'end': None}
                        item["word"].append(word)
                        item["start"] = i
                        item["end"] = i
                        item["type"] = tag.replace("B-", '')
                        # print(item)
                    elif len(item["word"]) > 0 and tag.startswith("I-"):
                        # 判断是否与前面标记数据一样类型，否则删除上面标记
                        if item.get("type") == tag.replace("I-", ''):
                            item["word"].append(word)
                            item["end"] = i
                        else:
                            item = {"type": '', "word": [],
                                    'start': None, 'end': None}

                    else:
                        # print("dd")
                        if len(item["word"]) > 0:
                            items.append(item)
                    pre_tag = tag
                elif self.markType == "BMES":
                    # 处理BMES格式数据
                    # print("")
                    if tag.startswith("B-"):
                        # 处理开头
                        item = {"type": '', "word": [],
                                'start': None, 'end': None}
                        item["word"].append(word)
                        item["start"] = i
                        item["type"] = tag.replace("B-", '')

                    elif len(item["word"]) > 0 and tag.startswith("M-"):
                        # 处理中间

                        # 判断是否与前面标记内容类型一样，否则进行重置
                        if item.get("type") == tag.replace("M-", ''):
                            item["word"].append(word)
                        else:
                            item = {"type": '', "word": [],
                                    'start': None, 'end': None}
                    elif len(item["word"]) > 0 and tag.startswith("E-"):
                        # 处理结尾
                        # 判断是否与前面标记内容类型一样，否则进行重置
                        if item.get("type") == tag.replace("E-", ''):
                            item["word"].append(word)
                            item["end"] = i
                            items.append(item)
                        else:
                            pass
                        item = {"type": '', "word": [],
                                'start': None, 'end': None}
                    elif tag.startswith("S-"):
                        # 处理单个
                        item = {"type": '', "word": [],
                                'start': None, 'end': None}
                        item["word"].append(word)
                        item["type"] = tag.replace("S-", '')
                        item["start"] = i
                        item["end"] = i
                        items.append(item)
                        item = {"type": '', "word": [],
                                'start': None, 'end': None}
                    else:
                        # print("dd")
                        if len(item["word"]) > 0 and pre_tag.startswith("E-"):
                            items.append(item)

                    pre_tag = tag

        # print("items", items[:10])
        return words, items

    def file2Data(self, file):
        """[从文件获取格式化后数据]

        Args:
            file ([type]): [description]
        """

        items = []
        item = []
        for i, line in enumerate(open(file)):
            if len(line.split(" ")) == 2:
                item.append(line)
                pass
            elif len(item) > 0:
                items.append(item)
                item = []
                pass

        # print(items[:10])
        for i, line in enumerate(items):
            # print(line)
            # print(self.toData(line))
            yield self.toData(line)

    def data2BMES(self, words, mark):
        """[将格式化的数据转换为BMES格式]

        Args: [[self.toData输出words, mark]]. Defaults to [].
        """
        # print(words, mark)
        for m in mark:
            # mWords=m.get("word")
            words[m.get("start")] = "[@"+words[m.get("start")]
            words[m.get("end")] = ""+words[m.get("end")]+"#"+m.get("type")+"*]"
        # print(words)

        for i, w in enumerate(words):
            words[i] = words[i].replace("##", "")
        # 此处存在问题，两个英文单词该如何处理
        return words
