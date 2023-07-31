// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Route53Resolver::ResolverEndpoint
 */
export function getResolverEndpoint(args: GetResolverEndpointArgs, opts?: pulumi.InvokeOptions): Promise<GetResolverEndpointResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:route53resolver:getResolverEndpoint", {
        "resolverEndpointId": args.resolverEndpointId,
    }, opts);
}

export interface GetResolverEndpointArgs {
    resolverEndpointId: string;
}

export interface GetResolverEndpointResult {
    readonly arn?: string;
    readonly hostVpcId?: string;
    readonly ipAddressCount?: string;
    readonly ipAddresses?: outputs.route53resolver.ResolverEndpointIpAddressRequest[];
    readonly name?: string;
    readonly resolverEndpointId?: string;
    readonly resolverEndpointType?: string;
    readonly tags?: outputs.route53resolver.ResolverEndpointTag[];
}
/**
 * Resource Type definition for AWS::Route53Resolver::ResolverEndpoint
 */
export function getResolverEndpointOutput(args: GetResolverEndpointOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetResolverEndpointResult> {
    return pulumi.output(args).apply((a: any) => getResolverEndpoint(a, opts))
}

export interface GetResolverEndpointOutputArgs {
    resolverEndpointId: pulumi.Input<string>;
}
