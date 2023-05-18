// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElasticLoadBalancing::LoadBalancer
 */
export function getLoadBalancer(args: GetLoadBalancerArgs, opts?: pulumi.InvokeOptions): Promise<GetLoadBalancerResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:elasticloadbalancing:getLoadBalancer", {
        "id": args.id,
    }, opts);
}

export interface GetLoadBalancerArgs {
    id: string;
}

export interface GetLoadBalancerResult {
    readonly accessLoggingPolicy?: outputs.elasticloadbalancing.LoadBalancerAccessLoggingPolicy;
    readonly appCookieStickinessPolicy?: outputs.elasticloadbalancing.LoadBalancerAppCookieStickinessPolicy[];
    readonly availabilityZones?: string[];
    readonly canonicalHostedZoneName?: string;
    readonly canonicalHostedZoneNameID?: string;
    readonly connectionDrainingPolicy?: outputs.elasticloadbalancing.LoadBalancerConnectionDrainingPolicy;
    readonly connectionSettings?: outputs.elasticloadbalancing.LoadBalancerConnectionSettings;
    readonly crossZone?: boolean;
    readonly dNSName?: string;
    readonly healthCheck?: outputs.elasticloadbalancing.LoadBalancerHealthCheck;
    readonly id?: string;
    readonly instances?: string[];
    readonly lBCookieStickinessPolicy?: outputs.elasticloadbalancing.LoadBalancerLBCookieStickinessPolicy[];
    readonly listeners?: outputs.elasticloadbalancing.LoadBalancerListeners[];
    readonly policies?: outputs.elasticloadbalancing.LoadBalancerPolicies[];
    readonly securityGroups?: string[];
    readonly sourceSecurityGroupGroupName?: string;
    readonly sourceSecurityGroupOwnerAlias?: string;
    readonly subnets?: string[];
    readonly tags?: outputs.elasticloadbalancing.LoadBalancerTag[];
}
/**
 * Resource Type definition for AWS::ElasticLoadBalancing::LoadBalancer
 */
export function getLoadBalancerOutput(args: GetLoadBalancerOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLoadBalancerResult> {
    return pulumi.output(args).apply((a: any) => getLoadBalancer(a, opts))
}

export interface GetLoadBalancerOutputArgs {
    id: pulumi.Input<string>;
}
