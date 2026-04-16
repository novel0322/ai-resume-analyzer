您好，这是我完成的「AI赋能的智能简历分析系统」笔试题提交内容。

1. GitHub 仓库地址：
   https://github.com/novel0322/ai-resume-analyzer

2. 前端演示地址：
   https://novel0322.github.io/ai-resume-analyzer/

3. 说明：
   本项目已完成前后端开发。前端已部署至 GitHub Pages，可公开访问。后端已完成本地运行、PDF 解析、关键信息提取、岗位匹配与评分等功能。由于部分免费云平台存在绑卡验证、额度限制或服务资源限制，本次提交以后端本地运行方式作为补充验收方案，完整运行步骤已写入 README.md 中。

感谢查阅。

# AI赋能的智能简历分析系统

## 一、项目简介
本项目是一个基于 **FastAPI + Vue3** 开发的智能简历分析系统，支持上传 PDF 简历文件，自动解析简历文本，提取候选人关键信息，并结合岗位描述进行关键词匹配与评分，帮助招聘者快速完成初步筛选。

项目包含前后端两个部分：
- 前端：Vue3 + Vite，实现简历上传、岗位描述输入、结果展示
- 后端：FastAPI，实现 PDF 解析、信息提取、岗位匹配、结果返回

---

## 二、项目功能

### 1. 简历上传与解析
- 支持上传单个 PDF 简历
- 支持解析多页 PDF
- 对提取出的文本进行清洗处理

### 2. 关键信息提取
从简历中提取以下信息：
- 姓名
- 电话
- 邮箱
- 地址
- 学历
- 工作年限
- 项目经历
- 求职意向
- 期望薪资

### 3. 岗位匹配与评分
- 接收岗位需求描述
- 提取岗位关键词
- 与简历技能和项目内容进行匹配
- 返回匹配分数、命中关键词、缺失关键词和分析结论

### 4. 结果返回与缓存
- 以 JSON 结构化返回解析结果
- 使用内存缓存机制，避免同一份简历重复解析

### 5. 前端页面
- 提供简洁可用的交互页面
- 支持上传 PDF、输入岗位描述、展示分析结果

---

## 三、项目技术栈

### 前端
- Vue 3
- Vite
- Axios
- CSS3

### 后端
- Python 3
- FastAPI
- Uvicorn
- PyMuPDF
- python-multipart

---

## 四、项目结构

```bash
ai-resume-analyzer
├── backend
│   ├── app
│   │   ├── api
│   │   │   └── resume.py
│   │   ├── models
│   │   │   └── schemas.py
│   │   └── services
│   │       ├── pdf_parser.py
│   │       ├── text_cleaner.py
│   │       ├── info_extractor.py
│   │       └── matcher.py
│   ├── main.py
│   └── requirements.txt
├── frontend
│   ├── src
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── style.css
│   ├── package.json
│   └── vite.config.js
└── README.md
