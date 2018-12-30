

# 导入包
from sklearn.feature_extraction.text import CountVectorizer

# 实例化CountVectorizer

vector = CountVectorizer()

# 调用fit_transform输入并转换数据

res = vector.fit_transform(['life is is short,i like python','life is too long , i dislike python'])

data = '今天好冷，我学习了机器学习的特征工程和文本特征提取'



# 打印结果
print(vector.get_feature_names())

print(res.toarray())