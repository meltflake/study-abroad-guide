#!/usr/bin/env python3
"""Generate remaining CA schools (concordia, tmu, carleton) and merge with existing partial data."""
import json, sys

# The last 3 schools that need to be added
last_3 = [
  {
    "id": "concordia",
    "country": "CA", "flag": "\U0001f1e8\U0001f1e6",
    "name": {"zh": "\u5eb7\u8003\u8fea\u4e9a\u5927\u5b66", "en": "Concordia University"},
    "city": {"zh": "\u9b41\u5317\u514b\u7701 \u8499\u7279\u5229\u5c14", "en": "Montreal, QC"},
    "qs": 551, "the": 601, "usnews": 601, "arwu": 601,
    "tuition": 42000, "tuitionRange": [30000, 42000], "safety": 7,
    "majors": {
      "zh": ["\u827a\u672f\u4e0e\u8bbe\u8ba1", "\u5de5\u7a0b\u5b66", "\u8ba1\u7b97\u673a\u79d1\u5b66", "\u5546\u5b66", "\u7535\u5f71\u5236\u4f5c"],
      "en": ["Art & Design", "Engineering", "Computer Science", "Commerce", "Film Production"]
    },
    "majorTuition": {
      "zh": "\u5eb7\u8003\u8fea\u4e9a\u5927\u5b66\u56fd\u9645\u751f\u5b66\u8d39\uff1a\n\u2022 \u6587\u79d1/\u827a\u672f\uff1aC$30,000/\u5e74\n\u2022 \u7406\u79d1\uff1aC$33,000/\u5e74\n\u2022 \u5546\u5b66(JMSB)\uff1aC$38,000/\u5e74\n\u2022 \u5de5\u7a0b/CS\uff1aC$42,000/\u5e74",
      "en": "Concordia international tuition:\n\u2022 Arts/Fine Arts: C$30,000/yr\n\u2022 Science: C$33,000/yr\n\u2022 Commerce (JMSB): C$38,000/yr\n\u2022 Engineering/CS: C$42,000/yr"
    },
    "desc": {
      "zh": "\u8499\u7279\u5229\u5c14\u7684\u82f1\u8bed\u7efc\u5408\u6027\u5927\u5b66\uff0c\u4ee5\u827a\u672f\u4e0e\u8bbe\u8ba1\u3001\u7535\u5f71\u5236\u4f5c\u548c\u6e38\u620f\u8bbe\u8ba1\u95fb\u540d\u3002JMSB\u5546\u5b66\u9662\u83b7AACSB\u8ba4\u8bc1\uff0c\u5de5\u7a0b\u548c\u8ba1\u7b97\u673a\u79d1\u5b66\u6301\u7eed\u8fdb\u6b65\u3002\u6821\u56ed\u5206\u5e03\u5728\u5e02\u4e2d\u5fc3\u548c\u897f\u90e8\u4e24\u4e2a\u6821\u533a\u3002",
      "en": "Montreal's English-language comprehensive university, known for art & design, film production, and game design. JMSB business school is AACSB-accredited. Engineering and CS programs growing. Two campuses: downtown and west end."
    },
    "tuitionBreakdown": {
      "zh": {"\u5b66\u8d39": 42000, "\u98df\u5bbf": 13000, "\u4e66\u672c\u8d39": 1000, "\u6742\u8d39": 1200},
      "en": {"Tuition": 42000, "Room & Board": 13000, "Books": 1000, "Incidentals": 1200}
    },
    "requirements": {"TOEFL": "90+\uff08\u5355\u9879\u4e0d\u4f4e\u4e8e20\uff09", "IELTS": "6.5+\uff08\u5355\u9879\u4e0d\u4f4e\u4e8e5.5\uff09", "SAT": "\u4e0d\u8981\u6c42/Not Required"},
    "deadline": {"zh": "2\u67081\u65e5\uff08\u76f4\u63a5\u5411Concordia\u7533\u8bf7\uff09", "en": "February 1 (apply directly to Concordia)"},
    "safetyDetail": {
      "zh": "\u8499\u7279\u5229\u5c14\u6cbb\u5b89\u826f\u597d\u3002\u5e02\u4e2d\u5fc3\u6821\u533a\u4ea4\u901a\u4fbf\u5229\uff0c\u897f\u6821\u533a\u73af\u5883\u5b89\u9759\u5b89\u5168\u3002",
      "en": "Montreal has good safety. Downtown campus is well-connected by transit; west campus is quiet and secure."
    },
    "climate": {
      "zh": "\u51ac\u5b63\u6f2b\u957f\u5bd2\u51b7\uff08-15\u00b0C\u81f3-5\u00b0C\uff09\uff0c\u964d\u96ea\u91cf\u5927\u3002\u590f\u5b63\u6e29\u6696\u6e7f\u6da6\uff0820-26\u00b0C\uff09\u3002",
      "en": "Long, cold winters (-15\u00b0C to -5\u00b0C) with heavy snow. Warm, humid summers (20-26\u00b0C)."
    },
    "livingCost": {"zh": "\u7ea6C$1,400-1,800/\u6708", "en": "~C$1,400-1,800/month"},
    "livingCostAnnual": 14400, "insurance": 1000, "flights": 2200,
    "visa": {
      "zh": "Study Permit\u5b66\u4e60\u8bb8\u53ef \u2192 \u6bd5\u4e1a\u540e\u53ef\u7533\u8bf7PGWP\u5de5\u7b7e\uff08\u6700\u957f3\u5e74\uff09\u2192 \u901a\u8fc7Express Entry\u6216\u9b41\u7701PEQ\u9879\u76ee\u7533\u8bf7\u6c38\u4e45\u5c45\u7559\u3002",
      "en": "Study Permit \u2192 PGWP (up to 3 years) \u2192 PR via Express Entry or Quebec PEQ."
    },
    "housing": {
      "zh": "\U0001f3e0 \u6821\u5185\u5bbf\u820d\uff1a\u7ea6C$9,000-14,000/\u5e74\n\U0001f3e2 \u6821\u5916\u79df\u623f\uff1a\u8499\u7279\u5229\u5c14\u79df\u91d1\u5b9e\u60e0\uff0cStudio\u7ea6C$1,000-1,500/\u6708\n\U0001f4cd \u63a8\u8350\u533a\u57df\uff1aNDG\u3001Westmount\u9644\u8fd1\u3001\u5e02\u4e2d\u5fc3",
      "en": "\U0001f3e0 On-campus: ~C$9,000-14,000/yr\n\U0001f3e2 Off-campus: Montreal affordable rents, studio ~C$1,000-1,500/mo\n\U0001f4cd Recommended: NDG, near Westmount, downtown"
    },
    "graduationRate": {
      "zh": "\u672c\u79d1\u56db\u5e74\u6bd5\u4e1a\u7387\u7ea660%\uff0c\u516d\u5e74\u6bd5\u4e1a\u7387\u7ea670%\u3002",
      "en": "4-year graduation rate ~60%, 6-year rate ~70%."
    },
    "employment": {
      "zh": "\U0001f4ca \u6bd5\u4e1a6\u4e2a\u6708\u5185\u5c31\u4e1a\u7387\u7ea682%\n\U0001f4bc \u6e38\u620f\u4ea7\u4e1a\uff08Ubisoft\u3001EA\uff09\u3001\u5f71\u89c6\u5236\u4f5c\u3001\u79d1\u6280\u521b\u4e1a\n\U0001f31f \u827a\u672f\u548c\u8bbe\u8ba1\u4e13\u4e1a\u5728\u8499\u7279\u5229\u5c14\u521b\u610f\u4ea7\u4e1a\u4e2d\u5f88\u53d7\u6b22\u8fce",
      "en": "\U0001f4ca ~82% employed within 6 months\n\U0001f4bc Gaming (Ubisoft, EA), film production, tech startups\n\U0001f31f Art and design grads popular in Montreal's creative industry"
    },
    "healthcare": {
      "zh": "\u2705 \u9b41\u7701\u56fd\u9645\u5b66\u751f\u9700\u52a0\u5165RAMQ\u6216\u8d2d\u4e70\u5b66\u6821\u5065\u5eb7\u4fdd\u9669\u3002",
      "en": "\u2705 Quebec international students need RAMQ or university health insurance."
    },
    "application": {
      "zh": "\U0001f4cb \u7533\u8bf7\u5e73\u53f0\uff1a\u76f4\u63a5\u901a\u8fc7Concordia\u5b98\u7f51\u7533\u8bf7\uff08\u9b41\u7701\u72ec\u7acb\u7cfb\u7edf\uff09\n\U0001f4c5 \u622a\u6b62\u65e5\u671f\uff1a2\u67081\u65e5\n\U0001f4b0 \u7533\u8bf7\u8d39\uff1aC$100\n\U0001f4dd \u6240\u9700\u6750\u6599\uff1a\u9ad8\u4e2d\u6210\u7ee9\u5355\u3001\u8bed\u8a00\u6210\u7ee9\u3001\u4f5c\u54c1\u96c6\uff08\u827a\u672f\u4e13\u4e1a\uff09",
      "en": "\U0001f4cb Platform: Apply directly via Concordia website (Quebec separate system)\n\U0001f4c5 Deadline: February 1\n\U0001f4b0 Fee: C$100\n\U0001f4dd Materials: Transcripts, English proficiency, portfolio (art programs)"
    }
  },
  {
    "id": "tmu",
    "country": "CA", "flag": "\U0001f1e8\U0001f1e6",
    "name": {"zh": "\u591a\u4f26\u591a\u90fd\u5e02\u5927\u5b66", "en": "Toronto Metropolitan University"},
    "city": {"zh": "\u5b89\u5927\u7565\u7701 \u591a\u4f26\u591a", "en": "Toronto, ON"},
    "qs": 801, "the": 601, "usnews": 801, "arwu": 801,
    "tuition": 45000, "tuitionRange": [33000, 45000], "safety": 7,
    "majors": {
      "zh": ["\u5546\u5b66", "\u5de5\u7a0b\u5b66", "\u8ba1\u7b97\u673a\u79d1\u5b66", "\u65b0\u95fb\u4f20\u5a92", "\u521b\u610f\u4ea7\u4e1a"],
      "en": ["Commerce", "Engineering", "Computer Science", "Journalism", "Creative Industries"]
    },
    "majorTuition": {
      "zh": "TMU\u56fd\u9645\u751f\u5b66\u8d39\uff1a\n\u2022 \u6587\u79d1/\u4f20\u5a92\uff1aC$33,000/\u5e74\n\u2022 \u7406\u79d1\uff1aC$36,000/\u5e74\n\u2022 \u5546\u5b66(TRSM)\uff1aC$40,000/\u5e74\n\u2022 \u5de5\u7a0b/CS\uff1aC$45,000/\u5e74",
      "en": "TMU international tuition:\n\u2022 Arts/Media: C$33,000/yr\n\u2022 Science: C$36,000/yr\n\u2022 Commerce (TRSM): C$40,000/yr\n\u2022 Engineering/CS: C$45,000/yr"
    },
    "desc": {
      "zh": "\u4f4d\u4e8e\u591a\u4f26\u591a\u5e02\u4e2d\u5fc3\u7684\u5e94\u7528\u578b\u5927\u5b66\uff0c\u4ee5\u521b\u4e1a\u521b\u65b0\u95fb\u540d\u3002\u62e5\u6709\u52a0\u62ff\u5927\u6700\u5927\u7684\u672c\u79d1\u5546\u5b66\u9662\u4e4b\u4e00\uff0c\u65b0\u95fb\u4f20\u5a92\u548c\u521b\u610f\u4ea7\u4e1a\u4e13\u4e1a\u5b9e\u529b\u5f3a\u3002\u6821\u56ed\u5730\u5904\u591a\u4f26\u591a\u6700\u7e41\u534e\u5730\u6bb5\uff0c\u5b9e\u4e60\u673a\u4f1a\u4e30\u5bcc\u3002",
      "en": "An applied university in downtown Toronto known for entrepreneurship and innovation. One of Canada's largest undergraduate business schools. Strong in journalism, media, and creative industries. Campus in Toronto's busiest area with abundant internship opportunities."
    },
    "tuitionBreakdown": {
      "zh": {"\u5b66\u8d39": 45000, "\u98df\u5bbf": 16000, "\u4e66\u672c\u8d39": 1000, "\u6742\u8d39": 1800},
      "en": {"Tuition": 45000, "Room & Board": 16000, "Books": 1000, "Incidentals": 1800}
    },
    "requirements": {"TOEFL": "83+\uff08\u5355\u9879\u4e0d\u4f4e\u4e8e20\uff09", "IELTS": "6.5+\uff08\u5355\u9879\u4e0d\u4f4e\u4e8e6.0\uff09", "SAT": "\u4e0d\u8981\u6c42/Not Required"},
    "deadline": {"zh": "2\u67081\u65e5\uff08\u5b89\u7701OUAC 105\uff09", "en": "February 1 (via OUAC 105)"},
    "safetyDetail": {
      "zh": "\u6821\u56ed\u4f4d\u4e8e\u591a\u4f26\u591a\u5e02\u4e2d\u5fc3\uff0c\u4eba\u6d41\u5bc6\u96c6\uff0c\u6574\u4f53\u5b89\u5168\u3002\u6709\u6821\u56ed\u5b89\u4fdd\u548c\u7d27\u6025\u7535\u8bdd\u7cfb\u7edf\u3002\u665a\u95f4\u6ce8\u610f\u5468\u8fb9\u73af\u5883\u3002",
      "en": "Campus in busy downtown Toronto, generally safe. Campus security and emergency phone system available. Be aware of surroundings at night."
    },
    "climate": {
      "zh": "\u56db\u5b63\u5206\u660e\uff0c\u51ac\u5b63\u5bd2\u51b7\uff08-7\u00b0C\u81f3-1\u00b0C\uff09\uff0c\u5e38\u6709\u964d\u96ea\u3002\u590f\u5b63\u6e29\u6696\u5b9c\u4eba\uff0820-27\u00b0C\uff09\u3002",
      "en": "Four distinct seasons. Cold winters (-7\u00b0C to -1\u00b0C) with frequent snow. Pleasant summers (20-27\u00b0C)."
    },
    "livingCost": {"zh": "\u7ea6C$2,000-2,500/\u6708", "en": "~C$2,000-2,500/month"},
    "livingCostAnnual": 19200, "insurance": 1100, "flights": 2200,
    "visa": {
      "zh": "Study Permit\u5b66\u4e60\u8bb8\u53ef \u2192 \u6bd5\u4e1a\u540e\u53ef\u7533\u8bf7PGWP\u5de5\u7b7e\uff08\u6700\u957f3\u5e74\uff09\u2192 \u901a\u8fc7Express Entry\u6216\u5b89\u7701\u7701\u63d0\u540d(OINP)\u7533\u8bf7\u6c38\u4e45\u5c45\u7559\u3002",
      "en": "Study Permit \u2192 PGWP (up to 3 years) \u2192 PR via Express Entry or Ontario PNP (OINP)."
    },
    "housing": {
      "zh": "\U0001f3e0 \u6821\u5185\u5bbf\u820d\uff1a\u6709\u9650\uff0c\u7ea6C$12,000-17,000/\u5e74\n\U0001f3e2 \u6821\u5916\u79df\u623f\uff1a\u591a\u4f26\u591a\u5e02\u4e2d\u5fc3Studio\u7ea6C$1,800-2,400/\u6708\n\U0001f4cd \u63a8\u8350\u533a\u57df\uff1aChurch-Yonge Corridor\u3001Cabbagetown\u3001Garden District",
      "en": "\U0001f3e0 On-campus: Limited, ~C$12,000-17,000/yr\n\U0001f3e2 Off-campus: Downtown Toronto studio ~C$1,800-2,400/mo\n\U0001f4cd Recommended: Church-Yonge Corridor, Cabbagetown, Garden District"
    },
    "graduationRate": {
      "zh": "\u672c\u79d1\u56db\u5e74\u6bd5\u4e1a\u7387\u7ea668%\uff0c\u516d\u5e74\u6bd5\u4e1a\u7387\u7ea676%\u3002",
      "en": "4-year graduation rate ~68%, 6-year rate ~76%."
    },
    "employment": {
      "zh": "\U0001f4ca \u6bd5\u4e1a6\u4e2a\u6708\u5185\u5c31\u4e1a\u7387\u7ea685%\n\U0001f4bc \u521b\u4e1a\u5b75\u5316\u5668(DMZ)\u5168\u7403\u6392\u540d\u7b2c\u4e00\uff0c\u79d1\u6280\u521b\u4e1a\u6c1b\u56f4\u6d53\u539a\n\U0001f31f \u4f4d\u4e8e\u591a\u4f26\u591a\u5e02\u4e2d\u5fc3\uff0c\u5b9e\u4e60\u548c\u5c31\u4e1a\u673a\u4f1a\u6781\u5176\u4fbf\u5229",
      "en": "\U0001f4ca ~85% employed within 6 months\n\U0001f4bc DMZ startup incubator ranked #1 globally; strong tech entrepreneurship\n\U0001f31f Downtown Toronto location offers exceptional internship and job access"
    },
    "healthcare": {
      "zh": "\u2705 \u5b89\u7701\u56fd\u9645\u5b66\u751f\u9700\u8d2d\u4e70UHIP\uff0c\u7ea6C$756/\u5e74\u3002",
      "en": "\u2705 Ontario international students must enroll in UHIP, ~C$756/yr."
    },
    "application": {
      "zh": "\U0001f4cb \u7533\u8bf7\u5e73\u53f0\uff1aOUAC 105\u901a\u9053\n\U0001f4c5 \u622a\u6b62\u65e5\u671f\uff1a2\u67081\u65e5\n\U0001f4b0 \u7533\u8bf7\u8d39\uff1aC$150\uff08OUAC + \u8865\u5145\u8d39\uff09\n\U0001f4dd \u6240\u9700\u6750\u6599\uff1a\u9ad8\u4e2d\u6210\u7ee9\u5355\u3001\u8bed\u8a00\u6210\u7ee9",
      "en": "\U0001f4cb Platform: OUAC Stream 105\n\U0001f4c5 Deadline: February 1\n\U0001f4b0 Fee: C$150 (OUAC + supplementary)\n\U0001f4dd Materials: Transcripts, English proficiency"
    }
  },
  {
    "id": "carleton",
    "country": "CA", "flag": "\U0001f1e8\U0001f1e6",
    "name": {"zh": "\u5361\u5c14\u987f\u5927\u5b66", "en": "Carleton University"},
    "city": {"zh": "\u5b89\u5927\u7565\u7701 \u6e25\u592a\u534e", "en": "Ottawa, ON"},
    "qs": 601, "the": 601, "usnews": 601, "arwu": 601,
    "tuition": 48000, "tuitionRange": [33000, 48000], "safety": 8,
    "majors": {
      "zh": ["\u5de5\u7a0b\u5b66", "\u8ba1\u7b97\u673a\u79d1\u5b66", "\u56fd\u9645\u4e8b\u52a1", "\u5efa\u7b51\u5b66", "\u65b0\u95fb\u4f20\u5a92"],
      "en": ["Engineering", "Computer Science", "International Affairs", "Architecture", "Journalism"]
    },
    "majorTuition": {
      "zh": "\u5361\u5c14\u987f\u5927\u5b66\u56fd\u9645\u751f\u5b66\u8d39\uff1a\n\u2022 \u6587\u79d1/\u793e\u79d1\uff1aC$33,000/\u5e74\n\u2022 \u7406\u79d1\uff1aC$36,000/\u5e74\n\u2022 \u5546\u5b66(Sprott)\uff1aC$42,000/\u5e74\n\u2022 \u5de5\u7a0b/CS\uff1aC$48,000/\u5e74",
      "en": "Carleton international tuition:\n\u2022 Arts/Social Sciences: C$33,000/yr\n\u2022 Science: C$36,000/yr\n\u2022 Commerce (Sprott): C$42,000/yr\n\u2022 Engineering/CS: C$48,000/yr"
    },
    "desc": {
      "zh": "\u4f4d\u4e8e\u52a0\u62ff\u5927\u9996\u90fd\u6e25\u592a\u534e\u7684\u7efc\u5408\u6027\u5927\u5b66\uff0c\u4ee5\u5de5\u7a0b\u3001\u8ba1\u7b97\u673a\u79d1\u5b66\u3001\u56fd\u9645\u4e8b\u52a1\u548c\u65b0\u95fb\u4e13\u4e1a\u95fb\u540d\u3002\u4e0e\u8054\u90a6\u653f\u5e9c\u548c\u79d1\u6280\u884c\u4e1a\u8054\u7cfb\u7d27\u5bc6\uff0cCo-op\u9879\u76ee\u4f18\u79c0\u3002\u6821\u56ed\u6cbfRideau\u8fd0\u6cb3\u800c\u5efa\uff0c\u73af\u5883\u4f18\u7f8e\u3002",
      "en": "A comprehensive university in Canada's capital Ottawa, known for engineering, CS, international affairs, and journalism. Strong ties to federal government and tech sector. Excellent co-op programs. Beautiful campus along the Rideau Canal."
    },
    "tuitionBreakdown": {
      "zh": {"\u5b66\u8d39": 48000, "\u98df\u5bbf": 13000, "\u4e66\u672c\u8d39": 1000, "\u6742\u8d39": 1500},
      "en": {"Tuition": 48000, "Room & Board": 13000, "Books": 1000, "Incidentals": 1500}
    },
    "requirements": {"TOEFL": "86+\uff08\u5199\u4f5c/\u53e3\u8bed22+\uff09", "IELTS": "6.5+\uff08\u5355\u9879\u4e0d\u4f4e\u4e8e6.0\uff09", "SAT": "\u4e0d\u8981\u6c42/Not Required"},
    "deadline": {"zh": "4\u67081\u65e5\uff08\u5b89\u7701OUAC 105\uff09", "en": "April 1 (via OUAC 105)"},
    "safetyDetail": {
      "zh": "\u6e25\u592a\u534e\u662f\u52a0\u62ff\u5927\u9996\u90fd\uff0c\u6cbb\u5b89\u975e\u5e38\u597d\u3002\u6821\u56ed\u6cbf\u8fd0\u6cb3\u800c\u5efa\uff0c\u73af\u5883\u5b89\u9759\u5b89\u5168\u3002",
      "en": "Ottawa is Canada's capital with excellent safety. Campus along the canal, quiet and secure environment."
    },
    "climate": {
      "zh": "\u51ac\u5b63\u5bd2\u51b7\uff08-15\u00b0C\u81f3-5\u00b0C\uff09\uff0c\u964d\u96ea\u91cf\u5927\u3002\u590f\u5b63\u6e29\u6696\uff0820-26\u00b0C\uff09\u3002\u6821\u56ed\u5730\u4e0b\u901a\u9053\u7cfb\u7edf\u53ef\u907f\u5bd2\u3002",
      "en": "Cold winters (-15\u00b0C to -5\u00b0C) with heavy snow. Warm summers (20-26\u00b0C). Campus underground tunnel system helps beat the cold."
    },
    "livingCost": {"zh": "\u7ea6C$1,400-1,800/\u6708", "en": "~C$1,400-1,800/month"},
    "livingCostAnnual": 14400, "insurance": 900, "flights": 2200,
    "visa": {
      "zh": "Study Permit\u5b66\u4e60\u8bb8\u53ef \u2192 \u6bd5\u4e1a\u540e\u53ef\u7533\u8bf7PGWP\u5de5\u7b7e\uff08\u6700\u957f3\u5e74\uff09\u2192 \u901a\u8fc7Express Entry\u6216\u5b89\u7701\u7701\u63d0\u540d(OINP)\u7533\u8bf7\u6c38\u4e45\u5c45\u7559\u3002",
      "en": "Study Permit \u2192 PGWP (up to 3 years) \u2192 PR via Express Entry or Ontario PNP (OINP)."
    },
    "housing": {
      "zh": "\U0001f3e0 \u6821\u5185\u5bbf\u820d\uff1a\u5927\u4e00\u4fdd\u8bc1\u4f4f\u5bbf\uff0c\u7ea6C$9,500-14,000/\u5e74\n\U0001f3e2 \u6821\u5916\u79df\u623f\uff1a\u6e25\u592a\u534e\u79df\u91d1\u4e2d\u7b49\uff0cStudio\u7ea6C$1,200-1,600/\u6708\n\U0001f4cd \u63a8\u8350\u533a\u57df\uff1aOld Ottawa South\u3001Glebe\u3001Heron Park",
      "en": "\U0001f3e0 On-campus: Guaranteed for first year, ~C$9,500-14,000/yr\n\U0001f3e2 Off-campus: Ottawa moderate rents, studio ~C$1,200-1,600/mo\n\U0001f4cd Recommended: Old Ottawa South, Glebe, Heron Park"
    },
    "graduationRate": {
      "zh": "\u672c\u79d1\u56db\u5e74\u6bd5\u4e1a\u7387\u7ea668%\uff0c\u516d\u5e74\u6bd5\u4e1a\u7387\u7ea676%\u3002",
      "en": "4-year graduation rate ~68%, 6-year rate ~76%."
    },
    "employment": {
      "zh": "\U0001f4ca \u6bd5\u4e1a6\u4e2a\u6708\u5185\u5c31\u4e1a\u7387\u7ea685%\n\U0001f4bc \u8054\u90a6\u653f\u5e9c\u3001\u79d1\u6280\u516c\u53f8\uff08Shopify\u3001BlackBerry QNX\uff09\u3001\u56fd\u9632\u4ea7\u4e1a\n\U0001f31f Co-op\u9879\u76ee\u4e0e\u653f\u5e9c\u548c\u79d1\u6280\u884c\u4e1a\u5408\u4f5c\u5e7f\u6cdb",
      "en": "\U0001f4ca ~85% employed within 6 months\n\U0001f4bc Federal government, tech (Shopify, BlackBerry QNX), defence\n\U0001f31f Co-op programs with extensive government and tech partnerships"
    },
    "healthcare": {
      "zh": "\u2705 \u5b89\u7701\u56fd\u9645\u5b66\u751f\u9700\u8d2d\u4e70UHIP\uff0c\u7ea6C$756/\u5e74\u3002\u6821\u5185\u6709\u5065\u5eb7\u670d\u52a1\u4e2d\u5fc3\u3002",
      "en": "\u2705 Ontario international students must enroll in UHIP, ~C$756/yr. On-campus Health Services available."
    },
    "application": {
      "zh": "\U0001f4cb \u7533\u8bf7\u5e73\u53f0\uff1aOUAC 105\u901a\u9053\n\U0001f4c5 \u622a\u6b62\u65e5\u671f\uff1a4\u67081\u65e5\n\U0001f4b0 \u7533\u8bf7\u8d39\uff1aC$150\uff08OUAC + \u8865\u5145\u8d39\uff09\n\U0001f4dd \u6240\u9700\u6750\u6599\uff1a\u9ad8\u4e2d\u6210\u7ee9\u5355\u3001\u8bed\u8a00\u6210\u7ee9",
      "en": "\U0001f4cb Platform: OUAC Stream 105\n\U0001f4c5 Deadline: April 1\n\U0001f4b0 Fee: C$150 (OUAC + supplementary)\n\U0001f4dd Materials: Transcripts, English proficiency"
    }
  }
]

# Write just these 3 as a temp file
with open('/tmp/last3_ca.json', 'w') as f:
    json.dump(last_3, f, ensure_ascii=False, indent=2)
print(f"Wrote {len(last_3)} schools to /tmp/last3_ca.json")
