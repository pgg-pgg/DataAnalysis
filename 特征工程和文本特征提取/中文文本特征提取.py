# 导入包
from sklearn.feature_extraction.text import CountVectorizer
import jieba

def textVec():
    # 实例化CountVectorizer

    vector = CountVectorizer()

    # 调用fit_transform输入并转换数据

    res = vector.fit_transform(['life is is short,i like python', 'life is too long , i dislike python'])

    data1= '今天好冷，我学习了机器学习的特征工程和文本特征提取'

    # 打印结果
    print(vector.get_feature_names())

    print(res.toarray())


def jiebafenci():
    jieba.cut("最近有很多人问我，大数据是怎么学?需要学什么技术以及这些技术的学习顺序是什么?")
    jieba.cut("本例实现一个带括号的GUI计算器，采用鼠标点击按钮输入.")
    jieba.cut("今天好冷，我学习了机器学习的特征工程和文本特征提取")


if __name__ == '__main__':
    textVec()