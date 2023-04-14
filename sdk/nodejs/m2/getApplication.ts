// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Represents an application that runs on an AWS Mainframe Modernization Environment
 */
export function getApplication(args: GetApplicationArgs, opts?: pulumi.InvokeOptions): Promise<GetApplicationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:m2:getApplication", {
        "applicationArn": args.applicationArn,
    }, opts);
}

export interface GetApplicationArgs {
    applicationArn: string;
}

export interface GetApplicationResult {
    readonly applicationArn?: string;
    readonly applicationId?: string;
    readonly description?: string;
    readonly tags?: outputs.m2.ApplicationTagMap;
}
/**
 * Represents an application that runs on an AWS Mainframe Modernization Environment
 */
export function getApplicationOutput(args: GetApplicationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetApplicationResult> {
    return pulumi.output(args).apply((a: any) => getApplication(a, opts))
}

export interface GetApplicationOutputArgs {
    applicationArn: pulumi.Input<string>;
}
