import re

def extract_info(text: str):
    phone = ""
    email = ""
    name = ""
    address = ""
    job_intention = ""
    expected_salary = ""
    work_years = ""
    education = ""
    projects = []

    # 手机号：兼容“电 话：”
    phone_match = re.search(r"电\s*话[:：]?\s*(1[3-9]\d{9})", text)
    if phone_match:
        phone = phone_match.group(1)
    else:
        phone_match = re.search(r"1[3-9]\d{9}", text)
        if phone_match:
            phone = phone_match.group()

    # 邮箱：兼容“邮 箱：”
    email_match = re.search(
        r"邮\s*箱[:：]?\s*([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})",
        text
    )
    if email_match:
        email = email_match.group(1)
    else:
        email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
        if email_match:
            email = email_match.group()

    # 姓名：兼容“姓 名：张新颖”
    name_match = re.search(r"姓\s*名[:：]?\s*([\u4e00-\u9fa5]{2,4})", text)
    if name_match:
        name = name_match.group(1)
    else:
        lines = text.split("\n")
        ignore_words = ["基本信息", "个人信息", "简历", "个人简历", "信息"]

        for i, line in enumerate(lines[:15]):
            line = line.strip()

            if not line:
                continue

            if line in ignore_words:
                continue

            if "信息" in line:
                continue

            if line == "姓名" and i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if 2 <= len(next_line) <= 4 and all('\u4e00' <= c <= '\u9fff' for c in next_line):
                    name = next_line
                    break

            if 2 <= len(line) <= 4 and all('\u4e00' <= c <= '\u9fff' for c in line):
                if "项目" not in line and "简介" not in line:
                    name = line
                    break

    # 地址：兼容“住 址：”
    address_match = re.search(r"住\s*址[:：]?\s*([^\n]+)", text)
    if address_match:
        address = address_match.group(1).strip()
        # 避免把后面的“学 历：本科”一起吃进去
        if "学 历" in address:
            address = address.split("学 历")[0].strip()
        if "学历" in address:
            address = address.split("学历")[0].strip()

    # 工作年限
    work_years_match = re.search(r"(\d+年)", text)
    if work_years_match:
        work_years = work_years_match.group(1)

    # 学历：兼容“学 历：本科”
    edu_match = re.search(r"学\s*历[:：]?\s*(本科|硕士|大专|专科|博士)", text)
    if edu_match:
        education = edu_match.group(1)
    else:
        if "本科" in text:
            education = "本科"
        elif "硕士" in text:
            education = "硕士"
        elif "大专" in text:
            education = "大专"

    # 求职意向
    intention_match = re.search(r"求\s*职\s*意\s*向[:：]?\s*([^\n]+)", text)
    if intention_match:
        job_intention = intention_match.group(1).strip()

    # 期望薪资
    salary_match = re.search(r"(\d{1,2}k-\d{1,2}k|\d{4,6}元/月|面议)", text, re.IGNORECASE)
    if salary_match:
        expected_salary = salary_match.group()

    # 项目经历
    lines = text.split("\n")
    for line in lines:
        line = line.strip()
        if "项目" in line and len(line) < 40:
            projects.append(line)

    return {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "job_intention": job_intention,
        "expected_salary": expected_salary,
        "work_years": work_years,
        "education": education,
        "projects": projects[:5]
    }