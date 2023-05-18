// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ApiGatewayV2::RouteResponse
 */
export function getRouteResponse(args: GetRouteResponseArgs, opts?: pulumi.InvokeOptions): Promise<GetRouteResponseResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:apigatewayv2:getRouteResponse", {
        "id": args.id,
    }, opts);
}

export interface GetRouteResponseArgs {
    id: string;
}

export interface GetRouteResponseResult {
    readonly id?: string;
    readonly modelSelectionExpression?: string;
    readonly responseModels?: any;
    readonly responseParameters?: any;
    readonly routeResponseKey?: string;
}
/**
 * Resource Type definition for AWS::ApiGatewayV2::RouteResponse
 */
export function getRouteResponseOutput(args: GetRouteResponseOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetRouteResponseResult> {
    return pulumi.output(args).apply((a: any) => getRouteResponse(a, opts))
}

export interface GetRouteResponseOutputArgs {
    id: pulumi.Input<string>;
}
