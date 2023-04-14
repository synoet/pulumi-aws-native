// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::DocDB::DBCluster
 */
export function getDBCluster(args: GetDBClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetDBClusterResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:docdb:getDBCluster", {
        "id": args.id,
    }, opts);
}

export interface GetDBClusterArgs {
    id: string;
}

export interface GetDBClusterResult {
    readonly backupRetentionPeriod?: number;
    readonly clusterResourceId?: string;
    readonly copyTagsToSnapshot?: boolean;
    readonly dBClusterParameterGroupName?: string;
    readonly deletionProtection?: boolean;
    readonly enableCloudwatchLogsExports?: string[];
    readonly endpoint?: string;
    readonly id?: string;
    readonly masterUserPassword?: string;
    readonly port?: number;
    readonly preferredBackupWindow?: string;
    readonly preferredMaintenanceWindow?: string;
    readonly readEndpoint?: string;
    readonly restoreToTime?: string;
    readonly restoreType?: string;
    readonly tags?: outputs.docdb.DBClusterTag[];
    readonly useLatestRestorableTime?: boolean;
    readonly vpcSecurityGroupIds?: string[];
}
/**
 * Resource Type definition for AWS::DocDB::DBCluster
 */
export function getDBClusterOutput(args: GetDBClusterOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDBClusterResult> {
    return pulumi.output(args).apply((a: any) => getDBCluster(a, opts))
}

export interface GetDBClusterOutputArgs {
    id: pulumi.Input<string>;
}
