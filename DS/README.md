### Data Sciecne Challenge
1. 明确产品的目标
2. 定义metrics
3. 数据清理
4. 提取跟产品目标相关的变量
5. 如何鉴别重要的变量
6. 产品改进推荐：发现问题要对应给出可以做的后续策略，通过后续变量的结果来看是不是策略成功
Business Sense (business questions): fraud高发期，例如

(1) transaction时间是holiday

(2) 大数额transaction比小的更重要

(3) 整数额transaction用于买gift card

(4) time是深夜

(5) ratio of balance/limit 来看是不是用的比例过高

(6) metrics的确定，比如关注对那些大数额fraud是不是能找出来，而不是把不同数额的fraud同等对待，考虑分析fraud的成本，因为要花analyst的时间


7. 实验设计


## C1 cases

> C1 cases 

Business Cases:

case 1:  add a mobile feature: check deposit因为在chase app上用过这个功能还蛮了解，这一轮聊的蛮好，上来先问revenue跟cost有哪些，然后就是2轮计算，最后问你还有什么要考虑的么？注意面试的时候要细心，特别是有的计算会用到上一题的条件，不要漏数据；

Case2: small business loan, 计算不难，最后一个讨论感觉答得不算特别好，问你有三个产品，A跟C 是C1 partner with others, B是C1独自推出的，A每年固定revenue 1M(数字记不清了）， B第一年loss 6M, 往后每年4M revenue, C第一年loss 10M, 往后每年6M revenue, 选哪个产品
Data Challenge: 面试官会要看code, 对data quality部分比较感兴趣，有夸我这部分做的好，会根据你做的东西随机follow up

case：credit card churn model to predict whether user will close the account and will increase cash back reward for those who may close. A total of 4 million rows of data including date, purchase amount, type of store...
1. Q: How would learn about the data(好像是）?
  (瞎说的) Exploratory Analysis?...
2. Q: How would you handle missing data?
Either Delete(row wise/ column wise and assumptions) or Impute(categorical: mode, as a level, logistic ; Continuous: mean, median, linear,0... )
3. feature engineering
4. (big data) what would you do if the data is updated hourly
后来问了面试官 好像意思要注意computation complexity
5. What if we have several years of data?
Hadoop MapReduce
6. What if only one computer or a single node is given
上个回复补充说了 但是不确定
7. What model would you use?
GBDT, RF, but also try other methods like LR
8. what language/lib will you use if data is like 1G
python/sklearn (稍微提了下 特别大会用spark 不知道对不对）
9. How to evaluate
AUC ROC
10. 如果模型结果不太好对business会有什么影响
11. 然后就是的5000 credit limit， 使用率相差很大的问题， 100% 和2%


面试官是一个在C1做了一年多的fraud方向的DS，之前背景偏business。

首先上来介绍了一下自己的background，问了一下我的background，做过的project等。

然后开始主要的Case Study。背景是每个月都有一部分人关信用卡，因为default所以被关卡的和主动关卡的，这里分析主要是主动关卡的。有两个table，一个是transaction table，包括transaction_id, time, store, cash back等。一个是card table, 包括customer_id, open_date, closed_date, card_it, credit_limit, accumulative_cash_back等。. 1point3acres

问：现在想推出一个promotion target那些近期可能要关卡的用户，问怎么找出那些用户？应该采取什么措施？
答：首先用classification model来predict出近期会关卡的用户，然后找出那些user有什么characters，相对应的分析原因，然后推出promotion，blah blah。。。. From 1point 3acres bbs

问：现在发现有一些missing value，问怎么处理？
答：根据missing value的数量和原因，要么drop要么infer。。
(这里给大家推荐一篇blog：https://towardsdatascience.com/h ... g-data-8646b18db0d4
当然我当时没答这么细，但大概意思是这样。。。)

问：根据我们有的数据，你会用哪些variable做feature？
答：从customer持卡的cost和benefit的角度出发，分析了一些variable，比如说activated的offer数量，近期要交的annual fee等等。。。

问：怎么分析model的优劣？
答：不能简单用accuracy，要结合misclassify customer的cost来取一个maximize我们profit的recall，specificity等。。。

问：找出来那些customer之后，你怎么做promotion？. From 1point 3acres bbs
答：先用clustering把customer segment一下， 然后再根据不同的客户采取相应的promotion。。。

----------------------------case study结束----------------------------------------
. 1point3acres
问：我们有好几年（重点）的transaction data，怎么找出所有unique customer？
答：data set如果还行不是特别大的话，可以上ec2开一个大instance。。如果实在是特别大的话，就用emr，mapReduce或者sparkSQL解决问题。。

问：mapReduce的话，map function和reduce function的pysdo code收一下？
答：先每个partition上去unique，再reduce到master node上去unique。。。

一面，business case, 面试官在总部，干了十几年，居然给我讲他中间也想过要跳槽，可是后来都没有。。。。不知道为啥要和我讲这个。开始15分钟behavor, 问最近犯的错，之后是case, 一个巴西超市要发credit card, 首先问credit card可能的revenue/cost来源， 之后问要break even的话， market share是多少，面试官不会给你全部数据， 你需要自己定义market share是什么， 有可能是营业额， 有可能是多少张卡， 不同的定义需要的数据不同， 我说我选# of cards，然后我说我需要全巴西有多少张卡，巴西有多少成年人， 成年人中有多少人是credit worthy, 之后他就给了我， 然后就很快算出来，之后又有很多follow up，只记得一个是怎么提高revenue云云， 反正第一面面试的很愉快。

之后第二面就是在那里break一小时。

第三面是另一个面试官，也是远程，问了一个游乐园的问题，首先分析游乐园的收益与成本来源， 之后给你一张纸，上面是有点像income balance sheet， 一个一个计算各种各样的item， 然后面试官各种update信息，给新的senario,然后你就要重新update balance sheet上的所有计算， 真阳大概来回了三四个senario, update 三四次所有的计算， 之后根据计算问很多folllow up，我计算的时候大概犯了一两个小错误， 面试官都提醒然后我很快改正。感觉capital one对于计算的要求很高，你需要脑子时刻保持清醒，最好不要犯太多错，你保持任何答案之前一定要想一想这是不是对的，不要想都不想就说。
第四面是role play， 说烂了，因为我平时给很多给不懂tech的人做类似的presentation所以很轻松的通过啦，我补充一下其他人没说过的， role play 主要是要记住时刻为客户着想，present的时候不要一直想着自己说，多问问他有什么问题，听懂了没有， 这样可以显示你为客户着想的一面，我觉得这个挺重要的。

最后一面 是tech， 问了一些基本公式的推到， 一些statistical tests，还有distribution的问题， 包括应用，还有一些ML模型的原理

我是面的SDE track，败在了case study，出了一个没见过的case，大致是给你一份信用卡账单，让你看有什么猫腻，答案是因为其他transaction都在VA，只有一笔是在三番，所以三番的可能是fraud，然后顺着这个思路，告诉你他们会接拿到其他公司的关于每一笔消费的明细来帮助确认是否真的是fraud，但是有成本，也不一定有帮助。现在有两个公司可以提供明细，他们的cost和准确率不一样，让你算一下用哪个公司比较划算，总之全程和编程无关，祝你好运

Case
可能是因为没睡饱，加上上一轮面试过于亢奋，这轮 Case 我处于一个全程精神涣散的状态。。。有时候甚至面试官在说什么我都没有听。。。
Personalized Credit Card 的 Case， 之前地里有面经。
C1想要增加一个服务，客户可以自行上传照片给自己的 profile，这样他们的卡上就会有这张照片（我十分怀疑面试官没说划线这句话，也可能是我漏听了。。。）
问， C1为什么要这么做？
注意划线那句话很重要，由于我没听到，导致我一直以为只是给客户的电子档案上传照片，答的就很不在点子上。。。
后来面试官大概是听不下去了，就把答案说了一下。。。
1、Fraud Detection 信用卡上的签名其实很不保险，但如果客户卡上有自己的头像的话，刷卡时候就更安全，因为对比一下真人和照片就可以立刻确定是不是盗刷。
2、卡上有Personalized 的标志会让客户更愿意掏卡/秀卡 消费。。。
Well...我个人觉得这就是强行找原因...因为我问面试官照片必须是头像吗还是什么照片都行，面试官说什么照片都行。那这两个原因就...自相矛盾嘛，加起来才是一个全集。【反正我是不会往卡上加自己头像的。。。
接下来就是算算算了。
先是一道 A 包含一部分 B，B 和 C 又有重合，问 A 和 C 重合有多少的那种题（真的记不起来了。。。）
精神涣散如我，听到题直接懵逼。后来心想，这么简单的烂题答不出来你肯定就凉了，心一横，开始在面试官面前画集合图。。。然后答对了= =
接下来开始做投放实验
41K的 Control group 和 Treatment Group，给 Treatment Group 里的人发 email 通知新功能，5%的人会 response。
Treatment Group 里 response 的人月消费600，没 response 的人月消费195
Control Group 里的人月消费200。
问，投放 email 前后，人均消费变化是多少。
很简单，就算下 Treatment Group Weighted average 再减去200 就行了。

接下来面试官问，那些没有 response 的人，在投放 email 之前的月消费是多少？
精神涣散的我再次懵逼，直接答了200，面试官大概是觉得我没救了，走去白板那里开始给我讲解。。。
5% *（average consumption before）+ 95% * x = 200, 195-x是答案。。。average consumption before 那个数我不记得了。。。Anyway 这个题我到现在也没太明白

最后投放2 million email，response rate依然是5%
Cost:
$0.02/email
$1/mail （意思是如果客户选择上传照片，新卡寄过来的费用）
求 profit。


Case
这个也是地里的面经。你是一个公司的 manager，手下有三个人，分别负责 coding, testing, documentation。
现在每2周固定产出1K lines code.
有一天，一个潜在客户希望你们每2周给他们产出1K lines code，这样你们的产出量就会变成2K，问你可不可行，或者说你要考虑什么？
答：我要知道每个人每2周最大产出量是多少，每个人的工资是多少，然后算下 profit。如果产出量达不到要求需要加班的话，我还得知道加班费，以及员工愿不愿意加班。
面试官就给了数据。
Producing Capability:
Coding: 15 lines/h,
Testing: 2 lines/5 mins
documentation: 1 line/2 mins

Salary:
Working hours: $16/h
Overtime: $24/h

先算了下两周正常工作时间每个人的产出量，
Coding 1.2K
Testing 1.92K
Documentation 2.4K

我说最大产出量1.2K，正常工作时长满足不了客户要求。需要加班
问：加多久
答：Coding 53.333 h, Testing 3.333h。
问：你觉得怎么样？
回：这样 coding 的人平均一天加班4-5小时，这太多了。。。他/她肯定不会答应的
问：那你觉得要怎么办
回：Testing, Documentation的人肯定也都懂 code，让他们帮着写。。。
问：不行，假装他们不会
回：那我再雇一个写 code 的
问：但这个客户不一定签我们，人雇好了，客户没了怎么办？再说还要培训，成本很高【？？？】
见我懵逼，面试官说我们不招 fulltime，招个 contractor【。。。】
contractor 每小时工资$24，
然后算了下招人前后每生产1 line的 cost （也就是工资）是多少，前面3点几，后面2点几
问：为啥招人之后反而每生产1 line 成本还下降了
答：因为 testing, documentation两个人在生产1K lines只需要工作1周，剩下的一周相当于白付工资不干活儿。巴拉巴拉-baidu 1point3acres
问：好了那你现在要跟大老板说这件事，你怎么说？
答：要签这个客户。招个 contractor。钱多。
面试官：不错，已经说得很好了，还可以补充的话就是，度过这两周之后，可以考虑招一个 full time，因为这样生产1 line 的成本会更低。
我：。。。

需要注意的点大概就是，算数的时候记得讲出来，一步一步来不要跳。我做第一个 Case 的时候由于精神涣散，算数的时候都没有讲话。。。后来中间休息的时候调整了一下，第二个 Case 计算的时候效果就好很多。


## Algorithm Study

http://www.hawstein.com/archive.html

> Dynamic Programming: From novice to advanced 

http://www.hawstein.com/posts/dp-novice-to-advanced.html

> STL

http://www.hawstein.com/posts/a-byte-of-stl.html

> GOOGLE JAVA/C++ style guide

http://www.hawstein.com/posts/google-java-style.html

http://www.hawstein.com/posts/google-cpp-style-guide.html


先说一下自己的情况，本人主要面Data Science analytics职位，做过的题目基本都是简单的模型+如何做AB test+如何做产品改善推荐这种类型的题目。不是machine learning相关的职位。做过湾区多家热门独角兽公司的data challenge，之前每战必败，现在通过率100%。做多了发现都是套路，所以希望自己的经验可以帮助在寻找data方面工作的战友们

好了废话完了，马上进入正题。这种take home data challenge的难点在于问题比较开放性+时间限制。短则3-4个小时，长的最多一周。下面我来说一下前期准备工作，以及拿到题目后如何短时间内把握住要领，写出面试官满意的报告来。


下面先说一下前期准备：
代码熟练：不管是sql,或者r, python，随便你选，但是一定要选你用的比较熟练的。因为你要短时间内完成数据分析+写报告，如果代码不熟练的话可能做不完。建议可以先准备一些模版，比如画图的，做模型的，做ab test的。我用的python，所以画图都是seaborn + matplotlib, 需要建模一律用random forest from h2O package。这里强烈推荐h2O random forest，自带auto bin的功能，解决了categorical level多的问题。不需要将 categorical variable 转化成numerical（对于python同学来说）, 不需要impute missing value。至于我为什么只用random forest, 下面会讲到
预习一些题目：这里推荐买这本书 “A Collection of Data Science Take-Home Challenges”。我以前买的时候可以单独买这本书，50块，现在好像得买整个package，有些小贵。这本书主要是给了几个例子，以及用r来做的详细解答。非常好的参考例子，我就是看了这个书以后才开窍的


下面言归正传，题目拿到手以后改咋办：
明确产品的目标： 一般都会给你描述一个产品，比如某社交网络公司想提高 rentention rate , 某电商公司想提高conversion rate。你下面的所有的分析一定要围绕这个目标来做。这个说起来容易，但是很多同学题目拿到手，都会脑补很多东西，想的太多了，反倒无从下手。建议就从跟产品目标最直观的开始分析
定义metrics：在清楚了产品的目标以后，哪些metrics可以用来衡量产品的成功与否呢。对于互联网产品，基本都是从user acquisition, retention, engagement. monetization 相关的这些目标来定义metrics的。多了解用户使用产品的漏斗模型 （AAARRR)。然后定义metrics的时候思考产品特点以及目标，往漏斗模型上面靠，每一层应该用什么metrics来衡量。可以看这篇科普的：http://startitup.co/guides/374/aarrr-startup-metrics
数据清理：也就是所谓的data cleaning。基本就是看看哪些变量的missing value太多了，或者某个变量只有一个level。这种情况下可以去掉那些没什么用的数据。另外如果你用h2O random forest建模，不用去impute missing value。
提取跟产品目标相关的变量：比如uber想提高driver rentention rate，你拿到数据后，看一下每个变量都什么意思，想想哪些变量有可能跟目标相关。下面说一下我遇到的比较普遍的需要做一些data munipulation的相关变量

时间变量：可以提取day of week, month, time of the day这种变量。还有一些time difference， 比如user sign up date，first time use this product，这里面的时间差也就是用户登记后多久开始使用产品，这也会是一个很重要的变量。
需要求平均值，次数求和这种变量：比如一周内使用了多少次产品，平均每次花了多少钱
去掉跟结果直接相关的变量：比如某个变量跟结果是显而易见的相关，虽然加入这个变量你的模型预测准确度达到99.9999%， 但是对于你后面做的产品推荐没有任何意义。比如某电商想看看用户的哪些行为能够促使最后花钱买产品，有个变量是是否到了check out页面。很显然用户到了check out 页面，购买的意向就已经很高了。在建模的时候要去掉这个变量，因为不用分析就知道这个变量重要。

如何鉴别重要的变量：一般的问题都是让你鉴别哪些变量对结果影响最大。选3-4个重要变量即可，千万不要把所有的都分析了，因为你没有时间！下面说两种我常用的方法

看分布：比如你觉得time difference是个很重要的变量，可以画个box plot，或者histogram，分别对retain and churn的人做图
直接用模型：根据模型结果看feature importance。我只用random forest。因为第一我建模的目的只是为了看哪个变量重要，并不需要很精确的预测；第二用h2O的random forest基本不用调试，结果就很不错了；第三我觉得random forest在鉴别feature importance比别的模型要好，因为它每次是取所有变量的一个子集来建立决策树，所以每个决策树选的变量都不太一样。最后平均下来看哪个feature最重要。感觉这种算法更可靠一些。不过哪种模型不重要，关键你把重要的变量选出来就好。这里提示一点：千万不要花时间去把模型调的很精确，只要模型结果可以接受就行。因为你是在做分析，你的重点是在做后面的产品改进推荐

产品改进推荐：也是最最最重要的一点！很多同学做模型啊，分析啊做的天花乱坠，然后都挂在这步了。一定要记住一点，你的模型是为了产品推荐用的，不是为了production用的。比如你发现用户登记以后越快使用你的产品，他们的rentention越高，那么就要想办法如何让用户尽快使用你的产品。你不能只说让用户尽快使用产品，要给出更具体的建议。比如给登记的用户发promotion，第一次购买可以便宜一些。有的职位偏重AB test，会问你接下来如何设计实验来测量你的推荐的有效性
实验设计：必看资料是udacity上面的AB test by Google https://www.udacity.com/course/ab-testing--ud257. 一般做题目常用的无非就是test mean difference or proportional difference ( t and z test), 上面都讲的很清楚应该如何做，如何选sample size。下面简要说一下如何分析结果

影响有多大：也就是what is the opportunity sizing. 这一点很重要，如果你的产品推荐只会对很少一部分人有影响，比如小于5%，那么你这个推荐是没有用的。但是有一个特例就是如果你那5%的人可以带来好几个million的收入增加，那么还是值得做的。
分析比较结果：比较爱问的问题有

Is this amount of lift enough? 比如做实验后发现有2% lift，这个结果好不好？这种题目一般就要看2% lift带来的实际影响，比如2%带来了几个million的收入的增加，那么就是好的。
Metric A going up, Metric B going down, should we still launch this product? 一般看哪个是最重要的metric，另外就是有些metric需要时间长一些才能看出来。比如某个社交网络的用户参与度增加了但是用户增长变慢了，假设这个产品改善后是希望增加用户的参与度。这种情况就要考虑network effect，随着用户的参与度的增加，用户的connection也会受到影响，久而久之他们也会变成日活或者月活的用户。


分析做完了，写报告应该注意啥：
思路清晰，言简意赅：看似是废话，但是很多同学，包括我以前，都恨不得做个特别复杂完美的图跟表格，然后展示给面试官我的技术有多牛掰。其实他们更看重的是你的分析是不是通俗易懂，非technical的人能不能一看你的图或者分析就知道怎么回事了。
图文并茂：这里强烈推荐大家都鄙视的excel作图功能，个人觉得比seaborn, ggplot, matplotlib都好用多了。也许是因为我代码能力不强，改个图得debug半天，还经常弄不出自己想要的效果，但是用excel简直是神器，轻松做出非常专业的图来，改起来也很方便。我一般简单的图，比如boxplot, heatmap，用seaborn这种直接出，但是要做一些复杂的cohort analysis，就上excel了。
不要写的太长：很多同学把data challenge当成论文来写，弄个几十页的报告，把能分析的都分析了一遍，结果还挂了。因为人家面试官根本没有时间看你的论文报告。确保他们花10-15分钟时间能把你的分析跟结论看懂。



我现在能想到的就这么多。最后总结一下主要步骤： 明确产品目标， 定义相关metrics，建模去预测关键指标，模型结果对产品改进有啥建议。希望这篇总结能对正在战斗或者打算战斗的战友们有点帮助。
