# 数据科学入门 *Data Science from Scratch*

第一章是大致简介了一下相关的工作内容，第二章是需要的python入门知识，第三章也就是我创建这个项目的这一章是数据可视化，介绍了一些数据可视化的内容。

## 数据可视化 *data-visualization*

简而言之就是基本见识一下matplotlib包，包括：

* 线图
* 条形图
* 散点图

更深入的，没涉及。

## 线性代数 *linear algebra*

## 梯度下降分析法 *gradient descent*
梯度下降分析法。简而言之就是顺着偏导数（导数）方向上，单步增加或减少以达到最优解的技术。 这次写了一个例子，算是搞明白了一点点，但不理解的是为什么要用步长与在
该点的导数值获取到用于更新参数的步长数组，不知道是梯度下降分析法就该这么乘得步长数组，还是仅仅适用于平方和函数。但确实得到了近似最优解。

## k最近邻法 *k-nearest neighbors*
不难看出思想很简单，但“距离”这个概念不适合相对较高的维度，如果要在高维度使用最近邻法，势必要在一个合适的平面做降维，这可能带来额外的问题...  
题外话是，想起一个笑话：如果你打算用正则解决一个问题，那么你就拥有了两个问题...  
当成本过高时，选择换一个方案似乎是更好的选择。

## 简单线性回归 *simple linear regression*
其实和上一章中间隔了一个朴素贝叶斯，但有朋友推荐我先看简单线性回归，因为这个朋友很专业，所以我听她的。  
这里用到了最小二乘法，但我并没有系统学习过相关的内容，所以去找了一下，[最小二乘法的本质](https://www.zhihu.com/question/37031188)，这个回答下的高赞用比较直观的方式讲了一下，
但感觉离学会还有点距离。  
练习了两天最小二乘法，对线性回归的最小二乘法有了点了解，做点简单的题目是没问题了。  
本章举的例子是线性回归，使用最小二乘法和梯度下降法都进行了计算，结果是一致的。那么就有一个问题：最小二乘法和梯度下降法的适用场景是什么？  
不难看出计算量上面显然的是最小二乘法相对更小，甚至可以说一次计算即可，但梯度下降法计算量极大。但随着维度的增加，最小二乘法的计算也趋向复杂、繁琐，而梯度下降法却没什么变化。  
所以简单分析一下的话，如上就是原因？

我理解的是，这里的目标函数是凸函数，且很容易求出对于每个变量的偏导的表达式，并且求解出让所有偏导为0的解析解。但对于很多更复杂的问题做不到这一点。比如说对于神经网络，可能动则几百几千个变量，而且loss function很难用具体的公式直接表达出来，所以只能用梯度下降等方法近似求数值解。

## 所有之外的话
如同我大学一战考研失败后想通的一点：既然想转计算机，为什么不直接考计算机的研究生呢？现在我也感受到差不多的想法了。烦心事似乎一直没有离我而去，真希望我能睡一个好觉。  
项目最终还是加起班来了，说好说坏？好歹我写上代码了，已经一个月工作没写代码了...  
最近除了加班还是加班，疫情、工作烦心，力扣也没咋刷了，数据科学也没咋学，真是慌慌张张，匆匆忙忙，好像有很多琐碎的事横亘在想法中央。
要说今天想干嘛？我今天不想学习
加班，不想学习  
勉强写完了统计假设检验的一个例子，说实话没咋看明白，后面看看原版是怎么写的吧。最近都是加班加班加班，严重怀疑那些996的是真的假的，这么煎熬
的生活感觉就算是给钱也熬不下来。
烦躁，虽然工作不顺，但这次是我自己的错，很难受。今天排查了一些业务逻辑的bug，又转过去接手了一个烂摊子，一个东拼西凑，最后勉强凑出来的烂摊子...烦心  
今天可能要加一个过12点的班 <- 实际上加班到11点42，莫名其妙感觉自己赚了  
纸上练习最小二乘法，感觉好累，好久没做过这些演算了...  
最近两天吃完晚饭都巨困，困意袭来翻江倒海那种，完全扛不住，只能暂时睡一会儿再起来洗澡，不知道是不是白天文档写多了太耗脑细胞了。今天回顾看了一下之前的多元分析，不知道
是因为太累还是怎么，看不下去，完全看不下去，硬看也看不懂，那就歇着吧。  
去看了线程装饰器相关的内容，打算写一篇博客，当然这是明天的事儿了，当然是Java的线程装饰器...  
今天朋友从苏州过来找我，没看什么东西  
有些许烦躁  
租房....  
在忙搬家的事
去买自行车，然后骑了回来，顶着一点的太阳骑回家，右手护腕处、左手手环处都被晒出了白圈，太阳太毒了。不过有趣的是第一次坐轮渡，感觉还挺好玩的，轮渡似乎有二楼，等我哪天脑子抽了特地坐轮渡时去二楼看看，风景应该还挺不错的。回来后发现没有车锁，下单了车锁，原本还在纠结不想去拿，突然想到可以叫代取，那一瞬间，幸福也不过如此了。感觉今天太缺水了，现在还有点渴，可惜没买水...没有水喝的我现在就要s  
很累，挑了一些日用品和几件衣服，累死我了，感觉现在一闭眼就会不省人事  
南京有四个密接，非常担心行李还能不能寄过来。上海的鬼天气，一直预报有雨，一直都只是刮风，吓唬我不敢骑车上班...  
东西差不多快寄到了，还买了个桌子，希望是正常可以用的，不然又会费事。买的衣服完全不能穿，迪卡侬也越来越拉了，又费劲巴拉地挑了一个多小时，挑的累死了，话说这都快成日记了，我 哪天是不是要把这东西转成private...  
回来继续看了多元回归的相关东西，果不其然已经看不明白了。明天再从头开始吧