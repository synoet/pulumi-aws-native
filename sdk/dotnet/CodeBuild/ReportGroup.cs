// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeBuild
{
    /// <summary>
    /// Resource Type definition for AWS::CodeBuild::ReportGroup
    /// </summary>
    [Obsolete(@"ReportGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:codebuild:ReportGroup")]
    public partial class ReportGroup : Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("deleteReports")]
        public Output<bool?> DeleteReports { get; private set; } = null!;

        [Output("exportConfig")]
        public Output<Outputs.ReportGroupReportExportConfig> ExportConfig { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.ReportGroupTag>> Tags { get; private set; } = null!;

        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a ReportGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ReportGroup(string name, ReportGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:codebuild:ReportGroup", name, args ?? new ReportGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ReportGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:codebuild:ReportGroup", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ReportGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ReportGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ReportGroup(name, id, options);
        }
    }

    public sealed class ReportGroupArgs : Pulumi.ResourceArgs
    {
        [Input("deleteReports")]
        public Input<bool>? DeleteReports { get; set; }

        [Input("exportConfig", required: true)]
        public Input<Inputs.ReportGroupReportExportConfigArgs> ExportConfig { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Inputs.ReportGroupTagArgs>? _tags;
        public InputList<Inputs.ReportGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ReportGroupTagArgs>());
            set => _tags = value;
        }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public ReportGroupArgs()
        {
        }
    }
}
