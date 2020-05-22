# 爬取学校课程中心

结合爬取大学mooc的仓库，作用于数据库比赛

1. **getJXDG：教学大纲、导学方案、考试大纲、知识点体系（需要vpn，爬取pdf后再上传oss返回地址）**
2. **getCourseMajor：获得课程适合的专业**
3. **getCourseHomePageMsg：获取teacher表，老师与课程之间的关系**
4. **getAlljactsk：获得交叉通识课程**
5. **getAllKcVyZyh/getMoRenKc：获取默认课程，及所有正常课程**
6. **getTeachingTeamPage：获取教学团队**
7. **test02：抓取学校专业及学院，根据教务在线上的构建college与major表。这是学院表**
8. **test03：这是抓取学校专业及学院，根据教务在线上的构建college与major表。这是专业表**
9. **biaobaiqiang：抓取表白墙相册失物招领信息**
10. **biaobaiqiang2：将信息写入文件**

#### zy:专业

![image-20200522212238471](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522212238471.png)

#### xy:学院

![image-20200522212259682](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522212259682.png)

#### teacher:老师及所属学院

![image-20200522212521728](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522212521728.png)

#### tc_kc:教师与课程对应关系及职责

![image-20200522212623891](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522212623891.png)

#### moren_kc:默认课程

![image-20200522212724875](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522212724875.png)

#### ksdg:考试大纲

![image-20200522212753598](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522212753598.png)

#### jxdg:教学大纲

![image-20200522212805313](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522212805313.png)

#### dxfa:导学方案

![image-20200522212826158](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522212826158.png)

#### course_major:课程适用于na xie哪些学校哪些专业

![image-20200522212851738](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522212851738.png)

#### all_jctsk:交叉通识课程

![image-20200522213110817](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522213110817.png)

#### resource:资源列表

![image-20200522213153111](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522213153111.png)

#### pdf:pdf列表

![image-20200522214525536](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522214525536.png)

#### biaobaiqiang:用于统计以往每天失物招领数量,作为调研的一部分

![image-20200522213405369](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522213405369.png)

![image-20200522214010709](https://cdn.jsdelivr.net/gh/1392517138/imgRepository@master/image-20200522214010709.png)