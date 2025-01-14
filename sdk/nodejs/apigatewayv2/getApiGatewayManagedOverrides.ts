// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ApiGatewayV2::ApiGatewayManagedOverrides
 */
export function getApiGatewayManagedOverrides(args: GetApiGatewayManagedOverridesArgs, opts?: pulumi.InvokeOptions): Promise<GetApiGatewayManagedOverridesResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:apigatewayv2:getApiGatewayManagedOverrides", {
        "id": args.id,
    }, opts);
}

export interface GetApiGatewayManagedOverridesArgs {
    id: string;
}

export interface GetApiGatewayManagedOverridesResult {
    readonly id?: string;
    readonly integration?: outputs.apigatewayv2.ApiGatewayManagedOverridesIntegrationOverrides;
    readonly route?: outputs.apigatewayv2.ApiGatewayManagedOverridesRouteOverrides;
    readonly stage?: outputs.apigatewayv2.ApiGatewayManagedOverridesStageOverrides;
}
/**
 * Resource Type definition for AWS::ApiGatewayV2::ApiGatewayManagedOverrides
 */
export function getApiGatewayManagedOverridesOutput(args: GetApiGatewayManagedOverridesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetApiGatewayManagedOverridesResult> {
    return pulumi.output(args).apply((a: any) => getApiGatewayManagedOverrides(a, opts))
}

export interface GetApiGatewayManagedOverridesOutputArgs {
    id: pulumi.Input<string>;
}
