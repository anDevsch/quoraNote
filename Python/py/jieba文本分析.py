import jieba
sentence="我喜欢上海东方明珠"
#全模式
w1=jieba.cut(sentence,cut_all=True)
for item in w1:
    print(item)
print("")
#默认采用精准模式
w2=jieba.cut(sentence,cut_all=False)
for item in w2:
    print(item)
print("")
#搜索引擎模式
w3=jieba.cut_for_search(sentence)
for item in w3:
    print(item)
print("")
#词性标注
import jieba.posseg
w5=jieba.posseg.cut(sentence)
#.flag词性
#.word词语
for item in w5:
    print(item.word+"----"+item.flag)
print("")
'''
a:形容词
c:连词
d:副词
e:叹词
f:方位词
i:成语
m:数词
n:名词
nr:人名
ns:地名
nt:机构团体
nz:其他专有名词
p:介词
r:代词
t:时间
u:助词
v:动词
vn:名动词
w:标点符号
un:未知词语
'''
#词典加载
#盘古词库下载应用
#jieba.load_userdict("绝对路径.txt")
#更改词频
jieba.suggest_freq("上海东方",True)

import jieba.analyse
tag=jieba.analyse.extract_tags(sentence,3)
print(tag)
print("")
#返回词语的位置
w9=jieba.tokenize(sentence,mode="search")
#w9=jieba.tokenize(sentence)
for item in w9:
    print(item)








