// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Pinpoint::GCMChannel
 */
export function getGCMChannel(args: GetGCMChannelArgs, opts?: pulumi.InvokeOptions): Promise<GetGCMChannelResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:pinpoint:getGCMChannel", {
        "id": args.id,
    }, opts);
}

export interface GetGCMChannelArgs {
    id: string;
}

export interface GetGCMChannelResult {
    readonly apiKey?: string;
    readonly enabled?: boolean;
    readonly id?: string;
}
/**
 * Resource Type definition for AWS::Pinpoint::GCMChannel
 */
export function getGCMChannelOutput(args: GetGCMChannelOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetGCMChannelResult> {
    return pulumi.output(args).apply((a: any) => getGCMChannel(a, opts))
}

export interface GetGCMChannelOutputArgs {
    id: pulumi.Input<string>;
}
