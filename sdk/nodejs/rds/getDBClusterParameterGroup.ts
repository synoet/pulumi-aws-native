// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::RDS::DBClusterParameterGroup resource creates a new Amazon RDS DB cluster parameter group. For more information, see Managing an Amazon Aurora DB Cluster in the Amazon Aurora User Guide.
 */
export function getDBClusterParameterGroup(args: GetDBClusterParameterGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetDBClusterParameterGroupResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:rds:getDBClusterParameterGroup", {
        "dBClusterParameterGroupName": args.dBClusterParameterGroupName,
    }, opts);
}

export interface GetDBClusterParameterGroupArgs {
    dBClusterParameterGroupName: string;
}

export interface GetDBClusterParameterGroupResult {
    /**
     * The list of tags for the cluster parameter group.
     */
    readonly tags?: outputs.rds.DBClusterParameterGroupTag[];
}

export function getDBClusterParameterGroupOutput(args: GetDBClusterParameterGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDBClusterParameterGroupResult> {
    return pulumi.output(args).apply(a => getDBClusterParameterGroup(a, opts))
}

export interface GetDBClusterParameterGroupOutputArgs {
    dBClusterParameterGroupName: pulumi.Input<string>;
}
