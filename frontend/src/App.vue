<template>
  <div class="page">
    <h1>AI赋能的智能简历分析系统</h1>

    <div class="card">
      <label>上传 PDF 简历：</label>
      <input type="file" accept=".pdf" @change="handleFileChange" />

      <label>岗位描述：</label>
      <textarea
        v-model="jobDescription"
        placeholder="请输入岗位需求描述，例如：招聘 Python 后端开发工程师，熟悉 FastAPI、MySQL、Redis"
        rows="8"
      ></textarea>

      <button @click="analyzeResume" :disabled="loading">
        {{ loading ? "分析中..." : "开始分析" }}
      </button>
    </div>

    <div v-if="result" class="result">
      <div class="card">
        <h2>简历解析结果</h2>
        <p><strong>姓名：</strong>{{ result.parsed_info.name }}</p>
        <p><strong>电话：</strong>{{ result.parsed_info.phone }}</p>
        <p><strong>邮箱：</strong>{{ result.parsed_info.email }}</p>
        <p><strong>地址：</strong>{{ result.parsed_info.address }}</p>
        <p><strong>求职意向：</strong>{{ result.parsed_info.job_intention }}</p>
        <p><strong>期望薪资：</strong>{{ result.parsed_info.expected_salary }}</p>
        <p><strong>工作年限：</strong>{{ result.parsed_info.work_years }}</p>
        <p><strong>学历：</strong>{{ result.parsed_info.education }}</p>

        <div>
          <strong>项目经历：</strong>
          <ul>
            <li v-for="(project, index) in result.parsed_info.projects" :key="index">
              {{ project }}
            </li>
          </ul>
        </div>
      </div>

      <div class="card">
        <h2>岗位匹配结果</h2>
        <p><strong>匹配分数：</strong>{{ result.match_result.score }}</p>
        <p><strong>关键词匹配率：</strong>{{ result.match_result.keyword_match_rate }}</p>
        <p><strong>命中关键词：</strong>{{ result.match_result.matched_keywords.join("，") }}</p>
        <p><strong>缺失关键词：</strong>{{ result.match_result.missing_keywords.join("，") }}</p>
        <p><strong>分析结论：</strong>{{ result.match_result.analysis }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import axios from "axios"

const selectedFile = ref(null)
const jobDescription = ref("")
const result = ref(null)
const loading = ref(false)

const handleFileChange = (event) => {
  selectedFile.value = event.target.files[0]
}

const analyzeResume = async () => {
  if (!selectedFile.value) {
    alert("请先上传 PDF 文件")
    return
  }

  if (!jobDescription.value.trim()) {
    alert("请输入岗位描述")
    return
  }

  const formData = new FormData()
  formData.append("file", selectedFile.value)
  formData.append("job_description", jobDescription.value)

  try {
    loading.value = true

    const response = await axios.post(
      "http://127.0.0.1:8000/api/resume/analyze",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      }
    )

    result.value = response.data
  } catch (error) {
    console.error(error)
    alert("分析失败，请检查后端是否启动，或者是否存在跨域问题")
  } finally {
    loading.value = false
  }
}
</script>