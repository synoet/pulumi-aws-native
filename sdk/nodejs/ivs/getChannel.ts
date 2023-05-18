// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IVS::Channel
 */
export function getChannel(args: GetChannelArgs, opts?: pulumi.InvokeOptions): Promise<GetChannelResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ivs:getChannel", {
        "arn": args.arn,
    }, opts);
}

export interface GetChannelArgs {
    /**
     * Channel ARN is automatically generated on creation and assigned as the unique identifier.
     */
    arn: string;
}

export interface GetChannelResult {
    /**
     * Channel ARN is automatically generated on creation and assigned as the unique identifier.
     */
    readonly arn?: string;
    /**
     * Whether the channel is authorized.
     */
    readonly authorized?: boolean;
    /**
     * Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.
     */
    readonly ingestEndpoint?: string;
    /**
     * Whether the channel allows insecure ingest.
     */
    readonly insecureIngest?: boolean;
    /**
     * Channel latency mode.
     */
    readonly latencyMode?: enums.ivs.ChannelLatencyMode;
    /**
     * Channel
     */
    readonly name?: string;
    /**
     * Channel Playback URL.
     */
    readonly playbackUrl?: string;
    /**
     * Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled).
     */
    readonly recordingConfigurationArn?: string;
    /**
     * A list of key-value pairs that contain metadata for the asset model.
     */
    readonly tags?: outputs.ivs.ChannelTag[];
    /**
     * Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.
     */
    readonly type?: enums.ivs.ChannelType;
}
/**
 * Resource Type definition for AWS::IVS::Channel
 */
export function getChannelOutput(args: GetChannelOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetChannelResult> {
    return pulumi.output(args).apply((a: any) => getChannel(a, opts))
}

export interface GetChannelOutputArgs {
    /**
     * Channel ARN is automatically generated on creation and assigned as the unique identifier.
     */
    arn: pulumi.Input<string>;
}
