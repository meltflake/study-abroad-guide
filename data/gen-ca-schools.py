#!/usr/bin/env python3
"""Generate all 20 Canadian schools as valid JSON."""
import json

schools = [
  {
    "id": "uoft",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "多伦多大学", "en": "University of Toronto"},
    "city": {"zh": "安大略省 多伦多", "en": "Toronto, ON"},
    "qs": 25, "the": 21, "usnews": 18, "arwu": 24,
    "tuition": 62250,
    "tuitionRange": [42680, 62250],
    "safety": 7,
    "majors": {
      "zh": ["工程学", "计算机科学", "商学", "生命科学", "人文社科"],
      "en": ["Engineering", "Computer Science", "Commerce", "Life Sciences", "Humanities & Social Sciences"]
    },
    "majorTuition": {
      "zh": "多大国际生学费按专业差异巨大：\n• 人文社科：C$42,680/年\n• 理科：C$47,230/年\n• 商学(Rotman)：C$57,020/年\n• 工程/CS：C$62,250/年",
      "en": "U of T international tuition varies dramatically by program:\n• Arts/Humanities: C$42,680/yr\n• Science: C$47,230/yr\n• Commerce (Rotman): C$57,020/yr\n• Engineering/CS: C$62,250/yr"
    },
    "desc": {
      "zh": "加拿大排名第一的综合性研究型大学，位于多伦多市中心。三大校区（圣乔治、密西沙加、士嘉堡）提供700+本科专业，学术声誉享誉全球。",
      "en": "Canada's top-ranked comprehensive research university, located in downtown Toronto. Three campuses (St. George, Mississauga, Scarborough) offer 700+ undergraduate programs with world-class academic reputation."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 62250, "食宿": 16500, "书本费": 1000, "杂费": 2000},
      "en": {"Tuition": 62250, "Room & Board": 16500, "Books": 1000, "Incidentals": 2000}
    },
    "requirements": {"TOEFL": "100+（写作22+）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "1月15日（安省OUAC 101/105）", "en": "January 15 (via OUAC 101/105)"},
    "safetyDetail": {
      "zh": "多伦多是加拿大最大城市，整体治安良好。校园有24小时安保巡逻和蓝光紧急电话系统。市中心部分区域夜间需注意安全，建议避免深夜独行。",
      "en": "Toronto is Canada's largest city with generally good safety. Campus has 24/7 security patrols and blue-light emergency phones. Exercise caution in some downtown areas at night."
    },
    "climate": {
      "zh": "四季分明，冬季寒冷（-7°C至-1°C），常有降雪。夏季温暖宜人（20-27°C）。需准备防寒衣物。",
      "en": "Four distinct seasons. Cold winters (-7°C to -1°C) with frequent snow. Pleasant summers (20-27°C). Warm clothing essential."
    },
    "livingCost": {"zh": "约C$2,000-2,500/月", "en": "~C$2,000-2,500/month"},
    "livingCostAnnual": 19200,
    "insurance": 1100,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 积累工作经验后通过Express Entry快速通道申请永久居留(PR)。加拿大移民政策对留学生友好，安省还有省提名项目(OINP)。",
      "en": "Study Permit → Post-Graduation Work Permit (PGWP, up to 3 years) → Permanent Residency via Express Entry or Ontario PNP (OINP). Canada has immigrant-friendly policies for international graduates."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一保证住宿，约C$12,000-18,000/年\n🏢 校外租房：市中心Studio约C$1,800-2,400/月\n📍 推荐区域：Annex、Harbord Village、Kensington附近",
      "en": "🏠 On-campus: Guaranteed for first year, ~C$12,000-18,000/yr\n🏢 Off-campus: Downtown studio ~C$1,800-2,400/mo\n📍 Recommended areas: Annex, Harbord Village, near Kensington"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约78%，六年毕业率约85%。学术要求较高，建议充分利用学术辅导资源。",
      "en": "4-year graduation rate ~78%, 6-year rate ~85%. Academically demanding; students are encouraged to use academic support services."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约89%\n💼 知名雇主：五大银行、四大会计师事务所、科技公司（Google、Amazon多伦多办公室）\n🌟 校友网络庞大，Bay Street金融中心就业机会丰富",
      "en": "📊 ~89% employed within 6 months of graduation\n💼 Top employers: Big Five banks, Big Four accounting, tech (Google, Amazon Toronto)\n🌟 Vast alumni network; proximity to Bay Street financial district"
    },
    "healthcare": {
      "zh": "✅ 安省国际学生需购买UHIP（University Health Insurance Plan），约C$756/年，覆盖基本医疗。看病需先预约家庭医生或去Walk-in Clinic。",
      "en": "✅ Ontario international students must enroll in UHIP (University Health Insurance Plan), ~C$756/yr, covering basic medical care. Visit family doctor or walk-in clinic for appointments."
    },
    "application": {
      "zh": "📋 申请平台：OUAC（安大略省大学申请中心）105通道\n📅 截止日期：1月15日\n💰 申请费：C$180（OUAC）+ 各专业补充材料费\n📝 所需材料：高中成绩单、语言成绩、个人陈述、补充申请（部分专业需视频面试）",
      "en": "📋 Platform: OUAC (Ontario Universities' Application Centre) Stream 105\n📅 Deadline: January 15\n💰 Fee: C$180 (OUAC) + supplementary fees per program\n📝 Materials: Transcripts, English proficiency, personal statement, supplementary application (some programs require video interview)"
    }
  },
  {
    "id": "ubc",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "不列颠哥伦比亚大学", "en": "University of British Columbia"},
    "city": {"zh": "不列颠哥伦比亚省 温哥华", "en": "Vancouver, BC"},
    "qs": 34, "the": 41, "usnews": 35, "arwu": 44,
    "tuition": 59000,
    "tuitionRange": [42803, 59000],
    "safety": 8,
    "majors": {
      "zh": ["工程学", "计算机科学", "商学", "林学", "生命科学"],
      "en": ["Engineering", "Computer Science", "Commerce", "Forestry", "Life Sciences"]
    },
    "majorTuition": {
      "zh": "UBC国际生学费因专业不同：\n• 文科：C$42,803/年\n• 理科：C$47,937/年\n• 商学(Sauder)：C$55,500/年\n• 工程/应用科学：C$59,000/年",
      "en": "UBC international tuition by program:\n• Arts: C$42,803/yr\n• Science: C$47,937/yr\n• Commerce (Sauder): C$55,500/yr\n• Engineering/Applied Science: C$59,000/yr"
    },
    "desc": {
      "zh": "位于温哥华西海岸的世界顶尖公立研究型大学，校园依山傍海，被评为全球最美校园之一。Sauder商学院和工程学院享有盛誉，Co-op项目丰富。",
      "en": "A world-class public research university on Vancouver's west coast, with one of the most beautiful campuses globally. Renowned Sauder School of Business and Engineering, with strong co-op programs."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 59000, "食宿": 15000, "书本费": 1000, "杂费": 1800},
      "en": {"Tuition": 59000, "Room & Board": 15000, "Books": 1000, "Incidentals": 1800}
    },
    "requirements": {"TOEFL": "90+（阅读/听力22+，写作/口语21+）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "1月15日（直接向UBC申请）", "en": "January 15 (apply directly to UBC)"},
    "safetyDetail": {
      "zh": "温哥华多年被评为全球最宜居城市之一，治安良好。UBC校园位于半岛尽头，环境安全封闭。校园安保完善，有免费夜间班车服务。",
      "en": "Vancouver consistently ranked among world's most livable cities. UBC campus is on a peninsula with secure, enclosed environment. Campus security and free night shuttle available."
    },
    "climate": {
      "zh": "温和的海洋性气候，冬季温和多雨（3-8°C），少有降雪。夏季凉爽舒适（15-22°C）。雨季（10月-3月）需备雨具。",
      "en": "Mild oceanic climate. Warm, rainy winters (3-8°C) with rare snow. Cool, comfortable summers (15-22°C). Rain gear essential for October-March rainy season."
    },
    "livingCost": {"zh": "约C$1,800-2,300/月", "en": "~C$1,800-2,300/month"},
    "livingCostAnnual": 18000,
    "insurance": 1000,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或BC省提名(BC PNP)申请永久居留。BC省对留学生移民政策优惠，科技类毕业生可走Tech Pilot快速通道。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or BC PNP. BC province offers favorable immigration for graduates; tech graduates can use BC Tech Pilot fast track."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一保证住宿，约C$11,000-16,000/年\n🏢 校外租房：校区周边Studio约C$1,600-2,200/月\n📍 推荐区域：Wesbrook Village、University Village、Dunbar",
      "en": "🏠 On-campus: Guaranteed for first year, ~C$11,000-16,000/yr\n🏢 Off-campus: Near-campus studio ~C$1,600-2,200/mo\n📍 Recommended: Wesbrook Village, University Village, Dunbar"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约80%，六年毕业率约87%。学术支持资源丰富，包括学术指导中心和同伴辅导。",
      "en": "4-year graduation rate ~80%, 6-year rate ~87%. Rich academic support including advising centre and peer tutoring."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约90%\n💼 温哥华科技产业蓬勃：Amazon、Microsoft、SAP、EA均设有办公室\n🌟 Co-op项目覆盖广泛，商学院就业率极高",
      "en": "📊 ~90% employed within 6 months\n💼 Vancouver tech hub: Amazon, Microsoft, SAP, EA offices\n🌟 Extensive co-op programs; Sauder grads have excellent placement rates"
    },
    "healthcare": {
      "zh": "✅ BC省国际学生可加入MSP（Medical Services Plan），等待期后享受与本地居民相同的基本医疗保障。学校另有补充健康保险iMED覆盖处方药、牙科、视力等。",
      "en": "✅ BC international students eligible for MSP (Medical Services Plan) after waiting period, same basic coverage as residents. UBC also provides iMED supplementary insurance for prescriptions, dental, vision."
    },
    "application": {
      "zh": "📋 申请平台：直接通过UBC官网在线申请\n📅 截止日期：1月15日\n💰 申请费：C$116.25\n📝 所需材料：高中成绩单、语言成绩、个人简介（Personal Profile）",
      "en": "📋 Platform: Apply directly via UBC website\n📅 Deadline: January 15\n💰 Fee: C$116.25\n📝 Materials: Transcripts, English proficiency, Personal Profile essay"
    }
  },
  {
    "id": "mcgill",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "麦吉尔大学", "en": "McGill University"},
    "city": {"zh": "魁北克省 蒙特利尔", "en": "Montreal, QC"},
    "qs": 30, "the": 49, "usnews": 54, "arwu": 73,
    "tuition": 58000,
    "tuitionRange": [35000, 58000],
    "safety": 7,
    "majors": {
      "zh": ["医学", "工程学", "计算机科学", "商学", "文学"],
      "en": ["Medicine", "Engineering", "Computer Science", "Commerce", "Arts"]
    },
    "majorTuition": {
      "zh": "McGill国际生学费因专业不同：\n• 文科：C$35,000/年\n• 理科：C$40,200/年\n• 商学(Desautels)：C$52,000/年\n• 工程/CS：C$58,000/年",
      "en": "McGill international tuition by program:\n• Arts: C$35,000/yr\n• Science: C$40,200/yr\n• Commerce (Desautels): C$52,000/yr\n• Engineering/CS: C$58,000/yr"
    },
    "desc": {
      "zh": "加拿大最负盛名的英语授课大学之一，位于蒙特利尔市中心皇家山脚下。以医学、法学和科学研究闻名，被誉为加拿大的「哈佛」。蒙特利尔是双语城市，生活成本相对较低。",
      "en": "One of Canada's most prestigious English-language universities, at the foot of Mount Royal in downtown Montreal. Renowned for medicine, law, and scientific research. Montreal is a bilingual city with relatively lower living costs."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 58000, "食宿": 14000, "书本费": 1000, "杂费": 1500},
      "en": {"Tuition": 58000, "Room & Board": 14000, "Books": 1000, "Incidentals": 1500}
    },
    "requirements": {"TOEFL": "90+（单项不低于21）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "1月15日（直接向McGill申请）", "en": "January 15 (apply directly to McGill)"},
    "safetyDetail": {
      "zh": "蒙特利尔治安良好，犯罪率低于多伦多和温哥华。校园位于市中心，周边生活便利。夜间校园有安保巡逻和步行陪伴服务。",
      "en": "Montreal has good safety with lower crime rates than Toronto and Vancouver. Downtown campus is convenient. Night security patrols and walk-safe escort services available."
    },
    "climate": {
      "zh": "冬季漫长寒冷（-15°C至-5°C），降雪量大。夏季温暖湿润（20-26°C）。需要厚实的冬季装备。",
      "en": "Long, cold winters (-15°C to -5°C) with heavy snowfall. Warm, humid summers (20-26°C). Heavy winter gear essential."
    },
    "livingCost": {"zh": "约C$1,500-2,000/月", "en": "~C$1,500-2,000/month"},
    "livingCostAnnual": 15600,
    "insurance": 1100,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或魁省PEQ项目申请永久居留。魁省PEQ项目要求法语达到B2水平，但对留学生移民有独特优势。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Quebec PEQ program. PEQ requires French B2 level but offers unique advantages for international graduates in Quebec."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一优先，约C$10,000-15,000/年\n🏢 校外租房：蒙特利尔租金相对实惠，Studio约C$1,000-1,600/月\n📍 推荐区域：Milton-Parc、Plateau、McGill Ghetto",
      "en": "🏠 On-campus: Priority for first year, ~C$10,000-15,000/yr\n🏢 Off-campus: Montreal rents relatively affordable, studio ~C$1,000-1,600/mo\n📍 Recommended: Milton-Parc, Plateau, McGill Ghetto"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约82%，六年毕业率约87%。学术标准高，但有丰富的辅导和学术支持资源。",
      "en": "4-year graduation rate ~82%, 6-year rate ~87%. High academic standards with rich tutoring and academic support resources."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约88%\n💼 蒙特利尔AI产业蓬勃（Mila研究所所在地）、游戏产业（Ubisoft）、航空航天\n🌟 校友网络全球广泛，毕业生遍布各行业",
      "en": "📊 ~88% employed within 6 months\n💼 Montreal AI hub (home of Mila), gaming (Ubisoft), aerospace\n🌟 Extensive global alumni network across industries"
    },
    "healthcare": {
      "zh": "✅ 魁省国际学生需加入RAMQ（魁省医疗保险）或购买学校提供的健康保险计划。来自有互惠协议国家的学生可直接加入RAMQ。中国学生需购买学校保险。",
      "en": "✅ Quebec international students need RAMQ (Quebec health insurance) or university health plan. Students from countries with reciprocal agreements can join RAMQ directly. Chinese students need university insurance."
    },
    "application": {
      "zh": "📋 申请平台：直接通过McGill官网申请（魁省独立系统）\n📅 截止日期：1月15日\n💰 申请费：C$129.03\n📝 所需材料：高中成绩单、语言成绩、个人陈述",
      "en": "📋 Platform: Apply directly via McGill website (Quebec separate system)\n📅 Deadline: January 15\n💰 Fee: C$129.03\n📝 Materials: Transcripts, English proficiency, personal statement"
    }
  },
  {
    "id": "mcmaster",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "麦克马斯特大学", "en": "McMaster University"},
    "city": {"zh": "安大略省 汉密尔顿", "en": "Hamilton, ON"},
    "qs": 176, "the": 103, "usnews": 138, "arwu": 98,
    "tuition": 57000,
    "tuitionRange": [35000, 57000],
    "safety": 7,
    "majors": {
      "zh": ["健康科学", "工程学", "商学", "理科", "人文社科"],
      "en": ["Health Sciences", "Engineering", "Commerce", "Science", "Humanities & Social Sciences"]
    },
    "majorTuition": {
      "zh": "McMaster国际生学费因专业不同：\n• 文科/社科：C$35,000/年\n• 理科：C$39,500/年\n• 商学(DeGroote)：C$48,000/年\n• 工程：C$57,000/年",
      "en": "McMaster international tuition by program:\n• Arts/Social Sciences: C$35,000/yr\n• Science: C$39,500/yr\n• Commerce (DeGroote): C$48,000/yr\n• Engineering: C$57,000/yr"
    },
    "desc": {
      "zh": "以创新教学方法闻名的研究型大学，其PBL（问题导向学习）教学法在全球医学教育中具有里程碑意义。健康科学、工程学和商学院实力雄厚，距多伦多仅1小时车程。",
      "en": "A research university renowned for innovative teaching methods. Its Problem-Based Learning (PBL) approach is a landmark in global medical education. Strong in health sciences, engineering, and business. Just 1 hour from Toronto."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 57000, "食宿": 13500, "书本费": 1000, "杂费": 1500},
      "en": {"Tuition": 57000, "Room & Board": 13500, "Books": 1000, "Incidentals": 1500}
    },
    "requirements": {"TOEFL": "86+（单项不低于20）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "1月15日（安省OUAC 105）", "en": "January 15 (via OUAC 105)"},
    "safetyDetail": {
      "zh": "汉密尔顿是中型城市，校园环境安全。学校有24小时安保、紧急电话和免费步行护送服务。",
      "en": "Hamilton is a mid-sized city with a safe campus environment. 24/7 security, emergency phones, and free walk-home escort service available."
    },
    "climate": {
      "zh": "四季分明，冬季寒冷（-7°C至-1°C），有降雪。夏季温暖（20-27°C）。靠近安大略湖，气候略温和。",
      "en": "Four distinct seasons. Cold winters (-7°C to -1°C) with snow. Warm summers (20-27°C). Near Lake Ontario, slightly moderated climate."
    },
    "livingCost": {"zh": "约C$1,400-1,800/月", "en": "~C$1,400-1,800/month"},
    "livingCostAnnual": 14400,
    "insurance": 900,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或安省省提名(OINP)申请永久居留。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Ontario PNP (OINP)."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一保证住宿，约C$9,500-14,000/年\n🏢 校外租房：汉密尔顿租金实惠，Studio约C$1,100-1,500/月\n📍 推荐区域：Westdale、Ainslie Wood",
      "en": "🏠 On-campus: Guaranteed for first year, ~C$9,500-14,000/yr\n🏢 Off-campus: Hamilton rents affordable, studio ~C$1,100-1,500/mo\n📍 Recommended: Westdale, Ainslie Wood"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约76%，六年毕业率约84%。学术支持包括学生成功中心和同伴辅导项目。",
      "en": "4-year graduation rate ~76%, 6-year rate ~84%. Academic support includes Student Success Centre and peer tutoring."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约87%\n💼 健康科学毕业生就业前景优异，工程Co-op项目与Hamilton钢铁/制造业紧密联系\n🌟 靠近多伦多，GTA就业市场可达",
      "en": "📊 ~87% employed within 6 months\n💼 Health sciences grads have excellent prospects; engineering co-op tied to Hamilton steel/manufacturing\n🌟 Proximity to Toronto and GTA job market"
    },
    "healthcare": {
      "zh": "✅ 安省国际学生需购买UHIP，约C$756/年，覆盖基本医疗。校内有学生健康中心提供医疗服务。",
      "en": "✅ Ontario international students must enroll in UHIP, ~C$756/yr. On-campus Student Wellness Centre provides medical services."
    },
    "application": {
      "zh": "📋 申请平台：OUAC 105通道\n📅 截止日期：1月15日\n💰 申请费：C$156（OUAC + 补充费）\n📝 所需材料：高中成绩单、语言成绩、补充申请（部分专业需要）",
      "en": "📋 Platform: OUAC Stream 105\n📅 Deadline: January 15\n💰 Fee: C$156 (OUAC + supplementary)\n📝 Materials: Transcripts, English proficiency, supplementary application (some programs)"
    }
  },
  {
    "id": "umontreal",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "蒙特利尔大学", "en": "Université de Montréal"},
    "city": {"zh": "魁北克省 蒙特利尔", "en": "Montreal, QC"},
    "qs": 159, "the": 111, "usnews": 156, "arwu": 151,
    "tuition": 35000,
    "tuitionRange": [30000, 35000],
    "safety": 7,
    "majors": {
      "zh": ["人工智能", "法学", "医学", "理科", "人文社科"],
      "en": ["Artificial Intelligence", "Law", "Medicine", "Science", "Humanities & Social Sciences"]
    },
    "majorTuition": {
      "zh": "蒙特利尔大学国际生学费（法语授课）：\n• 文科/社科：C$30,000/年\n• 理科：C$32,000/年\n• 工程（Polytechnique附属）：C$35,000/年\n注：学费相对英语大学更实惠",
      "en": "UdeM international tuition (French instruction):\n• Arts/Social Sciences: C$30,000/yr\n• Science: C$32,000/yr\n• Engineering (Polytechnique affiliate): C$35,000/yr\nNote: More affordable than English-language universities"
    },
    "desc": {
      "zh": "加拿大最大的法语大学，也是世界顶尖法语研究型大学。人工智能研究领域全球领先（Mila实验室附属），医学和法学实力雄厚。注意：主要以法语授课。",
      "en": "Canada's largest French-language university and a world-leading Francophone research institution. Global leader in AI research (affiliated with Mila lab). Strong in medicine and law. Note: Primarily French instruction."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 35000, "食宿": 13000, "书本费": 1000, "杂费": 1200},
      "en": {"Tuition": 35000, "Room & Board": 13000, "Books": 1000, "Incidentals": 1200}
    },
    "requirements": {"TOEFL": "不适用（法语授课）", "IELTS": "不适用（法语授课）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "2月1日（直接向UdeM申请）", "en": "February 1 (apply directly to UdeM)"},
    "safetyDetail": {
      "zh": "校园位于皇家山北坡，环境优美安全。蒙特利尔治安良好，校园有安保巡逻服务。",
      "en": "Campus on the north slope of Mount Royal, beautiful and safe. Montreal has good safety; campus security patrols available."
    },
    "climate": {
      "zh": "冬季漫长寒冷（-15°C至-5°C），降雪量大。夏季温暖湿润（20-26°C）。蒙特利尔地下城可避寒。",
      "en": "Long, cold winters (-15°C to -5°C) with heavy snow. Warm, humid summers (20-26°C). Montreal's underground city helps beat the cold."
    },
    "livingCost": {"zh": "约C$1,400-1,800/月", "en": "~C$1,400-1,800/month"},
    "livingCostAnnual": 14400,
    "insurance": 1000,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或魁省PEQ项目申请永久居留。法语授课学生在PEQ项目中有语言优势。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Quebec PEQ. French-instruction students have language advantage for PEQ immigration."
    },
    "housing": {
      "zh": "🏠 校内宿舍：约C$8,000-12,000/年\n🏢 校外租房：蒙特利尔租金实惠，Studio约C$1,000-1,500/月\n📍 推荐区域：Côte-des-Neiges、Outremont",
      "en": "🏠 On-campus: ~C$8,000-12,000/yr\n🏢 Off-campus: Montreal rents affordable, studio ~C$1,000-1,500/mo\n📍 Recommended: Côte-des-Neiges, Outremont"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约75%，六年毕业率约82%。提供法语语言支持项目帮助国际学生适应。",
      "en": "4-year graduation rate ~75%, 6-year rate ~82%. French language support programs available for international students."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约85%\n💼 蒙特利尔AI产业中心、制药、游戏产业就业机会丰富\n🌟 法语能力在魁省就业市场是巨大优势",
      "en": "📊 ~85% employed within 6 months\n💼 Montreal AI hub, pharma, gaming industry opportunities\n🌟 French proficiency is a major advantage in Quebec job market"
    },
    "healthcare": {
      "zh": "✅ 魁省国际学生需加入RAMQ或购买学校健康保险。法国等有互惠协议国家的学生可直接加入RAMQ。",
      "en": "✅ Quebec international students need RAMQ or university health insurance. Students from countries with reciprocal agreements (e.g., France) can join RAMQ directly."
    },
    "application": {
      "zh": "📋 申请平台：直接通过UdeM官网申请（魁省独立系统）\n📅 截止日期：2月1日\n💰 申请费：C$100\n📝 所需材料：高中成绩单、法语能力证明（TFI/DALF）",
      "en": "📋 Platform: Apply directly via UdeM website (Quebec separate system)\n📅 Deadline: February 1\n💰 Fee: C$100\n📝 Materials: Transcripts, French proficiency (TFI/DALF)"
    }
  },
  {
    "id": "ualberta",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "阿尔伯塔大学", "en": "University of Alberta"},
    "city": {"zh": "阿尔伯塔省 埃德蒙顿", "en": "Edmonton, AB"},
    "qs": 111, "the": 131, "usnews": 137, "arwu": 101,
    "tuition": 55000,
    "tuitionRange": [33000, 55000],
    "safety": 7,
    "majors": {
      "zh": ["工程学", "人工智能", "商学", "理科", "能源与环境"],
      "en": ["Engineering", "Artificial Intelligence", "Commerce", "Science", "Energy & Environment"]
    },
    "majorTuition": {
      "zh": "阿尔伯塔大学国际生学费：\n• 文科：C$33,000/年\n• 理科：C$36,500/年\n• 商学：C$46,000/年\n• 工程/CS：C$55,000/年",
      "en": "U of Alberta international tuition:\n• Arts: C$33,000/yr\n• Science: C$36,500/yr\n• Commerce: C$46,000/yr\n• Engineering/CS: C$55,000/yr"
    },
    "desc": {
      "zh": "加拿大顶尖研究型大学，位于阿尔伯塔省首府。以工程学、人工智能（DeepMind联合创始人母校）、能源研究见长。阿省无省销售税，生活成本较低。",
      "en": "A top Canadian research university in Alberta's capital. Renowned for engineering, AI (alma mater of DeepMind co-founder), and energy research. Alberta has no provincial sales tax, lower living costs."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 55000, "食宿": 12000, "书本费": 1000, "杂费": 1500},
      "en": {"Tuition": 55000, "Room & Board": 12000, "Books": 1000, "Incidentals": 1500}
    },
    "requirements": {"TOEFL": "90+（单项不低于21）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "3月1日（直接向UAlberta申请）", "en": "March 1 (apply directly to UAlberta)"},
    "safetyDetail": {
      "zh": "埃德蒙顿是安全的中型城市，校园广大且安保完善。冬季天黑较早，建议结伴出行。",
      "en": "Edmonton is a safe mid-sized city with a large, well-secured campus. Early darkness in winter; travel with companions recommended."
    },
    "climate": {
      "zh": "冬季极寒（-20°C至-10°C），是加拿大最冷的大学城之一。夏季凉爽宜人（15-23°C）。需准备专业防寒装备。",
      "en": "Extremely cold winters (-20°C to -10°C), one of Canada's coldest university cities. Cool, pleasant summers (15-23°C). Professional winter gear essential."
    },
    "livingCost": {"zh": "约C$1,200-1,600/月", "en": "~C$1,200-1,600/month"},
    "livingCostAnnual": 13200,
    "insurance": 900,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或阿省省提名(AINP)申请永久居留。阿省对科技和能源人才需求旺盛。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Alberta PNP (AINP). Alberta has strong demand for tech and energy talent."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一优先，约C$8,000-12,000/年\n🏢 校外租房：埃德蒙顿租金低廉，Studio约C$900-1,300/月\n📍 推荐区域：Garneau、Strathcona、Windsor Park",
      "en": "🏠 On-campus: Priority for first year, ~C$8,000-12,000/yr\n🏢 Off-campus: Edmonton rents low, studio ~C$900-1,300/mo\n📍 Recommended: Garneau, Strathcona, Windsor Park"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约73%，六年毕业率约80%。",
      "en": "4-year graduation rate ~73%, 6-year rate ~80%."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约86%\n💼 能源行业（石油天然气）、科技公司、政府部门\n🌟 AI领域强势，Edmonton是加拿大AI研究重镇",
      "en": "📊 ~86% employed within 6 months\n💼 Energy sector (oil & gas), tech companies, government\n🌟 Strong AI presence; Edmonton is a Canadian AI research hub"
    },
    "healthcare": {
      "zh": "✅ 阿省国际学生可加入AHCIP（Alberta Health Care Insurance Plan），享受与本地居民相同的基本医疗保障。无需额外购买基本医疗保险。",
      "en": "✅ Alberta international students eligible for AHCIP (Alberta Health Care Insurance Plan), same basic coverage as residents. No additional basic insurance needed."
    },
    "application": {
      "zh": "📋 申请平台：直接通过UAlberta官网申请\n📅 截止日期：3月1日\n💰 申请费：C$125\n📝 所需材料：高中成绩单、语言成绩",
      "en": "📋 Platform: Apply directly via UAlberta website\n📅 Deadline: March 1\n💰 Fee: C$125\n📝 Materials: Transcripts, English proficiency"
    }
  },
  {
    "id": "uottawa",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "渥太华大学", "en": "University of Ottawa"},
    "city": {"zh": "安大略省 渥太华", "en": "Ottawa, ON"},
    "qs": 203, "the": 177, "usnews": 215, "arwu": 201,
    "tuition": 55000,
    "tuitionRange": [35000, 55000],
    "safety": 8,
    "majors": {
      "zh": ["法学", "政治学", "工程学", "健康科学", "商学"],
      "en": ["Law", "Political Science", "Engineering", "Health Sciences", "Commerce"]
    },
    "majorTuition": {
      "zh": "渥太华大学国际生学费：\n• 文科/社科：C$35,000/年\n• 理科：C$40,000/年\n• 商学(Telfer)：C$48,000/年\n• 工程/CS：C$55,000/年",
      "en": "U of Ottawa international tuition:\n• Arts/Social Sciences: C$35,000/yr\n• Science: C$40,000/yr\n• Commerce (Telfer): C$48,000/yr\n• Engineering/CS: C$55,000/yr"
    },
    "desc": {
      "zh": "全球最大的英法双语大学，位于加拿大首都渥太华。靠近国会山和联邦政府机构，政治学、法学和公共政策专业优势突出。Co-op项目与政府合作紧密。",
      "en": "The world's largest English-French bilingual university, in Canada's capital Ottawa. Near Parliament Hill and federal institutions. Strong in political science, law, and public policy. Co-op programs closely tied to government."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 55000, "食宿": 13000, "书本费": 1000, "杂费": 1500},
      "en": {"Tuition": 55000, "Room & Board": 13000, "Books": 1000, "Incidentals": 1500}
    },
    "requirements": {"TOEFL": "86+（写作22+）", "IELTS": "6.5+（写作6.5+）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "4月1日（安省OUAC 105）", "en": "April 1 (via OUAC 105)"},
    "safetyDetail": {
      "zh": "渥太华是加拿大首都，治安非常好。校园位于市中心Rideau运河旁，环境优美安全。",
      "en": "Ottawa is Canada's capital with excellent safety. Campus alongside the Rideau Canal in downtown, beautiful and secure environment."
    },
    "climate": {
      "zh": "冬季寒冷（-15°C至-5°C），降雪量大。夏季温暖（20-26°C）。Rideau运河冬季结冰可滑冰。",
      "en": "Cold winters (-15°C to -5°C) with heavy snow. Warm summers (20-26°C). Rideau Canal freezes for ice skating in winter."
    },
    "livingCost": {"zh": "约C$1,400-1,800/月", "en": "~C$1,400-1,800/month"},
    "livingCostAnnual": 14400,
    "insurance": 900,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或安省省提名(OINP)申请永久居留。渥太华联邦政府就业机会丰富。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Ontario PNP (OINP). Ottawa has abundant federal government employment opportunities."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一保证住宿，约C$9,000-14,000/年\n🏢 校外租房：渥太华租金中等，Studio约C$1,200-1,600/月\n📍 推荐区域：Sandy Hill、Byward Market附近",
      "en": "🏠 On-campus: Guaranteed for first year, ~C$9,000-14,000/yr\n🏢 Off-campus: Ottawa moderate rents, studio ~C$1,200-1,600/mo\n📍 Recommended: Sandy Hill, near Byward Market"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约72%，六年毕业率约80%。提供英法双语学术支持。",
      "en": "4-year graduation rate ~72%, 6-year rate ~80%. Bilingual English-French academic support available."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约86%\n💼 联邦政府、国际组织、科技公司（Shopify总部在渥太华）\n🌟 Co-op项目与政府机构合作广泛，双语能力是就业加分项",
      "en": "📊 ~86% employed within 6 months\n💼 Federal government, international organizations, tech (Shopify HQ in Ottawa)\n🌟 Co-op programs with government agencies; bilingual skills are a major asset"
    },
    "healthcare": {
      "zh": "✅ 安省国际学生需购买UHIP，约C$756/年。校内有健康服务中心。",
      "en": "✅ Ontario international students must enroll in UHIP, ~C$756/yr. On-campus health services centre available."
    },
    "application": {
      "zh": "📋 申请平台：OUAC 105通道\n📅 截止日期：4月1日（部分专业更早）\n💰 申请费：C$150（OUAC + 补充费）\n📝 所需材料：高中成绩单、语言成绩",
      "en": "📋 Platform: OUAC Stream 105\n📅 Deadline: April 1 (some programs earlier)\n💰 Fee: C$150 (OUAC + supplementary)\n📝 Materials: Transcripts, English proficiency"
    }
  },
  {
    "id": "ucalgary",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "卡尔加里大学", "en": "University of Calgary"},
    "city": {"zh": "阿尔伯塔省 卡尔加里", "en": "Calgary, AB"},
    "qs": 182, "the": 201, "usnews": 175, "arwu": 201,
    "tuition": 52000,
    "tuitionRange": [31000, 52000],
    "safety": 8,
    "majors": {
      "zh": ["工程学", "能源与环境", "商学", "运动学", "理科"],
      "en": ["Engineering", "Energy & Environment", "Commerce", "Kinesiology", "Science"]
    },
    "majorTuition": {
      "zh": "卡尔加里大学国际生学费：\n• 文科：C$31,000/年\n• 理科：C$34,500/年\n• 商学(Haskayne)：C$45,000/年\n• 工程：C$52,000/年",
      "en": "U of Calgary international tuition:\n• Arts: C$31,000/yr\n• Science: C$34,500/yr\n• Commerce (Haskayne): C$45,000/yr\n• Engineering: C$52,000/yr"
    },
    "desc": {
      "zh": "位于加拿大能源之都卡尔加里的综合性研究型大学。能源工程、商学和运动学实力突出。毗邻落基山脉，户外活动丰富。阿省无省销售税，生活成本适中。",
      "en": "A comprehensive research university in Canada's energy capital, Calgary. Strong in energy engineering, business, and kinesiology. Near the Rocky Mountains with abundant outdoor activities. Alberta has no provincial sales tax."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 52000, "食宿": 12000, "书本费": 1000, "杂费": 1500},
      "en": {"Tuition": 52000, "Room & Board": 12000, "Books": 1000, "Incidentals": 1500}
    },
    "requirements": {"TOEFL": "86+（单项不低于20）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "3月1日（直接向UCalgary申请）", "en": "March 1 (apply directly to UCalgary)"},
    "safetyDetail": {
      "zh": "卡尔加里连续多年被评为全球最宜居城市之一，治安良好。校园面积大，安保系统完善。",
      "en": "Calgary consistently ranked among world's most livable cities with good safety. Large campus with comprehensive security systems."
    },
    "climate": {
      "zh": "冬季寒冷（-15°C至-5°C），但Chinook暖风可带来短暂升温。夏季凉爽干燥（15-23°C）。阳光充足，是加拿大阳光最多的城市之一。",
      "en": "Cold winters (-15°C to -5°C) but Chinook winds bring brief warm spells. Cool, dry summers (15-23°C). Very sunny; one of Canada's sunniest cities."
    },
    "livingCost": {"zh": "约C$1,300-1,700/月", "en": "~C$1,300-1,700/month"},
    "livingCostAnnual": 13800,
    "insurance": 900,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或阿省省提名(AINP)申请永久居留。卡尔加里能源和科技行业就业机会多。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Alberta PNP (AINP). Calgary has strong energy and tech employment opportunities."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一保证住宿，约C$8,500-13,000/年\n🏢 校外租房：卡尔加里租金适中，Studio约C$1,000-1,400/月\n📍 推荐区域：University Heights、Brentwood、Banff Trail",
      "en": "🏠 On-campus: Guaranteed for first year, ~C$8,500-13,000/yr\n🏢 Off-campus: Calgary moderate rents, studio ~C$1,000-1,400/mo\n📍 Recommended: University Heights, Brentwood, Banff Trail"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约71%，六年毕业率约79%。",
      "en": "4-year graduation rate ~71%, 6-year rate ~79%."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约85%\n💼 能源行业（石油天然气巨头总部）、金融、科技创业公司\n🌟 Haskayne商学院与能源行业联系紧密",
      "en": "📊 ~85% employed within 6 months\n💼 Energy sector (oil & gas HQs), finance, tech startups\n🌟 Haskayne School of Business closely tied to energy industry"
    },
    "healthcare": {
      "zh": "✅ 阿省国际学生可加入AHCIP，享受与本地居民相同的基本医疗保障。",
      "en": "✅ Alberta international students eligible for AHCIP, same basic coverage as residents."
    },
    "application": {
      "zh": "📋 申请平台：直接通过UCalgary官网申请\n📅 截止日期：3月1日\n💰 申请费：C$145\n📝 所需材料：高中成绩单、语言成绩",
      "en": "📋 Platform: Apply directly via UCalgary website\n📅 Deadline: March 1\n💰 Fee: C$145\n📝 Materials: Transcripts, English proficiency"
    }
  },
  {
    "id": "uwaterloo",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "滑铁卢大学", "en": "University of Waterloo"},
    "city": {"zh": "安大略省 滑铁卢", "en": "Waterloo, ON"},
    "qs": 112, "the": 158, "usnews": 199, "arwu": 151,
    "tuition": 65000,
    "tuitionRange": [38000, 65000],
    "safety": 8,
    "majors": {
      "zh": ["计算机科学", "工程学", "数学", "精算学", "商学"],
      "en": ["Computer Science", "Engineering", "Mathematics", "Actuarial Science", "Commerce"]
    },
    "majorTuition": {
      "zh": "滑铁卢大学国际生学费：\n• 文科：C$38,000/年\n• 数学：C$52,000/年\n• 商学(AFM/CFM)：C$55,000/年\n• CS/工程：C$65,000/年\n注：Co-op学期有额外Co-op费用",
      "en": "U of Waterloo international tuition:\n• Arts: C$38,000/yr\n• Mathematics: C$52,000/yr\n• Commerce (AFM/CFM): C$55,000/yr\n• CS/Engineering: C$65,000/yr\nNote: Co-op terms have additional co-op fees"
    },
    "desc": {
      "zh": "加拿大最具创新精神的大学，拥有全球最大的Co-op（带薪实习）项目。计算机科学和工程专业在北美享有极高声誉，毕业生遍布硅谷各大科技公司。数学和精算学全球领先。",
      "en": "Canada's most innovative university with the world's largest co-operative education program. CS and Engineering are highly respected in North America; graduates work at top Silicon Valley tech companies. World-leading in mathematics and actuarial science."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 65000, "食宿": 14000, "书本费": 1000, "杂费": 2000},
      "en": {"Tuition": 65000, "Room & Board": 14000, "Books": 1000, "Incidentals": 2000}
    },
    "requirements": {"TOEFL": "90+（写作/口语25+）", "IELTS": "6.5+（写作/口语6.5+）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "2月1日（安省OUAC 105）", "en": "February 1 (via OUAC 105)"},
    "safetyDetail": {
      "zh": "滑铁卢是安静安全的大学城，治安良好。校园安保24小时运行，社区友好。",
      "en": "Waterloo is a quiet, safe university town with good security. 24/7 campus security and a friendly community."
    },
    "climate": {
      "zh": "四季分明，冬季寒冷（-10°C至-2°C），降雪较多。夏季温暖（18-26°C）。",
      "en": "Four distinct seasons. Cold winters (-10°C to -2°C) with significant snow. Warm summers (18-26°C)."
    },
    "livingCost": {"zh": "约C$1,400-1,800/月", "en": "~C$1,400-1,800/month"},
    "livingCostAnnual": 14400,
    "insurance": 900,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或安省省提名(OINP)申请永久居留。Co-op期间也可合法工作，积累加拿大工作经验。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Ontario PNP (OINP). Co-op terms allow legal work experience, building Canadian work history."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一保证住宿，约C$9,500-15,000/年\n🏢 校外租房：滑铁卢租金适中，Studio约C$1,200-1,600/月\n📍 推荐区域：University Avenue周边、Lester Street",
      "en": "🏠 On-campus: Guaranteed for first year, ~C$9,500-15,000/yr\n🏢 Off-campus: Waterloo moderate rents, studio ~C$1,200-1,600/mo\n📍 Recommended: Near University Avenue, Lester Street"
    },
    "graduationRate": {
      "zh": "本科五年毕业率约82%（含Co-op实习年）。Co-op项目需五年完成本科学位。学术压力较大，但Co-op经验极有价值。",
      "en": "5-year graduation rate ~82% (including co-op work terms). Co-op programs require 5 years for undergraduate degree. Academically demanding but co-op experience is invaluable."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约93%（含Co-op返聘）\n💼 硅谷科技巨头（Google、Meta、Apple）、华尔街金融公司、加拿大科技公司\n🌟 Co-op项目使学生毕业前即积累2年工作经验，就业竞争力极强",
      "en": "📊 ~93% employed within 6 months (including co-op return offers)\n💼 Silicon Valley (Google, Meta, Apple), Wall Street, Canadian tech\n🌟 Co-op program provides ~2 years work experience before graduation; extremely competitive graduates"
    },
    "healthcare": {
      "zh": "✅ 安省国际学生需购买UHIP，约C$756/年。校内有Health Services提供基本医疗。",
      "en": "✅ Ontario international students must enroll in UHIP, ~C$756/yr. On-campus Health Services for basic medical care."
    },
    "application": {
      "zh": "📋 申请平台：OUAC 105通道\n📅 截止日期：2月1日\n💰 申请费：C$170（OUAC + 补充费）\n📝 所需材料：高中成绩单、语言成绩、AIF（入学信息表）、部分专业需视频面试或数学竞赛成绩",
      "en": "📋 Platform: OUAC Stream 105\n📅 Deadline: February 1\n💰 Fee: C$170 (OUAC + supplementary)\n📝 Materials: Transcripts, English proficiency, AIF (Admission Information Form), some programs need video interview or math competition results"
    }
  },
  {
    "id": "western",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "西安大略大学", "en": "Western University"},
    "city": {"zh": "安大略省 伦敦", "en": "London, ON"},
    "qs": 114, "the": 201, "usnews": 300, "arwu": 301,
    "tuition": 55000,
    "tuitionRange": [35000, 55000],
    "safety": 8,
    "majors": {
      "zh": ["商学", "医学", "工程学", "传媒学", "理科"],
      "en": ["Commerce", "Medicine", "Engineering", "Media Studies", "Science"]
    },
    "majorTuition": {
      "zh": "Western国际生学费：\n• 文科/社科：C$35,000/年\n• 理科：C$39,000/年\n• 商学(Ivey)：C$55,000/年\n• 工程：C$53,000/年",
      "en": "Western international tuition:\n• Arts/Social Sciences: C$35,000/yr\n• Science: C$39,000/yr\n• Commerce (Ivey): C$55,000/yr\n• Engineering: C$53,000/yr"
    },
    "desc": {
      "zh": "以Ivey商学院闻名的综合性大学，Ivey采用独特的案例教学法（Case Method），是加拿大顶尖商学院之一。校园被评为加拿大最美校园之一，校园文化活跃。",
      "en": "A comprehensive university renowned for its Ivey Business School, which uses the distinctive Case Method teaching approach. One of Canada's top business schools. Campus rated among Canada's most beautiful with vibrant campus culture."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 55000, "食宿": 13500, "书本费": 1000, "杂费": 1500},
      "en": {"Tuition": 55000, "Room & Board": 13500, "Books": 1000, "Incidentals": 1500}
    },
    "requirements": {"TOEFL": "83+（单项不低于20）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "1月15日（安省OUAC 105）", "en": "January 15 (via OUAC 105)"},
    "safetyDetail": {
      "zh": "伦敦(安省)是安静友好的中型城市，校园安全。提供24小时安保和免费护送服务。",
      "en": "London, Ontario is a quiet, friendly mid-sized city with a safe campus. 24/7 security and free escort services available."
    },
    "climate": {
      "zh": "四季分明，冬季寒冷（-8°C至-1°C），降雪适中。夏季温暖（19-26°C）。",
      "en": "Four distinct seasons. Cold winters (-8°C to -1°C) with moderate snow. Warm summers (19-26°C)."
    },
    "livingCost": {"zh": "约C$1,300-1,700/月", "en": "~C$1,300-1,700/month"},
    "livingCostAnnual": 13800,
    "insurance": 900,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或安省省提名(OINP)申请永久居留。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Ontario PNP (OINP)."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一保证住宿，约C$10,000-15,000/年\n🏢 校外租房：伦敦租金实惠，Studio约C$1,000-1,400/月\n📍 推荐区域：Richmond Row、Old North",
      "en": "🏠 On-campus: Guaranteed for first year, ~C$10,000-15,000/yr\n🏢 Off-campus: London affordable rents, studio ~C$1,000-1,400/mo\n📍 Recommended: Richmond Row, Old North"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约77%，六年毕业率约84%。",
      "en": "4-year graduation rate ~77%, 6-year rate ~84%."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约88%\n💼 Ivey商学院毕业生进入投行、咨询公司比例极高\n🌟 校友网络在金融和咨询行业尤为强大",
      "en": "📊 ~88% employed within 6 months\n💼 Ivey grads have very high placement in investment banking and consulting\n🌟 Alumni network particularly strong in finance and consulting"
    },
    "healthcare": {
      "zh": "✅ 安省国际学生需购买UHIP，约C$756/年。校内有学生健康服务中心。",
      "en": "✅ Ontario international students must enroll in UHIP, ~C$756/yr. On-campus Student Health Services available."
    },
    "application": {
      "zh": "📋 申请平台：OUAC 105通道\n📅 截止日期：1月15日\n💰 申请费：C$155（OUAC + 补充费）\n📝 所需材料：高中成绩单、语言成绩、部分专业需补充申请",
      "en": "📋 Platform: OUAC Stream 105\n📅 Deadline: January 15\n💰 Fee: C$155 (OUAC + supplementary)\n📝 Materials: Transcripts, English proficiency, supplementary application for some programs"
    }
  },
  {
    "id": "queens",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "皇后大学", "en": "Queen's University"},
    "city": {"zh": "安大略省 金斯顿", "en": "Kingston, ON"},
    "qs": 209, "the": 251, "usnews": 360, "arwu": 301,
    "tuition": 58000,
    "tuitionRange": [38000, 58000],
    "safety": 9,
    "majors": {
      "zh": ["商学", "工程学", "法学", "理科", "人文社科"],
      "en": ["Commerce", "Engineering", "Law", "Science", "Humanities & Social Sciences"]
    },
    "majorTuition": {
      "zh": "皇后大学国际生学费：\n• 文科/社科：C$38,000/年\n• 理科：C$42,000/年\n• 商学(Smith)：C$58,000/年\n• 工程：C$56,000/年",
      "en": "Queen's international tuition:\n• Arts/Social Sciences: C$38,000/yr\n• Science: C$42,000/yr\n• Commerce (Smith): C$58,000/yr\n• Engineering: C$56,000/yr"
    },
    "desc": {
      "zh": "加拿大历史悠久的名校之一，Smith商学院是加拿大顶尖商学院。位于安大略湖畔的金斯顿市，校园古典优美，学生满意度全加拿大最高。以强烈的校园归属感和校友文化著称。",
      "en": "One of Canada's most historic universities. Smith School of Business is a top Canadian business school. Located on Lake Ontario in Kingston, with a classic beautiful campus and highest student satisfaction in Canada. Known for strong school spirit and alumni culture."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 58000, "食宿": 14000, "书本费": 1000, "杂费": 1500},
      "en": {"Tuition": 58000, "Room & Board": 14000, "Books": 1000, "Incidentals": 1500}
    },
    "requirements": {"TOEFL": "88+（单项不低于20）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "2月1日（安省OUAC 105）", "en": "February 1 (via OUAC 105)"},
    "safetyDetail": {
      "zh": "金斯顿是非常安全的小城市，校园氛围温馨。社区治安极好，步行安全。",
      "en": "Kingston is a very safe small city with a warm campus atmosphere. Excellent community safety; very walkable."
    },
    "climate": {
      "zh": "四季分明，冬季寒冷（-10°C至-2°C），靠近安大略湖，降雪较多。夏季温暖（19-26°C）。",
      "en": "Four distinct seasons. Cold winters (-10°C to -2°C), near Lake Ontario with significant snowfall. Warm summers (19-26°C)."
    },
    "livingCost": {"zh": "约C$1,300-1,700/月", "en": "~C$1,300-1,700/month"},
    "livingCostAnnual": 13800,
    "insurance": 900,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或安省省提名(OINP)申请永久居留。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Ontario PNP (OINP)."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一保证住宿，约C$10,000-15,000/年\n🏢 校外租房：金斯顿租金实惠，Studio约C$1,000-1,400/月\n📍 推荐区域：University District、Sydenham Ward",
      "en": "🏠 On-campus: Guaranteed for first year, ~C$10,000-15,000/yr\n🏢 Off-campus: Kingston affordable rents, studio ~C$1,000-1,400/mo\n📍 Recommended: University District, Sydenham Ward"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约82%，六年毕业率约89%。学生满意度极高。",
      "en": "4-year graduation rate ~82%, 6-year rate ~89%. Extremely high student satisfaction."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约90%\n💼 Smith商学院毕业生在金融和咨询行业就业率极高\n🌟 校友文化强大，毕业生互助网络活跃",
      "en": "📊 ~90% employed within 6 months\n💼 Smith Commerce grads have excellent finance and consulting placement\n🌟 Strong alumni culture with active graduate mutual support network"
    },
    "healthcare": {
      "zh": "✅ 安省国际学生需购买UHIP，约C$756/年。校内有学生健康、咨询与无障碍服务中心。",
      "en": "✅ Ontario international students must enroll in UHIP, ~C$756/yr. On-campus Student Wellness Services available."
    },
    "application": {
      "zh": "📋 申请平台：OUAC 105通道\n📅 截止日期：2月1日\n💰 申请费：C$165（OUAC + 补充费）\n📝 所需材料：高中成绩单、语言成绩、个人陈述/补充申请",
      "en": "📋 Platform: OUAC Stream 105\n📅 Deadline: February 1\n💰 Fee: C$165 (OUAC + supplementary)\n📝 Materials: Transcripts, English proficiency, personal statement/supplementary application"
    }
  },
  {
    "id": "dalhousie",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "达尔豪斯大学", "en": "Dalhousie University"},
    "city": {"zh": "新斯科舍省 哈利法克斯", "en": "Halifax, NS"},
    "qs": 298, "the": 251, "usnews": 401, "arwu": 301,
    "tuition": 42000,
    "tuitionRange": [30000, 42000],
    "safety": 8,
    "majors": {
      "zh": ["海洋科学", "工程学", "商学", "医学", "计算机科学"],
      "en": ["Ocean Sciences", "Engineering", "Commerce", "Medicine", "Computer Science"]
    },
    "majorTuition": {
      "zh": "达尔豪斯大学国际生学费：\n• 文科：C$30,000/年\n• 理科：C$33,000/年\n• 商学(Rowe)：C$38,000/年\n• 工程/CS：C$42,000/年",
      "en": "Dalhousie international tuition:\n• Arts: C$30,000/yr\n• Science: C$33,000/yr\n• Commerce (Rowe): C$38,000/yr\n• Engineering/CS: C$42,000/yr"
    },
    "desc": {
      "zh": "大西洋加拿大地区最大的研究型大学，位于美丽的海港城市哈利法克斯。海洋科学全球领先，工程和医学实力强劲。生活成本相对较低，城市友好宜居。",
      "en": "The largest research university in Atlantic Canada, in the beautiful port city of Halifax. World-leading in ocean sciences, strong in engineering and medicine. Relatively low living costs in a friendly, livable city."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 42000, "食宿": 12000, "书本费": 1000, "杂费": 1200},
      "en": {"Tuition": 42000, "Room & Board": 12000, "Books": 1000, "Incidentals": 1200}
    },
    "requirements": {"TOEFL": "90+（单项不低于20）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "4月1日（直接向Dalhousie申请）", "en": "April 1 (apply directly to Dalhousie)"},
    "safetyDetail": {
      "zh": "哈利法克斯是友好安全的海港城市，人口约40万。校园安全，社区温馨。",
      "en": "Halifax is a friendly, safe port city of ~400K people. Safe campus with a warm community."
    },
    "climate": {
      "zh": "海洋性气候，冬季较冷（-8°C至0°C），降雪较多。夏季凉爽（16-23°C）。靠海湿度较大。",
      "en": "Maritime climate. Cold winters (-8°C to 0°C) with significant snow. Cool summers (16-23°C). Higher humidity near the ocean."
    },
    "livingCost": {"zh": "约C$1,200-1,600/月", "en": "~C$1,200-1,600/month"},
    "livingCostAnnual": 12600,
    "insurance": 1000,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或大西洋移民试点项目(AIP)申请永久居留。AIP为大西洋省份独有的移民快速通道。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Atlantic Immigration Program (AIP). AIP is a unique fast-track immigration pathway for Atlantic provinces."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一优先，约C$8,500-13,000/年\n🏢 校外租房：哈利法克斯租金低廉，Studio约C$1,000-1,400/月\n📍 推荐区域：South End、North End",
      "en": "🏠 On-campus: Priority for first year, ~C$8,500-13,000/yr\n🏢 Off-campus: Halifax low rents, studio ~C$1,000-1,400/mo\n📍 Recommended: South End, North End"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约70%，六年毕业率约78%。",
      "en": "4-year graduation rate ~70%, 6-year rate ~78%."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约83%\n💼 海洋产业、医疗、科技初创公司\n🌟 大西洋移民计划(AIP)为留学生提供独特的移民优势",
      "en": "📊 ~83% employed within 6 months\n💼 Ocean industry, healthcare, tech startups\n🌟 Atlantic Immigration Program offers unique immigration advantages for graduates"
    },
    "healthcare": {
      "zh": "✅ 新斯科舍省国际学生需购买学校提供的健康保险计划，约C$900/年。",
      "en": "✅ Nova Scotia international students need university-provided health insurance, ~C$900/yr."
    },
    "application": {
      "zh": "📋 申请平台：直接通过Dalhousie官网申请\n📅 截止日期：4月1日\n💰 申请费：C$70\n📝 所需材料：高中成绩单、语言成绩",
      "en": "📋 Platform: Apply directly via Dalhousie website\n📅 Deadline: April 1\n💰 Fee: C$70\n📝 Materials: Transcripts, English proficiency"
    }
  },
  {
    "id": "sfu",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "西蒙菲莎大学", "en": "Simon Fraser University"},
    "city": {"zh": "不列颠哥伦比亚省 本拿比/温哥华", "en": "Burnaby/Vancouver, BC"},
    "qs": 318, "the": 251, "usnews": 317, "arwu": 301,
    "tuition": 52000,
    "tuitionRange": [33000, 52000],
    "safety": 7,
    "majors": {
      "zh": ["计算机科学", "商学", "传媒学", "工程学", "环境科学"],
      "en": ["Computer Science", "Commerce", "Communication", "Engineering", "Environmental Science"]
    },
    "majorTuition": {
      "zh": "SFU国际生学费：\n• 文科：C$33,000/年\n• 理科：C$36,000/年\n• 商学(Beedie)：C$45,000/年\n• 工程/CS：C$52,000/年",
      "en": "SFU international tuition:\n• Arts: C$33,000/yr\n• Science: C$36,000/yr\n• Commerce (Beedie): C$45,000/yr\n• Engineering/CS: C$52,000/yr"
    },
    "desc": {
      "zh": "BC省创新型综合大学，三学期制（一年三个学期）让学生可以更灵活安排学业。Co-op项目优秀，商学院(Beedie)声誉良好。主校区位于本拿比山顶，建筑独特。",
      "en": "An innovative BC comprehensive university with a trimester system (3 terms/year) for flexible study. Excellent co-op programs and well-regarded Beedie School of Business. Main campus atop Burnaby Mountain with unique architecture."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 52000, "食宿": 14000, "书本费": 1000, "杂费": 1500},
      "en": {"Tuition": 52000, "Room & Board": 14000, "Books": 1000, "Incidentals": 1500}
    },
    "requirements": {"TOEFL": "88+（单项不低于20）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "1月31日（直接向SFU申请）", "en": "January 31 (apply directly to SFU)"},
    "safetyDetail": {
      "zh": "本拿比和温哥华治安良好。主校区在山顶，环境封闭安全。市中心校区交通便利。",
      "en": "Burnaby and Vancouver have good safety. Main campus atop mountain is enclosed and secure. Downtown campus well-connected by transit."
    },
    "climate": {
      "zh": "温和的海洋性气候，冬季温和多雨（3-8°C），夏季凉爽（15-22°C）。山顶校区雾气较多。",
      "en": "Mild oceanic climate. Warm, rainy winters (3-8°C), cool summers (15-22°C). Mountain campus can be foggy."
    },
    "livingCost": {"zh": "约C$1,600-2,100/月", "en": "~C$1,600-2,100/month"},
    "livingCostAnnual": 16800,
    "insurance": 1000,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或BC省提名(BC PNP)申请永久居留。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or BC PNP."
    },
    "housing": {
      "zh": "🏠 校内宿舍：约C$9,000-14,000/年\n🏢 校外租房：本拿比/温哥华Studio约C$1,400-2,000/月\n📍 推荐区域：UniverCity（校园社区）、Lougheed附近",
      "en": "🏠 On-campus: ~C$9,000-14,000/yr\n🏢 Off-campus: Burnaby/Vancouver studio ~C$1,400-2,000/mo\n📍 Recommended: UniverCity (campus community), near Lougheed"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约68%（三学期制下许多学生提前毕业），六年毕业率约76%。",
      "en": "4-year graduation rate ~68% (many students graduate early under trimester system), 6-year rate ~76%."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约86%\n💼 温哥华科技公司、媒体行业、商业咨询\n🌟 Co-op项目与温哥华企业联系紧密",
      "en": "📊 ~86% employed within 6 months\n💼 Vancouver tech companies, media, business consulting\n🌟 Co-op programs closely connected to Vancouver businesses"
    },
    "healthcare": {
      "zh": "✅ BC省国际学生可加入MSP，等待期后享受基本医疗保障。SFU另有补充健康保险。",
      "en": "✅ BC international students eligible for MSP after waiting period. SFU also provides supplementary health insurance."
    },
    "application": {
      "zh": "📋 申请平台：直接通过SFU官网申请\n📅 截止日期：1月31日\n💰 申请费：C$75\n📝 所需材料：高中成绩单、语言成绩",
      "en": "📋 Platform: Apply directly via SFU website\n📅 Deadline: January 31\n💰 Fee: C$75\n📝 Materials: Transcripts, English proficiency"
    }
  },
  {
    "id": "uvic",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "维多利亚大学", "en": "University of Victoria"},
    "city": {"zh": "不列颠哥伦比亚省 维多利亚", "en": "Victoria, BC"},
    "qs": 322, "the": 301, "usnews": 317, "arwu": 401,
    "tuition": 50000,
    "tuitionRange": [32000, 50000],
    "safety": 9,
    "majors": {
      "zh": ["工程学", "计算机科学", "商学", "环境科学", "法学"],
      "en": ["Engineering", "Computer Science", "Commerce", "Environmental Science", "Law"]
    },
    "majorTuition": {
      "zh": "维多利亚大学国际生学费：\n• 文科：C$32,000/年\n• 理科：C$35,000/年\n• 商学(Gustavson)：C$45,000/年\n• 工程/CS：C$50,000/年",
      "en": "UVic international tuition:\n• Arts: C$32,000/yr\n• Science: C$35,000/yr\n• Commerce (Gustavson): C$45,000/yr\n• Engineering/CS: C$50,000/yr"
    },
    "desc": {
      "zh": "位于BC省首府维多利亚市的综合性研究型大学，以Co-op项目闻名（加拿大第二大Co-op项目）。校园环境优美，气候是加拿大最温和的。海洋科学和清洁能源研究突出。",
      "en": "A comprehensive research university in BC's capital Victoria, known for its co-op program (Canada's second largest). Beautiful campus with Canada's mildest climate. Strong in ocean science and clean energy research."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 50000, "食宿": 13000, "书本费": 1000, "杂费": 1500},
      "en": {"Tuition": 50000, "Room & Board": 13000, "Books": 1000, "Incidentals": 1500}
    },
    "requirements": {"TOEFL": "90+（单项不低于20）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "2月28日（直接向UVic申请）", "en": "February 28 (apply directly to UVic)"},
    "safetyDetail": {
      "zh": "维多利亚是加拿大最安全的城市之一，治安极好。校园绿树环绕，环境宁静安全。",
      "en": "Victoria is one of Canada's safest cities. Campus surrounded by greenery, quiet and secure environment."
    },
    "climate": {
      "zh": "加拿大最温和的气候，冬季温和（3-8°C），极少降雪。夏季凉爽舒适（15-22°C）。全年适合户外活动。",
      "en": "Canada's mildest climate. Mild winters (3-8°C) with rare snow. Cool, comfortable summers (15-22°C). Year-round outdoor activities."
    },
    "livingCost": {"zh": "约C$1,500-2,000/月", "en": "~C$1,500-2,000/month"},
    "livingCostAnnual": 15600,
    "insurance": 1000,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或BC省提名(BC PNP)申请永久居留。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or BC PNP."
    },
    "housing": {
      "zh": "🏠 校内宿舍：大一保证住宿，约C$9,000-14,000/年\n🏢 校外租房：维多利亚Studio约C$1,300-1,800/月\n📍 推荐区域：Gordon Head、Cadboro Bay",
      "en": "🏠 On-campus: Guaranteed for first year, ~C$9,000-14,000/yr\n🏢 Off-campus: Victoria studio ~C$1,300-1,800/mo\n📍 Recommended: Gordon Head, Cadboro Bay"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约72%（含Co-op），六年毕业率约79%。",
      "en": "4-year graduation rate ~72% (with co-op), 6-year rate ~79%."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约87%\n💼 科技公司、政府（BC省府所在地）、清洁能源行业\n🌟 Co-op项目使学生在毕业前积累丰富工作经验",
      "en": "📊 ~87% employed within 6 months\n💼 Tech companies, government (BC's capital), clean energy\n🌟 Co-op program provides rich work experience before graduation"
    },
    "healthcare": {
      "zh": "✅ BC省国际学生可加入MSP，等待期后享受基本医疗保障。UVic有补充健康保险计划。",
      "en": "✅ BC international students eligible for MSP after waiting period. UVic provides supplementary health insurance."
    },
    "application": {
      "zh": "📋 申请平台：直接通过UVic官网申请\n📅 截止日期：2月28日\n💰 申请费：C$125\n📝 所需材料：高中成绩单、语言成绩、个人陈述",
      "en": "📋 Platform: Apply directly via UVic website\n📅 Deadline: February 28\n💰 Fee: C$125\n📝 Materials: Transcripts, English proficiency, personal statement"
    }
  },
  {
    "id": "laval",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "拉瓦尔大学", "en": "Université Laval"},
    "city": {"zh": "魁北克省 魁北克城", "en": "Quebec City, QC"},
    "qs": 420, "the": 351, "usnews": 395, "arwu": 401,
    "tuition": 33000,
    "tuitionRange": [30000, 33000],
    "safety": 9,
    "majors": {
      "zh": ["林学", "农学", "工程学", "医学", "人文社科"],
      "en": ["Forestry", "Agriculture", "Engineering", "Medicine", "Humanities & Social Sciences"]
    },
    "majorTuition": {
      "zh": "拉瓦尔大学国际生学费（法语授课）：\n• 文科/社科：C$30,000/年\n• 理科：C$31,500/年\n• 工程：C$33,000/年\n注：魁省法语大学学费相对实惠",
      "en": "Laval international tuition (French instruction):\n• Arts/Social Sciences: C$30,000/yr\n• Science: C$31,500/yr\n• Engineering: C$33,000/yr\nNote: Quebec French universities have relatively affordable tuition"
    },
    "desc": {
      "zh": "北美最古老的法语大学之一，位于美丽的世界遗产城市魁北克城。林学、农学在加拿大名列前茅。校园是北美最大的大学校园之一，设施完善。注意：法语授课。",
      "en": "One of North America's oldest French-language universities, in the beautiful UNESCO World Heritage city of Quebec City. Top-ranked in forestry and agriculture in Canada. One of North America's largest campuses. Note: French instruction."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 33000, "食宿": 11000, "书本费": 1000, "杂费": 1000},
      "en": {"Tuition": 33000, "Room & Board": 11000, "Books": 1000, "Incidentals": 1000}
    },
    "requirements": {"TOEFL": "不适用（法语授课）", "IELTS": "不适用（法语授课）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "2月1日（直接向Laval申请）", "en": "February 1 (apply directly to Laval)"},
    "safetyDetail": {
      "zh": "魁北克城是加拿大最安全的城市之一，犯罪率极低。校园宽广安全，社区友好。",
      "en": "Quebec City is one of Canada's safest cities with very low crime rates. Spacious, safe campus with a friendly community."
    },
    "climate": {
      "zh": "冬季漫长寒冷（-18°C至-7°C），降雪量非常大。夏季温暖宜人（18-25°C）。需要专业防寒装备。",
      "en": "Long, cold winters (-18°C to -7°C) with very heavy snowfall. Pleasant warm summers (18-25°C). Professional winter gear essential."
    },
    "livingCost": {"zh": "约C$1,100-1,500/月", "en": "~C$1,100-1,500/month"},
    "livingCostAnnual": 12000,
    "insurance": 1000,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或魁省PEQ项目申请永久居留。法语授课学生在PEQ移民中有显著优势。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Quebec PEQ. French-instruction students have significant advantage for PEQ immigration."
    },
    "housing": {
      "zh": "🏠 校内宿舍：约C$6,500-11,000/年\n🏢 校外租房：魁北克城租金极低，Studio约C$800-1,200/月\n📍 推荐区域：Sainte-Foy、校园周边",
      "en": "🏠 On-campus: ~C$6,500-11,000/yr\n🏢 Off-campus: Quebec City very low rents, studio ~C$800-1,200/mo\n📍 Recommended: Sainte-Foy, near campus"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约70%，六年毕业率约78%。",
      "en": "4-year graduation rate ~70%, 6-year rate ~78%."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约84%\n💼 魁省政府、林业/农业、保险和金融\n🌟 法语能力在魁省就业市场是必备技能",
      "en": "📊 ~84% employed within 6 months\n💼 Quebec government, forestry/agriculture, insurance and finance\n🌟 French proficiency is essential in Quebec job market"
    },
    "healthcare": {
      "zh": "✅ 魁省国际学生需加入RAMQ或购买学校健康保险计划。",
      "en": "✅ Quebec international students need RAMQ or university health insurance plan."
    },
    "application": {
      "zh": "📋 申请平台：直接通过Laval官网申请（魁省独立系统）\n📅 截止日期：2月1日\n💰 申请费：C$90\n📝 所需材料：高中成绩单、法语能力证明",
      "en": "📋 Platform: Apply directly via Laval website (Quebec separate system)\n📅 Deadline: February 1\n💰 Fee: C$90\n📝 Materials: Transcripts, French proficiency"
    }
  },
  {
    "id": "umanitoba",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "曼尼托巴大学", "en": "University of Manitoba"},
    "city": {"zh": "曼尼托巴省 温尼伯", "en": "Winnipeg, MB"},
    "qs": 601, "the": 351, "usnews": 401, "arwu": 401,
    "tuition": 42000,
    "tuitionRange": [30000, 42000],
    "safety": 7,
    "majors": {
      "zh": ["工程学", "农学", "医学", "商学", "理科"],
      "en": ["Engineering", "Agriculture", "Medicine", "Commerce", "Science"]
    },
    "majorTuition": {
      "zh": "曼尼托巴大学国际生学费：\n• 文科：C$30,000/年\n• 理科：C$33,000/年\n• 商学(Asper)：C$38,000/年\n• 工程：C$42,000/年",
      "en": "U of Manitoba international tuition:\n• Arts: C$30,000/yr\n• Science: C$33,000/yr\n• Commerce (Asper): C$38,000/yr\n• Engineering: C$42,000/yr"
    },
    "desc": {
      "zh": "西加拿大最古老的大学，位于曼尼托巴省首府温尼伯。工程学和农学研究实力强劲，生活成本是加拿大主要大学城中最低的之一。曼省移民政策对留学生非常友好。",
      "en": "Western Canada's oldest university, in Manitoba's capital Winnipeg. Strong engineering and agriculture research. Among the lowest living costs of major Canadian university cities. Manitoba has very immigrant-friendly policies for students."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 42000, "食宿": 11000, "书本费": 1000, "杂费": 1200},
      "en": {"Tuition": 42000, "Room & Board": 11000, "Books": 1000, "Incidentals": 1200}
    },
    "requirements": {"TOEFL": "86+（单项不低于20）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "3月1日（直接向UManitoba申请）", "en": "March 1 (apply directly to UManitoba)"},
    "safetyDetail": {
      "zh": "温尼伯部分区域治安需注意，但校园安保完善。建议避免深夜独行于市中心某些区域。",
      "en": "Some Winnipeg areas require caution, but campus security is comprehensive. Avoid walking alone late at night in certain downtown areas."
    },
    "climate": {
      "zh": "冬季极寒（-25°C至-12°C），是加拿大最冷的大城市之一。夏季温暖（17-26°C）。需要最高级别的防寒装备。",
      "en": "Extremely cold winters (-25°C to -12°C), one of Canada's coldest major cities. Warm summers (17-26°C). Top-tier winter gear absolutely essential."
    },
    "livingCost": {"zh": "约C$1,100-1,500/月", "en": "~C$1,100-1,500/month"},
    "livingCostAnnual": 12000,
    "insurance": 900,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或曼省省提名(MPNP)申请永久居留。MPNP是加拿大最友好的省提名项目之一，毕业即可申请。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Manitoba PNP (MPNP). MPNP is one of Canada's most accessible provincial nomination programs; graduates can apply immediately."
    },
    "housing": {
      "zh": "🏠 校内宿舍：约C$7,500-12,000/年\n🏢 校外租房：温尼伯租金极低，Studio约C$800-1,200/月\n📍 推荐区域：Fort Richmond、Pembina Highway附近",
      "en": "🏠 On-campus: ~C$7,500-12,000/yr\n🏢 Off-campus: Winnipeg very low rents, studio ~C$800-1,200/mo\n📍 Recommended: Fort Richmond, near Pembina Highway"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约65%，六年毕业率约74%。",
      "en": "4-year graduation rate ~65%, 6-year rate ~74%."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约82%\n💼 农业、制造业、政府、医疗行业\n🌟 MPNP省提名项目使曼省成为留学移民最容易的省份之一",
      "en": "📊 ~82% employed within 6 months\n💼 Agriculture, manufacturing, government, healthcare\n🌟 MPNP makes Manitoba one of easiest provinces for student immigration"
    },
    "healthcare": {
      "zh": "✅ 曼省国际学生可加入Manitoba Health，享受与本地居民相同的基本医疗保障。",
      "en": "✅ Manitoba international students eligible for Manitoba Health, same basic coverage as residents."
    },
    "application": {
      "zh": "📋 申请平台：直接通过UManitoba官网申请\n📅 截止日期：3月1日\n💰 申请费：C$100\n📝 所需材料：高中成绩单、语言成绩",
      "en": "📋 Platform: Apply directly via UManitoba website\n📅 Deadline: March 1\n💰 Fee: C$100\n📝 Materials: Transcripts, English proficiency"
    }
  },
  {
    "id": "usask",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "萨斯喀彻温大学", "en": "University of Saskatchewan"},
    "city": {"zh": "萨斯喀彻温省 萨斯卡通", "en": "Saskatoon, SK"},
    "qs": 601, "the": 401, "usnews": 450, "arwu": 401,
    "tuition": 40000,
    "tuitionRange": [30000, 40000],
    "safety": 7,
    "majors": {
      "zh": ["农学", "兽医学", "工程学", "水资源", "理科"],
      "en": ["Agriculture", "Veterinary Medicine", "Engineering", "Water Resources", "Science"]
    },
    "majorTuition": {
      "zh": "萨斯喀彻温大学国际生学费：\n• 文科：C$30,000/年\n• 理科：C$32,000/年\n• 商学(Edwards)：C$36,000/年\n• 工程：C$40,000/年",
      "en": "USask international tuition:\n• Arts: C$30,000/yr\n• Science: C$32,000/yr\n• Commerce (Edwards): C$36,000/yr\n• Engineering: C$40,000/yr"
    },
    "desc": {
      "zh": "位于加拿大草原省份的综合性研究型大学，拥有加拿大粒子加速器中心（CLS）。农学、兽医学和水资源研究全球知名。生活成本极低，校园沿南萨斯喀彻温河而建，风景优美。",
      "en": "A comprehensive research university in Canada's prairie province, home to the Canadian Light Source (CLS) synchrotron. Globally known for agriculture, veterinary medicine, and water resources. Very low living costs; scenic riverside campus."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 40000, "食宿": 10500, "书本费": 1000, "杂费": 1200},
      "en": {"Tuition": 40000, "Room & Board": 10500, "Books": 1000, "Incidentals": 1200}
    },
    "requirements": {"TOEFL": "86+（单项不低于19）", "IELTS": "6.5+（单项不低于6.0）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "4月1日（直接向USask申请）", "en": "April 1 (apply directly to USask)"},
    "safetyDetail": {
      "zh": "萨斯卡通是友好的中小城市，校园安全。建议冬季注意出行安全。",
      "en": "Saskatoon is a friendly small-medium city with a safe campus. Exercise winter travel caution."
    },
    "climate": {
      "zh": "冬季极寒（-25°C至-12°C），是加拿大最冷的地区之一。夏季温暖干燥（16-25°C）。阳光充足。",
      "en": "Extremely cold winters (-25°C to -12°C), among Canada's coldest. Warm, dry summers (16-25°C). Very sunny."
    },
    "livingCost": {"zh": "约C$1,000-1,400/月", "en": "~C$1,000-1,400/month"},
    "livingCostAnnual": 11400,
    "insurance": 900,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或萨省省提名(SINP)申请永久居留。SINP对留学生友好，门槛较低。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Saskatchewan PNP (SINP). SINP is immigrant-friendly with lower thresholds for students."
    },
    "housing": {
      "zh": "🏠 校内宿舍：约C$7,000-11,000/年\n🏢 校外租房：萨斯卡通租金极低，Studio约C$750-1,100/月\n📍 推荐区域：Varsity View、Nutana",
      "en": "🏠 On-campus: ~C$7,000-11,000/yr\n🏢 Off-campus: Saskatoon very low rents, studio ~C$750-1,100/mo\n📍 Recommended: Varsity View, Nutana"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约63%，六年毕业率约72%。",
      "en": "4-year graduation rate ~63%, 6-year rate ~72%."
    },
    "employment": {
      "zh": "📊 毕业6个月内就业率约80%\n💼 农业、矿业、政府、医疗\n🌟 SINP省提名使萨省成为移民友好省份",
      "en": "📊 ~80% employed within 6 months\n💼 Agriculture, mining, government, healthcare\n🌟 SINP makes Saskatchewan an immigrant-friendly province"
    },
    "healthcare": {
      "zh": "✅ 萨省国际学生可加入Saskatchewan Health，享受基本医疗保障。",
      "en": "✅ Saskatchewan international students eligible for Saskatchewan Health, basic medical coverage."
    },
    "application": {
      "zh": "📋 申请平台：直接通过USask官网申请\n📅 截止日期：4月1日\n💰 申请费：C$100\n📝 所需材料：高中成绩单、语言成绩",
      "en": "📋 Platform: Apply directly via USask website\n📅 Deadline: April 1\n💰 Fee: C$100\n📝 Materials: Transcripts, English proficiency"
    }
  },
  {
    "id": "concordia",
    "country": "CA",
    "flag": "🇨🇦",
    "name": {"zh": "康考迪亚大学", "en": "Concordia University"},
    "city": {"zh": "魁北克省 蒙特利尔", "en": "Montreal, QC"},
    "qs": 551, "the": 601, "usnews": 601, "arwu": 601,
    "tuition": 42000,
    "tuitionRange": [30000, 42000],
    "safety": 7,
    "majors": {
      "zh": ["艺术与设计", "工程学", "计算机科学", "商学", "电影制作"],
      "en": ["Art & Design", "Engineering", "Computer Science", "Commerce", "Film Production"]
    },
    "majorTuition": {
      "zh": "康考迪亚大学国际生学费：\n• 文科/艺术：C$30,000/年\n• 理科：C$33,000/年\n• 商学(JMSB)：C$38,000/年\n• 工程/CS：C$42,000/年",
      "en": "Concordia international tuition:\n• Arts/Fine Arts: C$30,000/yr\n• Science: C$33,000/yr\n• Commerce (JMSB): C$38,000/yr\n• Engineering/CS: C$42,000/yr"
    },
    "desc": {
      "zh": "蒙特利尔的英语综合性大学，以艺术与设计、电影制作和游戏设计闻名。JMSB商学院获AACSB认证，工程和计算机科学持续进步。校园分布在市中心和西部两个校区。",
      "en": "Montreal's English-language comprehensive university, known for art & design, film production, and game design. JMSB business school is AACSB-accredited. Engineering and CS programs growing. Two campuses: downtown and west end."
    },
    "tuitionBreakdown": {
      "zh": {"学费": 42000, "食宿": 13000, "书本费": 1000, "杂费": 1200},
      "en": {"Tuition": 42000, "Room & Board": 13000, "Books": 1000, "Incidentals": 1200}
    },
    "requirements": {"TOEFL": "90+（单项不低于20）", "IELTS": "6.5+（单项不低于5.5）", "SAT": "不要求/Not Required"},
    "deadline": {"zh": "2月1日（直接向Concordia申请）", "en": "February 1 (apply directly to Concordia)"},
    "safetyDetail": {
      "zh": "蒙特利尔治安良好。市中心校区交通便利，西校区环境安静安全。",
      "en": "Montreal has good safety. Downtown campus is well-connected by transit; west campus is quiet and secure."
    },
    "climate": {
      "zh": "冬季漫长寒冷（-15°C至-5°C），降雪量大。夏季温暖湿润（20-26°C）。",
      "en": "Long, cold winters (-15°C to -5°C) with heavy snow. Warm, humid summers (20-26°C)."
    },
    "livingCost": {"zh": "约C$1,400-1,800/月", "en": "~C$1,400-1,800/month"},
    "livingCostAnnual": 14400,
    "insurance": 1000,
    "flights": 2200,
    "visa": {
      "zh": "Study Permit学习许可 → 毕业后可申请PGWP工签（最长3年）→ 通过Express Entry或魁省PEQ项目申请永久居留。",
      "en": "Study Permit → PGWP (up to 3 years) → PR via Express Entry or Quebec PEQ."
    },
    "housing": {
      "zh": "🏠 校内宿舍：约C$9,000-14,000/年\n🏢 校外租房：蒙特利尔租金实惠，Studio约C$1,000-1,500/月\n📍 推荐区域：NDG、Westmount附近、市中心",
      "en": "🏠 On-campus: ~C$9,000-14,000/yr\n🏢 Off-campus: Montreal affordable rents, studio ~C$1,000-1,500/mo\n📍 Recommended: NDG, near Westmount, downtown"
    },
    "graduationRate": {
      "zh": "本科四年毕业率约60%，六年毕业率约70%。",
      "en": "4-year graduation rate ~60%, 6-year rate ~70%."
    },
    "employment": {
      "zh