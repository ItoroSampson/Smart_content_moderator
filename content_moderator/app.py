import boto3
import json
import base64
import os


def get_rekognition_client():
    regions_to_try = ['eu-north-1', 'us-east-1', 'eu-west-1']
    
    for region in regions_to_try:
        try:
            print(f"🔄 Trying Rekognition in region: {region}")
            client = boto3.client('rekognition', region_name=region)
            
            client.detect_moderation_labels(
                Image={'Bytes': b'test'},  
                MinConfidence=60.0
            )
        except Exception as e:
            if "InvalidImageFormatException" in str(e):
                print(f"✅ Region {region} is reachable!")
                return boto3.client('rekognition', region_name=region)
            else:
                print(f"❌ Region {region} failed: {e}")
                continue
    
    
    print("🚨 All regions failed, using default")
    return boto3.client('rekognition')

rekognition = get_rekognition_client()

def lambda_handler(event, context):
    print("🚀 Content Moderator - Testing Rekognition Connectivity")
    
    try:
        
        test_image = base64.b64decode("/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCdABmX/9k=")
        
        response = rekognition.detect_moderation_labels(
            Image={'Bytes': test_image},
            MinConfidence=60.0
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'SUCCESS! Rekognition is working',
                'labels': response['ModerationLabels'],
                'region': rekognition._client_config.region_name
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'message': 'Rekognition connection failed'
            })
        }