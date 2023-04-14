// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Backup
{
    /// <summary>
    /// Contains detailed information about a report plan in AWS Backup Audit Manager.
    /// </summary>
    [AwsNativeResourceType("aws-native:backup:ReportPlan")]
    public partial class ReportPlan : global::Pulumi.CustomResource
    {
        /// <summary>
        /// A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        /// </summary>
        [Output("reportDeliveryChannel")]
        public Output<Outputs.ReportDeliveryChannelProperties> ReportDeliveryChannel { get; private set; } = null!;

        /// <summary>
        /// An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
        /// </summary>
        [Output("reportPlanArn")]
        public Output<string> ReportPlanArn { get; private set; } = null!;

        /// <summary>
        /// An optional description of the report plan with a maximum of 1,024 characters.
        /// </summary>
        [Output("reportPlanDescription")]
        public Output<string?> ReportPlanDescription { get; private set; } = null!;

        /// <summary>
        /// The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        /// </summary>
        [Output("reportPlanName")]
        public Output<string?> ReportPlanName { get; private set; } = null!;

        /// <summary>
        /// Metadata that you can assign to help organize the report plans that you create. Each tag is a key-value pair.
        /// </summary>
        [Output("reportPlanTags")]
        public Output<ImmutableArray<Outputs.ReportPlanTag>> ReportPlanTags { get; private set; } = null!;

        /// <summary>
        /// Identifies the report template for the report. Reports are built using a report template.
        /// </summary>
        [Output("reportSetting")]
        public Output<Outputs.ReportSettingProperties> ReportSetting { get; private set; } = null!;


        /// <summary>
        /// Create a ReportPlan resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ReportPlan(string name, ReportPlanArgs args, CustomResourceOptions? options = null)
            : base("aws-native:backup:ReportPlan", name, args ?? new ReportPlanArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ReportPlan(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:backup:ReportPlan", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ReportPlan resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ReportPlan Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ReportPlan(name, id, options);
        }
    }

    public sealed class ReportPlanArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        /// </summary>
        [Input("reportDeliveryChannel", required: true)]
        public Input<Inputs.ReportDeliveryChannelPropertiesArgs> ReportDeliveryChannel { get; set; } = null!;

        /// <summary>
        /// An optional description of the report plan with a maximum of 1,024 characters.
        /// </summary>
        [Input("reportPlanDescription")]
        public Input<string>? ReportPlanDescription { get; set; }

        /// <summary>
        /// The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        /// </summary>
        [Input("reportPlanName")]
        public Input<string>? ReportPlanName { get; set; }

        [Input("reportPlanTags")]
        private InputList<Inputs.ReportPlanTagArgs>? _reportPlanTags;

        /// <summary>
        /// Metadata that you can assign to help organize the report plans that you create. Each tag is a key-value pair.
        /// </summary>
        public InputList<Inputs.ReportPlanTagArgs> ReportPlanTags
        {
            get => _reportPlanTags ?? (_reportPlanTags = new InputList<Inputs.ReportPlanTagArgs>());
            set => _reportPlanTags = value;
        }

        /// <summary>
        /// Identifies the report template for the report. Reports are built using a report template.
        /// </summary>
        [Input("reportSetting", required: true)]
        public Input<Inputs.ReportSettingPropertiesArgs> ReportSetting { get; set; } = null!;

        public ReportPlanArgs()
        {
        }
        public static new ReportPlanArgs Empty => new ReportPlanArgs();
    }
}
