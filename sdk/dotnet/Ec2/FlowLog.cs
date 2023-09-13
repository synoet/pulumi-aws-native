// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    /// <summary>
    /// Specifies a VPC flow log, which enables you to capture IP traffic for a specific network interface, subnet, or VPC.
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:FlowLog")]
    public partial class FlowLog : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts.
        /// </summary>
        [Output("deliverCrossAccountRole")]
        public Output<string?> DeliverCrossAccountRole { get; private set; } = null!;

        /// <summary>
        /// The ARN for the IAM role that permits Amazon EC2 to publish flow logs to a CloudWatch Logs log group in your account. If you specify LogDestinationType as s3 or kinesis-data-firehose, do not specify DeliverLogsPermissionArn or LogGroupName.
        /// </summary>
        [Output("deliverLogsPermissionArn")]
        public Output<string?> DeliverLogsPermissionArn { get; private set; } = null!;

        [Output("destinationOptions")]
        public Output<Outputs.DestinationOptionsProperties?> DestinationOptions { get; private set; } = null!;

        /// <summary>
        /// Specifies the destination to which the flow log data is to be published. Flow log data can be published to a CloudWatch Logs log group, an Amazon S3 bucket, or a Kinesis Firehose stream. The value specified for this parameter depends on the value specified for LogDestinationType.
        /// </summary>
        [Output("logDestination")]
        public Output<string?> LogDestination { get; private set; } = null!;

        /// <summary>
        /// Specifies the type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3.
        /// </summary>
        [Output("logDestinationType")]
        public Output<Pulumi.AwsNative.Ec2.FlowLogLogDestinationType?> LogDestinationType { get; private set; } = null!;

        /// <summary>
        /// The fields to include in the flow log record, in the order in which they should appear.
        /// </summary>
        [Output("logFormat")]
        public Output<string?> LogFormat { get; private set; } = null!;

        /// <summary>
        /// The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs. If you specify LogDestinationType as s3 or kinesis-data-firehose, do not specify DeliverLogsPermissionArn or LogGroupName.
        /// </summary>
        [Output("logGroupName")]
        public Output<string?> LogGroupName { get; private set; } = null!;

        /// <summary>
        /// The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).
        /// </summary>
        [Output("maxAggregationInterval")]
        public Output<int?> MaxAggregationInterval { get; private set; } = null!;

        /// <summary>
        /// The ID of the subnet, network interface, or VPC for which you want to create a flow log.
        /// </summary>
        [Output("resourceId")]
        public Output<string> ResourceId { get; private set; } = null!;

        /// <summary>
        /// The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.
        /// </summary>
        [Output("resourceType")]
        public Output<Pulumi.AwsNative.Ec2.FlowLogResourceType> ResourceType { get; private set; } = null!;

        /// <summary>
        /// The tags to apply to the flow logs.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.FlowLogTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
        /// </summary>
        [Output("trafficType")]
        public Output<Pulumi.AwsNative.Ec2.FlowLogTrafficType?> TrafficType { get; private set; } = null!;


        /// <summary>
        /// Create a FlowLog resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FlowLog(string name, FlowLogArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:FlowLog", name, args ?? new FlowLogArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FlowLog(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:FlowLog", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "deliverCrossAccountRole",
                    "deliverLogsPermissionArn",
                    "destinationOptions",
                    "logDestination",
                    "logDestinationType",
                    "logFormat",
                    "logGroupName",
                    "maxAggregationInterval",
                    "resourceId",
                    "resourceType",
                    "trafficType",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FlowLog resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FlowLog Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FlowLog(name, id, options);
        }
    }

    public sealed class FlowLogArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts.
        /// </summary>
        [Input("deliverCrossAccountRole")]
        public Input<string>? DeliverCrossAccountRole { get; set; }

        /// <summary>
        /// The ARN for the IAM role that permits Amazon EC2 to publish flow logs to a CloudWatch Logs log group in your account. If you specify LogDestinationType as s3 or kinesis-data-firehose, do not specify DeliverLogsPermissionArn or LogGroupName.
        /// </summary>
        [Input("deliverLogsPermissionArn")]
        public Input<string>? DeliverLogsPermissionArn { get; set; }

        [Input("destinationOptions")]
        public Input<Inputs.DestinationOptionsPropertiesArgs>? DestinationOptions { get; set; }

        /// <summary>
        /// Specifies the destination to which the flow log data is to be published. Flow log data can be published to a CloudWatch Logs log group, an Amazon S3 bucket, or a Kinesis Firehose stream. The value specified for this parameter depends on the value specified for LogDestinationType.
        /// </summary>
        [Input("logDestination")]
        public Input<string>? LogDestination { get; set; }

        /// <summary>
        /// Specifies the type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3.
        /// </summary>
        [Input("logDestinationType")]
        public Input<Pulumi.AwsNative.Ec2.FlowLogLogDestinationType>? LogDestinationType { get; set; }

        /// <summary>
        /// The fields to include in the flow log record, in the order in which they should appear.
        /// </summary>
        [Input("logFormat")]
        public Input<string>? LogFormat { get; set; }

        /// <summary>
        /// The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs. If you specify LogDestinationType as s3 or kinesis-data-firehose, do not specify DeliverLogsPermissionArn or LogGroupName.
        /// </summary>
        [Input("logGroupName")]
        public Input<string>? LogGroupName { get; set; }

        /// <summary>
        /// The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).
        /// </summary>
        [Input("maxAggregationInterval")]
        public Input<int>? MaxAggregationInterval { get; set; }

        /// <summary>
        /// The ID of the subnet, network interface, or VPC for which you want to create a flow log.
        /// </summary>
        [Input("resourceId", required: true)]
        public Input<string> ResourceId { get; set; } = null!;

        /// <summary>
        /// The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.
        /// </summary>
        [Input("resourceType", required: true)]
        public Input<Pulumi.AwsNative.Ec2.FlowLogResourceType> ResourceType { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.FlowLogTagArgs>? _tags;

        /// <summary>
        /// The tags to apply to the flow logs.
        /// </summary>
        public InputList<Inputs.FlowLogTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.FlowLogTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
        /// </summary>
        [Input("trafficType")]
        public Input<Pulumi.AwsNative.Ec2.FlowLogTrafficType>? TrafficType { get; set; }

        public FlowLogArgs()
        {
        }
        public static new FlowLogArgs Empty => new FlowLogArgs();
    }
}
