# URL

cookie: "JSESSIONID=7D49C38B81671E20503FC2B4DEDDCAF5"

## 获取图片

image: "http://cc.cqupt.edu.cn/upload/PIC/"+"imageID.jpg"

## 获取PDF

getPDF: "http://cc.cqupt.edu.cn/CquptCourseCenter/pages/classInfShow/docs/CourseCenterAttachment/"

param: fileName

## 获取默认课程

getMoRenKc="http://cc.cqupt.edu.cn/getMoRenKc"

param: "&unifyCode=1&page=1&count=12"

- page: 页数
- count: 数量

返回值：JSON

```json
{
	"data": {
		"total": 13,
		"courseList": [{
			"tpurl": "2017082521023292.png",
			"DQZT": "已上线",
			"kcbh": "A1050080",
			"kcjs": "...",
			"kkxymc": "外国语学院",
			"xs": "32.00",
			"kcmc": "高级口语",
			"xf": "2.00",
			"jysmc": "大学英语教研二部",
			"major": ["通信与信息工程学院-通信工程", "通信与信息工程学院-电子信息工程"]
		}, {},...,{}],
		"totalPages": 2
	},
	"meta": {
		"result": 100,
		"msg": "success"
	}
}
```

## 获取所有交叉通识课

getAllJctsk="http://cc.cqupt.edu.cn/getAllJctsk"

param: "&unifyCode=1&page=1&count=12"

return:

```json
{
	"data": {
		"total": 315,
		"courseList": [{
			"tpurl": "default.png",
			"kcbh": "070250",
			"kcpf": "5",
			"kcjs": "《老》《庄》与道家思想，是面向全校学生开设的一门人文社科类任选课。本课程力图在对《老子》《庄子》原文理解的基础上，引导学生进一步深入理解老庄道家哲学体系，并帮助那些认可和接受道家思想的学生用道家智慧指导人生。我们的人生总是会遇到这样那样的问题。在面对人生的问题的时候，每个人会有不同的态度和方法。比如信仰是一种方法，修养是一种方法，运用哲学的智慧也是一种方法。每个人都有选择信仰的自由以及修养方法的权利，也可以按照自己的喜好接受某一种哲学智慧。老庄道家思想既是一种哲学智慧又是一种修养方法。了解和解读道家思想，或许它就是你需要寻找的一种哲学智慧和修养方法。由于老庄道家思想恢宏博大，且历代方家解读版本甚多，皆通于道又不是道。故若执着于某一解读，作为“标准”教材，皆既合适又不合适。故本课以《老子》《庄子》原著为蓝本，辅以历代评注作为授课导读，师生共同探讨体悟。本课程16学时，以串讲形式学习老庄内容。",
			"kkxymc": "创新创业教育学院/继续教育学院",
			"xs": "16.00",
			"kcmc": "《老》《庄》与道家思想",
			"xf": "1.00",
			"jysmc": "素质教育教学研究部"
		}, ..., {
			"tpurl": "default.png",
			"kcbh": "A100003J",
			"kcpf": "5",
			"kcjs": "...",
			"kkxymc": "理学院",
			"xs": "8.00",
			"kcmc": "新生研讨课/专业概论",
			"xf": "0.50",
			"jysmc": "理学院"
		}],
		"totalPages": 27
	},
	"meta": {
		"result": 100,
		"msg": "success"
	}
}
```



## 根据专业号获取所有课程

getAllKcVyZyh="http://cc.cqupt.edu.cn/getAllKcByZyh"

param："&unifyCode=1&zyh=0101&count=12&page=3"

- unifyCode
- zyh: 专业号
- count: 数量
- page: 页数

返回值：JSON

```json
{
	"data": {
		"total": 77,
		"courseList": [{
			"tpurl": "2017071514550129.jpg",
			"DQZT": "已上线",
			"kcbh": "A1050140",
			"kcpf": "5",
			"kcjs": "...",
			"kkxymc": "外国语学院",
			"xs": "32.00",
			"kcmc": "商务交际英语",
			"xf": "2.00",
			"jysmc": "大学英语教研二部",
			"major": ["通信与信息工程学院-通信工程", "通信与信息工程学院-电子信息工程"]
		},{},...,{}],
		"totalPages": 7
	},
	"meta": {
		"result": 100,
		"msg": "success"
	}
}
```

## 获取开课单位学院专业

getAllKkdwZyXy="http://cc.cqupt.edu.cn/getAllKkdwZyXy"

parm: "&unifyCode=1"

返回值：JSON

``` json
{
	"data": {
		"teachingOfficeList": [{
			"kkxyh": "01",
			"kkxymc": "通信与信息工程学院",
			"jysh": "0100",
			"jysmc": "通信学院"
		},{},...,{}],
		"majorList": [{
			"xyh": "01",
			"zyh": "0101",
			"xymc": "通信与信息工程学院",
			"zymc": "通信工程"
		},{},...,{}]
	},
	"meta": {
		"result": 100,
		"msg": "success"
	}
}
```

## 获取课程详情页

### 课程状态

getCourseStatus="http://cc.cqupt.edu.cn/getCourseStatus"

param: "&courseNo=A1040040&unifyCode=1"

返回值：

```json
{
	"data": {
		"status": "已上线",
		"kclx": "1",
		"courseName": "C语言程序设计"
	},
	"meta": {
		"result": 100,
		"msg": "success"
	}
}
```

------------------------------------------------------------------------------------

### 课程信息

getMenu="http://cc.cqupt.edu.cn/getMenu"

param: "&unifyCode=1&module=2"

return:

```json
{
	"data": [{
		"cdmc": "课程首页",
		"cdurl": "",
		"ID": 201,
		"cdxh": 1
	}, ..., {
		"cdmc": "话题讨论",
		"cdurl": "",
		"ID": 287,
		"cdxh": 11
	}],
	"meta": {
		"result": 100,
		"msg": "success"
	}
}
```

----------------------------------------------------------------------------------

### 课程适合专业

getCourseMajor="http://cc.cqupt.edu.cn/getCourseMajor"

param: "courseNo=A1040040&unifyCode=1"

return:

```json
{
	"data": [{
		"xyh": "01",
		"zy": [{
			"zyh": "0101",
			"zymc": "通信工程"
		}, {
			"zyh": "0102",
			"zymc": "电子信息工程"
		}, {
			"zyh": "0104",
			"zymc": "信息工程"
		}, {
			"zyh": "0105",
			"zymc": "广播电视工程"
		}, {
			"zyh": "0106",
			"zymc": "数字媒体技术"
		}, {
			"zyh": "0190",
			"zymc": "通信工程专业卓越工程师班"
		}, {
			"zyh": "0191",
			"zymc": "通信学院IT精英班"
		}, {
			"zyh": "L011",
			"zymc": "通信工程(留学生)"
		}, {
			"zyh": "L012",
			"zymc": "电子信息工程(留学生)"
		}],
		"xymc": "通信与信息工程学院"
	},...,{}],
	"meta": {
		"result": 100,
		"msg": "success"
	}
}
```



------------------------------------------------------------------------------------------

### 课程主页信息

getCourseHomePageMsg="http://cc.cqupt.edu.cn/getCourseHomePageMsg"

param: "kcbh=A1040040&unifyCode=1"

返回值：JSON-

```json
{
	"data": {
		"courseBaseMsg": [{
			"tpurl": "2017070619434694.png",
			"kcbh": "A1040040",
			"kcpf": "5",
			"kclx": "1",
			"kcjs": "...",
			"kcmc": "C语言程序设计"
		}],
		"semesterCourse": [{
			"xm": "李红娟",
			"jxb": "A00191A1040040007",
			"jxblx": "必修"
		}, {},...,{}}],
		"teacherMsg": [{
			"dz": "",
			"xm": "聂永萍",
			"xymc": "计算机学院/人工智能学院",
			"jslx": "任课教师"
		}, {},...,{}],
		"courseIntrodeceList": [{
			"kcbh": "A1040040",
			"xs": "48.00",
			"applyMajor": ["通信与信息工程学院-通信工程", "通信与信息工程学院-电子信息工程"],
			"xf": "3.00"
		}]
	},
	"meta": {
		"result": 100,
		"msg": "success"
	}
}
```

### 教学大纲：

http://cc.cqupt.edu.cn/queryJXDG

param: "&unifyCode=1&courseNo=A1040040&place=2"

```json
{
	"data": {
		"fileName": "2019121208535728.pdf",
		"ableDownload": "2",
		"originName": "0A1040040教学大纲-20191212-最新修订.pdf"
	},
	"meta": {
		"result": 100,
		"msg": "success"
	}
}
```



--------------------------------------------------------------------------------

### 考试大纲 知识点体系 导学方案

http://cc.cqupt.edu.cn/queryAttachment

考试大纲："&unifyCode=1&courseNo=A1040040&type=1&place=2"

知识点体系："&unifyCode=1&courseNo=A1040040&type=5&place=2"

导学方案："&unifyCode=1&courseNo=A1040040&type=2&place=2"

```json
{
	"data": {
		"list": [{
			"fileName": "2018110618365056.pdf",
			"ableDownload": "2",
			"originName": "A1040040《C语言程序设计》课程考试大纲.pdf"
		}]
	},
	"meta": {
		"result": 100,
		"msg": "success"
	}
}
```



----------------------------------------------------

### 教学团队

http://cc.cqupt.edu.cn/getTeachingTeamPageMsg

param: "unifyCode=1&kcbh=A1040040"

return:

```json
{
	"data": {
		"member": [{
			"zw": "",	//职位
			"dz": "",	//教师主页
			"xm": "聂永萍",
			"xymc": "计算机学院/人工智能学院",
			"jslx": "任课教师"
		}, }],
		"tdjs": ""
	},
	"meta": {
		"result": 100,
		"msg": "success"
	}
}
```

