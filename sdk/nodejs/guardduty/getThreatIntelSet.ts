// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::GuardDuty::ThreatIntelSet
 */
export function getThreatIntelSet(args: GetThreatIntelSetArgs, opts?: pulumi.InvokeOptions): Promise<GetThreatIntelSetResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:guardduty:getThreatIntelSet", {
        "id": args.id,
    }, opts);
}

export interface GetThreatIntelSetArgs {
    id: string;
}

export interface GetThreatIntelSetResult {
    readonly activate?: boolean;
    readonly id?: string;
    readonly location?: string;
    readonly name?: string;
    readonly tags?: outputs.guardduty.ThreatIntelSetTag[];
}
/**
 * Resource Type definition for AWS::GuardDuty::ThreatIntelSet
 */
export function getThreatIntelSetOutput(args: GetThreatIntelSetOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetThreatIntelSetResult> {
    return pulumi.output(args).apply((a: any) => getThreatIntelSet(a, opts))
}

export interface GetThreatIntelSetOutputArgs {
    id: pulumi.Input<string>;
}
