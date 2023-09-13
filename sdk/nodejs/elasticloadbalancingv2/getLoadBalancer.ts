// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElasticLoadBalancingV2::LoadBalancer
 */
export function getLoadBalancer(args: GetLoadBalancerArgs, opts?: pulumi.InvokeOptions): Promise<GetLoadBalancerResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:elasticloadbalancingv2:getLoadBalancer", {
        "loadBalancerArn": args.loadBalancerArn,
    }, opts);
}

export interface GetLoadBalancerArgs {
    /**
     * The Amazon Resource Name (ARN) of the load balancer.
     */
    loadBalancerArn: string;
}

export interface GetLoadBalancerResult {
    /**
     * The ID of the Amazon Route 53 hosted zone associated with the load balancer.
     */
    readonly canonicalHostedZoneId?: string;
    /**
     * The public DNS name of the load balancer.
     */
    readonly dnsName?: string;
    /**
     * The type of IP addresses used by the subnets for your load balancer. The possible values are ipv4 (for IPv4 addresses) and dualstack (for IPv4 and IPv6 addresses).
     */
    readonly ipAddressType?: string;
    /**
     * The Amazon Resource Name (ARN) of the load balancer.
     */
    readonly loadBalancerArn?: string;
    /**
     * The load balancer attributes.
     */
    readonly loadBalancerAttributes?: outputs.elasticloadbalancingv2.LoadBalancerAttribute[];
    /**
     * The full name of the load balancer.
     */
    readonly loadBalancerFullName?: string;
    /**
     * The name of the load balancer.
     */
    readonly loadBalancerName?: string;
    /**
     * The IDs of the security groups for the load balancer.
     */
    readonly securityGroups?: string[];
    /**
     * The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both.
     */
    readonly subnetMappings?: outputs.elasticloadbalancingv2.LoadBalancerSubnetMapping[];
    /**
     * The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both. To specify an Elastic IP address, specify subnet mappings instead of subnets.
     */
    readonly subnets?: string[];
    /**
     * The tags to assign to the load balancer.
     */
    readonly tags?: outputs.elasticloadbalancingv2.LoadBalancerTag[];
}
/**
 * Resource Type definition for AWS::ElasticLoadBalancingV2::LoadBalancer
 */
export function getLoadBalancerOutput(args: GetLoadBalancerOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLoadBalancerResult> {
    return pulumi.output(args).apply((a: any) => getLoadBalancer(a, opts))
}

export interface GetLoadBalancerOutputArgs {
    /**
     * The Amazon Resource Name (ARN) of the load balancer.
     */
    loadBalancerArn: pulumi.Input<string>;
}
