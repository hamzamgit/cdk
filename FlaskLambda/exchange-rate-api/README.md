
# Exchange Rate API using CDK

This project is build using Lambda functions, API Gateway, EventBridge and DynamoDB and
deployed using AWS CDK.

We are scrapping currencies and current rate form the link below and populating it to the DynamoDB.
https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html

Scrap Lambda Endpoint:
- Collect 90days previous data
- Check if data is updated for 
- Parse xml and generate json
- populate DynamoDB with two dates in already present. else skip


Retreive Currency Lambda Endpoint
- Retreive Today rate from DynamoDB
- Retreive previous rate from DynamoDB
- Take a difference between current and previous dates.
- 

EventBridge
- Triggers Scrap Lambda function periodically.

DynamoDB Table
- Preserves data for scrapped items in the table.

## 1- Configure project

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

## 2. Deploy Application using CDK

To deploy the application to the cloud use commands mentioned below.

 * `cdk bootstrap`   Deployed cdk bootstrap to the AWS to deploy our application.
 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state


## Cheers!