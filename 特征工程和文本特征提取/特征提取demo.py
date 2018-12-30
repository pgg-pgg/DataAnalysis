from sklearn.feature_extraction import DictVectorizer


def dictvec():
    """
    字典数据抽取
    :return: None
    """
    # 实例化DictVectorizer
    dict = DictVectorizer(sparse=False)
    data = dict.fit_transform([{'city': '北京', 'temperature': 100},
                               {'city': '上海', 'temperature': 60},
                               {'city': '深圳', 'temperature': 30}])
    print(dict.get_feature_names())

    print(data)

    return None


if __name__ == '__main__':
    dictvec()
