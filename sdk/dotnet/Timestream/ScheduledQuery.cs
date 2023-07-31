// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Timestream
{
    /// <summary>
    /// The AWS::Timestream::ScheduledQuery resource creates a Timestream Scheduled Query.
    /// </summary>
    [AwsNativeResourceType("aws-native:timestream:ScheduledQuery")]
    public partial class ScheduledQuery : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("clientToken")]
        public Output<string?> ClientToken { get; private set; } = null!;

        [Output("errorReportConfiguration")]
        public Output<Outputs.ScheduledQueryErrorReportConfiguration> ErrorReportConfiguration { get; private set; } = null!;

        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        [Output("notificationConfiguration")]
        public Output<Outputs.ScheduledQueryNotificationConfiguration> NotificationConfiguration { get; private set; } = null!;

        [Output("queryString")]
        public Output<string> QueryString { get; private set; } = null!;

        [Output("scheduleConfiguration")]
        public Output<Outputs.ScheduledQueryScheduleConfiguration> ScheduleConfiguration { get; private set; } = null!;

        [Output("scheduledQueryExecutionRoleArn")]
        public Output<string> ScheduledQueryExecutionRoleArn { get; private set; } = null!;

        [Output("scheduledQueryName")]
        public Output<string?> ScheduledQueryName { get; private set; } = null!;

        /// <summary>
        /// Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.
        /// </summary>
        [Output("sqErrorReportConfiguration")]
        public Output<string> SqErrorReportConfiguration { get; private set; } = null!;

        /// <summary>
        /// The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with alias/. If ErrorReportConfiguration uses SSE_KMS as encryption type, the same KmsKeyId is used to encrypt the error report at rest.
        /// </summary>
        [Output("sqKmsKeyId")]
        public Output<string> SqKmsKeyId { get; private set; } = null!;

        /// <summary>
        /// The name of the scheduled query. Scheduled query names must be unique within each Region.
        /// </summary>
        [Output("sqName")]
        public Output<string> SqName { get; private set; } = null!;

        /// <summary>
        /// Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.
        /// </summary>
        [Output("sqNotificationConfiguration")]
        public Output<string> SqNotificationConfiguration { get; private set; } = null!;

        /// <summary>
        /// The query string to run. Parameter names can be specified in the query string @ character followed by an identifier. The named Parameter @scheduled_runtime is reserved and can be used in the query to get the time at which the query is scheduled to run. The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of @scheduled_runtime paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the @scheduled_runtime parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.
        /// </summary>
        [Output("sqQueryString")]
        public Output<string> SqQueryString { get; private set; } = null!;

        /// <summary>
        /// Configuration for when the scheduled query is executed.
        /// </summary>
        [Output("sqScheduleConfiguration")]
        public Output<string> SqScheduleConfiguration { get; private set; } = null!;

        /// <summary>
        /// The ARN for the IAM role that Timestream will assume when running the scheduled query.
        /// </summary>
        [Output("sqScheduledQueryExecutionRoleArn")]
        public Output<string> SqScheduledQueryExecutionRoleArn { get; private set; } = null!;

        /// <summary>
        /// Configuration of target store where scheduled query results are written to.
        /// </summary>
        [Output("sqTargetConfiguration")]
        public Output<string> SqTargetConfiguration { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.ScheduledQueryTag>> Tags { get; private set; } = null!;

        [Output("targetConfiguration")]
        public Output<Outputs.ScheduledQueryTargetConfiguration?> TargetConfiguration { get; private set; } = null!;


        /// <summary>
        /// Create a ScheduledQuery resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ScheduledQuery(string name, ScheduledQueryArgs args, CustomResourceOptions? options = null)
            : base("aws-native:timestream:ScheduledQuery", name, args ?? new ScheduledQueryArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ScheduledQuery(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:timestream:ScheduledQuery", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ScheduledQuery resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ScheduledQuery Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ScheduledQuery(name, id, options);
        }
    }

    public sealed class ScheduledQueryArgs : global::Pulumi.ResourceArgs
    {
        [Input("clientToken")]
        public Input<string>? ClientToken { get; set; }

        [Input("errorReportConfiguration", required: true)]
        public Input<Inputs.ScheduledQueryErrorReportConfigurationArgs> ErrorReportConfiguration { get; set; } = null!;

        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("notificationConfiguration", required: true)]
        public Input<Inputs.ScheduledQueryNotificationConfigurationArgs> NotificationConfiguration { get; set; } = null!;

        [Input("queryString", required: true)]
        public Input<string> QueryString { get; set; } = null!;

        [Input("scheduleConfiguration", required: true)]
        public Input<Inputs.ScheduledQueryScheduleConfigurationArgs> ScheduleConfiguration { get; set; } = null!;

        [Input("scheduledQueryExecutionRoleArn", required: true)]
        public Input<string> ScheduledQueryExecutionRoleArn { get; set; } = null!;

        [Input("scheduledQueryName")]
        public Input<string>? ScheduledQueryName { get; set; }

        [Input("tags")]
        private InputList<Inputs.ScheduledQueryTagArgs>? _tags;
        public InputList<Inputs.ScheduledQueryTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ScheduledQueryTagArgs>());
            set => _tags = value;
        }

        [Input("targetConfiguration")]
        public Input<Inputs.ScheduledQueryTargetConfigurationArgs>? TargetConfiguration { get; set; }

        public ScheduledQueryArgs()
        {
        }
        public static new ScheduledQueryArgs Empty => new ScheduledQueryArgs();
    }
}
