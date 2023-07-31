// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Neptune::DBInstance
 */
export function getDBInstance(args: GetDBInstanceArgs, opts?: pulumi.InvokeOptions): Promise<GetDBInstanceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:neptune:getDBInstance", {
        "id": args.id,
    }, opts);
}

export interface GetDBInstanceArgs {
    id: string;
}

export interface GetDBInstanceResult {
    readonly allowMajorVersionUpgrade?: boolean;
    readonly autoMinorVersionUpgrade?: boolean;
    readonly dbInstanceClass?: string;
    readonly dbParameterGroupName?: string;
    readonly endpoint?: string;
    readonly id?: string;
    readonly port?: string;
    readonly preferredMaintenanceWindow?: string;
    readonly tags?: outputs.neptune.DBInstanceTag[];
}
/**
 * Resource Type definition for AWS::Neptune::DBInstance
 */
export function getDBInstanceOutput(args: GetDBInstanceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDBInstanceResult> {
    return pulumi.output(args).apply((a: any) => getDBInstance(a, opts))
}

export interface GetDBInstanceOutputArgs {
    id: pulumi.Input<string>;
}
