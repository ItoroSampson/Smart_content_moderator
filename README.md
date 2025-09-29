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
