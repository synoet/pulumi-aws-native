// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ApiGatewayV2::Api
 */
export function getApi(args: GetApiArgs, opts?: pulumi.InvokeOptions): Promise<GetApiResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:apigatewayv2:getApi", {
        "apiId": args.apiId,
    }, opts);
}

export interface GetApiArgs {
    apiId: string;
}

export interface GetApiResult {
    readonly apiEndpoint?: string;
    readonly apiId?: string;
    readonly apiKeySelectionExpression?: string;
    readonly corsConfiguration?: outputs.apigatewayv2.ApiCors;
    readonly description?: string;
    readonly disableExecuteApiEndpoint?: boolean;
    readonly name?: string;
    readonly routeSelectionExpression?: string;
    /**
     * This resource type use map for Tags, suggest to use List of Tag
     */
    readonly tags?: any;
    readonly version?: string;
}
/**
 * Resource Type definition for AWS::ApiGatewayV2::Api
 */
export function getApiOutput(args: GetApiOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetApiResult> {
    return pulumi.output(args).apply((a: any) => getApi(a, opts))
}

export interface GetApiOutputArgs {
    apiId: pulumi.Input<string>;
}
