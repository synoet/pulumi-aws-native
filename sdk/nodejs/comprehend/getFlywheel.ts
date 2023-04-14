// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::Comprehend::Flywheel resource creates an Amazon Comprehend Flywheel that enables customer to train their model.
 */
export function getFlywheel(args: GetFlywheelArgs, opts?: pulumi.InvokeOptions): Promise<GetFlywheelResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:comprehend:getFlywheel", {
        "arn": args.arn,
    }, opts);
}

export interface GetFlywheelArgs {
    arn: string;
}

export interface GetFlywheelResult {
    readonly activeModelArn?: string;
    readonly arn?: string;
    readonly dataAccessRoleArn?: string;
    readonly dataSecurityConfig?: outputs.comprehend.FlywheelDataSecurityConfig;
    readonly tags?: outputs.comprehend.FlywheelTag[];
}
/**
 * The AWS::Comprehend::Flywheel resource creates an Amazon Comprehend Flywheel that enables customer to train their model.
 */
export function getFlywheelOutput(args: GetFlywheelOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetFlywheelResult> {
    return pulumi.output(args).apply((a: any) => getFlywheel(a, opts))
}

export interface GetFlywheelOutputArgs {
    arn: pulumi.Input<string>;
}
