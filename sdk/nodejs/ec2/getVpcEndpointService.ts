// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPCEndpointService
 */
export function getVpcEndpointService(args: GetVpcEndpointServiceArgs, opts?: pulumi.InvokeOptions): Promise<GetVpcEndpointServiceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getVpcEndpointService", {
        "serviceId": args.serviceId,
    }, opts);
}

export interface GetVpcEndpointServiceArgs {
    serviceId: string;
}

export interface GetVpcEndpointServiceResult {
    readonly acceptanceRequired?: boolean;
    readonly gatewayLoadBalancerArns?: string[];
    readonly networkLoadBalancerArns?: string[];
    readonly payerResponsibility?: string;
    readonly serviceId?: string;
}
/**
 * Resource Type definition for AWS::EC2::VPCEndpointService
 */
export function getVpcEndpointServiceOutput(args: GetVpcEndpointServiceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVpcEndpointServiceResult> {
    return pulumi.output(args).apply((a: any) => getVpcEndpointService(a, opts))
}

export interface GetVpcEndpointServiceOutputArgs {
    serviceId: pulumi.Input<string>;
}
