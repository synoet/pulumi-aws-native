// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SQS::Queue
 */
export class Queue extends pulumi.CustomResource {
    /**
     * Get an existing Queue resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Queue {
        return new Queue(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:sqs:Queue';

    /**
     * Returns true if the given object is an instance of Queue.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Queue {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Queue.__pulumiType;
    }

    /**
     * Amazon Resource Name (ARN) of the queue.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * For first-in-first-out (FIFO) queues, specifies whether to enable content-based deduplication. During the deduplication interval, Amazon SQS treats messages that are sent with identical content as duplicates and delivers only one copy of the message.
     */
    public readonly contentBasedDeduplication!: pulumi.Output<boolean | undefined>;
    /**
     * Specifies whether message deduplication occurs at the message group or queue level. Valid values are messageGroup and queue.
     */
    public readonly deduplicationScope!: pulumi.Output<string | undefined>;
    /**
     * The time in seconds for which the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes). The default value is 0.
     */
    public readonly delaySeconds!: pulumi.Output<number | undefined>;
    /**
     * If set to true, creates a FIFO queue. If you don't specify this property, Amazon SQS creates a standard queue.
     */
    public readonly fifoQueue!: pulumi.Output<boolean | undefined>;
    /**
     * Specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are perQueue and perMessageGroupId. The perMessageGroupId value is allowed only when the value for DeduplicationScope is messageGroup.
     */
    public readonly fifoThroughputLimit!: pulumi.Output<string | undefined>;
    /**
     * The length of time in seconds for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. The value must be an integer between 60 (1 minute) and 86,400 (24 hours). The default is 300 (5 minutes).
     */
    public readonly kmsDataKeyReusePeriodSeconds!: pulumi.Output<number | undefined>;
    /**
     * The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. To use the AWS managed CMK for Amazon SQS, specify the (default) alias alias/aws/sqs.
     */
    public readonly kmsMasterKeyId!: pulumi.Output<string | undefined>;
    /**
     * The limit of how many bytes that a message can contain before Amazon SQS rejects it. You can specify an integer value from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). The default value is 262,144 (256 KiB).
     */
    public readonly maximumMessageSize!: pulumi.Output<number | undefined>;
    /**
     * The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1,209,600 seconds (14 days). The default value is 345,600 seconds (4 days).
     */
    public readonly messageRetentionPeriod!: pulumi.Output<number | undefined>;
    /**
     * A name for the queue. To create a FIFO queue, the name of your FIFO queue must end with the .fifo suffix.
     */
    public readonly queueName!: pulumi.Output<string | undefined>;
    /**
     * URL of the source queue.
     */
    public /*out*/ readonly queueUrl!: pulumi.Output<string>;
    /**
     * Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, rather than returning an empty response if a message isn't yet available. You can specify an integer from 1 to 20. Short polling is used as the default or when you specify 0 for this property.
     */
    public readonly receiveMessageWaitTimeSeconds!: pulumi.Output<number | undefined>;
    /**
     * The string that includes the parameters for the permissions for the dead-letter queue redrive permission and which source queues can specify dead-letter queues as a JSON object.
     */
    public readonly redriveAllowPolicy!: pulumi.Output<any | undefined>;
    /**
     * A string that includes the parameters for the dead-letter queue functionality (redrive policy) of the source queue.
     */
    public readonly redrivePolicy!: pulumi.Output<any | undefined>;
    /**
     * Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (e.g. SSE-KMS or SSE-SQS ).
     */
    public readonly sqsManagedSseEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The tags that you attach to this queue.
     */
    public readonly tags!: pulumi.Output<outputs.sqs.QueueTag[] | undefined>;
    /**
     * The length of time during which a message will be unavailable after a message is delivered from the queue. This blocks other components from receiving the same message and gives the initial component time to process and delete the message from the queue. Values must be from 0 to 43,200 seconds (12 hours). If you don't specify a value, AWS CloudFormation uses the default value of 30 seconds.
     */
    public readonly visibilityTimeout!: pulumi.Output<number | undefined>;

    /**
     * Create a Queue resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: QueueArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["contentBasedDeduplication"] = args ? args.contentBasedDeduplication : undefined;
            resourceInputs["deduplicationScope"] = args ? args.deduplicationScope : undefined;
            resourceInputs["delaySeconds"] = args ? args.delaySeconds : undefined;
            resourceInputs["fifoQueue"] = args ? args.fifoQueue : undefined;
            resourceInputs["fifoThroughputLimit"] = args ? args.fifoThroughputLimit : undefined;
            resourceInputs["kmsDataKeyReusePeriodSeconds"] = args ? args.kmsDataKeyReusePeriodSeconds : undefined;
            resourceInputs["kmsMasterKeyId"] = args ? args.kmsMasterKeyId : undefined;
            resourceInputs["maximumMessageSize"] = args ? args.maximumMessageSize : undefined;
            resourceInputs["messageRetentionPeriod"] = args ? args.messageRetentionPeriod : undefined;
            resourceInputs["queueName"] = args ? args.queueName : undefined;
            resourceInputs["receiveMessageWaitTimeSeconds"] = args ? args.receiveMessageWaitTimeSeconds : undefined;
            resourceInputs["redriveAllowPolicy"] = args ? args.redriveAllowPolicy : undefined;
            resourceInputs["redrivePolicy"] = args ? args.redrivePolicy : undefined;
            resourceInputs["sqsManagedSseEnabled"] = args ? args.sqsManagedSseEnabled : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["visibilityTimeout"] = args ? args.visibilityTimeout : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["queueUrl"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["contentBasedDeduplication"] = undefined /*out*/;
            resourceInputs["deduplicationScope"] = undefined /*out*/;
            resourceInputs["delaySeconds"] = undefined /*out*/;
            resourceInputs["fifoQueue"] = undefined /*out*/;
            resourceInputs["fifoThroughputLimit"] = undefined /*out*/;
            resourceInputs["kmsDataKeyReusePeriodSeconds"] = undefined /*out*/;
            resourceInputs["kmsMasterKeyId"] = undefined /*out*/;
            resourceInputs["maximumMessageSize"] = undefined /*out*/;
            resourceInputs["messageRetentionPeriod"] = undefined /*out*/;
            resourceInputs["queueName"] = undefined /*out*/;
            resourceInputs["queueUrl"] = undefined /*out*/;
            resourceInputs["receiveMessageWaitTimeSeconds"] = undefined /*out*/;
            resourceInputs["redriveAllowPolicy"] = undefined /*out*/;
            resourceInputs["redrivePolicy"] = undefined /*out*/;
            resourceInputs["sqsManagedSseEnabled"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["visibilityTimeout"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["fifoQueue", "queueName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Queue.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Queue resource.
 */
export interface QueueArgs {
    /**
     * For first-in-first-out (FIFO) queues, specifies whether to enable content-based deduplication. During the deduplication interval, Amazon SQS treats messages that are sent with identical content as duplicates and delivers only one copy of the message.
     */
    contentBasedDeduplication?: pulumi.Input<boolean>;
    /**
     * Specifies whether message deduplication occurs at the message group or queue level. Valid values are messageGroup and queue.
     */
    deduplicationScope?: pulumi.Input<string>;
    /**
     * The time in seconds for which the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes). The default value is 0.
     */
    delaySeconds?: pulumi.Input<number>;
    /**
     * If set to true, creates a FIFO queue. If you don't specify this property, Amazon SQS creates a standard queue.
     */
    fifoQueue?: pulumi.Input<boolean>;
    /**
     * Specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are perQueue and perMessageGroupId. The perMessageGroupId value is allowed only when the value for DeduplicationScope is messageGroup.
     */
    fifoThroughputLimit?: pulumi.Input<string>;
    /**
     * The length of time in seconds for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. The value must be an integer between 60 (1 minute) and 86,400 (24 hours). The default is 300 (5 minutes).
     */
    kmsDataKeyReusePeriodSeconds?: pulumi.Input<number>;
    /**
     * The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. To use the AWS managed CMK for Amazon SQS, specify the (default) alias alias/aws/sqs.
     */
    kmsMasterKeyId?: pulumi.Input<string>;
    /**
     * The limit of how many bytes that a message can contain before Amazon SQS rejects it. You can specify an integer value from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). The default value is 262,144 (256 KiB).
     */
    maximumMessageSize?: pulumi.Input<number>;
    /**
     * The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1,209,600 seconds (14 days). The default value is 345,600 seconds (4 days).
     */
    messageRetentionPeriod?: pulumi.Input<number>;
    /**
     * A name for the queue. To create a FIFO queue, the name of your FIFO queue must end with the .fifo suffix.
     */
    queueName?: pulumi.Input<string>;
    /**
     * Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, rather than returning an empty response if a message isn't yet available. You can specify an integer from 1 to 20. Short polling is used as the default or when you specify 0 for this property.
     */
    receiveMessageWaitTimeSeconds?: pulumi.Input<number>;
    /**
     * The string that includes the parameters for the permissions for the dead-letter queue redrive permission and which source queues can specify dead-letter queues as a JSON object.
     */
    redriveAllowPolicy?: any;
    /**
     * A string that includes the parameters for the dead-letter queue functionality (redrive policy) of the source queue.
     */
    redrivePolicy?: any;
    /**
     * Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (e.g. SSE-KMS or SSE-SQS ).
     */
    sqsManagedSseEnabled?: pulumi.Input<boolean>;
    /**
     * The tags that you attach to this queue.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.sqs.QueueTagArgs>[]>;
    /**
     * The length of time during which a message will be unavailable after a message is delivered from the queue. This blocks other components from receiving the same message and gives the initial component time to process and delete the message from the queue. Values must be from 0 to 43,200 seconds (12 hours). If you don't specify a value, AWS CloudFormation uses the default value of 30 seconds.
     */
    visibilityTimeout?: pulumi.Input<number>;
}
