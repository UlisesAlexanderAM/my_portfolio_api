import pulumi
import pulumi_aws as aws

app = aws.elasticbeanstalk.Application("job_hunting_helper")
app_env = aws.elasticbeanstalk.Environment(
    "app_env",
    application=app.name,
    solution_stack_name="64bit Amazon Linux 2023 v4.0.1 running Python 3.11",
)
