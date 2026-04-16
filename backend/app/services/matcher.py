SKILL_KEYWORDS = [
    "Python",
    "Java",
    "FastAPI",
    "Flask",
    "Django",
    "Redis",
    "MySQL",
    "PostgreSQL",
    "Docker",
    "Linux",
    "RESTful",
    "API",
    "Git",
    "Vue",
    "Spring Boot",
    "SpringBoot",
    "HTML",
    "CSS",
    "JavaScript"
]


def extract_keywords(text: str):
    result = []
    lower_text = text.lower()

    for keyword in SKILL_KEYWORDS:
        if keyword.lower() in lower_text:
            result.append(keyword)

    return result


def match_resume_with_jd(resume_text: str, job_description: str):
    resume_keywords = set(extract_keywords(resume_text))
    jd_keywords = set(extract_keywords(job_description))

    if not jd_keywords:
        return {
            "score": 0,
            "keyword_match_rate": 0,
            "matched_keywords": [],
            "missing_keywords": [],
            "analysis": "岗位描述中未识别到有效关键词"
        }

    matched_keywords = list(resume_keywords & jd_keywords)
    missing_keywords = list(jd_keywords - resume_keywords)

    match_rate = len(matched_keywords) / len(jd_keywords)
    score = int(match_rate * 100)

    if score >= 80:
        analysis = "匹配度较高，建议优先面试。"
    elif score >= 60:
        analysis = "具备部分匹配技能，建议结合项目经验进一步评估。"
    else:
        analysis = f"匹配度较低，主要缺少：{', '.join(missing_keywords[:3])} 等关键技能。"

    return {
        "score": score,
        "keyword_match_rate": round(match_rate, 2),
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "analysis": analysis
    }