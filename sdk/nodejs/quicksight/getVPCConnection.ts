// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of the AWS::QuickSight::VPCConnection Resource Type.
 */
export function getVPCConnection(args: GetVPCConnectionArgs, opts?: pulumi.InvokeOptions): Promise<GetVPCConnectionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:quicksight:getVPCConnection", {
        "awsAccountId": args.awsAccountId,
        "vPCConnectionId": args.vPCConnectionId,
    }, opts);
}

export interface GetVPCConnectionArgs {
    awsAccountId: string;
    vPCConnectionId: string;
}

export interface GetVPCConnectionResult {
    readonly arn?: string;
    readonly availabilityStatus?: enums.quicksight.VPCConnectionAvailabilityStatus;
    readonly createdTime?: string;
    readonly dnsResolvers?: string[];
    readonly lastUpdatedTime?: string;
    readonly name?: string;
    readonly networkInterfaces?: outputs.quicksight.VPCConnectionNetworkInterface[];
    readonly roleArn?: string;
    readonly securityGroupIds?: string[];
    readonly status?: enums.quicksight.VPCConnectionResourceStatus;
    readonly tags?: outputs.quicksight.VPCConnectionTag[];
    readonly vPCId?: string;
}
/**
 * Definition of the AWS::QuickSight::VPCConnection Resource Type.
 */
export function getVPCConnectionOutput(args: GetVPCConnectionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVPCConnectionResult> {
    return pulumi.output(args).apply((a: any) => getVPCConnection(a, opts))
}

export interface GetVPCConnectionOutputArgs {
    awsAccountId: pulumi.Input<string>;
    vPCConnectionId: pulumi.Input<string>;
}
