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

我的onsite一共6轮，business case是一道卖酒题，假设你是老板，告诉你revenue，cost, 和gross margin, 让你算profit。我刚开始不懂gross margin，经过考官提醒用gross margin要算production cost, 最后把profit算出来。然后问你如果你有竞争者，你会怎么办？之后再给你这个竞争商家的数据，问这个竞争商家哪个数字你觉得有问题？面试的时候我一个一个数字看，看了一轮没有发现问题，面露囧态，考官提醒我要看product cost, 好像答案是竞争商家的cost占比比咱家高，考官问他家为什么高？我说了一通，然后给我图表，让我算我可以增加多少marketing cost能够刺激sales，还让我假设如果打价格战，我能承受的损失。数一点不难，可是平时少有功夫琢磨business，问题虽都解出来了，但是一路靠考官指点，几次把我从天马行空乱吹拉回到正轨。
-baidu 1point3acres
quant case是两道概率题，掷骰子求期望，本科水平，但是概率论题目千变万化，每个人面试题目可能都不一样。

role paly还是经典的飞机误点，发给你一堆slides, 把outlier, missing values, correlation, linear regression, logistic regression, p-value, r-squared, anova table概念搞透一点不难。考官要求说的时候用最简单的英语说，我就当他啥都不懂，一页一页slide和他解释每个图和数字分别代表什么。

分享一个capital one的onsite面经，面的是岗位business analyst，地点在mclean, va
总共是2个case和1个product interview；recruiter说如果不能决定的话，需要再面第三个case，因为接近thanksgiving，所以很多面试官都休假去了，需要的话会再约时间

product interview纯粹就是考验business sense，我也不知道能怎么准备，都是在当场临时想的，第一题算略有准备，是问怎么redesign umbrella，我之前搜过，有了些灵感，不过剩下的都是在现场乱想的，比如可以利用太阳能，通过伞给手机充电，哈哈

case interview还是有点难的，第一个是关于credit card的，给了一堆基本信息，让你计算要不要通过一个transaction，然后算出来是有利可图的，是可以通过的。然后问实际应用后，发现利润其实还不如拒绝呢，问有哪些可能的原因，然后给了别的参数，让我继续算，最后要算break even，并且要画图。我当中有点算错了，主要是知道cost of fund的利率，然后来计算balance，但是balance是每月在变的，所以这块没有考虑好（之前面试官已经提示过了，但我没有get到，悲剧），信用卡的例子是c1最擅长的，很容易就考到人，我的背景和这块完全无关，心中略虚，还好之前有稍微准备到一点点。。。不至于完全懵掉

第二个case是收麦子的，这个case的教育就是不要想的太复杂，把所有情况按照最简单的逻辑列出来就好了，比较一下哪种情况最优。我当中试图弄点公式出来，但是面试官打断了我，问我在想啥，我说了后，她说不用想那么多。。。。最后应该是算对了。。

technical: 45 mins, (15 mins behavior + 30 mins technical case): 

how to use data to predict credit card churn， 主要考点missing value, big data tool set, model selection, model comparison
-baidu 1point3acres
data challenge：nyc taxi 但是听说从4.1号以后题目就变了

onsite:
1st round: technical interview 主要聊experience，展示了一下data challenge，bias-variance trade off, tree pruing, overfitting, etc.
2nd round: case market personalized credit card (with user uploaded photo) to existing users 
1. why we want to do this?
2. some simple math. 1point3acres
3rd round: case life insurance 版上已经有比较详细的面经 
4th round: job fit 主要聊experience
5th round: role play 我选的decision tree, 主要考点, 用plain language给non technical background得人讲decision tree的基本原理. 1point3acres
以及找出slides里模型的问题，最后提出三点business recommendation，注意时间

第一轮是case 因为当时我们program已经有两位同学拿到了C1家实习的offer，而且据说面的都是life insurance的case 所以当时很心大的基本只准备了这个。。。结果一上来就是一道app的题。。。然后就只能硬着头皮上了。一上来先问app有什么赚钱方式，我说的两点是买app的钱和in-app purchase，他问还有呢,我思考了一小会, 面试官很好心的提醒了说 “想想instagram” 然后我就马上反应过来是广告费。然后他给了两列数字: 一列是 free app的，一列是paid app的。数字包括user number，ad rev per user，cost per user之类的大概六七行数字让算profit (注意这里是profit 不是breakeven哦) 挺简单的。 然后问应该选哪个。 因为记得free app的profit是400,000， paid app是600,000，所以肯定选paid 啦.  
然后面试官说ok 假设我们现在只有200,000个free用户 (之前是200,000个free用户 和50,000个paid用户)，现在要多少个人去paid才能达到之前600,000的profit。当时有些不太理解就问了面试官 “可是只要paid app用户少于之前的50,000，那肯定会比600,000的profit少啊” 然后我忘了他说了句啥我就反应过来：要找的是两种app在新的用户数的情况下，加起来的profit是600,000的那个点, 算两个app的用户分别要有多少。这边因为紧张算错了几次… 而且因为是视频面试, 脑子里一直想着不能安静太久不能让气氛变尴尬之类的所以就出错了。 但是面试官最后很nice说没关系不用担心，所以大家一定要记得不用太紧张～ 算完之后关于insight他就会问有什么提高profit的方法。我只是很框架的从增加revenue和减少cost的角度去分析。但是面试官其实想要说的是 paid app user到了free app以后 他们的 purchasing behavior不会变，所以其实free app 的in-app purchase那块的revenue会比原来的数字更高 以此来到达比600,000更高的profit。他会慢慢引导你说出答案，所以也不用担心一定要一次答对

第二轮是behavioral. 也是我面的最好的一轮, 问的问题是
Tell me a time you made a mistake，follow up是mistake有什么后果之类的
Tell me a time you helped a teammate，follow up是你做的这件事对team 有什么贡献
第三个时间太久忘了。。。因为在美国待了很多年了，再加上之前有过很多面behavioral的经历，所以这一轮和面试官聊的特别好。 个人觉得这种一定要提前想好例子 behavioral 不外乎就是teamwork, challenge, leadership几个大类 每种大类都要有1-2个例子 然后一定要自己practice几遍如何清晰的表达出来，自己在家对着镜子说几遍。还有一些偏门的behavioral平时有空也看看。
. 1point3acres
第三轮就是经典的role play啦。这一轮讲真面完我都绝望了。。。一个中东的大姐。看上去人还挺nice，但在我present的时候给特别严肃。。。anyway。。。首先就是20分钟看ppt，时间是真的有点紧。虽然之前在地里扒了很多面经，但是还是有很多的图表要理解，然后要整理思绪想着怎么说。这个地里也有非常多的面经了，就是一个只飞两个城市的航空公司，用model来predict晚不晚点，要找model和数据的问题基本就是missing data, negative value, 两个城市没有分开来算之类的。feature之间有correlation，还有就是根据图标判断哪些feature对于predict response没太大用。我就说一个之前地里好像没怎么看到过的吧（可能也是我不记得了）。中间由于时间有点紧 我就跳过了其中一页ppt（面试官之前也说过不用所有的都讲）。结果她直接就问前面那页你没有什么想说的吗，要我回去 然后我就慌真的慌了，内心os你不是应该什么都不懂的嘛。。。这一页的话就是data里有一部分的missing data并不是missing at random， 而是只在一个category里miss了。所以不可以直接impute。然后他是放在一页有四个类似于confusion matrix的ppt里所以大家看到那页的时候记得注意一下。反正最后磕磕绊绊的也算是说出来了。。。但是感觉这一轮面试官就是各种找茬，面完我真个人都绝望了感觉没戏了。。。回去在机场里还忍不住哭了觉得肯定没戏了（玻璃心的我）。。。

投了简历大概2周后，HR发来了一个Python notebook格式的data challenge，给了3个工作日时间做（这点C1蛮厚道的，因为周末不算在timeline里面，所以实际上有5天）。当时的介绍说是需要4小时左右完成，不过最后还是神奇般的拿到了offer，总结了一下可能也就这几个原因。第一是我的data challenge做的真的超级用心。虽然不说有多nb吧，但真的是试了很多不同的方法。然后再最后总结的时候就算没有用到的方法也在summary里提了（当然要让他们看到我的effort）。花了可能有25+个小时？  之前recruiter也说他们评判会看整个process。所以建议大家有空的话也是多花点点心思，说不定最后能自己把自己拯救了。还有就是交流能力真的很重要，大家没事在家多练练口语。

实际大概花了我10个小时。清理数据，写下各种observations和理由都花了很久。建议越早开始做越好。
然后就拿了on-site，去的是Richmond的office，C1会报销飞机和酒店。听说去McLean的同学们住的是Ritz，Richmond给的是一家Hilton。

面试当天一共是三场面试加午饭：
第一面统计知识：先是聊聊简历上的内容，然后大概45分钟时间给你一个case，上面有各种统计的图表和结果，面试官给你10分钟看，然后会回来假装是一位不懂统计的同事要你解释如何解读各种表格和统计名词。我回答的非常差，因为不是统计专业的，第一面结束后内心是绝望的。。。
第二面ML知识 + behavioral：面试官主要聊的是简历上的内容和各种ML算法，我跟面试官还聊得挺开心的，我记得聊了gradiant descent, GLM, online learning, etc.  Behavioral就是平常的那些问题，比如如果你和老板的意见不统一，你是如何说服你的老板的；如果老板给你布置你的任务很多，你会如何处理
第三面business case：这个case是假设你在一家巴西的类似沃尔玛的公司工作，他们想发行Store Credit Card。如何决定要不要发行这个卡，根据盈利率和客户群体等考虑。这个还蛮简单的，面试官很nice，一直在帮忙引导我。C1也会给准备材料。这种类型的问题没有标准答案，因为公司主要考察business sense。只要你说得有道理，面试官就会跟着你继续聊下去。

店面：
Walk through your resume，然后根据resume里面的project问了一些follow up。 接着问了一个广告的case，然后让你go through 整个建模的pipeline，有问一些spark的东西

onsite：
一共四轮：
第一轮：behavior + case，公司打算开发一个app，先让你提出一些metric衡量app的表现，然后说有两个版本，一个版本付费，一个版本不付费，然后让你计算哪种比较好（比较基础的计算量），做选择然后问问什么这么选。
第二轮：behavior + case，保险那道题，地里应有比较详细的了-baidu 1point3acres
第三轮：hiring manager 和善的聊天
第四轮：role play， 飞机延迟那道题，看图表说话。然后给客户解释一些tech的东西
第五轮： tech面，挑一些take home里面的东西，考了hypothesis testing，model为什么选这个不选那个，说说clustering的区别，怎么实现的，SQL statement，leftjoin casewhen什么的，然后一些casual inference的东西。

终于onsite了，上午三轮 2 case + 1 product，下午一轮。
-baidu 1point3acres
第一轮，面完感觉不是特别好，关键是我完全没理解题目。但是面试官非常helpful，你如果不知道怎么做，就多问问他，看他眼色，你们懂的。

第二轮，面试官和之前的面试者聊得太愉快，迟到十分钟。非常和蔼和nice，算了一道1% cashback，数字都是现场按照我说的给的，比如说以下对话。

面试官：你觉得多少钱比较合理？
我：最多$50，不能在多。
面试官：好，那我们就假设$50。
我: .......好

这是整个上午最顺的，面试官迟到也没有给面试时间带来多少压力，不像第一轮。提早十分钟结束，客客气气地问了他几个问题。

第三轮。product interview。面试官迟到20分钟，HR急飞。。。
这次是video chat，终于联系上了，两个问题，一个是Amazon drone，一个是你生活中最常用的东西。不太顺，因为线路问题，只有我一个人对着空气在说，没见到面试官的脸。。。

中午吃饭，六个人面试，但是HR有交代，你们不存在竞争关系，所以大家气氛都很friendly。一个三哥哥一上来就问我，你是什么学校毕业的。。。。anyway，中午的午饭很愉快，C1的两个同、高职位员工（其中一个也是中国人）介绍了很多，C1的优点就是benefits，flexibility，training opportunities。

下午回去通知加面一轮，然后开始了漫长的等待。等得刷起了手机，突然一个年轻的小哥闯了进来，然后告诉我之前所有面试官都归他管。。。。。

下午面试真的很难，完全都是think out loud。面试官只带了手机进来，我问他问题，他基本上都回答，I don't know. You tell me. 一路磕磕碰碰，到最后面试官自己都恍惚了。。。当时感觉基本要挂。。。。 

值得一提的是，上午全部通过才能进入下午，所以有下午加面的朋友，证明你们已经离成功只有一步之遥了！！！！


今天上午刚面的技术面，总结一下热乎的面经。希望能给接下来的人有个参考。顺便求大米。第一轮好久之前hr面，基本上问问visa的情况，问问background，不怎么筛人。. 1point3acres
第二轮就直接约的一个小时技术面。下面详细讲一下问题。
碰到的case是客户流失模型，跟地里一样。
问的问题就是：
1:这么多数据怎么处理？
从data review到feature extraction讲一遍，没什么追问。
2：什么feature觉得合理， 什么model 觉得合理
一般就是啥啥的mean， median，std之类的， classification 算法呗，列举几个例子-baidu 1point3acres
3：如果数据量变得特别大，需要各种retrain model，怎么办？
spark，而不是hadoop，因为要real time 更新results。
4： 如果给你好几年的数据，怎么办？
那就改用hadoop呗，毕竟不着急。
5：如果有个limit 5000的俩用户，一个用了100% 一个用了2%，模型给俩人呢分到 一类怎么办？
我答得不好，我后来也问了面试官怎么办，他支支吾吾的也没说好，就过了。
6：怎么在hadoop上实现RF
我说我没用过，不知道。
7： 怎么评价模型
AUC ROC
8: 怎么做调整？
K fold CV。
9： imbalance 怎么解决

2个business case. check 1point3acres for more.
有一个之前没看到过。
关于local的一个卖酒的商店的。会给很多的图表。每一年的gross revenue，average profit margin 以及基于channel的不同的profit margin。以及other costs
先算今年的profit。
然后说怎么样可以increase profit，前提是有一个更influential的competitor
然后给一个competitor的财务表之类的，让你看里面有什么数据有问题，就是profit margin偏低，然后问你为什么
最后是给一个不同的marketing expense增加的sale，问你哪一个点是optimal

另一个business case是关于信用卡计算transactor 和reserver的profit以及提出建议的。数学比较多，但是我之前在地里看到过类似的case


technical的问了大数据相关的和传统的machine learning，以及一个如何有效计算mean和var基于streaming data 写code那种


面试地点订在了mclean，当天加上我自己一共三个人面试，另外两个都有过工作经验。当天安排是case-case-data challenge，每一轮都安排了一个shadow person, 会在旁边跟着caser学。 
1）第一个case面试官上来问我有没有做过case interview，我直接说从来没有做过，然后他就很nice的给我讲解了具体流程。第一个case是说公司开发一个person-to-person的产品，举例子说比如venmo。然后这个产品已经运行了一年。问：你觉得这个产品能给公司带来的好处有什么？然后就是计算，两种交易type，debit vs. credit card，每种的手续费不一样，给你每个月的交易额还有其他数字，计算monthly profit。算出来好像是loss？忘记了。。问你如何improve。有一家企业联系了C1，想用到这个产品作为支付平台。于是公司考虑开发person-to-business，接着又是计算profit，结果为盈利，然后问需要多少家这样的企业breakeven。最后问你future strategy的建议。

2）网上有的small business loan的case，是否开发90-day short term loan。 
一家小企业想申请90day 短期贷款，公司目前没有这种短期贷款，问你是否应该开拓短期贷款的新市场。计算就是给你每个quarter的总贷款额，利率（分为两种，一种是到期偿还的利率，另一种是提前偿还），然后告诉你x%到期偿还，y%提前偿还，z% default。计算quarterly profit。算出来为负数。
然后加入新的计算条件，大概就是说另一家企业也想申请贷款，给出新的利率，计算profit和breakeven。
最后就是现在有两个公司和你谈合作，告诉你合作之后每个季度的营业额变化，要你选一个。没有正确答案，分情况讨论。

3）data challenge，因为离做data challenge这一轮时间过去太久了，细节已经忘了很多。面试官在这里问了很多细节问题，比如为什么model是这样，为什么用这个变量不用另外的，visualization还有没有其他更好的形式能更清楚显示出来。就算忘记了也只能硬着头瞎编，把自己的话原回来，我一直在问面试官我这样解释make sense么，他现在弄明白了么之类的。present完之后问到behavior的时候，由于我讲了太久，主动要求能不能歇一下喝口下了再继续。总之当天面完就觉得这一轮给弄砸了，前两轮case都聊的特别开心。问到的3个behavior问题：成就，mistake，和help others。之前有尝试准备这类问题，花了两天时间还是没思绪，于是当天临场发挥，但讲的都是我自己做过的小组project，所以不怕问到细节。 . From 1point 3acres bbs

大家不要紧张啊！不要像我一样第一次看到里面的帖子后吓的睡不着。。我认为onsite比data challenge要简单太多，面试官都很nice的，不懂就问。我还问了第一个面试官，能不能对我接下来的case interview给点建议。然后第二个面试官一进来就调侃他，甚至说了what a jerk哈哈哈。

之前在地里提过，自己开始申请的intern，然后慢慢被hr调整到了full time， 经过一个比较乱的筛选过程，自己现在到了onsite阶段-baidu 1point3acres


说一下今天电话面试的内容吧


case就是大家提的信用卡的case，因为看了大家的帖子，感觉自己在抢答问题哈哈


主要就是去建模判断用户要不要关账户

1.     Target/goals
2.     选feature
3.     data cleaning:
3.1  outliers( plot graphics, histogram or bar chart, scatterplot to watch the multivariate outliers)
Numeric Detection :
1 Plot histogram of each variable. Detect them based on real life situation/or based on data dictionary, filter out meaningless value.
2 Detect them based on IQR( interquartile range).
3 See the distribution (z score)
5 Clustering
3.2  missing values
1 Explore the reason of Na, if they have meaning treat them as a new category,
2 Delete. data not too much & really not make sense.
3 Means/median/mode: it influence the distribution of variables.
4 do regression/logistic regression to fill the
4.     Modeling: (including package)
4.1  random forest:
4.2  why not logistic regression or decision tree
4.3  how to improve or tuning parameter, for random forest, we can choose
5.     Overfitting / underfitting
6.     model performance:
1.1  ROC / AUC
1.2  Confusion matrix
7.     If data is really big (Map reduce / distribute computation)
2.1  tools package (Hadoop/spark)
Lighting Fast Processing
Real Time Stream Processing
Easy Integration with Hadoop
Ability to perform “in-memory” processin
8.     what if the model not accurate, how to influence bank
9.     imbalance of data
10.     如果用model predict得到了一堆target的值，应该怎样根据target发rewards

11.     两人都有5000limit，但是一个用100%一个只用2%，这两人都选择关户，要考虑原因

附上几个自己参考的网址，自己下午发邮件问来了feedback 然后就过了 最后感谢地里的大家，希望自己onsite好运

https://www.analyticsvidhya.com/blog/2017/03/imbalanced-classification-problem/
https://www.theanalysisfactor.com/seven-ways-to-make-up-data-common-methods-to-imputing-missing-data/

case的宗旨是在信用卡部，银行想要
identify一些可能会离去的customer，然后给他们一些激励比如cash bonus之类的，让他们能继续留下来。dataset里面有消费时间、金额、开户时间等等一系列银行有的feature。然后呢，label来自于历史数据，让你来build一个model。
这个背景我的第一想法就是个binary classification，正要开口说的时候，她突然说从data preprocessing开始描述，问如果是monthly data怎么处理，是weekly data这么处理，是hourly data怎么处理，问的非常细节。然后又接着问，如果是big data怎么处理，我也是很蒙了，因为平是真的没有非常pay attention to big data，所以也就只能general地描述一些。
说了半天终于说到model了，本来想好好描述一番，结果她只问了一个问题，
which models do you consider using，只让我说了说那些model的名字，完全没有深究models，然后就move on to怎样implement这些model，具体就是如果不是big data怎么implement，如果是big data怎么implement
整个过程只有半个来小时，我真的不知道为啥他们如此重视big data，这在面试里也是非常罕见了。这位小姐姐问完case后说了一句：i planned 5 mins for you ask questions, now i guess we have 25 mins, so feel free to ask me any questions you have。当时瞬间就觉得彻底没戏了，不仅仅是因为那些big data真的是扯了一些自己觉得不靠谱的东西，而且别人明确暗示了，跟你没啥好聊的。。

Onsite:
Round 1: Behavior
- Tell me a time when you helped your teammate
- Tell me a time when you did something creative
- Tell me about one failure
. From 1point 3acres bbs
(with follow-ups)

Round 2: Role Play
Flight Delay problem (永远是它！）

以下是我从其他面经整理的流程 . check 1point3acres for more.
* 你是一个data team manager，承包了capital one的一个项目。 
* 面试开始他会给你一叠slides，给你做一下背景介绍。 
* 问你要linear regression model还是decision tree model，把相应的slides给你（只能二选一，因为他说你没有时间过完所有的内容）。 
* 然后他会离开房间，给你15分钟整理思路。 
* 等他回来的时候，他是capital one那个项目的manager来听取你的汇报。 
* 你会有20分钟左右的时间： 1. present你们team的结果， 2. 整理报告中存在的问题， 3. 给出business recommendation。


以下是我从其他面经整理的存在问题：
* 模型选择不当（应为分类器而非回归）：公司只关心delay<8分钟与否，不care具体时间* week of day处理不当，correlation严重 
* day of the week (mon,tue…)当成了continuous variable 改成categorical 
* 起飞地点他没有区分，后面有一个图可以看出不同起飞地方增加地面服务人员影响不一样 * 没有加入飞机上面实际座位的影响，加这个进入predictor就可以了。 
* 还有就是他的图表有能有些数字不合理 比如座位书＝－１，你有空就看一下

我实际遇到的问题:
* 在共线性上拘泥太久，但实际上面试官的意思是airplane type基本可以涵盖很多共线变量，所以#passenger | #gate attendance 等等都可以不要
就是相当于plane type这个变量可以囊括其他这些变量。（realistically speaking）一架飞机越大，所载乘客越多，所需空乘和地勤越多这个道理。


Round 3: Life Issurance（这个case是真的不费脑子啊…当时的感觉就是纳尼这就完了不对感觉有阴谋）
所以就不多说了，其他面经里面或多或少有收录

第一轮 BI
1. 地里的原题 每一个问题都有followup. 1point3acres
Tell me about a time you explained a technical topic to someone without a technical background.  
Tell me about the project you are most proud of.  
Tell me about a time you learned something new.  
2. Case Interview
2001 C1 收购 ING， 有什么advantage  还有会有什么技术性的问题

1. Case interview: Life insurance（这个好像以前有人发过。。但是每次问的问题好像有点不同） 
   先问了一下你认为有哪些人我们不愿意轻易issue insurance给他们 （老人啊，有严重疾病的人，高危职业从事人员， etc）
   再问了一个death probability的问题，算一下在这个prob在什么时候我们可以考虑给保险。最后一个问题没记太清楚，大概是说各种dead prob的group，怎么样选择能使得profit最大。

2. Role play interview: Airplane delay （太多重复了，就不细说了） 我看地里有人被面到这道题时被面试官问了很多问题。。但是我一个问题都没问。。我讲完就直接说role play 结束了。。。感觉凉了。。
3. Behavior interview: 
   (1) A project that you are proud of;
   (2) Time about helping other people in your team
   (3) Time about failure and mistakes.
4. Job fit interview: 我都不知道有这么一轮。。一个印度人video面试。。问了几个问题。。完全不知所以然。。仅供参考：
   (1) 给你一个NY times 的报纸，有没有什么算法能够给出top 5 popular companies。。。。我说你这个至少要知道关键词吧。。他说不知道，没有关键词。。然后我说那你像apple这个词，那到底是apple公司呢 还只是一句话里面的什么apple tree，apple juice什么的呢。。他说你可以分别考虑。。。。。我就不知道了。。我觉得这个问题作为面试问题也太open-ended了吧。。。只能凭空yy。。

   (2) 给你10000个不同industry 的不同variable，如果有connection的variable就连起来。。形成一个graph，问如何估计这些connection。。。然后如何度量一个industry里面各种variable之间的联系。。

然后就是Onsite，Case study中有一个是Life Insurance的那个，首先什么样的人会买保险。。。【危险职位的人】，但这样的人我们不想卖给他保险，我们的target应该是什么样的人，我说应该是有familiy的人，同时又不太富裕，所以想给家人留财产。然后接下来就是大概就是死亡率多少时break even，如果你答的很快的话，就会不断深入，比如怎么提高profit啊之类的，我基本说了最直观的方法是提高premium，但是这样可能导致客户数目减少，所以我们要找到balance的点，然后他就问在实际应用中怎么找这个balance点，我说可以发送调查问卷，看有多少客户接受新的premium，然后根据这个比例判断。
第二个是Role play，还是飞机晚点问题，但午饭的时候我问那个人他说可能马上就换了。这个问题我因为见过，所以以为自己应该挺顺利的，但是当我说到有multicollinerity的variable应该从model里移除时，那个面试官一直在追问我为什么，然后我说correlation会导致variance增加，p-value不显著等等，bias estimate【难道不会影响estimate么？】，而且这些variables are telling same story。但是感觉面试官对这个回答并不满意，一直在追问，但是我学过的都是vif>5就移除啊。。。不是这样么？难道我要用PCA？但这个模型显然并不需要用PCA消除correlation这么麻烦啊。。。有什么别的方法么？求教。

我觉得第二个题的他想听到的应该是，存在multicollinerity会影响到我们对model的interpretation。
楼主可以看看
https://onlinecourses.science.psu.edu/stat501/print/book/export/html/346
Effect #1和#2

第三个又是Case Study，这个比较简单，关于ATM机的，也是break even，然后画了曲线。不过我第一次听错数字了。。。。真是对自己无语。
第四个Behavior问题是tell me a time系列，两个面试官是中国人，在面完前三轮之后看到中国人有一种松了一口气的感觉，他们人也很nice，其实所有面试官都很nice，所以我感觉更难过了。。。呜呜呜。。。
午饭后和director面最后一轮technical，他上来就说这是今天最简单的面试了，他说你可以把笔放下，我们聊聊天就好了，我天真的信了。然后他就说我们聊聊你的project吧，我就把实习的project说了，他问了model，我说我做的是Random Forest部分，他说那你对Random Forest了解多少。。。。然后。。。然后我就装逼了啊！！！我说我以前build model from scratch过，然后他就感兴趣了，他说那你说一下大概的流程，我就又把笔拿起来了啊！！！然后我就说错了，第一步应该是bagging我说成subsampling了。。。director同学很想纠正我这块来着，但是我完全没意识到啊！我就继续说下一步怎么建decision tree了，吧啦吧啦讲大概怎么算information gain，怎么分叉，怎么得出最后的结果，这时候director又尝试拯救我一下，问我这些decision tree会用怎样的不同，但我还是没有意识到。。。然后他决定再给我一次机会，问我还scratch啥model来着，我就说adaboost，这个说对了，然后就轮到我问他问题了。

2： 问简历上的项目，顺着项目问了些算法，比如RF和GBDT的区别，哪个更容易over-fitting, 为什么
3： 怎么预测用户是否会点击一个广告？如果有A, B两广告，点A一次平均盈利50，点B平均盈利60， 怎么去判断哪个盈利多？
4： 怎么对数据流提取特征？ 如果10分钟内有1T的数据，怎么取提取特征建模，用什么模型什么技术比较好?

现在开始进入正题，面试是聊一个credit card churn model，地里有人分享过，我就补充下细节：

      1. Feature engineering，比如从start date算出tenure 等等
      2. Missing value
      3. 用什么模型，为什么
      4. 现在数据量加大，怎么办？spark。如果你要选，用RSpark还是PySpark？为什么
      5. 现在模型output出来，一个credit limit 使用率0%的用户和使用率95%的用户都很危险，都很可能马上就关掉信用卡，你会怎么处理？我回答churn model是起点，一般marketing department会根据churn model的结果设计retention program。对于这两类危险用户，需要设计不同的incentive plan。
             1）使用率0%的用户，基本上很难挽回。
             2）使用率95%的用户大概率可以挽回，降低利率，增加cashback等等。。。
             3）可以根据测试结果再搞个uplift model，看哪些high churn users可以挽回的，着重施加treatment。


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
