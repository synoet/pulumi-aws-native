// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Redshift
{
    /// <summary>
    /// The `AWS::Redshift::ScheduledAction` resource creates an Amazon Redshift Scheduled Action.
    /// </summary>
    [AwsNativeResourceType("aws-native:redshift:ScheduledAction")]
    public partial class ScheduledAction : global::Pulumi.CustomResource
    {
        /// <summary>
        /// If true, the schedule is enabled. If false, the scheduled action does not trigger.
        /// </summary>
        [Output("enable")]
        public Output<bool?> Enable { get; private set; } = null!;

        /// <summary>
        /// The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger.
        /// </summary>
        [Output("endTime")]
        public Output<string?> EndTime { get; private set; } = null!;

        /// <summary>
        /// The IAM role to assume to run the target action.
        /// </summary>
        [Output("iamRole")]
        public Output<string?> IamRole { get; private set; } = null!;

        /// <summary>
        /// List of times when the scheduled action will run.
        /// </summary>
        [Output("nextInvocations")]
        public Output<ImmutableArray<string>> NextInvocations { get; private set; } = null!;

        /// <summary>
        /// The schedule in `at( )` or `cron( )` format.
        /// </summary>
        [Output("schedule")]
        public Output<string?> Schedule { get; private set; } = null!;

        /// <summary>
        /// The description of the scheduled action.
        /// </summary>
        [Output("scheduledActionDescription")]
        public Output<string?> ScheduledActionDescription { get; private set; } = null!;

        /// <summary>
        /// The name of the scheduled action. The name must be unique within an account.
        /// </summary>
        [Output("scheduledActionName")]
        public Output<string> ScheduledActionName { get; private set; } = null!;

        /// <summary>
        /// The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger.
        /// </summary>
        [Output("startTime")]
        public Output<string?> StartTime { get; private set; } = null!;

        /// <summary>
        /// The state of the scheduled action.
        /// </summary>
        [Output("state")]
        public Output<Pulumi.AwsNative.Redshift.ScheduledActionState> State { get; private set; } = null!;

        /// <summary>
        /// A JSON format string of the Amazon Redshift API operation with input parameters.
        /// </summary>
        [Output("targetAction")]
        public Output<Outputs.ScheduledActionType?> TargetAction { get; private set; } = null!;


        /// <summary>
        /// Create a ScheduledAction resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ScheduledAction(string name, ScheduledActionArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:redshift:ScheduledAction", name, args ?? new ScheduledActionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ScheduledAction(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:redshift:ScheduledAction", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ScheduledAction resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ScheduledAction Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ScheduledAction(name, id, options);
        }
    }

    public sealed class ScheduledActionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// If true, the schedule is enabled. If false, the scheduled action does not trigger.
        /// </summary>
        [Input("enable")]
        public Input<bool>? Enable { get; set; }

        /// <summary>
        /// The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger.
        /// </summary>
        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        /// <summary>
        /// The IAM role to assume to run the target action.
        /// </summary>
        [Input("iamRole")]
        public Input<string>? IamRole { get; set; }

        /// <summary>
        /// The schedule in `at( )` or `cron( )` format.
        /// </summary>
        [Input("schedule")]
        public Input<string>? Schedule { get; set; }

        /// <summary>
        /// The description of the scheduled action.
        /// </summary>
        [Input("scheduledActionDescription")]
        public Input<string>? ScheduledActionDescription { get; set; }

        /// <summary>
        /// The name of the scheduled action. The name must be unique within an account.
        /// </summary>
        [Input("scheduledActionName")]
        public Input<string>? ScheduledActionName { get; set; }

        /// <summary>
        /// The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger.
        /// </summary>
        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        /// <summary>
        /// A JSON format string of the Amazon Redshift API operation with input parameters.
        /// </summary>
        [Input("targetAction")]
        public Input<Inputs.ScheduledActionTypeArgs>? TargetAction { get; set; }

        public ScheduledActionArgs()
        {
        }
        public static new ScheduledActionArgs Empty => new ScheduledActionArgs();
    }
}
