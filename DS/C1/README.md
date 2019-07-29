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


给你一dataset，比如信用卡一年的交易记 录、客户个人信息，银行想预测客户会不会在一个月之内关户，如果会的话，银行打算发一点cashback rewards给这些 人挽留一下。让你建模预关户。feature, data cleaning, outlier, missing value, ...

废话说了一堆，来说说面经吧。在linkedin上海投的senior data analyst，recruiter第一次联系我都是一个半月以前的事了。之前在地里也看了几篇这个职位的面经，具体流程几乎完全一样，很标准化。
1. recruiter
第一次和recruiter聊几乎没问什么，就是基本信息吧，问你愿不愿意relocate，介绍了一下面试的具体流程：hackerrank coding challenge+data challenge+onsite，聊完就给我发了hackerrank的链接
2. hackerrank coding challenge
两道简单的称不上算法题的算法题，两道SQL。算法题具体是什么忘了，之前的面经好像有，反正所有test通过了提交就行，也没有时间复杂度的要求。SQL也挺直白的，用到什么group by再sum一下这种。
3. data challenge
airbnb和zillow的数据，之前有人发过。投资NYC的properties来short term rent，要决定哪些zip codes最profitable。要先进行data cleaning，check data quality（从completeness，accuracy，validity，timeliness方面，具体可以google一下），然后进行分析并data visualization，最后给出建议。hr建议花5-8小时，但我觉得我做了一周，也不知道做了几小时，反正每天都花点时间在做这个。
有人说C1比较偏好用Python做的，不过我用R写的也过了，因为要visualization个人觉得ggplot比较方便。onsite的时候有一轮是present data challeng。这轮的评价准则有三个方面：Data Management， Innovation和Business Intelligence。但也不清楚具体做到什么程度才能过。
4. onsite
data challenge过了以后就是onsite，约了三周以后，当时觉得时间很多，但准备着觉得时间还挺紧的因为要准备的内容挺多的。提前打电话给他们会帮你定好机票和酒店。
onsite包括三轮：data challenge+case+case（每一轮都会包括1-2个behavior的问题）之后会和公司的一个人和那天一起的candidates吃午饭，参观公司。

data challenge:
把之前做的data challenge present一下，我是做了个ppt，然后花了20分钟从头过了一遍我的整个分析。之后面试官会问一些问题，不一定是啥，反正就按照自己真实的想法回答就行。

case interview：
因为之前完全没有case，还挺紧张的，搜了各种consulting 的case的准备资料，也不知道该看什么。但其实这个case和consulting的case还差别挺大的，几乎都是profitability的case，万能公式profit=revenue-cost。首先面试官会给你一个背景，一开始会问关于business sense的问题，比如有哪些factor要考虑，revenue和cost的来源，为什么要做这个新的产品。然后就会给你一堆数据，有的是读给你听你要自己记下来，有的是已经打印在纸上了面试官这时拿出来给你看说我们有这些数据。下一步就是计算profit，或者break-even。接着是各种变体，比如一个变量发生了变化，再算profit或者break-even。计算得出的数有的会问你这说明了什么，你觉得这个结果怎么样。基本就这样。

我面的两个case都是银行相关的。第一个是ATM的，第二个是要发行一个personalized credit card。
ATM的case：
先问你知道ATM吗，为什么要有ATM，ATM revenue来源（收取不是本银行的人的手续费）。有两类ATM，在银行内部的和外面的。给了一些数据要算一年profit，但是自己要想到问面试官非本银行客户的百分比。然后下一个问题关于银行外部的，要考虑哪些因素。好像也给了些数据算什么break-even，需要非银行客户的百分比达到多少，并解释你认为这个百分比能不能达到。。

personalized credit card：
发行一种可以personalized的credit card，问为什么要这样做，一个原因是希望客户多花钱。然后有一个market campaign，给了response rate，普通客户每个月balance，response并定制了的客户每个月balance，要计算平均客户的balance，也就是weighted average。然后又给数字算选择定制的客户定制之前的平均balance，得出要比所有平均客户高，所以我们要target本身消费就高的那些客户。然后又
给数字计算profit好像。如果我们不是免费定制，而是加上每张卡5块的手续费，需要多少response rate保持同等profit。

真是金鱼记忆，三天前面的现在case的细节已经记不太清了。总之其实就是给场景的数学应用题，认真听面试官在说什么，计算认真就好了。
我准备case用到的资料有，recruiter给的pdf了或者官网上也有的关于magazine的例子，capital one的一个专门为analyst面试的case讲解视频，caseinterview.com的视频看了一些对case有了入门的理解，书case in point看了几个例子（虽然和C1的case本质还是不太一样的），然后就是glassdoor所有这个职位的面经例子。

behavior的话基本都是glassdoor上说到的题目，我的是介绍一个accomplishment，一个帮助过别人的例子，一个失败的例子并学到什么。

“1和2都是同样4组数据：transaction master data, wire transfer master data,branch master data， 第四个忘记了，用不着
1. 是算destiny country是canada，固定时间的，所有transaction总和 （第一，第二组inner join一下，加上条件，算个sum）
2. 是算固定时间下，ATM only的branch，列出branch id和transcationamount （要去branch master data里去lookup一下，对应“ATM only”的编号）
3. 是input一组string，逗号相隔，数有多少个不同的string，大小写忽略，标点符号啥的不忽略
4. input一组数，逗号相隔，输出被3整除的factor的总和，比如输入（3，6，9），输出6“
引用自
“Capital One Data Analyst 做题汇报
http://www.1point3acres.com/bbs/thread-228891-1-1.html
(出处:一亩三分地论坛)“ 如侵歉删

总之不要把这题目想复杂，其实后面这俩用python写基本都是一句话的事，跑过了基本就完事了。结果一般只要1天，然后就安排下一轮
2. Data Challenge 这个还是很耗神的，因为我以前多用SAS，但是这个Challenge只能用Open Source，所以最后决定用python，所以只能边摸索pandas边做，一周一直在做在修改，大概花了超过20个小时，肯定算是比较慢的。Case就是airbnb和zillow，帮一个地产公司看看哪个邮编适合投资。整体思路其实非常简单，就是dataquality check，按标准的六个部分来，然后inner join，然后算一个index，可以用breakeven year也可以用return rate，我用的后者，然后出一个图。个人建议不要做非常复杂的prediction，data有啥你就说啥，不要想当然得对一些缺data的zip做估计，因为很可能出错，所以如果有这类想法就写到what’snext里，证明自己想到了只是没时间做。。，这一轮最关键的除了代码质量其实还有business sense, 问题尽量想得全面一点。个人建议写一个详细的Report，写明整个流程和自己想到的所有问题，然后并且在代码里写好comment让人容易看懂。我Report写了6页，感觉对这轮通过和后面的onsite帮助很大。我记得地里有人share过data本身，大家可以找一下在接单前提前练手。
3 Onsite 第二轮过了以后就会联络onsite面试了，我选了比较晚的一个日期，因为之前很忙所以还是没啥时间准备。我准备上基本分了behavior, case,data challenge这几部分来，搜集了一些题目，很建议大家好好理解官方那个准备材料和youtube上的视频，会有不少帮助。然后data challenge基本照着report做了个ppt。就出发去richmond了，头一天飞机晚点导致转机误机，改签以后到达酒店已经是半夜1点了，睡了5个小时就退房吃早点然后坐酒店shuttle去了面试地点。面试分三场每场1小时，我的顺序是case-data challenge-case，这个HR会提前通知。然后每一场会先问一个behavior question。
我的behavior question分别是一个近期犯过的错误，一个accomplishment, 一个在工作中帮助他人的例子，都是tellme when系列，回答时尽量按STAR原则答，说得有条理像讲故事就好了，一定不要编，说真事哪怕不精彩都没事，多讲点细节就行了，我附件给大家一个我搜集的问题。
第一场case是我最紧张的一场，因为case完全没见过！说好的就那几个case的呢。。所以其实感觉面的有点翻车，所以按印象把题目分享给大家，大概是说你负责帮别人收麦子，问你需要考虑什么，然后会给你一张表格，上面写着土地面积6400亩，一台联合收割机每月收6000亩租金15000，一辆卡车每月可运走5000亩的麦子租金5000，每亩产量200斤，每斤售价0.15，第一问问如果租了收割机和卡车各两台那么profit是多少，第二问如果土地面积在0-12800之间可变，收割机和卡车数量可变，那么最优组合是什么以及profit多少？我第一问一开始理解有问题想复杂了，好吧其实是他题目介绍的东西太多弄晕了，所以就算一步说一步，到后面时间紧张了，第二问时间很短没能给出一个最优组合，给出了几个次优的情况没列完。这里注意一下behavior还是要控制时间，我这次就是前面short talk 有点多导致了后面没了时间。个人感觉这场面的不理想。
第二场是data challenge，之前对这场比较紧张因为总感觉准备的不好而且怕他刁难，实际上却面的不错，可能是因为ppt比较详细吧，我们就并排坐在电脑前给他讲我的ppt，我也给了他一份纸质的report，我大概讲了半个小时。。。当然他有问题就在中间直接问我了，但是完全没有深抓不放，我讲完之后基本也就没时间再问问题了，算是策略成功哈哈。
第三场case面的最轻松，面试官似乎急于面完，虽然也写了很多东西但是流程很快，case是ATM的那个，算是有准备到，就是问怎么盈利，两类atm一类是银行里的一类是其他公共场合的比如酒店车站，哪些revenue哪些cost，然后说分两种客户本行和非本行，非本行的可以每笔收3刀transactionfee, 告诉了每笔的cost，和fix cost，问非本行用户达到多少比例可以breakeven，我具体数不记得了因为面的太快，但是记得他给了两种情况算出来第一次是33%第二次是50%，然后问我是不是make sense 我说是。然后给我一张纸让我对这个比例和某个其他变量（不记得了）画个图，我是设了个xy然后算了个y=f(x)出来，大概样子是y=a +b/x, a和b都大于0，是具体的俩数字，然后画在了图上也不是很精确，然后他问我这线会不会碰到xy轴我说不会。然后就完事了，整个第三场花了不到35分钟，导致我后面有大把的时间闲晃等待其他candidate一起吃饭。
面完感觉很忐忑，因为面试官会在旁边会议室直接讨论结果，但是不会公布，而我第一场又感觉表现一般，而第三场又太快都不太正常。然后到了回家后第二天一早HR发邮件说feedback不错，所以算是有着落了，不过目前还没有讨论分组和teamfit，所以还没有完全踏实下来，先分享一下但愿我接下来顺利吧.

我的面试从早上8点到中午12点   Case-Behavior-Case-Role play。 但每个人都不一样，最好提前发邮件问一下Recruiter.
每个环节长度在45分钟到1小时左右，如果有多余的时间你可以选择问面试官问题也可以休息。
下面具体介绍下每个环节：
. check 1point3acres for more.
Case1:
两个面试官，一个是负责面试的，另外一个负责记录。（这是个特殊情况，负责面试的那个人正在接受面试培训，负责记录的那个人会记录我的表现，也会在面试后对这个实习面试官进行培训。之后的三个面试都只有一个面试官）
每个环节之前面试官都会自我介绍，这时候个人建议可以和面试官搭搭话，放松心情。

提醒：一下都是中文翻译，具体专业词汇可以上网多看些Case。
第一题的背景是：有一家新银行要进入某个新的信用卡市场，问你会考虑哪些要素。
我答曰考虑成本和收益。之后具体分析信用卡有哪些成本和收益。
成本：管理成本，制作成本，贷款成本，推销成本和违约损失。
收益：交易提成和利息。
然后给了面试官给了我管理成本，贷款成本，制作成本，Average Balance和Default Rate,让我算Break Even的市场份额，实际面试的时候不会都给，比如有时不考虑推销成本和交易提成等。
但是我列给她式子说算市场份额，必须要市场总人数才能算。
然后她又加了一个市场总人数，于是我开始动笔+计算器算，算完给她结果。（注意如果你算得慢，记得一遍算一遍保持沟通，不要沉默太久）
接着她改了某个参数，让我再算一遍。（大多数题都是这样，让你加个条件减个条件重新算）
最后让我给她些建议。
我就扯了些减少成本，增加顾客数量，同时要注意应对竞争者之类的。
总结，第一个因为面试官不成熟，总体感觉有些不流畅。
. 1point3acres
Behavior:
面试官是个美国人，一进来就问我的名字怎么发音，然后又和他聊到糟糕的天气和刚开的樱花。（再重复一次，每个面试官都很好，不需要有压力）
接着是三个常见的问题：

1.让我描述我完成一项任务
2.让我描述我怎么劝说别人
3.让我描述怎么应对变化
这些问题你都可以在他发你的参考文件和接下来我会给的网址里找到

Case2:
还是关于信用卡的案例，不过这次无关关市场份额。只要算一下达到利益均衡的时候Default Rate最高能到多少。-baidu 1point3acres
最后一个问题我卡了很久，一直没反应过来。他问我做之前计算的基本假设是什么，答案是所有的Default都在一年年末的时候发生。越早发生的话收到的利息就越少，因为一旦Default，我们的客户就会减少。

Role Play:
Statistcian特有的一个环节。面试官会给你10张左右的SAS输出表格，是关于航班延误的预测模型。
参数有：温度，飞机类型，座位数，旅客数，地勤人数，登机口工作人员人数，星期几
需要预测的是：延误时间
报告里的模型用了温度，地勤人数，登记口工作人员人数，旅客数，星期几
Response=1 如果延误时间大于0，反之 Response=0
但是在资料里写着，旅客不会在意延迟时间在8分钟以内的延迟。所以这个模型是不好的。
还有一个correlation table和一些各个参数之间的点图。
面试官给你15分钟时间准备，然后回来让你做个report，她扮演客户，只有基本的统计知识。
我在这里犯了一个错误，因为我在网上看到过会面这个，也知道这个模型不好，所以在report阶段就说了这个模型不好，应该用logistic而且应该把0和1的限制设在8分钟。
但后来仔细想想，report的时候应该认真做report，模型的好坏应该时候再论。

大概的情况就是这样，下面是几个有用的链接：
http://www.mitbbs.com/article_t/Statistics/31303221.html
http://www.mitbbs.com/article_t/Statistics/31255909.html
http://www.mitbbs.com/bbsdoc3/life.faq/JobHunting/mianshiexp/C1/5
http://blog.sina.com.cn/s/blog_dc8631550101dxwo.html
http://alstonrussell.typepad.com/blog/2012/01/chase-to-cross-sell-credit-card-insurance-to-card-holders.html
还有一个电面的小帖子：
http://www.englishbbs.net/bbs/forum.php?mod=viewthread&tid=4794
-baidu 1point3acres
今天当天去面试的两个人一个拿到了offer，一个被拒，还有另外一个和我在等，已然希望渺茫。祝各位看官，也祝我自己之后的求职道路一切顺利。

第二轮今天刚面完，是个电话case interview，我同学之前也面过这个position不过是芝加哥office，然后我们面了同一个case，之前我有问过他面经，不过我觉得完全没有帮助，因为真的很多数字还有好几个0需要你算来算去，说实话还是有点confuse……

我面的这个是说有一个NGO在为当地一个after school program募捐，问你要怎么办。我吧啦吧啦说了我的想法，我之前面blackrock有面过一个类似的case，不过那个是说blackrock打算搞一个募捐活动，你打算怎么办，完全是strategy的东西，没有很多计算……于是我拿出了我原来和客户神侃的本事，我们可以搞一个关于zzzzz的活动，要增加revenue我们可以xxxxx，要减少cost我们可以yyyyyy，我自己说得太嗨然后被无情打断了说let‘s stop here……给了我两个方案，一个是办一个gala，场馆只能容纳100人，一个人能捐1000块，cost是100/人，租场馆要花20000块（好像）；还有一个是online mkt campaign，只能reach 1000
人，捐多少钱我忘了，有个一次性的fix cost，多少钱又忘了……这题还挺简单的……

然后问我怎么增加net income，我又开始吧啦吧啦，然后他让我dont go too far……就说假设我们只能邀请/reach那么多人了，你要怎么办，我说了点怎么增加revenue怎么save cost，不知道这位大哥怎么想……

后来他又说总共的这些人里，1000人里有800个是low budget，捐的钱少，给了他们大概会捐的钱和cost，问big donator需要多少人，两个方案哪个更profitable，这个地方还是挺confuse的，他一开始根本没说这1000个人是总人数还是什么，我算到一半觉得不对了，就问他，他说你别忘了800 out of 1000啊，我说你不是说了第一个只能容纳100人吗，那我可以就按80%吗。大哥说可以……说实话我觉得这个不是特别make sense，你这1000个人里有800个人是，不代表那100个人里就有80个人是啊……但是这位大哥都这样说了，我还能怎么办……. From 1point 3acres bbs

最后算出来了人均的，online的比较高，大哥问我选哪个，我说不能只看人均还要看我们总共能搞到多少钱啊……如果有一个的人群数量有很多增加的potential，哪怕人均低也有可能会选啊……大哥又说我go too far了……然后说你别多想就先选吧……我选了online因为total高……大哥就说了个alright也没说对不对……
. check 1point3acres for more.
终于面完了我觉得我面到最后声音都tm在颤抖，然后大哥说虽然我们面了这个case但其实在C1我们平时根本不做这些东西嘿嘿嘿。（那还面个JB啊气死我了）然后说他们平时要帮data scientist做model啥啥啥的……其实我还是挺会瞎BB model和我的project，结果一句话没让我说就做case了，连自我介绍都没，妈个鸡……

据说他家下一轮还是case，于是我就开始为他们担忧了，如果有人特别会逼逼case，但实际上model和data啥的什么也不懂可怎么办，C1长此以往岂不是要完……好吧我又go too far了。

我现在说实话也有几个final round在面着，在国内和美国case也面过好几次了，他家的case和一般consulting的case的style还是有很大不同的，我个人感觉，根本不怎么看我的framework和strategy，就是让我拿一堆乱七八糟的数字算算算……这轮面试让我隐隐有一种我和C1不会很match的感觉……我估计我也没达到大哥的expectation，他中间两次嫌我太能BB了……目测是要挂……

据说C1给回信很快，我一个朋友面了之后第二天就收拒信了，我可能就是明天了吧……C1确实不是我唯一的选择，虽然今天这轮让我有一种我和C1并不match的隐忧（别人要不要我还不一定），但我还真的挺喜欢这个position的，做得事情我也很感兴趣，open的几个location我都很喜欢，原来recruiter问有没有location的preference，我为了找到工作都说没有，可是C1这次才是真·没有，如果C1瞎掉要了我，我的原计划是再也不跳槽直接养老的，现在感觉非常遥不可及了……唉。

说了一堆有的没的……我投的这个position上面写的是Richmond，也是Richmond的recruiter找的我，然后是Texas的一个manager面的我，我今天问了一下也并不是哪里的manager面你就会让你去哪里。

希望这个面经能给我攒一丢丢人品吧……ball ball u了C1的这位大哥……有其他再想起来的我再在评论里补充。

地里和glassdoor的人都遇到过这个题，这个简单到我记不得具体数字了，计算量也很小，题目包括：
   Issue 一个 life insurance 要考虑哪些因素  premium, term, death rate, target customers, marketing and operation cost, competitor
   然后大概给了上面的revenue 和 cost， 5、6个数据的样子，计算一年和6个月的death rate to break even.
   给了 ABCD四个组的 death rate, 问应该issue给哪个group combination, 并以x-axle 为 groups (A,AB,ABC,ABCD) y-axle为profit绘折线图，注意slope 和 最后profit要落在0以下
   如果硬要issue给高death rate 的人，你有啥建议to make profit


二轮Tech 就是问NYC Taxi 的那个homework， 你觉得哪些你做的好，哪些做的不好，然后他引导你改善。然后让我白板写了个one hot encoder 的伪代码。我engineer出身，所以这个很容易。

三轮role play, 亘古不变的flight delay 的predictive model,我选的linear regression，地里有一个很早年的帖子，里面的内容挺全了, 说白了就是挑毛病给建议。只要你看得懂AdjustedR square, P value, VIF, Correlation就可以了。15~20分钟presentation根本不够时间把所有毛病罗列一遍，最夸张的是居然把linear regression 当logistic regression在用，简直人神共愤，无力吐槽。 

补充内容 (2018-5-3 12:42):
四轮 更复杂的一个case，此题数字略多一不小心算错三次。是一个mobile app of game 的题。包括：
   1. 什么因素衡量app是否值得发布, 跟上边的差不多，所有case都是revenue，cost，再扯点其他的就可以了

补充内容 (2018-5-3 12:45):
   2. 给了#users, download price, in -app purchase per user, Ad rev per user, cost..将近10行的数据吧，2组产品free 和 paid的，问哪个更盈利。这个就是revenue-cost的题啊，很简单吧，别着急，复杂的在后面

补充内容 (2018-5-3 12:50):
3. 如果要同时发布两个产品，会发生什么。 当然是用户flow到另外一个组而影响profit了
4. 如果同时发布，问多少user从paid APP flow 到free app才break even， 这个计算的假设是什么

补充内容 (2018-5-3 12:53):
5. 难题来了，现在就是三个组了，free, transfer to free from paid, stay in paid 这三个组。 先计算free组的 ad rev per user, 然后更新每个组的profit，然后重新计算上题的break even point

补充内容 (2018-5-3 12:56):
6. 根据你的计算，如果要创造最大的profit, 那你有什么建议。
这个题从第5题开始，LZ就蒙了，而且由于是video面试，增加了面官给我纠错的难度。虽然最后在面官的引导下回答出了正确答案，想想还是心慌慌的

补充内容 (2018-5-3 12:59):
最后一轮 behavior，四道题，很快就结束了。. check 1point3acres for more.

大家都说C1的interviewer很好，LZ在这里表示can't agree more. 


补充内容 (2018-5-4 07:19):
Final round, Job fit on phone call, 其实不是面试，就是聊聊哪个组合适。后来从recruiter 那里得到的反馈居然是lunch的时候那俩senior manager 对我很满意。。。纳尼，不都是你们俩一直在说么。。。

是要达到一个数，我记得是$60K，然后有X的user从paid app跑到free app， 所以最后的公式是 profitOfFreeApp * (#originalFreeAppUser + X) + profitOfPaidApp * (#originalPaidAppUser - X)  = $60K, 其他具体的数我就不记得了。

首先，互相自我介绍，我把自己目前工作的情况说一下，他说一下他们组目前正在做什么，讲的非常详细，我讲了大概两分钟，他讲了有七八分钟的样子，这期间我也问了几个问题，因为他们组做的几个东西我觉得还挺有趣的，就随便聊了下。
然后，马上进入case，没有任何废话，准备好纸笔，仔细听他说什么，如果漏听了或者没听清，一定记得再问一遍不要怕，我就是他讲完，虽然我听得很清楚，但是我还是重复了一遍他的case，这样就不会有信息错误。我的case是：预测我们现在的信用卡客户会不会关闭目前的账户，数据有多大也告诉我了，4Million。他一直在强调不要进入模型回答问题，说我的business sense。
1. 典型的binary classification, 给了我六个features，让我谈一下不进入模型的时候对这六个features的认识，然后我会对他们做什么？我用什么语言做？会用到哪些包？这些包具体做什么的？
2. 问我用什么模型处理这个问题，为什么选这个模型？（我选的LR）decison tree可以做么？为什么不用？
3. 如何处理missing values, outliers?
4. 数据量增大，4个billion，我该怎么做如何让我们的模型有效？
5. 模型已经建好了，如何看performance of model?
6. overfitting如何处理？（并非直接问的，而是结合实际，拐弯抹角问的）. check 1point3acres for more.
7. Confusion matrix & ROC curve(也不会直接问，会结合实际场景问，一定要做到非常熟悉这两个东西)
8. 大家都知道feature engineering是很重要的一步，有几个问题我觉得他是在问我这个，但是我回答完他还是说先不谈模型，你会怎么做？我就绕来绕去还是扯回到了feature engineering上来。
9. MapReduce是什么？对于Hadoop, Spark这些了解么？
以上问题基本是我能记得的，还有一些细节问题我就不太记得了，我基本回答完他都会说that makes sense, correct,这样的话，我想应该是肯定我的回答吧。在回答问题的时候我也基本没有间隔，他问什么我就几乎一到两秒的反应就开始回答了，其中有一个题我不太记得是什么了，脑子突然走神，硬是愣了有个五六秒，我一直在支支吾吾，最后不过还好也算回答了，这种情况我想有一个一两次可以接受吧，但是如果全称支支吾吾那就不好了。总共是一个小时，除了自我介绍，case这部分大概不到五十分钟样子，电话打的超过了一个小时（计划是一小时的）。

10. 这是一个重磅题，最后一道题！我觉得我答的不好，因为是一个完全open的题目：有两个客户都是5000的credit limit，但是一个100%用了这5000，另一个只用了2%，但是我们的模型给了他们同样的label，该怎么处理？（我回答的不好，因为一直在考虑模型有问题，也设身处地考虑了一下我自己如果有张信用卡不怎么用的话会不会关掉这个账户，把我能想到的都讲给他听了，他应该还是不太满意，说如果不考虑模型，我该怎么做？最后结束面试，我问了他一下这个事到底怎么回事，他的解释就是要考虑现实考虑每个人的具体情况，因为模型归类了这两个人属于同一类的情况并不会太多，是非常少数的情况，我们需要挨个去查看根据不同的需求，他说了一大堆，我能听的明白的大概就这个吧，还有一些别的，我不是太懂，这是唯一觉得回答的不太好的问题。最后我说我真的尽力了，他还说非常感谢你的诚实，哈哈。


分享一个capital one Data Scientist 的面试经验，回馈地里，已跪，也算造福后人吧。

一年多工作经历，去年12月在网上海投，到今年18年2月末挂在onsite，2个月的时间，经历四轮面试+onsite，职位地点在纽约，Data Scientist。

12月末海投大概一周后收到通知，第一轮与HR电话聊聊经历，之后第二轮收到一个 HackerRank online coding challenge，两个小时三道题，并不很难，不涉及复杂算法。又大概一周后收到技术电面通知，也就是第三轮，一上来先聊简历，之后对方假设了一个数据条件和场景，然后一步步往下问，从cleaning，feature engining，到 model selection， validation，同时也涉及大数据量的情况，问当数据量很大的时候怎么处理，用什么工具，问的比较细致，有的地方要大概描述代码怎么实现，电话持续一小时。这一轮之后大概几天，HR通知过了，进入第四轮，第四轮是一个 data challenge，边写code边写思路，一周的时间，题是关于NYC green Taxi，地里有人分享过原题，大概是需要建一个回归模型预测出租车小费比例，个人觉得重点在于如何观察数据，清理数据，feature engining，数据中有缺失值，异常值，之后也要选择模型，对比模型表现，最后写出结论和future work，challenge的最后是一道5选一的开放题，我是选了做visualization，用tableau做了一个interactive dashboard。这个challenge挺花时间，我用了大概四天，尽量把思路都写清楚，值得一提的是github上能找到一些前人做的，可以提供一些思路。这轮之后过了一周，HR通知过challenge过了，安排了两周后的onsite。

onsite是在2月下旬，纽约办公室，全天面试，早上8点半到，9点开始，一直到下午3点半，中间1小时吃饭休息，一共6轮，每轮1小时，轮与轮之间几乎没有休息，一直在一间小会议室里，有几轮是远程视频，面试官都是 Data Science director 或者 VP data science。六轮中2轮business case，2轮tech（有一轮叫hiring manager interview 但实际是tech），1轮role play，1轮behavioral。网上有business case interview 的介绍视频，不了解的同学可以看一下。从9点开始，第一轮business case，场景是超市发放private credit card，有一些上一年的历史数据，问题涉及计算 profit，revenue，cost，market share，计算 market share 的时候要先计算全城有多少信用卡，面试官不会一下子把数据都给你，你要想计算时需要什么数据，考虑多种情况，同时问面试官某些数据有没有，比如说计算全城有多少信用卡就需要全程人口总数，成年人比例，和人均信用卡持有数三个数据，这些都需要问面试官才会得到。另外最后会有开放性的讨论，就是计算出一些结果，问你根据这个结果要采取什么样的行动，这个就比较靠business sense，要讲出道理。这一轮9点到10点，然后10点喝口水就又开始下一轮，第二轮同样是business case，一位VP，情景是电话接线员，给一周每天的平均电话时间，电话数量，还有一个是转接率（一个接线员不能解决问题需要转接的情况），计算围绕每个电话的平均通话时间，转接电话数量等等，最后也是开放讨论，如何才能降低转接率，提高接线效率。之后11点开始role play，role play 是飞机delay经典问题，网上可以搜得到，我再具体讲一些，就是假设你是一个数据咨询公司的咨询师，面试官是你的客户，一位business manager，假设他不懂统计和模型，他给你提供另一个数据咨询公司做的分析，是大概10几页slide，里面有各种分析图表和一个预测模型，让你给他讲一下这个分析都做了什么，根据它提供一些解决delay的思路，同时评价一下这个分析做的好不好，不好的地方提出改进思路。给你15分钟自己看材料，然后25分钟给他讲。讲的时候我是把材料一页一页都过了一遍，以咨询师的角度，抓住几个重点，1是讲解材料内容解释数据图表和模型，数据中不合理的地方要指出（如异常值）；2是发现问题提出改进，分析做的不好的地方，没意义的图表，模型的缺陷等等，提出改进办法；3是要时刻为客户着想，通过手上的材料，客户可以采取哪些行动和尝试来减少delay。这一轮真是挺考基本功和交流能力的，看数据和图表要细心，要尽量考虑全面，比如可以增加哪些feature，如何提高模型。这一轮12点结束，之后开始第四轮behavioral，也是上午的最后一轮，主要问了如何团队合作，如何向他人学习，如何解决矛盾冲突，如何合理安排任务优先级，如何面对挑战等等。都是先问一个问题，你讲一个事例，然后他根据你讲的事例深挖不同的问题，我是一共讲了三个事例，每个事例都被问了三个问题的样子。

1点上午的面试结束，中午跟一个 senior data scientist 吃饭，相互聊了聊经历和公司环境。下午是两轮tech，第一轮2点开始，问了multinomial distribution，结合不同的模型谈这个分布的应用，然后白板写sampling from multinomial distribution，之后问了variance 和 bias， 解释和如何检测，最后聊了聊如何根据不同分布生成fake data。我是这一轮答的不好，其实挺基础，但我之前并不常用这个分布也没准备到，最后也就挂在了这一轮。后面最后一轮，面试官非常细致的问了我简历上的一个task，从数据到模型到结果，之后又问了前后端如何衔接（我简历上有提到但应该不是DS必备），模型如何应用到实际等等，本来还应该问data challenge，但面试官说我的challenege写的很清楚明了就不问了。至此，下午三点半多，结束整天的面试，HR送我出办公室。

最后谈一些感想和如何准备，首先onsite是所有轮都通过才算通过（我事后问了HR），所以每一轮都不要放松警惕，哪怕前5轮都很顺利，最后一轮也不能放松，因为就算5个面试官都很喜欢你，但有一个说你不行，你还是拿不到offer。保持一整天的清晰思路挺不容易，所以要做好准备。关于准备，business case方面网上挺多资料，视频和文字都有，多看几个，尤其C1家是做银行信用卡，这方便的知识术语应该提前了解一下，比如信用卡业务如何盈利，成本和收入都有哪些方面，business sense也是平时的积累。behavioral 也要准备几个case/story，网上有几个大类问题的例子（合作，冲突，挑战，失败，领导力等），可以参照着找自己类似的经历。剩下就是tech技术，coding，数据分析建模，统计，机器学习，这几方面的基本功，不一定考的很深，但知识的全面覆盖和应对是有一定难度。

基本也就这些，整体感觉DS找工作还是挺不容易，竞争激烈考察点宽泛，祝愿DS求职者可以拿到心仪公司的offer。C1家整体感觉挺不错，技术环境都不错，有近期面试的祝愿可以拿到offer。

1）OA 2 SQL 2 “algorithm”。 SQL就是基本的query，吧leetcode sql部分做一遍就行，算法加引号因为只需要把东西做出来就成，什么运行时间啥的都不用考虑，我的经验就是吧简单的题做会就行。一道我忘了，另一道是把text里所有单词以及出现次数找出来，用python str内置语句加dict就可以解决。

2） Data Challenge 这个我觉得是最难不好把握的一点，题目说大约一周时间，总共8个小时左右可以做完，但实际上如果你想做的好，最好花个15-6小时做。data quality方面，主要考虑uniqueness completeness consistency validity （细节可以google data quality一下，算是标准的东西，对于我这种一直在和data 打交道但不知道标准流程的人来说还是挺有用的。data quality最关键的是你要仔细考虑data 中出现的问题，以及如果这些问题没被处理会有啥后果（之后on-site会被问到）。接着是visualization，考官会为你为什么你用了line plot而不用bar，或者你有没有考虑过其他的visualiation。最后是business sense。我个人的建议是把 data challenge 做成 consulting project，仔细分析data，考虑 market segment， time seires pattern， competitor analysis。形成一个逻辑自洽的解释，并提出建议。建议方面我是按照consulting case 做的，直接上结论，接着写3条原因。

但基本上是interviewer led 的profitability 的case，找均衡点的。第一问都是问你busienss sense，比如需要考虑哪些方面等等。这部分我建议用case interview 的profitability framework，先说考虑revenue 和 cost， 然后里面再说的细一点，尽量做到MECE。第二问基本上都是math，分析均衡点。数学比较简单，但要心细。最重要的是尽量不要用short cut，要把interviewer 当傻逼，一点点地喂。我的做法是把问题分成一步步，每一步算一个变量。比如求profit，你先告诉interviewer我要用revenue-cost，然后告诉他我要算revenue，算完了再告诉他我要算cost，总之就是把每一步都解释清楚。不要自己在脑海里憋着算。如果你练习过management consulting 的case，capital one 的要求类似，但程度应该是没那么严格。毕竟面你的人不是consultant，对softskill的要求没那么高。一般第三问往后就是和你讨论各种alternative situation，比如把这个变量变成2倍会如何等等。有时候会让你画图。最后会让你出个receommendation，你就照着consulting 的标准就行了。附件里是我网上找的题，我觉得帮助挺大的，尤其是如何计算信用卡收入支出这块，很有帮助。
最后是behavior， 你找找glassdoor的例题就行，但要注意interviewer会问的比较深入，所以如果你编了一个例子，最好把细节想好。。。

基本是。我面的时候第一个case是分析银行推出一个新的服务，做了一个实验，分treatment group 和 control group， population 分两类人，根据给的数据分析出每类人消费变化。第二题是冰淇淋，关于找到最优数量的制冰机和搅拌机。影响因子有机器费用和客户需求cap等等。算是profit 问题的一个变体吧。根据我的体验，附件pdf的很有代表性，我觉得你把附件里的case研究透了，on-site的时候再心细些，就ok了。剩下的就是注意表达和交流，这些你可以看看consulting的case 材料。

这个其实就是adverse selection。你容易招人，节省费用，但找到人容易default，增加费用。这里有个tradeoff。 所以会有最优解，response rate 太低，找不到人。 response rate 太高，default 费用超出了收入，所以会有这个曲线。

关于第二个问题，我建议你case的时候最好和interview 确认一下，一般请款下，apr就是年化率，这时候如果balance是恒定的，就不用乘12，premium是月支出，所以乘12，当然你一定要喝面试官确认。

1. Case - ATM机profitability。有两种ATM, 一种银行内的，一种银行外的。cost有比如维修费新建设备费等，Revenue有interchange fee等，两种情况下分别算profit。数学部分很简单，但是千万别出错，而且一定要跟面试官保持良好的交流。也不要怕答错，就怕你不说话，如果答错面试官会给你合理的提示，你顺着他给的线索分析，当你看到他脸上微妙的围笑之后大概就能知道自己猜对了方向。
2. Behavioral - 三个问题。Biggest challenge， 怎样说服他人，还有一个不好意思实在想不起来了。。不过他们都是很标准的tell me a time系列，没有意外的题目
3. Case - 这个是我面试过程中最匪夷所思的一个了，完全get不到面试老头的点。。大概就是一个coding company，假设你是里面的一个manager，手下有三个人，有一个程序猿，一个测试的，一个负责document。告诉你他们的productivity，让你计算分析客户要在一周内产出2000行code可不可行，怎么样最优分配。这个计算几乎没怎么有，主要是business sense，也是我觉得最难的地方，勉强撑到最后。老头拿到我的笔记说了一句，that's highly organized。现在看来应该算是唯一的加分点吧。。惭愧
4. job fitting - present之前做的data challenge project，然后回答他们提出的问题，就跟他们表明你的思路就好了。

Here is one list of behavioral-based interview questions:
Describe a situation in which you were able to use persuasion to successfully convince someone to see things your way.
Describe a time when you were faced with a stressful situation that demonstrated your coping skills.
Give me a specific example of a time when you used good judgment and logic in solving a problem.
Give me an example of a time when you set a goal and were able to meet or achieve it.
Tell me about a time when you had to use your presentation skills to influence someone opinion.
Give me a specific example of a time when you had to conform to a policy with which you did not agree.
Please discuss an important written document you were required to complete.
Tell me about a time when you had to go above and beyond the call of duty in order to get a job done.
Tell me about a time when you had too many things to do and you were required to prioritize your tasks.
Give me an example of a time when you had to make a split second decision.
What is your typical way of dealing with conflict? Give me an example.
Tell me about a time you were able to successfully deal with another person even when that individual may not have personally liked you (or vice versa).
Tell me about a difficult decision you have made in the last year.
Give me an example of a time when something you tried to accomplish and failed.
Give me an example of when you showed initiative and took the lead.
Tell me about a recent situation in which you had to deal with a very upset customer or co-worker.
Give me an example of a time when you motivated others.
Tell me about a time when you delegated a project effectively.
Give me an example of a time when you used your fact-finding skills to solve a problem.
Tell me about a time when you missed an obvious solution to a problem.
Describe a time when you anticipated potential problems and developed preventive measures.
Tell me about a time when you were forced to make an unpopular decision.
Please tell me about a time you had to fire a friend.
Describe a time when you set your sights too high (or too low).

言归正传，onsite一共五轮，上午俩case，一个role play，一个behavioral。下午一个返场技术面聊你的data science challenge。

我的第一个case是关于pricing的，这也是我今天唯一的得意之作，和面试官互动的很不错，开放的问题都能够有来有回思想交锋。

至于具体的计算部分算是两个经典例子的合体吧，大家去翻翻未名空间，找找一个利率的case和一个phone vs email的case。具体来说我们有仨策略，发邮件请人办信用卡，但offer三种不同利率，那么会对应三种不同的respond rate，以及三个不同的客户average balance，请分别算利润。之后又说可能现在duration会不同，再分别算利润，然后default rate也会有所不同，又分别算利润。层层推进的时候会伴随着开放的问题引导你，这就看你的business sense了，能不能即使抓到他的思路。



相似的，我的另一个case是关于autoloan的，这回我在开放题部分就做的超级差，根本不造老哥想把我的思路引导去哪里。至于计算部分是这样，真。坏人的概率是3%，而我们的模型预测出总人口里面5%是“坏人”，其中，里面有15%是真。坏人，然后让你算了两个条件概率，反正活用贝叶斯公式，条件概率公式，全概率公式就能够顺利做出（据说算不出直接挂），事后我想到的最方便的办法其实是做个2*2列联表，然后把四个交叉概率算出来，然后要啥条件概率一步就有。因为这一关里面，面试官总是费了九牛二虎之力才把我引进下一个话题，估计我在他心里印象一定有个nerdy的标签吧，所以我觉得自己完成的很差。不过没关系，哥们上一关做的更差。

也就说在两个case之间，我完成了经典的role play问题，飞机晚点，具体问题大家可以去查一下未名空间，总之有个线性回归模型（也可以选决策树）来分析飞机为什么晚点，看完材料以后跟客户提建议，之后客户化身专业人士深入聊。我在内容处理上主要犯了俩大毛病，一是时间没安排好，15分钟里面刚刚看完材料，根本没时间总结，另外在展示上，我没有很好的区分给客户讲和给专业人士讲的分别，因为之前看了很多经验都是讲第二部分模型问题的，所以注意力全在挑毛病上面了，没能够先简要总结现有模型。另外展示还犯了三个毛病，互动交流不够，没给客户看ppt，老转笔（哥们这不是虚的么），这都是后来他们反馈我的，哎，引以为戒，下次做好吧。具体来说模型的问题在于，模型选择不当（应为分类器而非回归），数据清理，week of day处理不当，correlation严重，起降地没有被考虑，温度这个变量没啥用等。另外问了你r square 和adjusted r square是啥，p value，为什么r square低，共线性怎么处理等等。另外有一些现象出现的原因你要会和实际结合起来。总之这一轮结束我就觉得自己已经走远了其实，人生的大起大落就是这么快。

上午最后一波是behavioral，这个还好，之前给过你一个单子，照着准备就是，都是tell me a time系列的。对方明确表示要遵循star原则。建议大家还是要勤练，多练几遍不吃亏，我就是总想着准备几个案例到处套，其实现场表达的不太好。

吃完午饭逛了一圈以后，下午最后来了一轮tech，一据说教授出身的大boss跟我聊了我做的data science challenge，比我想象的好，就围绕着我用的模型描述比较了一番，因为这哥们好像就是负责发明和测试各种666的模型的。我在project里用的都是经典的随机森林，boosting和ANN，稍微聊了聊我对这些模型的理解和实际跑的效果就过去了，本来为了准备前一天还看了CNN，RNN，rule ensemble什么的，当时或许应该强行加一句，我觉得其实可以再试试xxx模型。另外
因为我提到了rspark包，所以他问我懂不懂spark，我就老实说，只在其他平台上调用过，spark具体结构和原理不太懂。另外最后我强行拉住他让他听我讲我在bonus部分做的傅立叶变换预测模型，想忽悠他一波，

听完后他一句请说说你的结果有哪些实际应用又把我噎回去了。总之这一轮也算我表现还行的一轮了，他当场说我对模型理解不错，不但会用还懂原理，认为我有做ds的素质（也不知是不是对谁都这么说），让我不管结果怎么样加他一下linkedin（这时候我感觉自己应该是没戏了），欢迎随时问他问题。

总之大致就是这样，面完以后很快推我的哥们（再次衷心感谢他一下）就告诉我role play挂了，表达问题很大，然后普遍认为我数学统计过硬，商业sense不够。结果也算在意料之中吧，起码组委会还讨论了一下我的去留，可能普遍觉得我硬功夫还行吧，最后没要我看来也是软实力短板实在太严重了。另外俩印哥哥直接挂在case上也是让我出乎意料，我还以为他们会输在表达，因为英语真的有够烂，结果表达不好的反而是我自己😂。。。按照内部人士说法，我起码让组委会审核了一波，所以也算小胜他们为国争光了（强行吹逼一波）。
. From 1point 3acres bbs
总之以上就是我的经验与大家分享，希望大家不要犯我的错误，既能算对题，也能讲明白case，软硬功夫两手抓。另外推荐一下youtube上一个教case interview的教程，好像叫MConsulting，适合哥们这样的商业分析小白。

虽然和幻想中的principal data scientist职位失之交臂有点可惜，不过想到郭德纲说的话，成事得靠三分能耐，六分运气，一分贵人扶持，如今虽有贵人扶持，无奈自己实力不济，也怪不得时乖运蹇。求职之路漫漫，大不了总结教训再战一波。雄关漫道真如铁，而今迈步从头越！

题目是有一个运动产品的零售商，来找你优化他们的在线广告竞拍系统，提高response rate。假设你有的数据是3, 000, 000用户的访问数据，每行数据有150多个column，已知overall的response rate是1/1000。
被问的问题有：
1. 选什么作为target？
Response or not
2. 选什么metrics?. 1point3acres
AUC-ROC
3. 怎么处理NA? 
It depends. If NA is meaningful, leave it there. If NA is missing due to data extracation, do some simple if-else condition/mean(median)/regression to fill
4. 怎么做feature engineering? . check 1point3acres for more.
Encode categorical varaible, use 'groupby' and 'mean/medium/std' to generate some features
4. 数据量特别大怎么办？
mapreduce，但是我没用过，就拿本地并行优化举了个例子，怎么分配数据给各个线程，然后怎么把数据收回来合并。
5. 模型用什么？
GBDT，lightGBM/XGB
6. 怎么评估模型表现？
k-fold CV
7. Overfitting/underfitting怎么办？
分别讨论了一下。想办法获取更多的数据，调整hyper-parameter。
8. 如果模型预测出了问题，会有什么影响？
分情况讨论了一下整体上会有什么变化，对单个用户有什么影响。

1.        你会选哪些feature？（感觉是随便说，只要有关系。追问如果是一堆transaction的日期之类的，应该怎样rebuild feature）
2.        怎么做data cleaning： 
    a.            怎样detect outlier？
    b.            怎样fill in missing data？(我说可以填constant比如mean，然后他追问填mean在什么情况下不合适、怎样更好)
    c.            如果target value也missing了怎么办
3.        你选什么model？(我说decision tree，然后他让我说有没有其他model，优缺点分别是什么，target是什么。target应该是一个binary的值whether the customer will close the account in one month，如果regression得到了0~1之间的值就代表how likely)
4.        怎么看model 的performance，用什么package
5.        如果data size很大有1TB，怎样sample，用什么package
6.        如果model不准确，会给银行造成什么损失？
7.        如果用model predict得到了一堆target的值，应该怎样根据target发rewards (我说画个distribution，给最可能关户的百分之几客户发rewards。追问除了这种方式还有什么方式，我也不确定是考modeling还是business sense). check 1point3acres for more.
8.        最后一个是地里看到的一模一样的open question，两人都有5000limit，但是一个用100%一个只用2%，这两人有没有可能都在一月之内关户。面试官应该看你第一反应是考虑model的问题还是考虑其他方面。

case interview 是关于life insurance的，之前地里有人提过。先问你对insurance了解有多少，如果你是manager，为了考虑到顾客死亡的概率 你会收集哪些顾客的信息。然后就是计算的部分了，很简单小学数学题。算达到break－even的死亡的概率是多少。然后面试官画了一个柱状图，有四个组，分别代表high risk low risk，median high 和 median low， 柱状图给出每组的死亡概率，然后有四种方案，1:全包括，2:只包括low risk，3:包括low 和median low 4:包括low, mdiean low 和 median high 问你会选哪个方案（假设每个组的人数一样）。如果想更赚钱你会怎么做。最后是opening question，如果你想去predict 死亡的概率 你会用什么方法，为什么。

role play 还是flight delay的题，地里已经讲的很详细了。这个大家要好好准备，15分钟看report时间还是有点紧的，要想好如何和一个non-statistian交流

behavior interview： 三个问题 每个问题都会根据你的回答有follow－up question。 1，challenge task  2，persuade someone. 3，deal with changing objectives in your project。

1. 简历问题，问的非常细致，我之前做过一个推荐系统，这个面试官对这一块非常擅长，所以问得很细很专业，我没答好，加上一开始的确听不懂。所以建议大家可以先linkedin面试官，看看他擅长什么，我遇到过几次面试官喜欢问自己擅长的东西。
2. 一个超市，有100个顾客的list，
70个男的，30个女的，如果用这个数据做数据分析会有什么statistical issues，问这个100个顾客会是什么样的distribution
3. walk through一个mapreduce问题，一组数据，四个columns: name, category, # of transactions in 2014, dollar values of transaction in 2014，需要知道每个category的average dollar values per transaction，怎么用mapreduce做，其实就specify一下mapper和reducer的input和output，然后在reducer里求一下平均值什么的。



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
