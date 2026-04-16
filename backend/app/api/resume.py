from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.pdf_parser import extract_pdf_text
from app.services.text_cleaner import clean_resume_text
from app.services.info_extractor import extract_info
from app.services.matcher import match_resume_with_jd
import hashlib

router = APIRouter()

CACHE = {}


@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="只支持 PDF 文件")

    file_bytes = await file.read()
    file_hash = hashlib.md5(file_bytes).hexdigest()

    if file_hash in CACHE:
        cached_data = CACHE[file_hash]
        parsed_info = cached_data["parsed_info"]
        clean_text = cached_data["clean_text"]
        print("==== 命中缓存，直接复用解析结果 ====")
    else:
        raw_text = extract_pdf_text(file_bytes)

        print("==== PDF原始内容开始 ====")
        print(raw_text)
        print("==== PDF原始内容结束 ====")

        clean_text = clean_resume_text(raw_text)

        print("==== 清洗后文本开始 ====")
        print(clean_text)
        print("==== 清洗后文本结束 ====")

        parsed_info = extract_info(clean_text)

        CACHE[file_hash] = {
            "clean_text": clean_text,
            "parsed_info": parsed_info
        }

    match_result = match_resume_with_jd(clean_text, job_description)

    return {
        "resume_id": file_hash,
        "filename": file.filename,
        "parsed_info": parsed_info,
        "match_result": match_result
    }