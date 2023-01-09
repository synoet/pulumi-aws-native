// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Specifies an Amazon Redshift subnet group.
 */
export function getClusterSubnetGroup(args: GetClusterSubnetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterSubnetGroupResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:redshift:getClusterSubnetGroup", {
        "clusterSubnetGroupName": args.clusterSubnetGroupName,
    }, opts);
}

export interface GetClusterSubnetGroupArgs {
    /**
     * This name must be unique for all subnet groups that are created by your AWS account. If costumer do not provide it, cloudformation will generate it. Must not be "Default". 
     */
    clusterSubnetGroupName: string;
}

export interface GetClusterSubnetGroupResult {
    /**
     * This name must be unique for all subnet groups that are created by your AWS account. If costumer do not provide it, cloudformation will generate it. Must not be "Default". 
     */
    readonly clusterSubnetGroupName?: string;
    /**
     * The description of the parameter group.
     */
    readonly description?: string;
    /**
     * The list of VPC subnet IDs
     */
    readonly subnetIds?: string[];
}

export function getClusterSubnetGroupOutput(args: GetClusterSubnetGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetClusterSubnetGroupResult> {
    return pulumi.output(args).apply(a => getClusterSubnetGroup(a, opts))
}

export interface GetClusterSubnetGroupOutputArgs {
    /**
     * This name must be unique for all subnet groups that are created by your AWS account. If costumer do not provide it, cloudformation will generate it. Must not be "Default". 
     */
    clusterSubnetGroupName: pulumi.Input<string>;
}
