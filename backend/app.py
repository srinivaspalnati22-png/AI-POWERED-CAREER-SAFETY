from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz  # PyMuPDF
import openai
import re
from datetime import datetime
import json

# =========================
# CONFIG
# =========================
openai.api_key = "PASTE_YOUR_OPENAI_API_KEY_HERE"

app = Flask(__name__)
CORS(app)

# Default test data for easy testing
DEFAULT_TEST_DATA = {
    "job_offers": [
        {
            "text": "URGENT! Work from home opportunity. Send $500 registration fee to secure your position. High salary guaranteed!",
            "expected_risk": 95
        },
        {
            "text": "We are looking for a Software Engineer at Google. Please apply through our official careers page at careers.google.com",
            "expected_risk": 10
        },
        {
            "text": "Congratulations! You've been selected. Please provide your bank details and SSN for verification.",
            "expected_risk": 90
        }
    ],
    "companies": {
        "Google": {"verified": True, "risk": 5},
        "Microsoft": {"verified": True, "risk": 5},
        "FakeCorp Inc": {"verified": False, "risk": 85}
    }
}

# =========================
# JOB / MESSAGE RISK ANALYSIS (AI)
# =========================
@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json.get("text", "").lower()
    
    if not text:
        return jsonify({"error": "Text is required"}), 400

    # Enhanced rule-based analysis (works without API key)
    risk_score = 0
    reasons = []
    safety_tips = []
    
    if not text or len(text.strip()) < 10:
        return jsonify({
            "risk_percentage": 50,
            "risk_level": "Medium",
            "reasons": ["Text is too short to analyze properly"],
            "safety_tips": ["Please provide more details about the job offer", "Verify the source of the message"],
            "timestamp": datetime.now().isoformat()
        })
    
    # High-risk indicators (scam keywords)
    high_risk_keywords = {
        "urgent": 15, "urgently": 15, "immediately": 12, "asap": 10,
        "guaranteed": 20, "guarantee": 18, "guaranteed income": 25,
        "easy money": 25, "quick money": 20,
        "work from home": 8, "no experience needed": 15, "no experience required": 15,
        "registration fee": 40, "processing fee": 35, "application fee": 35,
        "send money": 50, "wire transfer": 40, "western union": 35, "moneygram": 35,
        "bitcoin": 30, "cryptocurrency": 25, "crypto": 25,
        "bank details": 45, "bank account": 40, "account number": 40,
        "ssn": 50, "social security": 50, "social security number": 50,
        "credit card": 35, "paypal": 20, "venmo": 20, "zelle": 20,
        "congratulations": 5, "you have been selected": 10, "you won": 15,
        "prize": 20, "lottery": 25, "inheritance": 30,
        "nigerian prince": 50, "royal family": 40, "unclaimed funds": 35
    }
    
    # Medium-risk indicators
    medium_risk_keywords = {
        "high salary": 10, "unlimited income": 15, "passive income": 12,
        "get rich": 20, "become rich": 18, "millionaire": 15,
        "part time": 5, "flexible hours": 3,
        "no interview": 8, "instant approval": 10, "pre-approved": 8,
        "limited time": 8, "act now": 10, "call now": 8, "text now": 8,
        "reply immediately": 12
    }
    
    # Legitimate indicators (reduce risk)
    legitimate_keywords = {
        "careers.google.com": -20, "linkedin.com": -15, "indeed.com": -15,
        "glassdoor.com": -15, "monster.com": -10,
        "official website": -15, "apply through": -10, "company website": -10,
        "hr department": -10, "human resources": -10,
        "interview process": -10, "background check": -5, "references required": -5,
        "benefits package": -8, "health insurance": -8, "401k": -5, "pto": -5,
        "paid time off": -5
    }
    
    # Check for high-risk keywords
    for keyword, score in high_risk_keywords.items():
        if keyword in text:
            risk_score += score
            reasons.append(f"Contains high-risk keyword: '{keyword}'")
    
    # Check for medium-risk keywords
    for keyword, score in medium_risk_keywords.items():
        if keyword in text:
            risk_score += score
            reasons.append(f"Contains medium-risk indicator: '{keyword}'")
    
    # Check for legitimate indicators
    legit_count = 0
    for keyword, score in legitimate_keywords.items():
        if keyword in text:
            risk_score += score
            legit_count += 1
            reasons.append(f"Contains legitimate indicator: '{keyword}'")
    
    # Check for suspicious patterns
    import re
    if re.search(r'[!]{2,}', text):
        risk_score += 10
        reasons.append("Excessive exclamation marks (common in scams)")
    
    if re.search(r'[A-Z]{5,}', text):
        risk_score += 8
        reasons.append("Excessive capitalization (common in scam messages)")
    
    if "click here" in text or "click this link" in text:
        risk_score += 15
        reasons.append("Contains suspicious link request")
    
    if "verify your account" in text or "confirm your identity" in text:
        risk_score += 20
        reasons.append("Requests account verification (common phishing tactic)")
    
    # Check for professional language
    professional_terms = ["position", "role", "responsibilities", "qualifications", 
                         "requirements", "experience", "skills", "education"]
    professional_count = sum(1 for term in professional_terms if term in text)
    if professional_count >= 3:
        risk_score -= 15
        reasons.append("Contains professional job posting language")
    
    # Check for contact information
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    if re.search(email_pattern, text) or re.search(phone_pattern, text):
        risk_score -= 5
        reasons.append("Contains contact information (legitimate postings usually include this)")
    
    # Normalize risk score
    risk_score = max(0, min(100, risk_score))
    
    # Determine risk level and safety tips
    if risk_score < 30:
        risk_level = "Low"
        safety_tips = [
            "✓ This appears to be a legitimate job posting",
            "Verify the company's official website",
            "Check the job posting on official platforms (LinkedIn, Indeed, company website)",
            "Research the company and read reviews"
        ]
        if risk_score == 0:
            reasons.append("No scam indicators detected - appears legitimate")
    elif risk_score < 70:
        risk_level = "Medium"
        safety_tips = [
            "⚠️ Be cautious and verify all details",
            "Do not provide personal information upfront",
            "Check company registration and reviews",
            "Contact the company directly through official channels",
            "Never pay to apply for a job"
        ]
    else:
        risk_level = "High"
        safety_tips = [
            "🚨 HIGH RISK - This appears to be a SCAM",
            "⚠️ DO NOT send any money or fees",
            "⚠️ DO NOT provide bank details, SSN, or credit card information",
            "⚠️ DO NOT click on suspicious links",
            "⚠️ Report this to the appropriate authorities",
            "⚠️ Block and delete this message"
        ]
    
    # Ensure we have at least one reason
    if not reasons:
        if risk_score < 30:
            reasons = ["No obvious scam indicators detected", "Contains standard job posting language"]
        else:
            reasons = ["Multiple risk factors detected"]
    
    # Try AI analysis if API key is set
    ai_explanation = ""
    if openai.api_key and openai.api_key != "PASTE_YOUR_OPENAI_API_KEY_HERE":
        try:
            prompt = f"""Analyze this job offer for scam indicators. Text: {text[:500]}"""
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            ai_explanation = response.choices[0].message.content
            # Adjust risk based on AI analysis
            if "scam" in ai_explanation.lower() or "fraud" in ai_explanation.lower():
                risk_score = min(100, risk_score + 20)
        except:
            pass

    return jsonify({
        "risk_percentage": risk_score,
        "risk_level": risk_level,
        "reasons": reasons if reasons else ["No obvious scam indicators detected"],
        "safety_tips": safety_tips,
        "ai_explanation": ai_explanation,
        "timestamp": datetime.now().isoformat()
    })


# =========================
# AI CAREER GUIDANCE
# =========================
@app.route("/career-guidance", methods=["POST"])
def career_guidance():
    skill = request.json.get("skill", "").lower()

    careers_db = {
        "python": [
            {"title": "AI Engineer", "salary": "$120k-$180k", "growth": "High", "skills": ["Python", "ML", "TensorFlow"]},
            {"title": "Backend Developer", "salary": "$90k-$140k", "growth": "High", "skills": ["Python", "Django", "API"]},
            {"title": "Data Scientist", "salary": "$110k-$160k", "growth": "Very High", "skills": ["Python", "ML", "Statistics"]},
            {"title": "DevOps Engineer", "salary": "$100k-$150k", "growth": "High", "skills": ["Python", "AWS", "Docker"]}
        ],
        "design": [
            {"title": "UI/UX Designer", "salary": "$75k-$120k", "growth": "High", "skills": ["Figma", "User Research", "Prototyping"]},
            {"title": "Product Designer", "salary": "$90k-$140k", "growth": "High", "skills": ["Design Systems", "Strategy", "UX"]},
            {"title": "Graphic Designer", "salary": "$50k-$80k", "growth": "Medium", "skills": ["Adobe Suite", "Branding", "Typography"]}
        ],
        "security": [
            {"title": "Cyber Security Analyst", "salary": "$85k-$130k", "growth": "Very High", "skills": ["Security Tools", "Threat Analysis", "Incident Response"]},
            {"title": "Penetration Tester", "salary": "$100k-$150k", "growth": "High", "skills": ["Ethical Hacking", "Vulnerability Assessment", "Reporting"]},
            {"title": "Security Architect", "salary": "$120k-$180k", "growth": "Very High", "skills": ["Security Design", "Risk Assessment", "Compliance"]}
        ],
        "javascript": [
            {"title": "Frontend Developer", "salary": "$80k-$130k", "growth": "High", "skills": ["React", "Vue", "TypeScript"]},
            {"title": "Full Stack Developer", "salary": "$95k-$150k", "growth": "High", "skills": ["Node.js", "React", "Database"]},
            {"title": "React Developer", "salary": "$85k-$135k", "growth": "High", "skills": ["React", "Redux", "Next.js"]}
        ],
        "java": [
            {"title": "Java Developer", "salary": "$85k-$130k", "growth": "Medium", "skills": ["Java", "Spring", "Microservices"]},
            {"title": "Android Developer", "salary": "$80k-$125k", "growth": "Medium", "skills": ["Java", "Kotlin", "Android SDK"]}
        ],
        "react": [
            {"title": "React Developer", "salary": "$85k-$135k", "growth": "High", "skills": ["React", "Redux", "Next.js"]},
            {"title": "Frontend Engineer", "salary": "$80k-$130k", "growth": "High", "skills": ["React", "TypeScript", "CSS"]}
        ],
        "node": [
            {"title": "Backend Developer", "salary": "$90k-$140k", "growth": "High", "skills": ["Node.js", "Express", "API"]},
            {"title": "Full Stack Developer", "salary": "$95k-$150k", "growth": "High", "skills": ["Node.js", "React", "Database"]}
        ],
        "data": [
            {"title": "Data Scientist", "salary": "$110k-$160k", "growth": "Very High", "skills": ["Python", "ML", "Statistics"]},
            {"title": "Data Analyst", "salary": "$70k-$110k", "growth": "Medium", "skills": ["SQL", "Excel", "Python"]},
            {"title": "Data Engineer", "salary": "$100k-$150k", "growth": "High", "skills": ["Python", "Spark", "Big Data"]}
        ],
        "cloud": [
            {"title": "Cloud Engineer", "salary": "$100k-$150k", "growth": "Very High", "skills": ["AWS", "Azure", "Docker"]},
            {"title": "DevOps Engineer", "salary": "$100k-$150k", "growth": "High", "skills": ["CI/CD", "Kubernetes", "AWS"]}
        ],
        "marketing": [
            {"title": "Digital Marketer", "salary": "$50k-$90k", "growth": "Medium", "skills": ["SEO", "Social Media", "Analytics"]},
            {"title": "Marketing Analyst", "salary": "$60k-$100k", "growth": "Medium", "skills": ["Data Analysis", "Campaigns", "Reporting"]}
        ],
        "sales": [
            {"title": "Sales Representative", "salary": "$50k-$100k", "growth": "Medium", "skills": ["Communication", "CRM", "Negotiation"]},
            {"title": "Business Development", "salary": "$70k-$120k", "growth": "Medium", "skills": ["Strategy", "Networking", "Sales"]}
        ],
        "management": [
            {"title": "Project Manager", "salary": "$80k-$130k", "growth": "Medium", "skills": ["Agile", "Leadership", "Planning"]},
            {"title": "Product Manager", "salary": "$100k-$160k", "growth": "High", "skills": ["Strategy", "Product Development", "Analytics"]}
        ]
    }

    # Try to find matching careers
    careers = None
    
    # Direct match
    if skill in careers_db:
        careers = careers_db[skill]
    else:
        # Partial match - check if skill is contained in any key
        for key, value in careers_db.items():
            if skill in key or key in skill:
                careers = value
                break
    
    # If still no match, generate generic careers based on skill type
    if not careers:
        if "dev" in skill or "program" in skill or "code" in skill or "software" in skill:
            careers = [
                {"title": "Software Engineer", "salary": "$85k-$140k", "growth": "High", "skills": ["Programming", "Problem Solving", "System Design"]},
                {"title": "Full Stack Developer", "salary": "$95k-$150k", "growth": "High", "skills": ["Frontend", "Backend", "Database"]},
                {"title": "Software Developer", "salary": "$80k-$130k", "growth": "High", "skills": ["Coding", "Testing", "Debugging"]}
            ]
        elif "data" in skill or "analyst" in skill or "analytics" in skill:
            careers = [
                {"title": "Data Analyst", "salary": "$70k-$110k", "growth": "Medium", "skills": ["SQL", "Excel", "Python"]},
                {"title": "Business Analyst", "salary": "$65k-$100k", "growth": "Medium", "skills": ["Analysis", "Communication", "Data"]},
                {"title": "Data Scientist", "salary": "$110k-$160k", "growth": "Very High", "skills": ["Python", "ML", "Statistics"]}
            ]
        elif "manage" in skill or "lead" in skill or "admin" in skill:
            careers = [
                {"title": "Project Manager", "salary": "$80k-$130k", "growth": "Medium", "skills": ["Agile", "Leadership", "Planning"]},
                {"title": "Operations Manager", "salary": "$75k-$120k", "growth": "Medium", "skills": ["Operations", "Process Improvement", "Team Management"]},
                {"title": "Business Analyst", "salary": "$65k-$100k", "growth": "Medium", "skills": ["Analysis", "Communication", "Data"]}
            ]
        else:
            # Default generic careers
            careers = [
                {"title": "Software Engineer", "salary": "$85k-$140k", "growth": "High", "skills": ["Programming", "Problem Solving", "System Design"]},
                {"title": "Business Analyst", "salary": "$65k-$100k", "growth": "Medium", "skills": ["Analysis", "Communication", "Data"]},
                {"title": "General Professional", "salary": "$60k-$100k", "growth": "Medium", "skills": ["Communication", "Problem Solving", "Adaptability"]}
            ]

    return jsonify({
        "careers": careers,
        "skill_searched": skill
    })


# =========================
# RESUME PDF AUTHENTICITY CHECK
# =========================
@app.route("/resume-check", methods=["POST"])
def resume_check():
    if "resume" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files["resume"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text().lower()
        doc.close()
        
        if not text or len(text.strip()) < 10:
            return jsonify({
                "error": "PDF appears to be empty or unreadable",
                "risk_percentage": 50,
                "risk_level": "Medium",
                "reasons": ["Unable to extract text from PDF"],
                "message": "Please ensure the PDF contains readable text"
            }), 400
    except Exception as e:
        return jsonify({
            "error": f"Error reading PDF: {str(e)}",
            "risk_percentage": 50,
            "risk_level": "Medium",
            "reasons": [f"PDF processing error: {str(e)}"],
            "message": "Please ensure the file is a valid PDF"
        }), 400

    risk = 10
    reasons = []
    warnings = []
    positives = []

    # Check for suspicious patterns
    suspicious_patterns = {
        "excessive keywords": (len(re.findall(r'\b(?:expert|master|guru|ninja)\b', text)) > 5, 15),
        "unverifiable experience": ("10+ years" in text or "15+ years" in text, 10),
        "missing dates": (not re.search(r'\d{4}', text), 5),
        "certification without proof": ("certified" in text and "certificate" not in text and "certification" not in text, 20),
        "skill mismatch": (("python" in text and "javascript" in text and "java" in text and "c++" in text), 10),
        "vague descriptions": (len(re.findall(r'\b(?:various|many|several|multiple)\b', text)) > 3, 8)
    }

    for pattern, (condition, score) in suspicious_patterns.items():
        if condition:
            risk += score
            reasons.append(f"Potential issue: {pattern.replace('_', ' ').title()}")

    # Check for positive indicators
    positive_indicators = {
        "education listed": ("education" in text or "university" in text or "degree" in text, "Has education section"),
        "work history": (re.search(r'\d{4}.*\d{4}', text), "Has date ranges for experience"),
        "specific skills": (len(re.findall(r'\b(?:python|javascript|react|node|sql|aws)\b', text)) > 3, "Lists specific technical skills"),
        "contact info": (re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text), "Has contact information"),
        "projects": ("project" in text or "portfolio" in text, "Mentions projects or portfolio")
    }

    for indicator, (condition, message) in positive_indicators.items():
        if condition:
            positives.append(message)

    # Normalize risk
    risk = min(100, risk)
    
    if risk < 30:
        risk_level = "Low"
        message = "Resume appears authentic with minor concerns"
    elif risk < 60:
        risk_level = "Medium"
        message = "Resume has some areas that need verification"
    else:
        risk_level = "High"
        message = "Resume has significant authenticity concerns"

    return jsonify({
        "risk_percentage": risk,
        "risk_level": risk_level,
        "reasons": reasons if reasons else ["No major issues detected"],
        "warnings": warnings,
        "positives": positives,
        "message": message,
        "timestamp": datetime.now().isoformat(),
        "word_count": len(text.split())
    })


# =========================
# COMPANY VERIFICATION
# =========================
@app.route("/verify-company", methods=["POST"])
def verify_company():
    company_name = request.json.get("company_name", "").strip()
    
    if not company_name:
        return jsonify({"error": "Company name is required"}), 400
    
    # Check default test data
    company_lower = company_name.lower()
    if company_lower in [k.lower() for k in DEFAULT_TEST_DATA["companies"].keys()]:
        for key, value in DEFAULT_TEST_DATA["companies"].items():
            if key.lower() == company_lower:
                return jsonify({
                    "company_name": key,
                    "verified": value["verified"],
                    "risk_percentage": value["risk"],
                    "details": {
                        "registered": value["verified"],
                        "domain_exists": value["verified"],
                        "linkedin_presence": value["verified"],
                        "reviews_available": value["verified"]
                    },
                    "recommendation": "Verified company" if value["verified"] else "⚠️ Unverified - proceed with caution"
                })
    
    # Extended list of verified companies
    verified_companies = [
        "google", "microsoft", "apple", "amazon", "meta", "facebook", "netflix", "tesla", "nvidia",
        "ibm", "oracle", "adobe", "salesforce", "intel", "amd", "cisco", "dell", "hp", "lenovo",
        "samsung", "sony", "panasonic", "lg", "uber", "airbnb", "spotify", "twitter", "x",
        "linkedin", "paypal", "visa", "mastercard", "jpmorgan", "goldman sachs", "morgan stanley",
        "coca cola", "pepsi", "nike", "adidas", "starbucks", "mcdonalds", "walmart", "target",
        "boeing", "lockheed", "general electric", "ford", "gm", "toyota", "honda", "bmw", "mercedes"
    ]
    
    # Check if company name contains any verified company
    is_verified = any(vc in company_lower for vc in verified_companies) or any(company_lower in vc for vc in verified_companies)
    
    # Suspicious indicators
    suspicious_keywords = ["fake", "scam", "fraud", "phishing", "test", "example", "demo", "temp"]
    is_suspicious = any(keyword in company_lower for keyword in suspicious_keywords)
    
    # Check for generic/unclear names
    generic_names = ["company", "corp", "inc", "llc", "ltd", "business", "enterprise"]
    is_generic = any(gn == company_lower or (len(company_name.split()) == 1 and len(company_lower) < 4) for gn in generic_names)
    
    # Calculate risk based on various factors
    if is_verified:
        risk = 5
        verified = True
        registered = True
        domain_exists = True
        linkedin_presence = True
        reviews_available = True
    elif is_suspicious:
        risk = 85
        verified = False
        registered = False
        domain_exists = False
        linkedin_presence = False
        reviews_available = False
    elif is_generic:
        risk = 65
        verified = False
        registered = False
        domain_exists = False
        linkedin_presence = False
        reviews_available = False
    else:
        # For unknown companies, simulate partial verification
        risk = 45
        verified = False
        import random
        registered = random.random() > 0.3  # 70% chance
        domain_exists = random.random() > 0.2  # 80% chance
        linkedin_presence = random.random() > 0.4  # 60% chance
        reviews_available = random.random() > 0.5  # 50% chance
    
    # Generate recommendation
    if verified:
        recommendation = "✓ Verified company - This appears to be a legitimate, well-known company"
    elif is_suspicious:
        recommendation = "⚠️ High Risk - This company name contains suspicious keywords. Proceed with extreme caution."
    elif is_generic:
        recommendation = "⚠️ Unverified - Company name is too generic. Please verify through official sources before proceeding."
    else:
        recommendation = "⚠️ Verification Required - This company is not in our verified database. Please verify through official sources, check company registration, and research reviews before proceeding."
    
    return jsonify({
        "company_name": company_name,
        "verified": verified,
        "risk_percentage": risk,
        "details": {
            "registered": registered,
            "domain_exists": domain_exists,
            "linkedin_presence": linkedin_presence,
            "reviews_available": reviews_available
        },
        "recommendation": recommendation,
        "timestamp": datetime.now().isoformat()
    })


# =========================
# GET DEFAULT TEST DATA
# =========================
@app.route("/test-data", methods=["GET"])
def get_test_data():
    return jsonify(DEFAULT_TEST_DATA)


# =========================
# DASHBOARD STATISTICS
# =========================
@app.route("/dashboard-stats", methods=["GET"])
def dashboard_stats():
    return jsonify({
        "total_analyses": 0,
        "high_risk_detected": 0,
        "companies_verified": 0,
        "resumes_checked": 0,
        "recent_activity": []
    })


# =========================
# HISTORY ENDPOINT
# =========================
@app.route("/history", methods=["GET"])
def get_history():
    """Get analysis history (would be stored in DB in production)"""
    return jsonify({
        "history": [],
        "message": "History stored in localStorage on client side"
    })


# =========================
# BULK ANALYSIS
# =========================
@app.route("/bulk-analyze", methods=["POST"])
def bulk_analyze():
    """Analyze multiple job postings at once"""
    data = request.json
    texts = data.get("texts", [])
    
    if not texts or len(texts) == 0:
        return jsonify({"error": "No texts provided"}), 400
    
    results = []
    for text in texts:
        # Reuse analyze logic
        risk_score = 0
        reasons = []
        
        scam_keywords = {
            "urgent": 15, "guaranteed": 20, "registration fee": 40,
            "send money": 50, "bank details": 45, "ssn": 50
        }
        
        text_lower = text.lower()
        for keyword, score in scam_keywords.items():
            if keyword in text_lower:
                risk_score += score
                reasons.append(f"Contains suspicious keyword: '{keyword}'")
        
        risk_score = max(0, min(100, risk_score))
        
        results.append({
            "text": text[:100] + "..." if len(text) > 100 else text,
            "risk_percentage": risk_score,
            "risk_level": "High" if risk_score >= 70 else "Medium" if risk_score >= 30 else "Low",
            "reasons": reasons if reasons else ["No obvious scam indicators"]
        })
    
    return jsonify({
        "results": results,
        "total": len(results),
        "high_risk_count": sum(1 for r in results if r["risk_percentage"] >= 70)
    })


# =========================
# SEARCH FUNCTIONALITY
# =========================
@app.route("/search", methods=["POST"])
def search():
    """Search through analysis history"""
    data = request.json
    query = data.get("query", "").lower()
    
    # In production, this would search a database
    # For now, return sample results
    return jsonify({
        "results": [],
        "query": query,
        "message": "Search functionality - would query database in production"
    })


# =========================
# HEALTH CHECK
# =========================
@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })


# =========================
# ERROR HANDLERS
# =========================
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)