from constructs import Construct
from aws_cdk import (
    Stack,
    App,
    RemovalPolicy,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_s3 as s3,
    aws_sns_subscriptions as subs,
)


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.myBucket = s3.Bucket(self, "RomanMBucket", 
                  block_public_access=s3.BlockPublicAccess.BLOCK_ALL, 
                  encryption=s3.BucketEncryption.S3_MANAGED, 
                  enforce_ssl=True, 
                  versioned=False, 
                  removal_policy=RemovalPolicy.RETAIN)

