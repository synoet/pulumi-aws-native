// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Schema for AWS::EKS::FargateProfile
 */
export function getFargateProfile(args: GetFargateProfileArgs, opts?: pulumi.InvokeOptions): Promise<GetFargateProfileResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:eks:getFargateProfile", {
        "clusterName": args.clusterName,
        "fargateProfileName": args.fargateProfileName,
    }, opts);
}

export interface GetFargateProfileArgs {
    /**
     * Name of the Cluster
     */
    clusterName: string;
    /**
     * Name of FargateProfile
     */
    fargateProfileName: string;
}

export interface GetFargateProfileResult {
    readonly arn?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.eks.FargateProfileTag[];
}
/**
 * Resource Schema for AWS::EKS::FargateProfile
 */
export function getFargateProfileOutput(args: GetFargateProfileOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetFargateProfileResult> {
    return pulumi.output(args).apply((a: any) => getFargateProfile(a, opts))
}

export interface GetFargateProfileOutputArgs {
    /**
     * Name of the Cluster
     */
    clusterName: pulumi.Input<string>;
    /**
     * Name of FargateProfile
     */
    fargateProfileName: pulumi.Input<string>;
}
