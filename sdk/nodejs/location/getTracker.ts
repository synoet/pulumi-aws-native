// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Definition of AWS::Location::Tracker Resource Type
 */
export function getTracker(args: GetTrackerArgs, opts?: pulumi.InvokeOptions): Promise<GetTrackerResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:location:getTracker", {
        "trackerName": args.trackerName,
    }, opts);
}

export interface GetTrackerArgs {
    trackerName: string;
}

export interface GetTrackerResult {
    readonly arn?: string;
    readonly createTime?: string;
    readonly pricingPlanDataSource?: string;
    readonly trackerArn?: string;
    readonly updateTime?: string;
}

export function getTrackerOutput(args: GetTrackerOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTrackerResult> {
    return pulumi.output(args).apply(a => getTracker(a, opts))
}

export interface GetTrackerOutputArgs {
    trackerName: pulumi.Input<string>;
}
