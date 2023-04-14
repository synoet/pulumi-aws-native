// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Kinesis::Stream
 */
export function getStream(args: GetStreamArgs, opts?: pulumi.InvokeOptions): Promise<GetStreamResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:kinesis:getStream", {
        "name": args.name,
    }, opts);
}

export interface GetStreamArgs {
    /**
     * The name of the Kinesis stream.
     */
    name: string;
}

export interface GetStreamResult {
    /**
     * The Amazon resource name (ARN) of the Kinesis stream
     */
    readonly arn?: string;
    /**
     * The number of hours for the data records that are stored in shards to remain accessible.
     */
    readonly retentionPeriodHours?: number;
    /**
     * The number of shards that the stream uses. Required when StreamMode = PROVISIONED is passed.
     */
    readonly shardCount?: number;
    /**
     * When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream.
     */
    readonly streamEncryption?: outputs.kinesis.StreamEncryption;
    /**
     * The mode in which the stream is running.
     */
    readonly streamModeDetails?: outputs.kinesis.StreamModeDetails;
    /**
     * An arbitrary set of tags (key–value pairs) to associate with the Kinesis stream.
     */
    readonly tags?: outputs.kinesis.StreamTag[];
}
/**
 * Resource Type definition for AWS::Kinesis::Stream
 */
export function getStreamOutput(args: GetStreamOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStreamResult> {
    return pulumi.output(args).apply((a: any) => getStream(a, opts))
}

export interface GetStreamOutputArgs {
    /**
     * The name of the Kinesis stream.
     */
    name: pulumi.Input<string>;
}
