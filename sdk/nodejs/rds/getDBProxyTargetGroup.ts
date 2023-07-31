// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::RDS::DBProxyTargetGroup
 */
export function getDBProxyTargetGroup(args: GetDBProxyTargetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetDBProxyTargetGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:rds:getDBProxyTargetGroup", {
        "targetGroupArn": args.targetGroupArn,
    }, opts);
}

export interface GetDBProxyTargetGroupArgs {
    /**
     * The Amazon Resource Name (ARN) representing the target group.
     */
    targetGroupArn: string;
}

export interface GetDBProxyTargetGroupResult {
    readonly connectionPoolConfigurationInfo?: outputs.rds.DBProxyTargetGroupConnectionPoolConfigurationInfoFormat;
    readonly dbClusterIdentifiers?: string[];
    readonly dbInstanceIdentifiers?: string[];
    /**
     * The Amazon Resource Name (ARN) representing the target group.
     */
    readonly targetGroupArn?: string;
}
/**
 * Resource schema for AWS::RDS::DBProxyTargetGroup
 */
export function getDBProxyTargetGroupOutput(args: GetDBProxyTargetGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDBProxyTargetGroupResult> {
    return pulumi.output(args).apply((a: any) => getDBProxyTargetGroup(a, opts))
}

export interface GetDBProxyTargetGroupOutputArgs {
    /**
     * The Amazon Resource Name (ARN) representing the target group.
     */
    targetGroupArn: pulumi.Input<string>;
}
