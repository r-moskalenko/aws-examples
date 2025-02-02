import boto3
import random
import uuid

# Define the name of the S3 bucket
bucket_name = 'maksim-bucket'
#print(bucket_name)


# Initialize the S3 resource
s3 = boto3.resource('s3')

#s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'})

# List all available S3 buckets and print their names
for bucket in s3.buckets.all():
    print(bucket.name)

# Generate a random number of files (between 1 and 6) to upload
number_of_files = random.randint(1, 60)
print("Number of files:", number_of_files)

# Iterate through the range of files to create and upload them
for i in range(number_of_files):
    print("Processing file index:", i)
    filename = f'file_{i}.txt'  # Define a unique filename
    output_path = f"/tmp/{filename}"  # Set the local file path
    
    # Create and write a random UUID string to the file
    with open(output_path, 'w') as f:
        f.write(str(uuid.uuid4()))
        
    # Open the file in binary mode and upload it to the specified S3 bucket
    with open(output_path, 'rb') as data:
        s3.Bucket(bucket_name).put_object(Key=filename, Body=data)
