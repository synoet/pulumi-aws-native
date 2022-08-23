// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::MSK::ServerlessCluster
 */
export function getServerlessCluster(args: GetServerlessClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetServerlessClusterResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:msk:getServerlessCluster", {
        "arn": args.arn,
    }, opts);
}

export interface GetServerlessClusterArgs {
    arn: string;
}

export interface GetServerlessClusterResult {
    readonly arn?: string;
}

export function getServerlessClusterOutput(args: GetServerlessClusterOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetServerlessClusterResult> {
    return pulumi.output(args).apply(a => getServerlessCluster(a, opts))
}

export interface GetServerlessClusterOutputArgs {
    arn: pulumi.Input<string>;
}
