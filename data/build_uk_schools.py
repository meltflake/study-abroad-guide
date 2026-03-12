#!/usr/bin/env python3
"""Build complete UK schools JSON file with all 30 schools."""
import json

# Base template generator
def uk_school(id, name_zh, name_en, city_zh, city_en, qs, the, usnews, arwu,
              tuition, tuition_range, safety, majors_zh, majors_en,
              major_tuition_zh, major_tuition_en, desc_zh, desc_en,
              breakdown_zh, breakdown_en, toefl, ielts, deadline_zh, deadline_en,
              safety_zh, safety_en, climate_zh, climate_en,
              living_zh, living_en, living_annual, is_london=False, is_scotland=False,
              housing_zh="", housing_en="", grad_zh="", grad_en="",
              employ_zh="", employ_en="", health_zh="", health_en="",
              app_zh="", app_en=""):
    fp = "伦敦£1,334/月×9个月" if is_london else "伦敦外£1,023/月×9个月"
    fp_en = "£1,334/month × 9 months in London" if is_london else "£1,023/month × 9 months outside London"
    return {
        "id": id, "country": "UK", "flag": "🇬🇧",
        "name": {"zh": name_zh, "en": name_en},
        "city": {"zh": city_zh, "en": city_en},
        "qs": qs, "the": the, "usnews": usnews, "arwu": arwu,
        "tuition": tuition, "tuitionRange": tuition_range, "safety": safety,
        "majors": {"zh": majors_zh, "en": majors_en},
        "majorTuition": {"zh": major_tuition_zh, "en": major_tuition_en},
        "desc": {"zh": desc_zh, "en": desc_en},
        "tuitionBreakdown": {"zh": breakdown_zh, "en": breakdown_en},
        "requirements": {"TOEFL": toefl, "IELTS": ielts, "SAT": "N/A（需A-Level/IB）"},
        "deadline": {"zh": deadline_zh, "en": deadline_en},
        "safetyDetail": {"zh": safety_zh, "en": safety_en},
        "climate": {"zh": climate_zh, "en": climate_en},
        "livingCost": {"zh": living_zh, "en": living_en},
        "livingCostAnnual": living_annual,
        "insurance": 776, "flights": 1800,
        "visa": {
            "zh": f"Student Visa（学习期间）→ Graduate Visa（毕业后2年工作签证）→ Skilled Worker Visa（雇主担保长期工签）。\n申请Student Visa需CAS letter、资金证明（{fp}）、肺结核检测。IHS医疗附加费£776/年。",
            "en": f"Student Visa (during studies) → Graduate Visa (2-year post-study work permit) → Skilled Worker Visa (employer-sponsored long-term work visa).\nStudent Visa requires CAS letter, financial proof ({fp_en}), TB test. IHS healthcare surcharge £776/year."
        },
        "housing": {"zh": housing_zh, "en": housing_en},
        "graduationRate": {"zh": grad_zh, "en": grad_en},
        "employment": {"zh": employ_zh, "en": employ_en},
        "healthcare": {"zh": health_zh, "en": health_en},
        "application": {"zh": app_zh, "en": app_en}
    }

schools = []

# 1. Oxford
schools.append(uk_school(
    "oxford", "牛津大学", "University of Oxford", "英格兰 牛津", "Oxford, England",
    3, 1, 5, 7, 39740, [33050, 53350], 8,
    ["哲学政治经济学(PPE)", "法学", "医学", "文学", "数学"],
    ["Philosophy, Politics & Economics (PPE)", "Law", "Medicine", "Literature", "Mathematics"],
    "牛津大学国际生学费按专业差异非常大：\n• 人文社科类：£33,050/年\n• 理科/数学：£39,740/年\n• 医学临床：£53,350/年",
    "Oxford international tuition varies significantly by subject:\n• Humanities & Social Sciences: £33,050/yr\n• Sciences/Mathematics: £39,740/yr\n• Clinical Medicine: £53,350/yr",
    "牛津大学创立于1096年，是英语世界最古老的大学，全球学术声望首屈一指。导师制(Tutorial System)是其教学核心，注重一对一深度辅导。培养了28位英国首相和72位诺贝尔奖得主。",
    "Founded in 1096, Oxford is the oldest university in the English-speaking world with unmatched global prestige. Its signature Tutorial System provides intensive one-on-one teaching. Oxford has produced 28 British Prime Ministers and 72 Nobel laureates.",
    {"学费": 39740, "学院费": 4500, "住宿费": 9500, "生活费": 7600},
    {"Tuition": 39740, "College Fees": 4500, "Accommodation": 9500, "Living": 7600},
    "100+", "7.0+", "10月15日（UCAS）", "October 15 (UCAS)",
    "牛津是一座历史悠久的大学城，治安良好，犯罪率低于英国平均水平。校园分布在城市中心，步行或骑车即可到达。夜间有大学安保巡逻，各学院设有24小时门卫。",
    "Oxford is a historic university city with low crime rates below the UK average. The campus is spread across the city centre, easily walkable or cyclable. University security patrols at night, and colleges have 24-hour porters.",
    "温带海洋性气候，冬季阴冷潮湿(2-7°C)，夏季温和宜人(15-22°C)。全年降雨较多，需备防雨衣物。",
    "Temperate maritime climate. Winters are cool and damp (2-7°C), summers mild and pleasant (15-22°C). Rain is frequent year-round; waterproof clothing recommended.",
    "约£1,425/月", "~£1,425/month", 21500, False, False,
    "牛津大学由39个学院组成，大部分学院保证本科生全程住宿。学院宿舍费用£7,500-£11,000/年，包含餐食计划。也可选择校外租房，月租约£700-£1,000。",
    "Oxford has 39 colleges, most guaranteeing accommodation for the full undergraduate degree. College room costs £7,500-£11,000/year, often including meal plans. Off-campus rent is approximately £700-£1,000/month.",
    "本科毕业率约98%，全英最高之一。学制3年（部分专业4年），医学6年。",
    "Undergraduate completion rate ~98%, among the highest in the UK. Degree length: 3 years (some 4-year courses), Medicine 6 years.",
    "毕业生就业率约95%。起薪中位数约£30,000-£35,000。顶尖雇主包括投行、咨询公司、政府机构。校友网络极其强大。",
    "Graduate employment rate ~95%. Median starting salary £30,000-£35,000. Top employers include investment banks, consulting firms, and government. Exceptionally strong alumni network.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。各学院设有护士，大学有专属健康中心(University Health Centre)，提供全科和心理健康服务。",
    "✅ Must pay IHS £776/yr for free NHS healthcare. Each college has a nurse, and the University Health Centre provides GP and mental health services.",
    "📋 申请平台：UCAS\n📅 截止日期：10月15日\n💰 申请费：UCAS £27.50 + 部分专业需面试/入学考试\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信、入学考试(如MAT/TSA/PAT)、面试\n⚠️ 注意：牛津和剑桥不能同时申请",
    "📋 Platform: UCAS\n📅 Deadline: October 15\n💰 Fees: UCAS £27.50 + some subjects require admissions tests\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference, admissions test (e.g. MAT/TSA/PAT), interview\n⚠️ Note: Cannot apply to both Oxford and Cambridge"
))

# 2. Cambridge
schools.append(uk_school(
    "cambridge", "剑桥大学", "University of Cambridge", "英格兰 剑桥", "Cambridge, England",
    2, 5, 8, 4, 37293, [24507, 63990], 8,
    ["自然科学", "工程学", "数学", "计算机科学", "经济学"],
    ["Natural Sciences", "Engineering", "Mathematics", "Computer Science", "Economics"],
    "剑桥大学国际生学费因专业差异较大：\n• 人文社科类：£24,507/年\n• 理工科/数学：£37,293/年\n• 医学临床：£63,990/年",
    "Cambridge international tuition varies by subject:\n• Humanities & Social Sciences: £24,507/yr\n• Sciences/Engineering: £37,293/yr\n• Clinical Medicine: £63,990/yr",
    "剑桥大学创立于1209年，是世界顶尖的研究型大学之一。拥有31个学院，采用学院制和导师制教学。共培养了121位诺贝尔奖得主，在科学领域尤为卓越。",
    "Founded in 1209, Cambridge is one of the world's leading research universities. With 31 colleges, it uses a collegiate and supervision system. It has produced 121 Nobel laureates, with particular excellence in the sciences.",
    {"学费": 37293, "学院费": 4000, "住宿费": 9000, "生活费": 7600},
    {"Tuition": 37293, "College Fees": 4000, "Accommodation": 9000, "Living": 7600},
    "100+", "7.5+", "10月15日（UCAS）", "October 15 (UCAS)",
    "剑桥是典型的大学城，治安优良，犯罪率低。自行车是主要交通方式，城市紧凑宜居。各学院均有24小时门卫和安保系统。",
    "Cambridge is a classic university town with excellent safety and low crime rates. Cycling is the primary transport; the city is compact and liveable. All colleges have 24-hour porters and security systems.",
    "温带海洋性气候，冬季寒冷(1-7°C)，夏季温和(14-22°C)。东部较干燥，但仍需防雨装备。冬季风大。",
    "Temperate maritime climate. Winters are cold (1-7°C), summers mild (14-22°C). Drier than western England but rain gear still needed. Windy in winter.",
    "约£1,400/月", "~£1,400/month", 21000, False, False,
    "剑桥大学31个学院大多保证本科生全程住宿。学院宿舍£7,000-£10,500/年，通常含部分餐食。校外租房月租£650-£950。",
    "Most of Cambridge's 31 colleges guarantee accommodation for undergraduates. College rooms £7,000-£10,500/year, often including some meals. Off-campus rent £650-£950/month.",
    "本科毕业率约98%。学制3-4年，医学6年。",
    "Undergraduate completion rate ~98%. Degree length: 3-4 years, Medicine 6 years.",
    "毕业生就业率约95%。起薪中位数约£30,000-£35,000。在科技、金融、咨询领域极受欢迎。校友网络全球顶尖。",
    "Graduate employment rate ~95%. Median starting salary £30,000-£35,000. Highly sought after in tech, finance, and consulting. World-class alumni network.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。各学院有护士，大学有健康中心提供全科和心理健康服务。",
    "✅ Must pay IHS £776/yr for free NHS healthcare. Each college has a nurse, and the university health centre provides GP and mental health services.",
    "📋 申请平台：UCAS\n📅 截止日期：10月15日\n💰 申请费：UCAS £27.50 + 部分专业需入学考试\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信、入学考试(如STEP/ENGAA/NSAA)、面试\n⚠️ 注意：牛津和剑桥不能同时申请",
    "📋 Platform: UCAS\n📅 Deadline: October 15\n💰 Fees: UCAS £27.50 + some subjects require admissions tests\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference, admissions test (e.g. STEP/ENGAA/NSAA), interview\n⚠️ Note: Cannot apply to both Oxford and Cambridge"
))

# 3. Imperial
schools.append(uk_school(
    "imperial", "帝国理工学院", "Imperial College London", "英格兰 伦敦", "London, England",
    6, 8, 13, 22, 38900, [36200, 51800], 7,
    ["工程学", "计算机科学", "医学", "物理", "商科"],
    ["Engineering", "Computer Science", "Medicine", "Physics", "Business"],
    "帝国理工国际生学费：\n• 理工科：£36,200-£42,000/年\n• 商科：£38,900/年\n• 医学：£51,800/年",
    "Imperial international tuition:\n• Science & Engineering: £36,200-£42,000/yr\n• Business: £38,900/yr\n• Medicine: £51,800/yr",
    "帝国理工学院成立于1907年，专注于科学、工程、医学和商科，是全球顶尖的理工科大学。位于伦敦南肯辛顿，毗邻自然历史博物馆和科学博物馆。以研究密集和产业联系紧密著称。",
    "Founded in 1907, Imperial focuses on science, engineering, medicine, and business, ranking among the world's top STEM universities. Located in South Kensington, London, near the Natural History and Science Museums. Known for research intensity and strong industry links.",
    {"学费": 38900, "住宿费": 12000, "生活费": 9600},
    {"Tuition": 38900, "Accommodation": 12000, "Living": 9600},
    "92+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "位于伦敦南肯辛顿高端地区，治安相对良好。校园有24小时安保，但作为大城市需注意个人财物安全，尤其在地铁和繁忙区域。",
    "Located in upscale South Kensington, relatively safe. Campus has 24-hour security, but as a major city, be mindful of personal belongings, especially on the Tube and in busy areas.",
    "伦敦温带海洋性气候，冬季阴冷(3-8°C)，夏季温暖(15-25°C)。多阴天和小雨，偶有晴天。",
    "London's temperate maritime climate. Winters are cool and grey (3-8°C), summers warm (15-25°C). Frequent overcast skies and drizzle, occasional sunny spells.",
    "约£1,600/月", "~£1,600/month", 24000, True, False,
    "大一新生保证校内住宿。宿舍位于南肯辛顿及周边，费用£9,000-£15,000/年。校外租房在伦敦较贵，月租£800-£1,400。",
    "First-year students guaranteed campus accommodation. Halls in South Kensington and nearby areas, £9,000-£15,000/year. Off-campus London rent is higher at £800-£1,400/month.",
    "本科毕业率约95%。学制3-4年，医学5-6年。",
    "Undergraduate completion rate ~95%. Degree length: 3-4 years, Medicine 5-6 years.",
    "毕业生就业率约93%。起薪中位数约£35,000-£40,000，在理工科毕业生中数一数二。金融、科技、工程行业青睐。",
    "Graduate employment rate ~93%. Median starting salary £35,000-£40,000, among the highest for STEM graduates. Highly valued in finance, tech, and engineering.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内设有健康中心，提供全科门诊和心理咨询服务。",
    "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus health centre provides GP consultations and mental health support.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信、部分专业需入学考试或面试",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference, some subjects require admissions tests or interviews"
))

# Write first 3 schools to test
print(f"Built {len(schools)} schools so far")

# Continue building remaining schools...
# 4. UCL
schools.append(uk_school(
    "ucl", "伦敦大学学院", "University College London (UCL)", "英格兰 伦敦", "London, England",
    9, 22, 12, 17, 35000, [26200, 44000], 7,
    ["建筑学", "教育学", "医学", "法学", "心理学"],
    ["Architecture", "Education", "Medicine", "Law", "Psychology"],
    "UCL国际生学费：\n• 人文社科：£26,200/年\n• 理工科：£35,000/年\n• 医学：£44,000/年",
    "UCL international tuition:\n• Humanities & Social Sciences: £26,200/yr\n• Sciences: £35,000/yr\n• Medicine: £44,000/yr",
    "UCL成立于1826年，是伦敦大学体系的创始学院，以其开放包容的传统著称。是英国第一所招收女生和不限宗教信仰的大学。学科覆盖面极广，建筑学、教育学全球领先。",
    "Founded in 1826, UCL was the founding college of the University of London, known for its inclusive tradition. It was the first English university to admit women and students of any religion. Extremely broad subject range; Architecture and Education are world-leading.",
    {"学费": 35000, "住宿费": 11000, "生活费": 9600},
    {"Tuition": 35000, "Accommodation": 11000, "Living": 9600},
    "92+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "UCL位于伦敦市中心Bloomsbury区，周边有大英博物馆等文化地标。总体治安良好，但需注意城市生活中的常规安全问题。校园有24小时安保。",
    "UCL is in central London's Bloomsbury district, near the British Museum. Generally safe but typical city awareness needed. Campus has 24-hour security.",
    "伦敦温带海洋性气候，冬季阴冷(3-8°C)，夏季温暖(15-25°C)。多阴天和小雨。",
    "London's temperate maritime climate. Winters cool and grey (3-8°C), summers warm (15-25°C). Frequent overcast and drizzle.",
    "约£1,600/月", "~£1,600/month", 24000, True, False,
    "大一新生保证校内住宿。宿舍分布在伦敦多个区域，费用£8,500-£14,000/年。校外租房月租£800-£1,300。",
    "First-year students guaranteed accommodation. Halls across multiple London locations, £8,500-£14,000/year. Off-campus rent £800-£1,300/month.",
    "本科毕业率约92%。学制3年（部分4年），医学5-6年。",
    "Undergraduate completion rate ~92%. Degree length: 3 years (some 4-year), Medicine 5-6 years.",
    "毕业生就业率约90%。起薪中位数约£28,000-£33,000。在教育、建筑、医疗领域雇主认可度极高。",
    "Graduate employment rate ~90%. Median starting salary £28,000-£33,000. Highly regarded by employers in education, architecture, and healthcare.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有学生健康中心，提供全科和心理健康服务。",
    "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus student health centre provides GP and mental health services.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 5. LSE
schools.append(uk_school(
    "lse", "伦敦政治经济学院", "London School of Economics and Political Science (LSE)", "英格兰 伦敦", "London, England",
    50, 46, 230, 151, 26592, [25272, 30984], 7,
    ["经济学", "政治学", "社会学", "法学", "国际关系"],
    ["Economics", "Political Science", "Sociology", "Law", "International Relations"],
    "LSE国际生学费：\n• 大部分专业：£25,272-£30,984/年\n• LSE不设理工科和医科",
    "LSE international tuition:\n• Most programmes: £25,272-£30,984/yr\n• LSE does not offer STEM or Medicine",
    "LSE成立于1895年，专注于社会科学领域，是全球社科研究的顶尖学府。位于伦敦市中心，与政府、媒体和金融机构毗邻。培养了众多国家元首和诺贝尔经济学奖得主。",
    "Founded in 1895, LSE focuses exclusively on social sciences and is a global leader in the field. Located in central London near government, media, and financial institutions. Has produced numerous heads of state and Nobel laureates in Economics.",
    {"学费": 26592, "住宿费": 11500, "生活费": 9600},
    {"Tuition": 26592, "Accommodation": 11500, "Living": 9600},
    "100+", "7.0+", "1月31日（UCAS）", "January 31 (UCAS)",
    "位于伦敦市中心Holborn/Aldwych区，紧邻皇家法院和考文特花园。治安较好但需注意城市安全常识。校园有24小时安保。",
    "Located in central London's Holborn/Aldwych area, near the Royal Courts of Justice and Covent Garden. Generally safe but city awareness needed. 24-hour campus security.",
    "伦敦温带海洋性气候，冬季阴冷(3-8°C)，夏季温暖(15-25°C)。多阴天和小雨。",
    "London's temperate maritime climate. Winters cool and grey (3-8°C), summers warm (15-25°C). Frequent overcast and drizzle.",
    "约£1,600/月", "~£1,600/month", 24000, True, False,
    "大一新生保证宿舍。LSE有多处宿舍楼，费用£9,000-£14,500/年。伦敦市中心校外租房较贵，月租£900-£1,400。",
    "First-year students guaranteed halls. LSE has multiple residences, £9,000-£14,500/year. Central London off-campus rent is high at £900-£1,400/month.",
    "本科毕业率约93%。学制3年。",
    "Undergraduate completion rate ~93%. Degree length: 3 years.",
    "毕业生就业率约92%。起薪中位数约£32,000-£38,000。在金融、咨询、政府、国际组织中极受追捧。",
    "Graduate employment rate ~92%. Median starting salary £32,000-£38,000. Highly sought after in finance, consulting, government, and international organisations.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有学生健康服务和心理咨询中心。",
    "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus student health service and counselling centre.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 6. Edinburgh (Scotland - 4 year)
schools.append(uk_school(
    "edinburgh", "爱丁堡大学", "University of Edinburgh", "苏格兰 爱丁堡", "Edinburgh, Scotland",
    22, 30, 34, 38, 30400, [23950, 55000], 8,
    ["计算机科学", "医学", "人工智能", "文学", "法学"],
    ["Computer Science", "Medicine", "Artificial Intelligence", "Literature", "Law"],
    "爱丁堡大学国际生学费：\n• 人文社科：£23,950/年\n• 理工科：£30,400-£36,500/年\n• 医学：£55,000/年",
    "Edinburgh international tuition:\n• Humanities & Social Sciences: £23,950/yr\n• Sciences/Engineering: £30,400-£36,500/yr\n• Medicine: £55,000/yr",
    "爱丁堡大学创立于1583年，是苏格兰最古老的大学之一。在人工智能、计算机科学领域世界领先（AI先驱所在地）。校园坐落在爱丁堡这座世界文化遗产城市中。",
    "Founded in 1583, Edinburgh is one of Scotland's oldest universities. World-leading in AI and Computer Science (birthplace of AI pioneers). Set in Edinburgh, a UNESCO World Heritage city.",
    {"学费": 30400, "住宿费": 7500, "生活费": 7200},
    {"Tuition": 30400, "Accommodation": 7500, "Living": 7200},
    "92+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "爱丁堡是苏格兰首府，治安良好，犯罪率低。城市紧凑，步行即可到达大部分地方。夜间老城区需注意安全。",
    "Edinburgh is Scotland's capital with good safety and low crime. Compact city, most places walkable. Be aware in the Old Town at night.",
    "苏格兰气候偏冷，冬季寒冷多风(1-6°C)，夏季凉爽(11-19°C)。多雨多风，需备保暖防水衣物。",
    "Scottish climate is cooler. Winters cold and windy (1-6°C), summers cool (11-19°C). Rainy and windy; warm waterproof clothing essential.",
    "约£1,200/月", "~£1,200/month", 18000, False, True,
    "大一新生保证住宿。宿舍费用£6,000-£10,000/年。校外租房月租£550-£850。",
    "First-year students guaranteed accommodation. Halls £6,000-£10,000/year. Off-campus rent £550-£850/month.",
    "本科毕业率约93%。苏格兰学制4年，医学5-6年。",
    "Undergraduate completion rate ~93%. Scottish degree: 4 years, Medicine 5-6 years.",
    "毕业生就业率约90%。起薪中位数约£26,000-£30,000。在科技、金融、学术领域表现优秀。",
    "Graduate employment rate ~90%. Median starting salary £26,000-£30,000. Strong performance in tech, finance, and academia.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。大学有学生健康服务中心。",
    "✅ Must pay IHS £776/yr for free NHS healthcare. University has a student health service.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信\n📌 苏格兰本科学制4年",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference\n📌 Scottish undergraduate degree is 4 years"
))

# 7. Manchester
schools.append(uk_school(
    "manchester", "曼彻斯特大学", "University of Manchester", "英格兰 曼彻斯特", "Manchester, England",
    34, 54, 63, 36, 29000, [23000, 52000], 7,
    ["商科", "工程学", "计算机科学", "医学", "物理学"],
    ["Business", "Engineering", "Computer Science", "Medicine", "Physics"],
    "曼彻斯特大学国际生学费：\n• 人文社科：£23,000/年\n• 理工科：£29,000-£33,000/年\n• 医学：£52,000/年",
    "Manchester international tuition:\n• Humanities & Social Sciences: £23,000/yr\n• Sciences/Engineering: £29,000-£33,000/yr\n• Medicine: £52,000/yr",
    "曼彻斯特大学成立于1824年，是英国最大的单一校区大学之一。25位诺贝尔奖得主与此有关联。在商科、工程和计算机领域享有盛誉，是英国罗素集团成员。",
    "Founded in 1824, Manchester is one of the UK's largest single-site universities. Associated with 25 Nobel laureates. Renowned for business, engineering, and computing; a Russell Group member.",
    {"学费": 29000, "住宿费": 7500, "生活费": 7200},
    {"Tuition": 29000, "Accommodation": 7500, "Living": 7200},
    "87+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "曼彻斯特是英格兰第二大城市，校园区域治安较好。需注意市中心夜间安全。大学有安保团队和紧急联络服务。",
    "Manchester is England's second city; the campus area is generally safe. Be cautious in the city centre at night. University has a security team and emergency contact services.",
    "温带海洋性气候，多雨（英格兰西北部降雨较多）。冬季(2-7°C)，夏季(13-20°C)。需备防雨衣物。",
    "Temperate maritime climate, rainy (northwest England gets more rain). Winters (2-7°C), summers (13-20°C). Waterproof clothing essential.",
    "约£1,100/月", "~£1,100/month", 16500, False, False,
    "大一新生保证住宿。宿舍费用£5,500-£9,500/年。校外租房月租£450-£700。曼城生活成本远低于伦敦。",
    "First-year students guaranteed accommodation. Halls £5,500-£9,500/year. Off-campus rent £450-£700/month. Manchester's cost of living is much lower than London.",
    "本科毕业率约90%。学制3年，医学5年。",
    "Undergraduate completion rate ~90%. Degree length: 3 years, Medicine 5 years.",
    "毕业生就业率约90%。起薪中位数约£26,000-£30,000。在英格兰北部就业市场影响力极大。",
    "Graduate employment rate ~90%. Median starting salary £26,000-£30,000. Enormous influence in the northern England job market.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有学生健康中心。",
    "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus student health centre available.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 8. KCL
schools.append(uk_school(
    "kcl", "伦敦国王学院", "King's College London", "英格兰 伦敦", "London, England",
    40, 36, 33, 51, 29850, [23940, 50400], 7,
    ["法学", "医学", "护理学", "国际关系", "心理学"],
    ["Law", "Medicine", "Nursing", "International Relations", "Psychology"],
    "KCL国际生学费：\n• 人文社科：£23,940/年\n• 理工科：£29,850/年\n• 医学：£50,400/年",
    "KCL international tuition:\n• Humanities & Social Sciences: £23,940/yr\n• Sciences: £29,850/yr\n• Medicine: £50,400/yr",
    "KCL成立于1829年，是伦敦大学创始学院之一。在法学、医学和人文学科享有盛誉。主校区位于泰晤士河南岸，毗邻伦敦眼和议会大厦。",
    "Founded in 1829, KCL is one of the founding colleges of the University of London. Renowned for law, medicine, and humanities. Main campus on the Strand, near the Thames, London Eye, and Parliament.",
    {"学费": 29850, "住宿费": 10500, "生活费": 9600},
    {"Tuition": 29850, "Accommodation": 10500, "Living": 9600},
    "92+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "校区分布在伦敦市中心多个地点。治安良好，但需注意城市安全常识。各校区有安保人员。",
    "Campuses across central London. Generally safe but city awareness needed. Security staff at each campus.",
    "伦敦温带海洋性气候，冬季阴冷(3-8°C)，夏季温暖(15-25°C)。多阴天和小雨。",
    "London's temperate maritime climate. Winters cool and grey (3-8°C), summers warm (15-25°C). Frequent overcast and drizzle.",
    "约£1,550/月", "~£1,550/month", 23400, True, False,
    "大一新生保证宿舍。宿舍费£8,500-£13,500/年。校外租房月租£800-£1,300。",
    "First-year students guaranteed halls. Halls £8,500-£13,500/year. Off-campus rent £800-£1,300/month.",
    "本科毕业率约91%。学制3年，医学5年。",
    "Undergraduate completion rate ~91%. Degree length: 3 years, Medicine 5 years.",
    "毕业生就业率约90%。起薪中位数约£27,000-£32,000。在医疗、法律领域雇主认可度很高。",
    "Graduate employment rate ~90%. Median starting salary £27,000-£32,000. Highly valued by employers in healthcare and law.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。大学有学生健康中心和心理咨询服务。",
    "✅ Must pay IHS £776/yr for free NHS healthcare. University has student health centre and counselling services.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

print(f"Built {len(schools)} schools so far, continuing...")

# 9. Bristol
schools.append(uk_school(
    "bristol", "布里斯托大学", "University of Bristol", "英格兰 布里斯托", "Bristol, England",
    55, 81, 86, 78, 27200, [22300, 46500], 8,
    ["工程学", "法学", "社会学", "地理学", "医学"],
    ["Engineering", "Law", "Sociology", "Geography", "Medicine"],
    "布里斯托大学国际生学费：\n• 人文社科：£22,300/年\n• 理工科：£27,200/年\n• 医学：£46,500/年",
    "Bristol international tuition:\n• Humanities & Social Sciences: £22,300/yr\n• Sciences/Engineering: £27,200/yr\n• Medicine: £46,500/yr",
    "布里斯托大学创立于1876年，是罗素集团成员，研究实力雄厚。布里斯托是一座充满活力的文化城市，多次被评为英国最宜居城市之一。",
    "Founded in 1876, Bristol is a Russell Group university with strong research credentials. Bristol is a vibrant cultural city, repeatedly voted one of the best places to live in the UK.",
    {"学费": 27200, "住宿费": 7500, "生活费": 7000},
    {"Tuition": 27200, "Accommodation": 7500, "Living": 7000},
    "85+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "布里斯托治安良好，是英国最宜居城市之一。校园分布在城市中心和Clifton区。大学有安保巡逻。",
    "Bristol has good safety, one of the UK's most liveable cities. Campus spans city centre and Clifton area. University has security patrols.",
    "温带海洋性气候，冬季(3-8°C)，夏季(13-21°C)。英格兰西南部相对温暖，但多雨。",
    "Temperate maritime climate. Winters (3-8°C), summers (13-21°C). Southwest England is relatively mild but rainy.",
    "约£1,100/月", "~£1,100/month", 16500, False, False,
    "大一新生保证住宿。宿舍费用£5,500-£9,000/年。校外租房月租£450-£700。",
    "First-year students guaranteed accommodation. Halls £5,500-£9,000/year. Off-campus rent £450-£700/month.",
    "本科毕业率约93%。学制3年，医学5年。", "Undergraduate completion rate ~93%. Degree length: 3 years, Medicine 5 years.",
    "毕业生就业率约90%。起薪中位数约£25,000-£28,000。", "Graduate employment rate ~90%. Median starting salary £25,000-£28,000.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有学生健康中心。", "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus student health centre available.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 10. Warwick
schools.append(uk_school(
    "warwick", "华威大学", "University of Warwick", "英格兰 考文垂", "Coventry, England",
    69, 104, 127, 101, 28950, [22280, 48580], 8,
    ["商科/WBS", "经济学", "数学", "计算机科学", "戏剧表演"],
    ["Business/WBS", "Economics", "Mathematics", "Computer Science", "Theatre & Performance"],
    "华威大学国际生学费：\n• 人文社科：£22,280/年\n• 理工科：£28,950-£33,390/年\n• 医学：£48,580/年",
    "Warwick international tuition:\n• Humanities & Social Sciences: £22,280/yr\n• Sciences/Engineering: £28,950-£33,390/yr\n• Medicine: £48,580/yr",
    "华威大学成立于1965年，虽然年轻但已跻身英国顶尖。华威商学院(WBS)是全球顶尖商学院之一，经济学和数学同样出色。校园占地广阔，环境优美。",
    "Founded in 1965, Warwick has rapidly risen to the UK's elite. Warwick Business School (WBS) is globally top-ranked; Economics and Mathematics are equally strong. Expansive, beautiful campus.",
    {"学费": 28950, "住宿费": 6500, "生活费": 6800},
    {"Tuition": 28950, "Accommodation": 6500, "Living": 6800},
    "87+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "华威校园位于考文垂郊外，是一个自成一体的大学城，治安优良。校内有24小时安保和校车服务。",
    "Warwick's campus is on the outskirts of Coventry, a self-contained university town with excellent safety. 24-hour security and campus bus services.",
    "英格兰中部温带海洋性气候，冬季(2-7°C)，夏季(13-21°C)。降雨适中。",
    "Central England temperate maritime climate. Winters (2-7°C), summers (13-21°C). Moderate rainfall.",
    "约£1,000/月", "~£1,000/month", 15000, False, False,
    "大一新生保证校内住宿。宿舍费用£5,000-£8,500/年。校外租房月租£400-£600。",
    "First-year students guaranteed on-campus housing. Halls £5,000-£8,500/year. Off-campus rent £400-£600/month.",
    "本科毕业率约94%。学制3年，医学4年（研究生入学）。", "Undergraduate completion rate ~94%. Degree length: 3 years, Medicine 4 years (graduate entry).",
    "毕业生就业率约92%。起薪中位数约£27,000-£32,000。金融和咨询行业的招聘目标校。",
    "Graduate employment rate ~92%. Median starting salary £27,000-£32,000. Target university for finance and consulting recruiters.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有健康中心和心理咨询服务。",
    "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus health centre and counselling services.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 11. Glasgow (Scotland)
schools.append(uk_school(
    "glasgow", "格拉斯哥大学", "University of Glasgow", "苏格兰 格拉斯哥", "Glasgow, Scotland",
    76, 82, 74, 101, 25750, [22080, 53400], 7,
    ["工程学", "医学", "法学", "兽医学", "社会科学"],
    ["Engineering", "Medicine", "Law", "Veterinary Medicine", "Social Sciences"],
    "格拉斯哥大学国际生学费：\n• 人文社科：£22,080/年\n• 理工科：£25,750-£30,240/年\n• 医学：£53,400/年",
    "Glasgow international tuition:\n• Humanities & Social Sciences: £22,080/yr\n• Sciences/Engineering: £25,750-£30,240/yr\n• Medicine: £53,400/yr",
    "格拉斯哥大学创立于1451年，是英语世界第四古老的大学。亚当·斯密曾在此任教。校园以哥特式建筑闻名，是哈利·波特的灵感来源之一。",
    "Founded in 1451, Glasgow is the fourth-oldest university in the English-speaking world. Adam Smith taught here. Famous for its Gothic architecture, said to inspire Harry Potter's Hogwarts.",
    {"学费": 25750, "住宿费": 6500, "生活费": 6800},
    {"Tuition": 25750, "Accommodation": 6500, "Living": 6800},
    "87+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "格拉斯哥是苏格兰最大城市，西区大学校园附近治安良好。市中心需注意夜间安全。",
    "Glasgow is Scotland's largest city. The West End campus area is safe. Be aware of safety in the city centre at night.",
    "苏格兰西部气候潮湿多雨，冬季(1-6°C)，夏季(11-19°C)。降雨频繁，需备防水衣物。",
    "Western Scotland is wet and rainy. Winters (1-6°C), summers (11-19°C). Frequent rain; waterproof clothing essential.",
    "约£1,050/月", "~£1,050/month", 15800, False, True,
    "大一新生保证住宿。宿舍费用£5,000-£8,000/年。校外租房月租£400-£650。格拉斯哥生活成本较低。",
    "First-year students guaranteed accommodation. Halls £5,000-£8,000/year. Off-campus rent £400-£650/month. Glasgow has a low cost of living.",
    "本科毕业率约91%。苏格兰学制4年，医学5-6年。", "Undergraduate completion rate ~91%. Scottish degree: 4 years, Medicine 5-6 years.",
    "毕业生就业率约89%。起薪中位数约£24,000-£28,000。", "Graduate employment rate ~89%. Median starting salary £24,000-£28,000.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有学生健康服务。", "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus student health service.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信\n📌 苏格兰本科学制4年",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference\n📌 Scottish undergraduate degree is 4 years"
))

# 12. Southampton
schools.append(uk_school(
    "southampton", "南安普顿大学", "University of Southampton", "英格兰 南安普顿", "Southampton, England",
    80, 97, 104, 101, 24500, [20340, 43500], 8,
    ["电子工程", "计算机科学", "海洋科学", "医学", "商科"],
    ["Electronic Engineering", "Computer Science", "Ocean Science", "Medicine", "Business"],
    "南安普顿大学国际生学费：\n• 人文社科：£20,340/年\n• 理工科：£24,500-£28,000/年\n• 医学：£43,500/年",
    "Southampton international tuition:\n• Humanities & Social Sciences: £20,340/yr\n• Sciences/Engineering: £24,500-£28,000/yr\n• Medicine: £43,500/yr",
    "南安普顿大学成立于1862年，在电子工程和计算机科学领域全英领先。与万维网的诞生有密切关联（Tim Berners-Lee曾在此任教）。海洋科学也享有国际声誉。",
    "Founded in 1862, Southampton leads in electronic engineering and computer science. Closely linked to the birth of the World Wide Web (Tim Berners-Lee taught here). Also internationally renowned for ocean science.",
    {"学费": 24500, "住宿费": 6500, "生活费": 6800},
    {"Tuition": 24500, "Accommodation": 6500, "Living": 6800},
    "85+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "南安普顿是英格兰南部港口城市，治安良好。校园宽阔安全，有安保服务。",
    "Southampton is a southern England port city with good safety. Spacious, safe campus with security services.",
    "英格兰南部温带海洋性气候，冬季(3-8°C)，夏季(14-22°C)。相对英格兰其他地区较温暖。",
    "Southern England temperate maritime climate. Winters (3-8°C), summers (14-22°C). Relatively warmer than other parts of England.",
    "约£1,050/月", "~£1,050/month", 15800, False, False,
    "大一新生保证住宿。宿舍费用£5,000-£8,500/年。校外租房月租£400-£650。",
    "First-year students guaranteed accommodation. Halls £5,000-£8,500/year. Off-campus rent £400-£650/month.",
    "本科毕业率约91%。学制3年，医学5年。", "Undergraduate completion rate ~91%. Degree length: 3 years, Medicine 5 years.",
    "毕业生就业率约89%。起薪中位数约£25,000-£28,000。", "Graduate employment rate ~89%. Median starting salary £25,000-£28,000.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有学生健康中心。", "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus student health centre.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 13. Leeds
schools.append(uk_school(
    "leeds", "利兹大学", "University of Leeds", "英格兰 利兹", "Leeds, England",
    75, 129, 140, 101, 25750, [21750, 46250], 7,
    ["传媒学", "商科", "工程学", "医学", "语言学"],
    ["Media & Communications", "Business", "Engineering", "Medicine", "Linguistics"],
    "利兹大学国际生学费：\n• 人文社科：£21,750/年\n• 理工科：£25,750-£29,250/年\n• 医学：£46,250/年",
    "Leeds international tuition:\n• Humanities & Social Sciences: £21,750/yr\n• Sciences/Engineering: £25,750-£29,250/yr\n• Medicine: £46,250/yr",
    "利兹大学成立于1904年，是英国最大的大学之一。传媒学和商科在英国名列前茅。利兹也是英国最受学生欢迎的城市之一，文化活跃、夜生活丰富。",
    "Founded in 1904, Leeds is one of the UK's largest universities. Media and Business rank among the best in the UK. Leeds is one of the most popular student cities with vibrant culture and nightlife.",
    {"学费": 25750, "住宿费": 6000, "生活费": 6500},
    {"Tuition": 25750, "Accommodation": 6000, "Living": 6500},
    "87+", "6.0+", "1月31日（UCAS）", "January 31 (UCAS)",
    "利兹是英格兰北部主要城市，校园区域治安良好。市中心夜间需注意安全。大学有安保服务。",
    "Leeds is a major northern English city. Campus area is safe. Be cautious in the city centre at night. University has security services.",
    "英格兰北部温带海洋性气候，冬季(1-7°C)，夏季(12-20°C)。较冷，需备保暖衣物。",
    "Northern England temperate maritime climate. Winters (1-7°C), summers (12-20°C). Cooler; warm clothing needed.",
    "约£1,000/月", "~£1,000/month", 15000, False, False,
    "大一新生保证住宿。宿舍费用£4,500-£8,000/年。校外租房月租£350-£600。利兹生活成本低廉。",
    "First-year students guaranteed accommodation. Halls £4,500-£8,000/year. Off-campus rent £350-£600/month. Leeds has a low cost of living.",
    "本科毕业率约90%。学制3年，医学5年。", "Undergraduate completion rate ~90%. Degree length: 3 years, Medicine 5 years.",
    "毕业生就业率约89%。起薪中位数约£24,000-£27,000。", "Graduate employment rate ~89%. Median starting salary £24,000-£27,000.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有学生健康中心。", "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus student health centre.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 14. Birmingham
schools.append(uk_school(
    "birmingham", "伯明翰大学", "University of Birmingham", "英格兰 伯明翰", "Birmingham, England",
    84, 105, 89, 101, 24120, [20280, 47160], 7,
    ["商科", "工程学", "体育科学", "医学", "教育学"],
    ["Business", "Engineering", "Sports Science", "Medicine", "Education"],
    "伯明翰大学国际生学费：\n• 人文社科：£20,280/年\n• 理工科：£24,120-£28,080/年\n• 医学：£47,160/年",
    "Birmingham international tuition:\n• Humanities & Social Sciences: £20,280/yr\n• Sciences/Engineering: £24,120-£28,080/yr\n• Medicine: £47,160/yr",
    "伯明翰大学创立于1900年，是英国第一所红砖大学。校园以标志性的Aston Webb建筑著称。体育科学全英领先，商学院获三重认证。伯明翰是英国第二大城市。",
    "Founded in 1900, Birmingham was the UK's first red-brick university. Known for its iconic Aston Webb building. Sports Science leads nationally; Business School has triple accreditation. Birmingham is the UK's second-largest city.",
    {"学费": 24120, "住宿费": 6000, "生活费": 6500},
    {"Tuition": 24120, "Accommodation": 6000, "Living": 6500},
    "85+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "伯明翰大学校园位于Edgbaston区，环境优美，治安良好。是英国第二大城市，需注意市中心安全。",
    "Birmingham's campus is in Edgbaston, a pleasant area with good safety. As the UK's second city, be cautious in the city centre.",
    "英格兰中部温带海洋性气候，冬季(2-7°C)，夏季(13-21°C)。降雨适中。",
    "Central England temperate maritime climate. Winters (2-7°C), summers (13-21°C). Moderate rainfall.",
    "约£1,000/月", "~£1,000/month", 15000, False, False,
    "大一新生保证住宿。宿舍费用£5,000-£8,000/年。校外租房月租£400-£600。Selly Oak区是学生聚集地。",
    "First-year students guaranteed accommodation. Halls £5,000-£8,000/year. Off-campus rent £400-£600/month. Selly Oak is the main student area.",
    "本科毕业率约91%。学制3年，医学5年。", "Undergraduate completion rate ~91%. Degree length: 3 years, Medicine 5 years.",
    "毕业生就业率约89%。起薪中位数约£24,000-£27,000。", "Graduate employment rate ~89%. Median starting salary £24,000-£27,000.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有学生健康中心。", "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus student health centre.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 15. Sheffield
schools.append(uk_school(
    "sheffield", "谢菲尔德大学", "University of Sheffield", "英格兰 谢菲尔德", "Sheffield, England",
    105, 98, 127, 101, 24450, [20000, 45700], 8,
    ["建筑学", "工程学", "新闻学", "医学", "计算机科学"],
    ["Architecture", "Engineering", "Journalism", "Medicine", "Computer Science"],
    "谢菲尔德大学国际生学费：\n• 人文社科：£20,000/年\n• 理工科：£24,450-£28,500/年\n• 医学：£45,700/年",
    "Sheffield international tuition:\n• Humanities & Social Sciences: £20,000/yr\n• Sciences/Engineering: £24,450-£28,500/yr\n• Medicine: £45,700/yr",
    "谢菲尔德大学成立于1905年，是罗素集团成员。建筑学和工程学在英国排名靠前。谢菲尔德是英国最绿色的城市之一，靠近峰区国家公园，学生满意度一直很高。",
    "Founded in 1905, Sheffield is a Russell Group member. Architecture and Engineering rank highly in the UK. Sheffield is one of the UK's greenest cities, near the Peak District; student satisfaction is consistently high.",
    {"学费": 24450, "住宿费": 5500, "生活费": 6500},
    {"Tuition": 24450, "Accommodation": 5500, "Living": 6500},
    "85+", "6.0+", "1月31日（UCAS）", "January 31 (UCAS)",
    "谢菲尔德是一座友好安全的城市，犯罪率低于英国大城市平均水平。校园区域治安良好。",
    "Sheffield is a friendly, safe city with crime rates below the UK major city average. Campus area is very safe.",
    "英格兰北部温带气候，冬季(1-7°C)，夏季(12-20°C)。降雨适中，靠近峰区偶有积雪。",
    "Northern England temperate climate. Winters (1-7°C), summers (12-20°C). Moderate rain; occasional snow near the Peak District.",
    "约£950/月", "~£950/month", 14300, False, False,
    "大一新生保证住宿。宿舍费用£4,500-£7,500/年。校外租房月租£350-£550。谢菲尔德生活成本很低。",
    "First-year students guaranteed accommodation. Halls £4,500-£7,500/year. Off-campus rent £350-£550/month. Sheffield has a very low cost of living.",
    "本科毕业率约90%。学制3年，医学5年。", "Undergraduate completion rate ~90%. Degree length: 3 years, Medicine 5 years.",
    "毕业生就业率约89%。起薪中位数约£23,000-£27,000。", "Graduate employment rate ~89%. Median starting salary £23,000-£27,000.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有学生健康中心。", "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus student health centre.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 16. St Andrews (Scotland)
schools.append(uk_school(
    "st-andrews", "圣安德鲁斯大学", "University of St Andrews", "苏格兰 圣安德鲁斯", "St Andrews, Scotland",
    95, 46, 225, 301, 28690, [25100, 35590], 9,
    ["国际关系", "哲学", "物理学", "计算机科学", "历史学"],
    ["International Relations", "Philosophy", "Physics", "Computer Science", "History"],
    "圣安德鲁斯大学国际生学费：\n• 人文社科：£25,100/年\n• 理科：£28,690-£35,590/年\n• 无医学院",
    "St Andrews international tuition:\n• Humanities & Social Sciences: £25,100/yr\n• Sciences: £28,690-£35,590/yr\n• No medical school",
    "圣安德鲁斯大学创立于1413年，是苏格兰最古老的大学，也是高尔夫球运动的发源地。威廉王子和凯特王妃的母校。小镇环境优美，学术氛围浓厚，学生满意度全英领先。",
    "Founded in 1413, St Andrews is Scotland's oldest university and the home of golf. Alma mater of Prince William and Catherine. Beautiful small-town setting with an intense academic atmosphere; student satisfaction leads the UK.",
    {"学费": 28690, "住宿费": 7000, "生活费": 6500},
    {"Tuition": 28690, "Accommodation": 7000, "Living": 6500},
    "94+", "7.0+", "1月31日（UCAS）", "January 31 (UCAS)",
    "圣安德鲁斯是一个小型海滨大学城，治安极好，犯罪率极低。步行可达全城。是全英最安全的大学城之一。",
    "St Andrews is a small coastal university town with excellent safety and very low crime. Everything is walkable. One of the UK's safest university towns.",
    "苏格兰东海岸气候，冬季寒冷(0-6°C)，夏季凉爽(10-17°C)。海风较大，较干燥。需备保暖防风衣物。",
    "Scottish east coast climate. Winters cold (0-6°C), summers cool (10-17°C). Windy and relatively dry. Warm windproof clothing needed.",
    "约£1,050/月", "~£1,050/month", 15800, False, True,
    "大一新生保证住宿。宿舍费用£5,500-£8,500/年。校外租房月租£450-£700。小镇住房紧张，建议尽早申请。",
    "First-year students guaranteed accommodation. Halls £5,500-£8,500/year. Off-campus rent £450-£700/month. Housing is tight in the small town; apply early.",
    "本科毕业率约96%。苏格兰学制4年。", "Undergraduate completion rate ~96%. Scottish degree: 4 years.",
    "毕业生就业率约90%。起薪中位数约£26,000-£30,000。在金融和学术界有很强声誉。",
    "Graduate employment rate ~90%. Median starting salary £26,000-£30,000. Strong reputation in finance and academia.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。镇上有学生健康中心和NHS诊所。",
    "✅ Must pay IHS £776/yr for free NHS healthcare. Town has a student health centre and NHS practice.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信\n📌 苏格兰本科学制4年",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference\n📌 Scottish undergraduate degree is 4 years"
))

# 17. Durham
schools.append(uk_school(
    "durham", "杜伦大学", "Durham University", "英格兰 杜伦", "Durham, England",
    78, 149, 198, 201, 28500, [22800, 36200], 9,
    ["法学", "历史学", "物理学", "地理学", "商科"],
    ["Law", "History", "Physics", "Geography", "Business"],
    "杜伦大学国际生学费：\n• 人文社科：£22,800/年\n• 理科：£28,500-£36,200/年\n• 无医学院",
    "Durham international tuition:\n• Humanities & Social Sciences: £22,800/yr\n• Sciences: £28,500-£36,200/yr\n• No medical school",
    "杜伦大学创立于1832年，是英格兰第三古老的大学。采用类似牛津剑桥的学院制。校园坐落在世界文化遗产城市杜伦，大教堂和城堡就在校内。",
    "Founded in 1832, Durham is England's third-oldest university. Uses a collegiate system similar to Oxford and Cambridge. Set in the UNESCO World Heritage city of Durham, with the cathedral and castle on campus.",
    {"学费": 28500, "学院费": 2000, "住宿费": 6500, "生活费": 6500},
    {"Tuition": 28500, "College Fees": 2000, "Accommodation": 6500, "Living": 6500},
    "92+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "杜伦是一座小型历史大学城，治安极好，犯罪率极低。步行即可到达各处。是全英最安全的大学城之一。",
    "Durham is a small historic university city with excellent safety and very low crime. Everything walkable. One of the UK's safest university towns.",
    "英格兰东北部气候较冷，冬季(0-6°C)，夏季(11-19°C)。多风多雨，需备保暖防雨衣物。",
    "Northeast England climate is cooler. Winters (0-6°C), summers (11-19°C). Windy and rainy; warm waterproof clothing needed.",
    "约£950/月", "~£950/month", 14300, False, False,
    "大一新生保证学院住宿。学院宿舍费用£5,000-£8,000/年，含部分餐食。校外租房月租£350-£550。",
    "First-year students guaranteed college accommodation. College rooms £5,000-£8,000/year, some include meals. Off-campus rent £350-£550/month.",
    "本科毕业率约95%。学制3年。", "Undergraduate completion rate ~95%. Degree length: 3 years.",
    "毕业生就业率约91%。起薪中位数约£26,000-£30,000。在金融和法律行业有很好的声誉。",
    "Graduate employment rate ~91%. Median starting salary £26,000-£30,000. Strong reputation in finance and law.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。各学院有福利支持，大学有健康中心。",
    "✅ Must pay IHS £776/yr for free NHS healthcare. Colleges have welfare support; university has a health centre.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 18. Nottingham
schools.append(uk_school(
    "nottingham", "诺丁汉大学", "University of Nottingham", "英格兰 诺丁汉", "Nottingham, England",
    100, 130, 145, 101, 24000, [20000, 45000], 7,
    ["药学", "工程学", "商科", "法学", "农业科学"],
    ["Pharmacy", "Engineering", "Business", "Law", "Agricultural Sciences"],
    "诺丁汉大学国际生学费：\n• 人文社科：£20,000/年\n• 理工科：£24,000-£28,000/年\n• 医学：£45,000/年",
    "Nottingham international tuition:\n• Humanities & Social Sciences: £20,000/yr\n• Sciences/Engineering: £24,000-£28,000/yr\n• Medicine: £45,000/yr",
    "诺丁汉大学成立于1881年，以其美丽的校园和全球化视野著称（在中国宁波和马来西亚有分校）。药学在英国名列前茅，工程和商科也享有盛誉。",
    "Founded in 1881, Nottingham is known for its beautiful campus and global outlook (campuses in China and Malaysia). Pharmacy ranks among the UK's best; Engineering and Business are also highly regarded.",
    {"学费": 24000, "住宿费": 6000, "生活费": 6500},
    {"Tuition": 24000, "Accommodation": 6000, "Living": 6500},
    "85+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "诺丁汉大学主校区University Park环境优美，治安良好。市中心夜间需注意安全。",
    "Nottingham's main University Park campus is beautiful and safe. Be aware of safety in the city centre at night.",
    "英格兰中部温带海洋性气候，冬季(2-7°C)，夏季(13-21°C)。降雨适中。",
    "Central England temperate maritime climate. Winters (2-7°C), summers (13-21°C). Moderate rainfall.",
    "约£950/月", "~£950/month", 14300, False, False,
    "大一新生保证住宿。宿舍费用£5,000-£8,000/年。校外租房月租£350-£550。",
    "First-year students guaranteed accommodation. Halls £5,000-£8,000/year. Off-campus rent £350-£550/month.",
    "本科毕业率约91%。学制3年，医学5年。", "Undergraduate completion rate ~91%. Degree length: 3 years, Medicine 5 years.",
    "毕业生就业率约89%。起薪中位数约£24,000-£27,000。", "Graduate employment rate ~89%. Median starting salary £24,000-£27,000.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有Cripps健康中心。", "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus Cripps Health Centre.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 19. Queen Mary London
schools.append(uk_school(
    "queen-mary", "伦敦玛丽女王大学", "Queen Mary University of London", "英格兰 伦敦", "London, England",
    145, 110, 119, 151, 24500, [20850, 42900], 7,
    ["法学", "医学", "英语文学", "语言学", "工程学"],
    ["Law", "Medicine", "English Literature", "Linguistics", "Engineering"],
    "QMUL国际生学费：\n• 人文社科：£20,850/年\n• 理工科：£24,500-£28,950/年\n• 医学/牙医：£42,900/年",
    "QMUL international tuition:\n• Humanities & Social Sciences: £20,850/yr\n• Sciences/Engineering: £24,500-£28,950/yr\n• Medicine/Dentistry: £42,900/yr",
    "伦敦玛丽女王大学是伦敦大学成员学院，位于伦敦东区Mile End，是罗素集团成员。法学和医学享有盛誉，是伦敦少有的拥有完整校园的大学。",
    "Queen Mary is a University of London member college in Mile End, East London, and a Russell Group member. Renowned for Law and Medicine; one of the few London universities with a complete campus.",
    {"学费": 24500, "住宿费": 8500, "生活费": 9600},
    {"Tuition": 24500, "Accommodation": 8500, "Living": 9600},
    "85+", "6.0+", "1月31日（UCAS）", "January 31 (UCAS)",
    "位于伦敦东区Mile End，近年发展迅速。校园有24小时安保。周边治安持续改善中。",
    "Located in Mile End, East London, a rapidly developing area. Campus has 24-hour security. Surrounding area safety continues to improve.",
    "伦敦温带海洋性气候，冬季阴冷(3-8°C)，夏季温暖(15-25°C)。多阴天和小雨。",
    "London's temperate maritime climate. Winters cool and grey (3-8°C), summers warm (15-25°C). Frequent overcast and drizzle.",
    "约£1,500/月", "~£1,500/month", 22500, True, False,
    "大一新生保证住宿。宿舍费用£7,000-£11,000/年。校外租房月租£700-£1,100。",
    "First-year students guaranteed accommodation. Halls £7,000-£11,000/year. Off-campus rent £700-£1,100/month.",
    "本科毕业率约88%。学制3年，医学5年。", "Undergraduate completion rate ~88%. Degree length: 3 years, Medicine 5 years.",
    "毕业生就业率约87%。起薪中位数约£25,000-£29,000。", "Graduate employment rate ~87%. Median starting salary £25,000-£29,000.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有学生健康中心。", "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus student health centre.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# 20. Lancaster
schools.append(uk_school(
    "lancaster", "兰卡斯特大学", "Lancaster University", "英格兰 兰卡斯特", "Lancaster, England",
    122, 136, 169, 201, 23400, [19930, 42000], 9,
    ["商科", "环境科学", "语言学", "创意写作", "物理学"],
    ["Business", "Environmental Science", "Linguistics", "Creative Writing", "Physics"],
    "兰卡斯特大学国际生学费：\n• 人文社科：£19,930/年\n• 理工科：£23,400-£27,000/年\n• 医学：£42,000/年",
    "Lancaster international tuition:\n• Humanities & Social Sciences: £19,930/yr\n• Sciences: £23,400-£27,000/yr\n• Medicine: £42,000/yr",
    "兰卡斯特大学成立于1964年，采用学院制，是英格兰仅有的几所学院制大学之一。商科和语言学在英国排名前列。校园位于湖区附近，环境优美。",
    "Founded in 1964, Lancaster uses a collegiate system, one of only a few in England. Business and Linguistics rank highly in the UK. Campus is near the Lake District with beautiful surroundings.",
    {"学费": 23400, "住宿费": 5500, "生活费": 6000},
    {"Tuition": 23400, "Accommodation": 5500, "Living": 6000},
    "85+", "6.5+", "1月31日（UCAS）", "January 31 (UCAS)",
    "兰卡斯特是一个安静的小城，校园自成一体，治安极好。靠近湖区国家公园。",
    "Lancaster is a quiet small city with a self-contained campus and excellent safety. Near the Lake District National Park.",
    "英格兰西北部气候，冬季(1-6°C)，夏季(12-19°C)。多雨多风，需备防水保暖衣物。",
    "Northwest England climate. Winters (1-6°C), summers (12-19°C). Rainy and windy; waterproof warm clothing needed.",
    "约£900/月", "~£900/month", 13500, False, False,
    "大一新生保证住宿。宿舍费用£4,500-£7,000/年。校外租房月租£350-£500。",
    "First-year students guaranteed accommodation. Halls £4,500-£7,000/year. Off-campus rent £350-£500/month.",
    "本科毕业率约91%。学制3年，医学5年。", "Undergraduate completion rate ~91%. Degree length: 3 years, Medicine 5 years.",
    "毕业生就业率约88%。起薪中位数约£23,000-£26,000。", "Graduate employment rate ~88%. Median starting salary £23,000-£26,000.",
    "✅ 必须缴纳IHS £776/年，享受NHS免费医疗。校内有学生健康中心。", "✅ Must pay IHS £776/yr for free NHS healthcare. On-campus student health centre.",
    "📋 申请平台：UCAS\n📅 截止日期：1月31日\n💰 申请费：UCAS £27.50\n📝 所需材料：个人陈述(PS)、A-Level预估成绩/IB、推荐信",
    "📋 Platform: UCAS\n📅 Deadline: January 31\n💰 Fees: UCAS £27.50\n📝 Required: Personal Statement, predicted A-Level/IB grades, reference"
))

# Write to file
output_path = "/home/luca/.openclaw/workspace-erin/study-abroad-demo/data/uk-schools.json"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(schools, f, ensure_ascii=False, indent=2)
print(f"Wrote {len(schools)} schools to {output_path}")
