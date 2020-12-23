# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .cidr import *
from .get_account_id import *
from .get_azs import *
from .get_partition import *
from .get_region import *
from .get_ssm_parameter_list import *
from .get_ssm_parameter_string import *
from .get_stack_id import *
from .get_stack_name import *
from .get_url_suffix import *
from .import_value import *
from .provider import *
from ._inputs import *
from . import outputs

# Make subpackages available:
from . import (
    accessanalyzer,
    acmpca,
    amazonmq,
    amplify,
    apigateway,
    apigatewayv2,
    appconfig,
    appflow,
    applicationautoscaling,
    applicationinsights,
    appmesh,
    appstream,
    appsync,
    ask,
    athena,
    auditmanager,
    autoscaling,
    autoscalingplans,
    backup,
    batch,
    budgets,
    cassandra,
    certificatemanager,
    chatbot,
    cloud9,
    cloudformation,
    cloudfront,
    cloudtrail,
    cloudwatch,
    codeartifact,
    codebuild,
    codecommit,
    codedeploy,
    codeguruprofiler,
    codegurureviewer,
    codepipeline,
    codestar,
    codestarconnections,
    codestarnotifications,
    cognito,
    config,
    configuration,
    databrew,
    datapipeline,
    dax,
    detective,
    devopsguru,
    directoryservice,
    dlm,
    dms,
    docdb,
    dynamodb,
    ec2,
    ecr,
    ecs,
    efs,
    eks,
    elasticache,
    elasticbeanstalk,
    elasticloadbalancing,
    elasticloadbalancingv2,
    elasticsearch,
    emr,
    events,
    eventschemas,
    fms,
    fsx,
    gamelift,
    globalaccelerator,
    glue,
    greengrass,
    greengrassv2,
    groundstation,
    guardduty,
    iam,
    imagebuilder,
    inspector,
    iot,
    iot1click,
    iotanalytics,
    iotevents,
    iotsitewise,
    iotthingsgraph,
    ivs,
    kendra,
    kinesis,
    kinesisanalytics,
    kinesisanalyticsv2,
    kinesisfirehose,
    kms,
    lakeformation,
    lambda_,
    licensemanager,
    logs,
    macie,
    managedblockchain,
    mediaconvert,
    medialive,
    mediapackage,
    mediastore,
    msk,
    mwaa,
    neptune,
    networkfirewall,
    networkmanager,
    opsworks,
    opsworkscm,
    pinpoint,
    pinpointemail,
    qldb,
    ram,
    rds,
    redshift,
    resourcegroups,
    robomaker,
    route53,
    route53resolver,
    s3,
    sagemaker,
    sdb,
    secretsmanager,
    securityhub,
    servicecatalog,
    servicediscovery,
    ses,
    signer,
    sns,
    sqs,
    ssm,
    sso,
    stepfunctions,
    synthetics,
    timestream,
    transfer,
    waf,
    wafregional,
    wafv2,
    workspaces,
)

def _register_module():
    import pulumi
    from . import _utilities


    class Package(pulumi.runtime.ResourcePackage):
        _version = _utilities.get_semver_version()

        def version(self):
            return Package._version

        def construct_provider(self, name: str, typ: str, urn: str) -> pulumi.ProviderResource:
            if typ != "pulumi:providers:cloudformation":
                raise Exception(f"unknown provider type {typ}")
            return Provider(name, pulumi.ResourceOptions(urn=urn))


    pulumi.runtime.register_resource_package("cloudformation", Package())

_register_module()
