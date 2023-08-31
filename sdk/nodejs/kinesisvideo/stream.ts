// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type Definition for AWS::KinesisVideo::Stream
 */
export class Stream extends pulumi.CustomResource {
    /**
     * Get an existing Stream resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Stream {
        return new Stream(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:kinesisvideo:Stream';

    /**
     * Returns true if the given object is an instance of Stream.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Stream {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Stream.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the Kinesis Video stream.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The number of hours till which Kinesis Video will retain the data in the stream
     */
    public readonly dataRetentionInHours!: pulumi.Output<number | undefined>;
    /**
     * The name of the device that is writing to the stream.
     */
    public readonly deviceName!: pulumi.Output<string | undefined>;
    /**
     * AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.
     */
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    /**
     * The media type of the stream. Consumers of the stream can use this information when processing the stream.
     */
    public readonly mediaType!: pulumi.Output<string | undefined>;
    /**
     * The name of the Kinesis Video stream.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * An array of key-value pairs associated with the Kinesis Video Stream.
     */
    public readonly tags!: pulumi.Output<outputs.kinesisvideo.StreamTag[] | undefined>;

    /**
     * Create a Stream resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: StreamArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["dataRetentionInHours"] = args ? args.dataRetentionInHours : undefined;
            resourceInputs["deviceName"] = args ? args.deviceName : undefined;
            resourceInputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            resourceInputs["mediaType"] = args ? args.mediaType : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["dataRetentionInHours"] = undefined /*out*/;
            resourceInputs["deviceName"] = undefined /*out*/;
            resourceInputs["kmsKeyId"] = undefined /*out*/;
            resourceInputs["mediaType"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Stream.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Stream resource.
 */
export interface StreamArgs {
    /**
     * The number of hours till which Kinesis Video will retain the data in the stream
     */
    dataRetentionInHours?: pulumi.Input<number>;
    /**
     * The name of the device that is writing to the stream.
     */
    deviceName?: pulumi.Input<string>;
    /**
     * AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.
     */
    kmsKeyId?: pulumi.Input<string>;
    /**
     * The media type of the stream. Consumers of the stream can use this information when processing the stream.
     */
    mediaType?: pulumi.Input<string>;
    /**
     * The name of the Kinesis Video stream.
     */
    name?: pulumi.Input<string>;
    /**
     * An array of key-value pairs associated with the Kinesis Video Stream.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.kinesisvideo.StreamTagArgs>[]>;
}
