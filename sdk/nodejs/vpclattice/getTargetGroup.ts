// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A group of related Targets that a Service may serve a request to
 */
export function getTargetGroup(args: GetTargetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetTargetGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:vpclattice:getTargetGroup", {
        "arn": args.arn,
    }, opts);
}

export interface GetTargetGroupArgs {
    arn: string;
}

export interface GetTargetGroupResult {
    readonly arn?: string;
    readonly config?: outputs.vpclattice.TargetGroupConfig;
    readonly createdAt?: string;
    readonly id?: string;
    readonly lastUpdatedAt?: string;
    readonly status?: enums.vpclattice.TargetGroupStatus;
    readonly tags?: outputs.vpclattice.TargetGroupTag[];
    readonly targets?: outputs.vpclattice.TargetGroupTarget[];
}
/**
 * A group of related Targets that a Service may serve a request to
 */
export function getTargetGroupOutput(args: GetTargetGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTargetGroupResult> {
    return pulumi.output(args).apply((a: any) => getTargetGroup(a, opts))
}

export interface GetTargetGroupOutputArgs {
    arn: pulumi.Input<string>;
}
