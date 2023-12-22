// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AppSync::GraphQLApi
 */
export function getGraphQlApi(args: GetGraphQlApiArgs, opts?: pulumi.InvokeOptions): Promise<GetGraphQlApiResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:appsync:getGraphQlApi", {
        "id": args.id,
    }, opts);
}

export interface GetGraphQlApiArgs {
    id: string;
}

export interface GetGraphQlApiResult {
    readonly additionalAuthenticationProviders?: outputs.appsync.GraphQlApiAdditionalAuthenticationProvider[];
    readonly apiId?: string;
    readonly apiType?: string;
    readonly arn?: string;
    readonly authenticationType?: string;
    readonly graphQlDns?: string;
    readonly graphQlEndpointArn?: string;
    readonly graphQlUrl?: string;
    readonly id?: string;
    readonly lambdaAuthorizerConfig?: outputs.appsync.GraphQlApiLambdaAuthorizerConfig;
    readonly logConfig?: outputs.appsync.GraphQlApiLogConfig;
    readonly mergedApiExecutionRoleArn?: string;
    readonly name?: string;
    readonly openIdConnectConfig?: outputs.appsync.GraphQlApiOpenIdConnectConfig;
    readonly ownerContact?: string;
    readonly realtimeDns?: string;
    readonly realtimeUrl?: string;
    readonly tags?: outputs.appsync.GraphQlApiTag[];
    readonly userPoolConfig?: outputs.appsync.GraphQlApiUserPoolConfig;
    readonly visibility?: string;
    readonly xrayEnabled?: boolean;
}
/**
 * Resource Type definition for AWS::AppSync::GraphQLApi
 */
export function getGraphQlApiOutput(args: GetGraphQlApiOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetGraphQlApiResult> {
    return pulumi.output(args).apply((a: any) => getGraphQlApi(a, opts))
}

export interface GetGraphQlApiOutputArgs {
    id: pulumi.Input<string>;
}
