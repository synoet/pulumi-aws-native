// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra
{
    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html
    /// </summary>
    [AwsNativeResourceType("aws-native:kendra:Faq")]
    public partial class Faq : Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-description
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-fileformat
        /// </summary>
        [Output("fileFormat")]
        public Output<string?> FileFormat { get; private set; } = null!;

        [Output("id")]
        public Output<string> Id { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-indexid
        /// </summary>
        [Output("indexId")]
        public Output<string> IndexId { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-rolearn
        /// </summary>
        [Output("roleArn")]
        public Output<string> RoleArn { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-s3path
        /// </summary>
        [Output("s3Path")]
        public Output<Outputs.FaqS3Path> S3Path { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-tags
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Faq resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Faq(string name, FaqArgs args, CustomResourceOptions? options = null)
            : base("aws-native:kendra:Faq", name, args ?? new FaqArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Faq(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:kendra:Faq", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Faq resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Faq Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Faq(name, id, options);
        }
    }

    public sealed class FaqArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-description
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-fileformat
        /// </summary>
        [Input("fileFormat")]
        public Input<string>? FileFormat { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-indexid
        /// </summary>
        [Input("indexId", required: true)]
        public Input<string> IndexId { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-name
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-rolearn
        /// </summary>
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-s3path
        /// </summary>
        [Input("s3Path", required: true)]
        public Input<Inputs.FaqS3PathArgs> S3Path { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-tags
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public FaqArgs()
        {
        }
    }
}
