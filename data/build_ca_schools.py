#!/usr/bin/env python3
"""Build all 20 Canadian schools JSON."""
import json

# Helper to create a school entry
def school(id, name_zh, name_en, city_zh, city_en, qs, the, usnews, arwu, 
           tuition, tuition_range, safety, majors_zh, majors_en,
           major_tuition_zh, major_tuition_en, desc_zh, desc_en,
           breakdown_zh, breakdown_en, req_toefl, req_ielts,
           deadline_zh, deadline_en, safety_detail_zh, safety_detail_en,
           climate_zh, climate_en, living_zh, living_en, living_annual,
           insurance, visa_zh, visa_en, housing_zh, housing_en,
           grad_zh, grad_en, employ_zh, employ_en,
           health_zh, health_en, app_zh, app_en):
    return {
        "id": id, "country": "CA", "flag": "🇨🇦",
        "name": {"zh": name_zh, "en": name_en},
        "city": {"zh": city_zh, "en": city_en},
        "qs": qs, "the": the, "usnews": usnews, "arwu": arwu,
        "tuition": tuition, "tuitionRange": tuition_range, "safety": safety,
        "majors": {"zh": majors_zh, "en": majors_en},
        "majorTuition": {"zh": major_tuition_zh, "en": major_tuition_en},
        "desc": {"zh": desc_zh, "en": desc_en},
        "tuitionBreakdown": {"zh": breakdown_zh, "en": breakdown_en},
        "requirements": {"TOEFL": req_toefl, "IELTS": req_ielts, "SAT": "不要求/Not Required"},
        "deadline": {"zh": deadline_zh, "en": deadline_en},
        "safetyDetail": {"zh": safety_detail_zh, "en": safety_detail_en},
        "climate": {"zh": climate_zh, "en": climate_en},
        "livingCost": {"zh": living_zh, "en": living_en},
        "livingCostAnnual": living_annual, "insurance": insurance, "flights": 2200,
        "visa": {"zh": visa_zh, "en": visa_en},
        "housing": {"zh": housing_zh, "en": housing_en},
        "graduationRate": {"zh": grad_zh, "en": grad_en},
        "employment": {"zh": employ_zh, "en": employ_en},
        "healthcare": {"zh": health_zh, "en": health_en},
        "application": {"zh": app_zh, "en": app_en}
    }

# Load existing 2 schools
with open('ca-schools.json.bak', 'w') as f:
    f.write('backup')  # just in case

# Build all schools
schools = []

# 1. Toronto
schools.append(school(
    "uoft", "多伦多大学", "University of Toronto",
    "安大略省 多伦多", "Toronto, ON",
    25, 21, 18, 24, 62250, [42680, 62250], 7,
    ["工程学", "计算机科学", "商学", "生命科学", "人文社科"],
    ["Engineering", "Computer Science", "Commerce", "Life Sciences", "Humanities & Social Sciences"],
    "多大国际生学费按专业差异巨大：\n• 人文社科：C$42,680/年\n• 理科：C$47,230/年\n• 商学(Rotman)：C$57,020/年\n• 工程/CS：C$62,250/年",
    "U of T international tuition varies dramatically by program:\n• Arts/Humanities: C$42,680/yr\n• Science: C$47,230/yr\n• Commerce (Rotman): C$57,020/yr\n• Engineering/CS: C$62,250/yr",
    "加拿大排名第一的综合性研究型大学，位于多伦多市中心。三大校区（圣乔治、密西沙加、士嘉堡）提供700+本科专业，学术声誉享誉全球。",
    "Canada's top-ranked comprehensive research university, located in downtown Toronto. Three campuses (St. George, Mississauga, Scarborough) offer 700+ undergraduate programs with world-class academic reputation.",
    {"学费": 62250, "食宿": 16500, "书本费": 1000, "杂费": 2000},
    {"Tuition": 62250, "Room & Board": 16500, "Books": 1000, "Incidentals": 2000},
    "100+（写作22+）", "6.5+（单项不低于6.0）",
    "1月15日（安省OUAC 101/105）", "January 15 (via OUAC 101/105)",
    "多伦多是加拿大最大城市，整体治安良好。校园有24小时安保巡逻和蓝光紧急电话系统。市中心部分区域夜间需注意安全。",
    "Toronto is Canada's largest city with generally good safety. Campus has 24/7 security patrols and blue-light emergency phones.",
    "四季分明，冬季寒冷（-7°C至-1°C），常有降雪。夏季温暖宜人（20-27°C）。",
    "Four distinct seasons. Cold winters (-7°C to -1°C) with frequent snow. Pleasant summers (20-27°C).",
    "约C$2,000-2,500/月", "~C$2,000-2,500/month", 19200, 1100,
    "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或安省省提名(OINP)申请永久居留(PR)。",
    "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Ontario PNP (OINP).",
    "🏠 校内宿舍：大一保证住宿，约C$12,000-18,000/年\n🏢 校外租房：市中心Studio约C$1,800-2,400/月\n📍 推荐区域：Annex、Harbord Village",
    "🏠 On-campus: Guaranteed for first year, ~C$12,000-18,000/yr\n🏢 Off-campus: Downtown studio ~C$1,800-2,400/mo\n📍 Recommended: Annex, Harbord Village",
    "本科四年毕业率约78%，六年毕业率约85%。学术要求较高。",
    "4-year graduation rate ~78%, 6-year rate ~85%. Academically demanding.",
    "📊 毕业6个月内就业率约89%\n💼 知名雇主：五大银行、四大会计师事务所、科技公司\n🌟 校友网络庞大，Bay Street金融中心就业机会丰富",
    "📊 ~89% employed within 6 months\n💼 Top employers: Big Five banks, Big Four accounting, tech (Google, Amazon)\n🌟 Vast alumni network; proximity to Bay Street",
    "✅ 安省国际学生需购买UHIP，约C$756/年，覆盖基本医疗。",
    "✅ Ontario international students must enroll in UHIP, ~C$756/yr.",
    "📋 申请平台：OUAC 105通道\n📅 截止日期：1月15日\n💰 申请费：C$180\n📝 所需材料：高中成绩单、语言成绩、个人陈述、补充申请",
    "📋 Platform: OUAC Stream 105\n📅 Deadline: January 15\n💰 Fee: C$180\n📝 Materials: Transcripts, English proficiency, personal statement"
))

# 2. UBC
schools.append(school(
    "ubc", "不列颠哥伦比亚大学", "University of British Columbia",
    "不列颠哥伦比亚省 温哥华", "Vancouver, BC",
    34, 41, 35, 44, 59000, [42803, 59000], 8,
    ["工程学", "计算机科学", "商学", "林学", "生命科学"],
    ["Engineering", "Computer Science", "Commerce", "Forestry", "Life Sciences"],
    "UBC国际生学费因专业不同：\n• 文科：C$42,803/年\n• 理科：C$47,937/年\n• 商学(Sauder)：C$55,500/年\n• 工程：C$59,000/年",
    "UBC international tuition by program:\n• Arts: C$42,803/yr\n• Science: C$47,937/yr\n• Commerce (Sauder): C$55,500/yr\n• Engineering: C$59,000/yr",
    "位于温哥华西海岸的世界顶尖公立研究型大学，校园依山傍海，被评为全球最美校园之一。Sauder商学院和工程学院享有盛誉，Co-op项目丰富。",
    "A world-class public research university on Vancouver's west coast, with one of the most beautiful campuses globally. Renowned Sauder School of Business and Engineering, with strong co-op programs.",
    {"学费": 59000, "食宿": 15000, "书本费": 1000, "杂费": 1800},
    {"Tuition": 59000, "Room & Board": 15000, "Books": 1000, "Incidentals": 1800},
    "90+（阅读/听力22+，写作/口语21+）", "6.5+（单项不低于6.0）",
    "1月15日（直接向UBC申请）", "January 15 (apply directly to UBC)",
    "温哥华多年被评为全球最宜居城市之一，治安良好。UBC校园位于半岛尽头，环境安全。",
    "Vancouver consistently ranked among world's most livable cities. UBC campus is on a peninsula with secure environment.",
    "温和的海洋性气候，冬季温和多雨（3-8°C），少有降雪。夏季凉爽舒适（15-22°C）。",
    "Mild oceanic climate. Warm, rainy winters (3-8°C) with rare snow. Cool summers (15-22°C).",
    "约C$1,800-2,300/月", "~C$1,800-2,300/month", 18000, 1000,
    "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或BC省提名(BC PNP)申请永久居留。",
    "Study Permit → PGWP (up to 3 years) → PR via Express Entry or BC PNP.",
    "🏠 校内宿舍：大一保证住宿，约C$11,000-16,000/年\n🏢 校外租房：校区周边Studio约C$1,600-2,200/月\n📍 推荐区域：Wesbrook Village、Dunbar",
    "🏠 On-campus: Guaranteed for first year, ~C$11,000-16,000/yr\n🏢 Off-campus: Near-campus studio ~C$1,600-2,200/mo\n📍 Recommended: Wesbrook Village, Dunbar",
    "本科四年毕业率约80%，六年毕业率约87%。",
    "4-year graduation rate ~80%, 6-year rate ~87%.",
    "📊 毕业6个月内就业率约90%\n💼 温哥华科技产业蓬勃：Amazon、Microsoft、SAP均设有办公室\n🌟 Co-op项目覆盖广泛",
    "📊 ~90% employed within 6 months\n💼 Vancouver tech hub: Amazon, Microsoft, SAP offices\n🌟 Extensive co-op programs",
    "✅ BC省国际学生可加入MSP，等待期后享受基本医疗保障。学校另有补充健康保险iMED。",
    "✅ BC international students eligible for MSP after waiting period. UBC also provides iMED supplementary insurance.",
    "📋 申请平台：直接通过UBC官网在线申请\n📅 截止日期：1月15日\n💰 申请费：C$116.25\n📝 所需材料：高中成绩单、语言成绩、Personal Profile",
    "📋 Platform: Apply directly via UBC website\n📅 Deadline: January 15\n💰 Fee: C$116.25\n📝 Materials: Transcripts, English proficiency, Personal Profile essay"
))

# 3. McGill
schools.append(school(
    "mcgill", "麦吉尔大学", "McGill University",
    "魁北克省 蒙特利尔", "Montreal, QC",
    30, 49, 54, 73, 58000, [35000, 58000], 7,
    ["医学", "工程学", "计算机科学", "商学", "文学"],
    ["Medicine", "Engineering", "Computer Science", "Commerce", "Arts"],
    "McGill国际生学费因专业不同：\n• 文科：C$35,000/年\n• 理科：C$40,200/年\n• 商学(Desautels)：C$52,000/年\n• 工程/CS：C$58,000/年",
    "McGill international tuition by program:\n• Arts: C$35,000/yr\n• Science: C$40,200/yr\n• Commerce (Desautels): C$52,000/yr\n• Engineering/CS: C$58,000/yr",
    "加拿大最负盛名的英语授课大学之一，位于蒙特利尔市中心皇家山脚下。以医学、法学和科学研究闻名，被誉为加拿大的「哈佛」。蒙特利尔是双语城市，生活成本相对较低。",
    "One of Canada's most prestigious English-language universities, at the foot of Mount Royal in downtown Montreal. Renowned for medicine, law, and scientific research. Montreal is a bilingual city with relatively lower living costs.",
    {"学费": 58000, "食宿": 14000, "书本费": 1000, "杂费": 1500},
    {"Tuition": 58000, "Room & Board": 14000, "Books": 1000, "Incidentals": 1500},
    "90+（单项不低于21）", "6.5+（单项不低于6.0）",
    "1月15日（直接向McGill申请）", "January 15 (apply directly to McGill)",
    "蒙特利尔治安良好，犯罪率低于多伦多和温哥华。校园位于市中心，夜间有安保巡逻服务。",
    "Montreal has good safety with lower crime rates than Toronto and Vancouver. Night security patrols available.",
    "冬季漫长寒冷（-15°C至-5°C），降雪量大。夏季温暖湿润（20-26°C）。",
    "Long, cold winters (-15°C to -5°C) with heavy snowfall. Warm, humid summers (20-26°C).",
    "约C$1,500-2,000/月", "~C$1,500-2,000/month", 15600, 1100,
    "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或魁省PEQ项目申请永久居留。PEQ要求法语B2。",
    "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Quebec PEQ program (requires French B2).",
    "🏠 校内宿舍：大一优先，约C$10,000-15,000/年\n🏢 校外租房：蒙特利尔租金实惠，Studio约C$1,000-1,600/月\n📍 推荐区域：Milton-Parc、Plateau",
    "🏠 On-campus: Priority for first year, ~C$10,000-15,000/yr\n🏢 Off-campus: Montreal affordable, studio ~C$1,000-1,600/mo\n📍 Recommended: Milton-Parc, Plateau",
    "本科四年毕业率约82%，六年毕业率约87%。",
    "4-year graduation rate ~82%, 6-year rate ~87%.",
    "📊 毕业6个月内就业率约88%\n💼 蒙特利尔AI产业蓬勃（Mila研究所）、游戏产业（Ubisoft）、航空航天\n🌟 校友网络全球广泛",
    "📊 ~88% employed within 6 months\n💼 Montreal AI hub (Mila), gaming (Ubisoft), aerospace\n🌟 Extensive global alumni network",
    "✅ 魁省国际学生需加入RAMQ或购买学校健康保险。中国学生需购买学校保险。",
    "✅ Quebec international students need RAMQ or university health plan. Chinese students need university insurance.",
    "📋 申请平台：直接通过McGill官网申请（魁省独立系统）\n📅 截止日期：1月15日\n💰 申请费：C$129\n📝 所需材料：高中成绩单、语言成绩、个人陈述",
    "📋 Platform: Apply directly via McGill website (Quebec separate system)\n📅 Deadline: January 15\n💰 Fee: C$129\n📝 Materials: Transcripts, English proficiency, personal statement"
))

print(f"Built {len(schools)} schools so far...")
# Save partial progress
with open('/tmp/ca_schools_partial.json', 'w') as f:
    json.dump(schools, f, ensure_ascii=False, indent=2)
print("Saved partial to /tmp/ca_schools_partial.json")
