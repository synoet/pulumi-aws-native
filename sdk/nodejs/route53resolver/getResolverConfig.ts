// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Route53Resolver::ResolverConfig.
 */
export function getResolverConfig(args: GetResolverConfigArgs, opts?: pulumi.InvokeOptions): Promise<GetResolverConfigResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:route53resolver:getResolverConfig", {
        "resourceId": args.resourceId,
    }, opts);
}

export interface GetResolverConfigArgs {
    /**
     * ResourceId
     */
    resourceId: string;
}

export interface GetResolverConfigResult {
    /**
     * ResolverAutodefinedReverseStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.
     */
    readonly autodefinedReverse?: enums.route53resolver.ResolverConfigAutodefinedReverse;
    /**
     * Id
     */
    readonly id?: string;
    /**
     * AccountId
     */
    readonly ownerId?: string;
}
/**
 * Resource schema for AWS::Route53Resolver::ResolverConfig.
 */
export function getResolverConfigOutput(args: GetResolverConfigOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetResolverConfigResult> {
    return pulumi.output(args).apply((a: any) => getResolverConfig(a, opts))
}

export interface GetResolverConfigOutputArgs {
    /**
     * ResourceId
     */
    resourceId: pulumi.Input<string>;
}
