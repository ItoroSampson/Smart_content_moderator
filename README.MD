 Smart Content Moderator

Automated image moderation using AWS Lambda, Rekognition, and S3.

 Architecture
- Trigger: S3 file upload
- AI Analysis: Amazon Rekognition  
- Processing: Lambda + Pillow
- Notifications: SNS alerts

Deployment
```bash
sam deploy

# Smart Content Moderator

AWS Serverless AI-powered content moderation system.

 Current Status: PHASE 1 COMPLETE
- ✅ Lambda function deployed
- ✅ Amazon Rekognition integration working
- ✅ Cross-region AI service calls (us-east-1)
- ✅ Base64 image testing capability

  Next Phase: S3 Integration
- Add S3 buckets for image upload/processing
- Manual S3 trigger configuration
- Full image moderation workflow

 Tech Stack
- AWS Lambda (Python 3.13)
- Amazon Rekognition (AI content analysis)
- AWS SAM (Infrastructure as Code)