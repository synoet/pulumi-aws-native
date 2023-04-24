// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::MediaLive::Channel
 */
export function getChannel(args: GetChannelArgs, opts?: pulumi.InvokeOptions): Promise<GetChannelResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:medialive:getChannel", {
        "id": args.id,
    }, opts);
}

export interface GetChannelArgs {
    id: string;
}

export interface GetChannelResult {
    readonly arn?: string;
    readonly cdiInputSpecification?: outputs.medialive.ChannelCdiInputSpecification;
    readonly channelClass?: string;
    readonly destinations?: outputs.medialive.ChannelOutputDestination[];
    readonly encoderSettings?: outputs.medialive.ChannelEncoderSettings;
    readonly id?: string;
    readonly inputAttachments?: outputs.medialive.ChannelInputAttachment[];
    readonly inputSpecification?: outputs.medialive.ChannelInputSpecification;
    readonly inputs?: string[];
    readonly logLevel?: string;
    readonly maintenance?: outputs.medialive.ChannelMaintenanceCreateSettings;
    readonly name?: string;
    readonly roleArn?: string;
    readonly tags?: any;
}
/**
 * Resource Type definition for AWS::MediaLive::Channel
 */
export function getChannelOutput(args: GetChannelOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetChannelResult> {
    return pulumi.output(args).apply((a: any) => getChannel(a, opts))
}

export interface GetChannelOutputArgs {
    id: pulumi.Input<string>;
}
