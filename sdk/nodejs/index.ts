// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { CidrArgs, CidrResult, CidrOutputArgs } from "./cidr";
export const cidr: typeof import("./cidr").cidr = null as any;
export const cidrOutput: typeof import("./cidr").cidrOutput = null as any;
utilities.lazyLoad(exports, ["cidr","cidrOutput"], () => require("./cidr"));

export { ExtensionResourceArgs } from "./extensionResource";
export type ExtensionResource = import("./extensionResource").ExtensionResource;
export const ExtensionResource: typeof import("./extensionResource").ExtensionResource = null as any;
utilities.lazyLoad(exports, ["ExtensionResource"], () => require("./extensionResource"));

export { GetAccountIdResult } from "./getAccountId";
export const getAccountId: typeof import("./getAccountId").getAccountId = null as any;
utilities.lazyLoad(exports, ["getAccountId"], () => require("./getAccountId"));

export { GetAzsArgs, GetAzsResult, GetAzsOutputArgs } from "./getAzs";
export const getAzs: typeof import("./getAzs").getAzs = null as any;
export const getAzsOutput: typeof import("./getAzs").getAzsOutput = null as any;
utilities.lazyLoad(exports, ["getAzs","getAzsOutput"], () => require("./getAzs"));

export { GetPartitionResult } from "./getPartition";
export const getPartition: typeof import("./getPartition").getPartition = null as any;
utilities.lazyLoad(exports, ["getPartition"], () => require("./getPartition"));

export { GetRegionResult } from "./getRegion";
export const getRegion: typeof import("./getRegion").getRegion = null as any;
utilities.lazyLoad(exports, ["getRegion"], () => require("./getRegion"));

export { GetSsmParameterListArgs, GetSsmParameterListResult, GetSsmParameterListOutputArgs } from "./getSsmParameterList";
export const getSsmParameterList: typeof import("./getSsmParameterList").getSsmParameterList = null as any;
export const getSsmParameterListOutput: typeof import("./getSsmParameterList").getSsmParameterListOutput = null as any;
utilities.lazyLoad(exports, ["getSsmParameterList","getSsmParameterListOutput"], () => require("./getSsmParameterList"));

export { GetSsmParameterStringArgs, GetSsmParameterStringResult, GetSsmParameterStringOutputArgs } from "./getSsmParameterString";
export const getSsmParameterString: typeof import("./getSsmParameterString").getSsmParameterString = null as any;
export const getSsmParameterStringOutput: typeof import("./getSsmParameterString").getSsmParameterStringOutput = null as any;
utilities.lazyLoad(exports, ["getSsmParameterString","getSsmParameterStringOutput"], () => require("./getSsmParameterString"));

export { GetUrlSuffixResult } from "./getUrlSuffix";
export const getUrlSuffix: typeof import("./getUrlSuffix").getUrlSuffix = null as any;
utilities.lazyLoad(exports, ["getUrlSuffix"], () => require("./getUrlSuffix"));

export { ImportValueArgs, ImportValueResult, ImportValueOutputArgs } from "./importValue";
export const importValue: typeof import("./importValue").importValue = null as any;
export const importValueOutput: typeof import("./importValue").importValueOutput = null as any;
utilities.lazyLoad(exports, ["importValue","importValueOutput"], () => require("./importValue"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));


// Export enums:
export * from "./types/enums";

// Export sub-modules:
import * as accessanalyzer from "./accessanalyzer";
import * as acmpca from "./acmpca";
import * as amazonmq from "./amazonmq";
import * as amplify from "./amplify";
import * as amplifyuibuilder from "./amplifyuibuilder";
import * as apigateway from "./apigateway";
import * as apigatewayv2 from "./apigatewayv2";
import * as appconfig from "./appconfig";
import * as appflow from "./appflow";
import * as appintegrations from "./appintegrations";
import * as applicationautoscaling from "./applicationautoscaling";
import * as applicationinsights from "./applicationinsights";
import * as appmesh from "./appmesh";
import * as apprunner from "./apprunner";
import * as appstream from "./appstream";
import * as appsync from "./appsync";
import * as aps from "./aps";
import * as ask from "./ask";
import * as athena from "./athena";
import * as auditmanager from "./auditmanager";
import * as autoscaling from "./autoscaling";
import * as autoscalingplans from "./autoscalingplans";
import * as backup from "./backup";
import * as backupgateway from "./backupgateway";
import * as batch from "./batch";
import * as billingconductor from "./billingconductor";
import * as budgets from "./budgets";
import * as cassandra from "./cassandra";
import * as ce from "./ce";
import * as certificatemanager from "./certificatemanager";
import * as chatbot from "./chatbot";
import * as cloud9 from "./cloud9";
import * as cloudformation from "./cloudformation";
import * as cloudfront from "./cloudfront";
import * as cloudtrail from "./cloudtrail";
import * as cloudwatch from "./cloudwatch";
import * as codeartifact from "./codeartifact";
import * as codebuild from "./codebuild";
import * as codecommit from "./codecommit";
import * as codedeploy from "./codedeploy";
import * as codeguruprofiler from "./codeguruprofiler";
import * as codegurureviewer from "./codegurureviewer";
import * as codepipeline from "./codepipeline";
import * as codestar from "./codestar";
import * as codestarconnections from "./codestarconnections";
import * as codestarnotifications from "./codestarnotifications";
import * as cognito from "./cognito";
import * as comprehend from "./comprehend";
import * as config from "./config";
import * as configuration from "./configuration";
import * as connect from "./connect";
import * as connectcampaigns from "./connectcampaigns";
import * as controltower from "./controltower";
import * as cur from "./cur";
import * as customerprofiles from "./customerprofiles";
import * as databrew from "./databrew";
import * as datapipeline from "./datapipeline";
import * as datasync from "./datasync";
import * as dax from "./dax";
import * as detective from "./detective";
import * as devicefarm from "./devicefarm";
import * as devopsguru from "./devopsguru";
import * as directoryservice from "./directoryservice";
import * as dlm from "./dlm";
import * as dms from "./dms";
import * as docdb from "./docdb";
import * as docdbelastic from "./docdbelastic";
import * as dynamodb from "./dynamodb";
import * as ec2 from "./ec2";
import * as ecr from "./ecr";
import * as ecs from "./ecs";
import * as efs from "./efs";
import * as eks from "./eks";
import * as elasticache from "./elasticache";
import * as elasticbeanstalk from "./elasticbeanstalk";
import * as elasticloadbalancing from "./elasticloadbalancing";
import * as elasticloadbalancingv2 from "./elasticloadbalancingv2";
import * as elasticsearch from "./elasticsearch";
import * as emr from "./emr";
import * as emrcontainers from "./emrcontainers";
import * as emrserverless from "./emrserverless";
import * as events from "./events";
import * as eventschemas from "./eventschemas";
import * as evidently from "./evidently";
import * as finspace from "./finspace";
import * as fis from "./fis";
import * as fms from "./fms";
import * as forecast from "./forecast";
import * as frauddetector from "./frauddetector";
import * as fsx from "./fsx";
import * as gamecast from "./gamecast";
import * as gamelift from "./gamelift";
import * as globalaccelerator from "./globalaccelerator";
import * as glue from "./glue";
import * as grafana from "./grafana";
import * as greengrass from "./greengrass";
import * as greengrassv2 from "./greengrassv2";
import * as groundstation from "./groundstation";
import * as guardduty from "./guardduty";
import * as healthlake from "./healthlake";
import * as iam from "./iam";
import * as identitystore from "./identitystore";
import * as imagebuilder from "./imagebuilder";
import * as inspector from "./inspector";
import * as inspectorv2 from "./inspectorv2";
import * as internetmonitor from "./internetmonitor";
import * as iot from "./iot";
import * as iot1click from "./iot1click";
import * as iotanalytics from "./iotanalytics";
import * as iotcoredeviceadvisor from "./iotcoredeviceadvisor";
import * as iotevents from "./iotevents";
import * as iotfleethub from "./iotfleethub";
import * as iotfleetwise from "./iotfleetwise";
import * as iotsitewise from "./iotsitewise";
import * as iotthingsgraph from "./iotthingsgraph";
import * as iottwinmaker from "./iottwinmaker";
import * as iotwireless from "./iotwireless";
import * as ivs from "./ivs";
import * as ivschat from "./ivschat";
import * as kafkaconnect from "./kafkaconnect";
import * as kendra from "./kendra";
import * as kendraranking from "./kendraranking";
import * as kinesis from "./kinesis";
import * as kinesisanalytics from "./kinesisanalytics";
import * as kinesisanalyticsv2 from "./kinesisanalyticsv2";
import * as kinesisfirehose from "./kinesisfirehose";
import * as kinesisvideo from "./kinesisvideo";
import * as kms from "./kms";
import * as lakeformation from "./lakeformation";
import * as lambda from "./lambda";
import * as lex from "./lex";
import * as licensemanager from "./licensemanager";
import * as lightsail from "./lightsail";
import * as location from "./location";
import * as logs from "./logs";
import * as lookoutequipment from "./lookoutequipment";
import * as lookoutmetrics from "./lookoutmetrics";
import * as lookoutvision from "./lookoutvision";
import * as m2 from "./m2";
import * as macie from "./macie";
import * as managedblockchain from "./managedblockchain";
import * as mediaconnect from "./mediaconnect";
import * as mediaconvert from "./mediaconvert";
import * as medialive from "./medialive";
import * as mediapackage from "./mediapackage";
import * as mediastore from "./mediastore";
import * as mediatailor from "./mediatailor";
import * as memorydb from "./memorydb";
import * as msk from "./msk";
import * as mwaa from "./mwaa";
import * as neptune from "./neptune";
import * as networkfirewall from "./networkfirewall";
import * as networkmanager from "./networkmanager";
import * as nimblestudio from "./nimblestudio";
import * as oam from "./oam";
import * as omics from "./omics";
import * as opensearchserverless from "./opensearchserverless";
import * as opensearchservice from "./opensearchservice";
import * as opsworks from "./opsworks";
import * as opsworkscm from "./opsworkscm";
import * as organizations from "./organizations";
import * as osis from "./osis";
import * as panorama from "./panorama";
import * as personalize from "./personalize";
import * as pinpoint from "./pinpoint";
import * as pinpointemail from "./pinpointemail";
import * as pipes from "./pipes";
import * as proton from "./proton";
import * as qldb from "./qldb";
import * as quicksight from "./quicksight";
import * as ram from "./ram";
import * as rds from "./rds";
import * as redshift from "./redshift";
import * as redshiftserverless from "./redshiftserverless";
import * as refactorspaces from "./refactorspaces";
import * as rekognition from "./rekognition";
import * as resiliencehub from "./resiliencehub";
import * as resourceexplorer2 from "./resourceexplorer2";
import * as resourcegroups from "./resourcegroups";
import * as robomaker from "./robomaker";
import * as rolesanywhere from "./rolesanywhere";
import * as route53 from "./route53";
import * as route53recoverycontrol from "./route53recoverycontrol";
import * as route53recoveryreadiness from "./route53recoveryreadiness";
import * as route53resolver from "./route53resolver";
import * as rum from "./rum";
import * as s3 from "./s3";
import * as s3objectlambda from "./s3objectlambda";
import * as s3outposts from "./s3outposts";
import * as sagemaker from "./sagemaker";
import * as scheduler from "./scheduler";
import * as sdb from "./sdb";
import * as secretsmanager from "./secretsmanager";
import * as securityhub from "./securityhub";
import * as servicecatalog from "./servicecatalog";
import * as servicecatalogappregistry from "./servicecatalogappregistry";
import * as servicediscovery from "./servicediscovery";
import * as ses from "./ses";
import * as signer from "./signer";
import * as simspaceweaver from "./simspaceweaver";
import * as sns from "./sns";
import * as sqs from "./sqs";
import * as ssm from "./ssm";
import * as ssmcontacts from "./ssmcontacts";
import * as ssmincidents from "./ssmincidents";
import * as sso from "./sso";
import * as stepfunctions from "./stepfunctions";
import * as supportapp from "./supportapp";
import * as synthetics from "./synthetics";
import * as systemsmanagersap from "./systemsmanagersap";
import * as timestream from "./timestream";
import * as transfer from "./transfer";
import * as types from "./types";
import * as voiceid from "./voiceid";
import * as vpclattice from "./vpclattice";
import * as waf from "./waf";
import * as wafregional from "./wafregional";
import * as wafv2 from "./wafv2";
import * as wisdom from "./wisdom";
import * as workspaces from "./workspaces";
import * as xray from "./xray";

export {
    accessanalyzer,
    acmpca,
    amazonmq,
    amplify,
    amplifyuibuilder,
    apigateway,
    apigatewayv2,
    appconfig,
    appflow,
    appintegrations,
    applicationautoscaling,
    applicationinsights,
    appmesh,
    apprunner,
    appstream,
    appsync,
    aps,
    ask,
    athena,
    auditmanager,
    autoscaling,
    autoscalingplans,
    backup,
    backupgateway,
    batch,
    billingconductor,
    budgets,
    cassandra,
    ce,
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
    comprehend,
    config,
    configuration,
    connect,
    connectcampaigns,
    controltower,
    cur,
    customerprofiles,
    databrew,
    datapipeline,
    datasync,
    dax,
    detective,
    devicefarm,
    devopsguru,
    directoryservice,
    dlm,
    dms,
    docdb,
    docdbelastic,
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
    emrcontainers,
    emrserverless,
    events,
    eventschemas,
    evidently,
    finspace,
    fis,
    fms,
    forecast,
    frauddetector,
    fsx,
    gamecast,
    gamelift,
    globalaccelerator,
    glue,
    grafana,
    greengrass,
    greengrassv2,
    groundstation,
    guardduty,
    healthlake,
    iam,
    identitystore,
    imagebuilder,
    inspector,
    inspectorv2,
    internetmonitor,
    iot,
    iot1click,
    iotanalytics,
    iotcoredeviceadvisor,
    iotevents,
    iotfleethub,
    iotfleetwise,
    iotsitewise,
    iotthingsgraph,
    iottwinmaker,
    iotwireless,
    ivs,
    ivschat,
    kafkaconnect,
    kendra,
    kendraranking,
    kinesis,
    kinesisanalytics,
    kinesisanalyticsv2,
    kinesisfirehose,
    kinesisvideo,
    kms,
    lakeformation,
    lambda,
    lex,
    licensemanager,
    lightsail,
    location,
    logs,
    lookoutequipment,
    lookoutmetrics,
    lookoutvision,
    m2,
    macie,
    managedblockchain,
    mediaconnect,
    mediaconvert,
    medialive,
    mediapackage,
    mediastore,
    mediatailor,
    memorydb,
    msk,
    mwaa,
    neptune,
    networkfirewall,
    networkmanager,
    nimblestudio,
    oam,
    omics,
    opensearchserverless,
    opensearchservice,
    opsworks,
    opsworkscm,
    organizations,
    osis,
    panorama,
    personalize,
    pinpoint,
    pinpointemail,
    pipes,
    proton,
    qldb,
    quicksight,
    ram,
    rds,
    redshift,
    redshiftserverless,
    refactorspaces,
    rekognition,
    resiliencehub,
    resourceexplorer2,
    resourcegroups,
    robomaker,
    rolesanywhere,
    route53,
    route53recoverycontrol,
    route53recoveryreadiness,
    route53resolver,
    rum,
    s3,
    s3objectlambda,
    s3outposts,
    sagemaker,
    scheduler,
    sdb,
    secretsmanager,
    securityhub,
    servicecatalog,
    servicecatalogappregistry,
    servicediscovery,
    ses,
    signer,
    simspaceweaver,
    sns,
    sqs,
    ssm,
    ssmcontacts,
    ssmincidents,
    sso,
    stepfunctions,
    supportapp,
    synthetics,
    systemsmanagersap,
    timestream,
    transfer,
    types,
    voiceid,
    vpclattice,
    waf,
    wafregional,
    wafv2,
    wisdom,
    workspaces,
    xray,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:index:ExtensionResource":
                return new ExtensionResource(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "index", _module)
pulumi.runtime.registerResourcePackage("aws-native", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:aws-native") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
