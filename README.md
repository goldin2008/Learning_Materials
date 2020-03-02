# Learning-Materials
Learning Materials for ML, DL, DS

# Udacity-Materials
```

12/19/2019
Data Streaming 2 months 02/19/2020
Cloud DevOps Developer 4 months 04/19/2020
Cloud Developer 4 months 04/19/2020
Data Scientist 4 months 04/19/2020
Data Engineer 5 months 05/19/2020

```

### ML Engineer Interview

我之前在另一个帖子里面分享了，ML design 面试的解题思路总结，大家反应很有用。最近又在实践中总结出来一套ML design答题模板，成功的过了几个大厂的ML design面试。因此分享给大家。
求加米，给我米不会减少你自己的米，举手之劳，互惠互利。

面试就是要在有限的时间里，尽量把自己懂的东西都让面试官看到。你懂那么多模型理论，怎么才能让面试官也觉得你很懂呢？要有策略，有重点。什么样的策略好用呢?
抓住核心，兼顾深度和广度。

ML design的核心，万变不离其宗，本质都是train一个model来实现某个task，比如prediction/ranking/classification。有经验的人都知道，实际上给定一个问题，好用/常用的solution基本上只有很少的几种。所以想要显得你懂很多，不仅要从深度上要cover这几种solution，更要从广度上显示你有end-to-end的experience。具体怎么实行呢？

Step 1：理清核心问题。
-        不是每个面试官都能用一目了然的方式提问。有的面试官水平差，自己也理不清问题的逻辑。遇到问题很模糊的时候，要尽快理清核心问题。抽象出来，可用信息/输入有哪些，要求的输出是什么样的，这是一个classification的问题，还是regression，还是relevance/matching/ranking？理清楚核心问题，就能判断需要train哪种类型的model，整个pipeline就很容易flow out了。

Step 2：理清核心问题后，请白板画图，最好是一个diagram。有前后逻辑关系的work flow最能展示你思维的广度。
-        在理清核心问题后，具体分析model之前，先把solution的大体框架在白板上画出来。目的是让整个讲解过程逻辑清晰。按照逻辑的先后关系，typical的解答逻辑包括这几大块：training/testing data, input representation, model, output, evaluation, optimization(parameter estimation). 我一般从model开始画，一个框框摆在中间，这是核心。然后画上游，下游。在这里，只要把框架搭好，告诉面试官，我要讲这些内容，面试官有个心理准备，就可以开始听你讲课了。

Step 3：讨论model。为什么我用“讨论”这个词？因为能seriously被考到design的人，都不是entry level。对于更senior的人来说，面试的最好氛围不是你问我答，而是我把我知道的都讲给你听，你看看还有什么想听的。所以你讲的过程中要和面试官互动。要看ta的反应，哪里皱眉了，哪里表情不轻松了，你就要停下来，问他Is there anywhere that you want me to talk more? 这给面试官一个机会表达自己，也帮助你更好的address面试官的考点。
-        Model方面，针对task 的类型，propose哪些model可用，把你能想到的都name出来。选择2-3个常用的，比较优劣，然后选择一个大家常用的。不同的model，输入输出可能不一样。所以决定了model，其他的component就很自然的浮现了。这一步，要在你的model框框里，把关键的component列出来，说明它们之间的关系。分析各个model的优劣，可能需要在旁边额外画出model的visualization，比如说到dnn，你就画几层multi perceptron layer，再顺便提一下SGD和ADAM。说到用logistic regression 做classification，你就顺手写一下log likelihood，显得你optimization也很懂。说到regularization，你就写写L1 norm和L2 norm。显示你的深度，主要就靠这一步。
有时候面试官会告诉你ta想用的model，你就按照ta的来，你也可以在讲解完几个model的优劣后，根据经验自己决定一个model。

Step 4：输入输出。
- 前面一步把model定下来。根据不同的model，解释一下input 和output的format。比如dnn就有one-hot encoding，这种最好用上embedding，顺便讲一下有什么好处。比如需要自己设计feature的，就重点讲一下有哪些常用的feature。

到此，这轮面试的核心你都cover住了，可以得到60分。Step 5和step 6 是能区别ML**和ML老手的部分。如果你做了，答的一般可以再拿20分，答的好可以再拿40分。有ML经验的人在这两个部分，一定要把握。

Step5：data。不讲data的ML design是没有灵魂的。
-从2个方面identify data：training + label,  testing + ground truth。1. propose可用的data 来源+data format。2. how to preprocess data -> make training data, how to build/create label, etc. 完成建模。根据具体的问题，data的solution可以非常creative。甚至Training data和testing有时候不一致。比如language model方面的问题：decide一个twitter post是什么语言？training 可能就用wikipedia，testing则可以收集user data或者platform-specific的data，这时候也需要指明testing如何get ground truth(testing label).


Step6：evaluation
- evaluation很容易讲，重点在metrics。主要有三个部分，一个是ROC/AUC curve。第二个是domain specific metrics，比如广告就有CTR。第三个是confusion matrix，重点是从它延申出来precision/recall/accuracy等等对你的solution重要的metrics。

最后再说几个加分项：
-        熟练的讲解参数估计，能显示solid的数学背景。讲估计参数可以用哪些optimization的方法(MSE, loglikelihood+GD, SGD-training data太大量, ADAM-sparse input)，比较优劣.
-        解答逻辑的每个部分，尤其是你熟悉的方面，要自己主动讲，因为每个部分都很重要。别问面试官想不想听你说，除非他明确制止你讲(如果面试官说不用讲，你就失去了一个展示自己的机会)。正确的做法是，lead conversation，一边白板画框图，一边告知面试官我要讲XXX这几个部分。整个design讲完了以后，再问面试官：Is there anywhere that you feel I missed?

求加米，等米看贴，给我米不会减少你自己的米，举手之劳，互惠互利!

The last but not the least: 每一步都尽快和面试官确认，move on，不耽误时间。想要在45分钟之内把面试官讲的心服口服，这么多个component，每个只有很少的时间。

我偏向于将evaluation metrics分为两类：general metrics (AUC-ROC, accuracy, precision, confusion matrix...)，以及domain-specific metrics (online CTR, offline CTR...)。


地里的面经很多，但是很少有人写总结，尤其是Machine learning这一块。我根据自己面试的经验，总结了一下ML design的面试中，解题的思路，抛砖引玉，分享给大家。


求加米，给我米不会减少你自己的米，举手之劳，互惠互利。

1. 结构化表达:

通过结构化的表达来让答案显得很有逻辑。结构化表达，针对一个问题，一般讲三点答案，逻辑上依次有递进的关系，这样就会显得你逻辑清楚。超过三点，听的人容易lost，所以也没必要。
比如被问了一个design的问题，答案比较复杂，有很多部分。回答的时候，第一句话先说，这个问题可以从2(数字)方面来考虑：用户和系统。用户这方面有2(数字)个solution，系统这方面有3(数字)个solution。因为面试官不知道你想讲什么，在讲细节之前，先把框架说出来，这样有助于面试官follow 你的逻辑，即使中间在细节上仔细询问你，他也知道你后面还有内容要讲，会配合让你讲完。

2. 讲自己做过的项目，怎么讲？
讲自己的项目时，主题最好和这个组的方向相关，技术越新越厉害，越好。出于NDA，最好避开自己在当前公司的工作。雷区：这样可能会导致只能讲好几年前的工作和技术。怎么解决呢？在报告的结尾，给一个rethink，讲两部分。
第一，        反思如果现在做同样的问题，哪些地方可以提高。[重点显示你的见识提高了，不是反思你的缺点]
分三个部分：新技术[比如以前用 logistic regression，现在可以用 deep learning/LSTM]，data size scale up[比如以前只有10k的data，现在是100M，可以使用更复杂的模型]，system[single pc -> distributed system/GPU，training could be paralleled or in the cloud. 更advanced approach to collect labels，比如大公司都会有自己的crowd sourcing judgment platform]。
第二，        概述一下，你在目前的职位做过的工作，使用了哪些最新的技术，这样显得你的skillset在与时俱进，没有过时。

3. -        It is your opportunity to shin!  你会被要求讲自己的经历，可能很多次，面试官根据你的经历来问问题。在讲经历的时候，突出哪些关键字和技术？一是和对方相关，二是新技术，三是显得你水平高的内容。当然一定要是你熟悉的，如果你被问到什么，答不上来，会特别减分。

4. -        讲到使用哪个model的时候，列举2-3个相关的model，答案的重点是讲一下各自的优缺点，以及当前问题的特质，基于这些比较，从而决定选哪一个。
以下内容需要积分高于 100 您已经可以浏览

5. -        Lead conversation，主动推进谈话。比如讲完一段话或者回答了一个问题，主动询问：Does it make sense to you？比如讲一个复杂的系统之前，先告知对方：I’m going to talk about a few components. If you feel interested in some particular ones, you can point out and we’ll discuss more over them.

6. -        会沟通。有些问题问的非常模糊，可能是面试官故意的，也可能是面试官的表达能力差。这种时候，通过rephrase问题 + make concrete example，来主动probe面试官，去除面试官自己的误差，clarify需求。

7.-        会接话，能听出面试官的concern，不要等面试官停下来就接过话题，address面试官的concern。有的面试官在交谈中，不是每个问题都会explicitly的问，然后停下来，然后等你答。你要能在交谈中，听出弦外之音的问题，立刻想答案，然后看准时机，当机立断的接过面试官的话题，给出让人满意的答案。

8. -        Stress test。碰到面试官很不友善的时候，没法develop一个很好的答案，要坚持the principle of problem solving: Break down problem to solvable subtasks. 比如被问到这个问题“你deliver了一个ML的产品/系统，用户使用以后，汇报系统的accuracy 远低于你自己test 的accuracy，哪些方面可能出问题了？要求不能看log。” 从problem solving的角度来看，整个系统有两个element：你的ML系统，用户的application。每个element都可能出问题。那么把大问题break down成两个element自己的问题+element之间衔接的问题，就是一个很好的答案。两个element自己的问题包括：产品的问题(overfitting，training data coverage，etc)，用户的application的问题(使用产品的domain和develop 产品的domain不一致， 使用方数据的distribution和training data不一致，etc)，用户的问题(没有按照设计的方式来使用系统，measure的方法不对，使用了和开发方不一样的metrics，etc)。

### Spark

Lazy Evaluation - Key Points
Lazy evaluation means an expression is not evaluated until a certain condition is met. In Spark, this is when an action triggers the DAG. Transformations are lazy and do not execute immediately. Spark adds them to a DAG of computation, and only when the driver requests some data (with an action function) does this DAG actually get executed.

These are some advantages of lazy evaluation:

Users can organize their Apache Spark program into smaller operations. It reduces the number of passes on data by grouping operations.
Saves resources by not executing every step. It saves the network trips between driver and cluster. This also saves time.

Explain in detail how lazy evaluation is advantageous in Spark. What are some use cases that you can think of to take best advantage of lazy evaluation in Spark?

When you know your Spark job has many actions. This means that your Spark job will already have tons of network and machine shuffles due to existing action functions and this will materialize your intermediate datasets every time you execute action functions. Evidently, this will spike your GC (garbage collection) cost. In this case, you want to minimize network and machine shuffles using as much transformation functions as possible to reduce network and machine shuffles.
Let’s say you have two tables - one table has the information about the 50 states in the US, like state in two letters (NY, CA, ..) and all the state’s zip codes, and the other table has all the residents in the US, with a column of which zip code they live in. Say you want to join two tables, and query only the people in California. In SQL, you would have to join them together, and then filter on “state = ‘CA’”. But in Spark, having lazy evaluation helps - since that one table is relatively small, Spark can switch the order of operations so that the smaller subset of dataframes is filtered first and then joined.



### Data Engineer

高强度专业培训第一阶段：Big Data Infrastructure强化训练
第一阶段目标：搭建一个实时的数据分析平台。

第一个月将会从最基础的大数据框架出发，分析它们的优势劣势，学习当前业界最火的系统架构，并将其应用到我们的项目当中，从而构建出一个高性能的实时数据分析平台。同学们将使用AWS，搭建起属于自己的云服务并使用Docker技术，简单快速拥有属于自己大数据平台。从数据采集，到利用NoSql数据库数据存储(Cassandra)，到数据传输(Kafka)，再到数据分析(Spark)和最终的数据展示(Nodejs)。学员将经历一个完整的高性能数据pipeline的搭建。同时也将使用(Zookeeper)以保证平台的高可用性和(Redis)以达到工作压力的合理分配。在这一个月中对于每一个技术，我们都将深究其内部原理，做到知其然，还知其所以然，而不是简单的利用API的调用。

高强度专业培训--第一阶段 Big Data Infrastructure强化训练
     第一阶段目标：搭建一个实时的数据分析平台。

     第一个月将会从最基础的大数据框架出发，分析它们的优势劣势，学习当前业界最火的系统架构，并将其应用到我们的项目当中，从而构建出一个高性能的实时数据分析平台。同学们将使用AWS，搭建起属于自己的云服务并使用Docker技术，简单快速拥有属于自己大数据平台。从数据采集，到利用NoSql数据库数据存储(Cassandra)，到数据传输(Kafka)，再到数据分析(Spark)和最终的数据展示(nodejs)。学员将经历一个完整的高性能数据pipeline的搭建。同时也将使用(Zookeeper)以保证平台的高可用性和(Redis)以达到工作压力的合理分配。在这一个月中对于每一个技术，我们都将深究其内部原理，做到知其然，还知其所以然，而不是简单的利用API的调用。



课程具体安排如下：

     第一周

          1. 学习和了解大数据开源技术

          2. 了解大数据内涵及分布式系统

          3. 了解Apache Zookeeper，Docker

          4. 理解AWS的基本原理

          5. 在命令行中使用Apache Zookeeper，Kafka

          6. 用kafka实现data ingestion layer

   

     第二周 

          1. 了解NoSQL，Apache HBase，Apache Cassandra技术

          2. 进一步学习AWS的使用

          3. 在命令行中使用HBase，Cassandra

          4. 用Cassandra实现data storage layer

          5. 在AWS上部署Zookeeper，Kafka，Cassandra

     

     第三周 

          1. 理解Big Data Computing技术的起源

          2. 学习并了解Apache Spark

          3. 在命令行中使用Spark

          4. 用Spark Streaming library和Spark运行data computation layer

     

     第四周 

          1. 学习并理解Node.js及Apache Mesos (内部原理)

          2. 了解single vs multi threads的区别

          3. 了解Sync io vs async io的区别

          4. 在命令行使用Redis，Node.js

          5. 使用Redis，Node.js运行data visualization layer

          6. 在AWS上部署Mesos，Spark
          
          
高强度专业培训第二阶段：Apache开源项目强化训练
第二阶段目标：熟练掌握基于Hadoop的数据分析，Hadoop的基本Use Case和Pig/Hive的编程，有真实大数据系统的实战经验，同时还将具备开源软件的开发能力。

第二个月我们将着重训练同学们对Apache系列软件的应用及开发能力。我们将从Hadoop生态系统的主要项目介绍开始，先从熟悉DFS、MapReduce、Tez, Zookeeper、Pig、Hive、Oozie, Sqoop、Flume、HBase、Phoenix、Ambari、Nutch、Zeppelin等工具的理解及应用开始逐渐建立对Hadoop的更深层理解，能清楚理解Hadoop能解决什么问题，ETL的基本操作以及如何用Pig实现ETL，如何用Hive做数据分析，在此之上更希望同学能主动思考，提出对软件的自我理解，成为Apache的Contributor。

高强度专业培训--第二阶段 Apache开源项目强化训练
     第二阶段目标：熟练掌握基于Hadoop的数据分析，Hadoop的基本Use Case，Pig/Hive的编程，有真实大数据系统的实战经验，同时还将具备开源软件的开发能力。

     第二个月我们将着重训练同学们对Apache系列软件的应用及开发能力。我们将从Hadoop生态系统的主要项目介绍开始，先从熟悉DFS, MapReduce, Tez, Zookeeper, Pig, Hive, Oozie, Sqoop, Flume, HBase, Phoenix, Ambari, Nutch, Zeppelin等工具的理解及应用开始逐渐建立对Hadoop的更深层理解，能清楚理解Hadoop能解决什么问题，ETL的基本操作以及如何用Pig实现ETL，如何用Hive做数据分析，在此之上更希望同学能主动思考，提出对软件的自我理解，成为Apache的Contributor。



课程具体安排如下：

     第一周

          1. 什么是Hadoop？

          2. Hadoop的历史 

          3. Hadoop主要Use Case

          4. Hadoop Ecosystem主要项目介绍

          5. 实例: 用Hadoop实现网络爬虫

     第二周

          1. Pig简介

          2. Pig数据类型

          3. Pig的基本操作: group, join, order, distinct

          4. 如何编写Pig UDF

          5. Pig程序调试优化

          6. Pig ETL实例

     第三周

          1. Hive简介

          2. Hive SQL详解

          3. 如何编写Hive UDF

          4. Hive程序调试优化

          5. 用Hive做数据分析实例

     第四周

          1. Apache Software Foundation介绍

          2. Apache项目开发工具和流程: Jira, git/svn, maven/ant, eclipse

          3. 如何成为Apache contributor 

          4. 实例：如何搜索Apache代码，发现问题，解决问题，提交Apache代码
          
第三阶段：企业级Capstone项目
在经历两个月高强度学习与实战之后，每位学员将被分配相应的项目目标并在老师的指导下完成。两位主讲老师将以Manager的身份监督引导学员完成各自项目。



项目设计的例子涉及：

Cloudacl公司数据挖掘与分析系统

开放数据挖掘与分析系统

Apache Pig和Apache Hive开源项目Contribution

  Alluxio 开源项目Contribution



*Capstone 项目方向会实时更新，欢迎大家及时查看课程主页。

成为Apache开源项目Contributor
在Apache多个开源项目的Committer的Daniel老师带领下，你将更加深入，细致的了解诸多Apache开源项目的原理，开发及其应用。同学们更可以通过Apache开源项目强化训练中完成的项目，提交自己的代码，成为Apache开源项目的Contributor。

公司实习-Capstone项目
      在经历两个月高强度学习与实战之后，每位学员将被分配相应的项目目标并在老师的指导下完成。两位主讲老师将以Manager的身份监督引导学员完成各自项目。并可以将完成项目作为实习经历写进自己的简历。项目设计的例子涉及：



基本的统计信息，报表

异常分析，某一天的数据量异常，如果寻找原因

建立数据仓库，用可视化工具进行数据探索

数据挖掘

Fix开源系统的Bug

打造最强简历
     * 完成第一个月的学习及项目之后，你可以将Design a Big Data Stock Platform写进简历中。

     * 完成第二个月的学习及项目之后，你将在拥有新的项目之后同时成为Apache的Contributor。

     * 完成第三个月的Capstone项目之后，你将拥有资格将本次经历写成为实习经历，放进简历中。课程最后部分项目设计，学员将被分成不同的Track，参考项目题目有：



基本的统计信息，报表

异常分析，某一天的数据量异常，如果寻找原因

建立数据仓库，用可视化工具进行数据探索

数据挖掘

Fix开源系统的Bug

      本课程的项目将会使用真实的大数据，不是Demo，让学生真实体验实际运营的系统。通过这个课程，大多数同学可以成为Apache Contributor。
      
      
背景介绍+项目展示+开发环境配置+Apache Kafka+Apache Cassandra
介绍Big Data的背景，生态圈及相关的开源项目和技术:

- Data Storage: Apache HBase, Apache Cassandra, etc
- Data Transportation: Apache Kafka, RabbitMQ, NSQ, ZeroMQ, etc
- Data Processing: Apache Hadoop, Apache Spark, etc
- Resource Management: Apache Mesos, Kubernetes, etc
- Container: Docker, Docker Machine, Docker Swarm, etc

Big Data Platform项目展示:

- 目标功能
- 介绍应用的技术栈
- 介绍技术选型原则及技巧

开发环境配置:

- Docker + Docker Machine

Apache Kafka:

- Apache Kafka介绍
- Apache Kafka内部实现细节

Apache Cassandra:

- Apache Cassandra介绍
- Apache Cassandra内部实现细节

Redis+NodeJS+Apache Spark+ Apache Mesos+系统部署+系统运维
Redis

- Redis介绍
- Redis内部实现细节

NodeJS

- NodeJS介绍及相关框架

Apache Spark

- Apache Spark介绍
- Apache Spark内部实现细节

Apache Mesos

- Apache Mesos介绍
- Apache Mesos内部实现细节
- Apache Mesos相关框架

系统部署

- AWS + Terraform + Chef/Puppet/Ansible/Salt

系统运维

- 系统运维相关工具介绍
