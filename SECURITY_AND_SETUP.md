# CareerSafe Backend - Security & Setup Guide

## 🔒 Security Improvements Applied

### Critical Fixes
✅ **API Key Security**: Moved from hardcoded to environment variables
✅ **CORS Hardening**: Restricted to localhost only (update for production)
✅ **Rate Limiting**: Implemented per-endpoint rate limiting
✅ **Input Validation**: Added length checks and sanitization
✅ **File Upload Validation**: Type and size restrictions on PDF uploads
✅ **Error Handling**: Proper status codes with secure error messages
✅ **Logging**: Improved logging with rotation (10MB per file, 5 backups)

## 🚀 Quick Start

### 1. Set Environment Variables
```bash
# Windows CMD
set GEMINI_API_KEY=your_api_key_here
set PORT=5000
set DEBUG=False

# Windows PowerShell
$env:GEMINI_API_KEY="your_api_key_here"
$env:PORT=5000
$env:DEBUG="False"

# Linux/Mac
export GEMINI_API_KEY=your_api_key_here
export PORT=5000
export DEBUG=False
```

### 2. Get Gemini API Key
1. Visit: https://ai.google.dev/
2. Click "Get API Key"
3. Create a new API key
4. Copy and paste it to your environment variable

### 3. Start Server
```bash
python app.py
```

Expected startup output:
```
============================================================
Starting CareerSafe Backend Server
============================================================
API Key Configured: True
Rate Limiting: 100 requests per 3600s
Max Text Length: 10000 chars
Max File Size: 50MB
============================================================
 * Running on http://0.0.0.0:5000
```

## 📋 Rate Limiting (Per Endpoint)

| Endpoint | Limit | Window |
|----------|-------|--------|
| `/analyze` | 20 | 60s |
| `/verify-company` | 15 | 60s |
| `/career-guidance` | 15 | 60s |
| `/resume-check` | 10 | 60s |
| `/bulk-analyze` | 5 | 60s |
| `/search` | 30 | 60s |

Exceeding limits returns `429 Too Many Requests`

## 📏 Input Validation

| Parameter | Max Length | Notes |
|-----------|-----------|-------|
| Text (analyze) | 10,000 chars | Must be 1+ chars |
| Company Name | 500 chars | HTML chars removed |
| Resume File | 50MB | PDF only |
| Skill | 200 chars | For career guidance |
| Search Query | 200 chars | For search |
| Bulk Texts | 50 items | Max 50 per request |

## 📊 API Response Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad Request (validation failed) |
| 404 | Endpoint not found |
| 429 | Rate limit exceeded |
| 500 | Internal server error |
| 503 | Service degraded |

## 🔍 Testing Endpoints

### Test 1: Health Check
```bash
curl http://localhost:5000/health
```

### Test 2: Analyze Text
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "Work from home opportunity, send $500 registration fee"}'
```

### Test 3: Verify Company
```bash
curl -X POST http://localhost:5000/verify-company \
  -H "Content-Type: application/json" \
  -d '{"company_name": "Google"}'
```

### Test 4: Get Test Data
```bash
curl http://localhost:5000/test-data
```

### Test 5: Dashboard Stats
```bash
curl http://localhost:5000/dashboard-stats
```

## 📝 Logging

Log files are created in the working directory:
- **app.log**: Main application log (rotated at 10MB)
- **Backups**: app.log.1, app.log.2, etc. (max 5 backups)

View recent logs:
```bash
# Last 50 lines
tail -50 app.log

# Watch logs in real-time
tail -f app.log

# Filter for errors
grep ERROR app.log

# Filter for warnings
grep WARNING app.log
```

## 🔧 For Production

### 1. Security Checklist
- [ ] Change CORS origins to your domain
- [ ] Set `DEBUG=False`
- [ ] Use strong API key (rotate regularly)
- [ ] Enable HTTPS/TLS
- [ ] Set up firewall rules
- [ ] Monitor logs regularly
- [ ] Implement authentication (optional)
- [ ] Add API key validation

### 2. Update CORS
Edit line 77 in app.py:
```python
CORS(app, 
     resources={r"/*": {"origins": ["https://yourdomain.com"], ...}},
     supports_credentials=False)
```

### 3. Environment Configuration
```bash
export GEMINI_API_KEY=prod_key_here
export PORT=5000
export DEBUG=False
```

### 4. Deployment Options
- **Render**: Uses PORT env var, set GEMINI_API_KEY in dashboard
- **Railway**: Same as Render
- **Heroku**: Create Procfile (already exists), set config vars
- **AWS**: Use ECS/Lambda with environment variables

## 🐛 Troubleshooting

### Issue: "GEMINI_API_KEY not set"
**Solution**: 
```bash
# Check if env var is set
echo $GEMINI_API_KEY  # Linux/Mac
echo %GEMINI_API_KEY%  # Windows CMD
```

### Issue: "429 Rate Limit Exceeded"
**Solution**: Wait 60 seconds before making more requests to that endpoint

### Issue: "File size exceeds limit"
**Solution**: Resume PDF must be < 50MB

### Issue: "Only PDF files supported"
**Solution**: Ensure resume file has .pdf extension

### Issue: Connection refused
**Solution**: 
- Check if server is running
- Verify PORT matches in curl command
- Check firewall settings

## 📈 Performance Tips

1. **Disable debug mode** in production
2. **Use rate limiting** to prevent abuse
3. **Monitor log files** for errors
4. **Cache responses** for repeated queries
5. **Use async processing** for bulk operations

## 📚 API Documentation

All endpoints return JSON responses. See `/health` endpoint for status.

### Response Format
```json
{
  "error": "string (only on errors)",
  "status": 200,
  "data": {},
  "timestamp": "2024-01-01T00:00:00.000000"
}
```

## 🆘 Support

For issues:
1. Check error message in app.log
2. Verify API key is set correctly
3. Check rate limits haven't been exceeded
4. Verify input validation requirements
5. Contact: [Support Email]

---
**Last Updated**: 2024
**Version**: 1.0.0
