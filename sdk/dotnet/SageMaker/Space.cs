// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    /// <summary>
    /// Resource Type definition for AWS::SageMaker::Space
    /// </summary>
    [AwsNativeResourceType("aws-native:sagemaker:Space")]
    public partial class Space : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the associated Domain.
        /// </summary>
        [Output("domainId")]
        public Output<string> DomainId { get; private set; } = null!;

        /// <summary>
        /// The space Amazon Resource Name (ARN).
        /// </summary>
        [Output("spaceArn")]
        public Output<string> SpaceArn { get; private set; } = null!;

        /// <summary>
        /// A name for the Space.
        /// </summary>
        [Output("spaceName")]
        public Output<string> SpaceName { get; private set; } = null!;

        /// <summary>
        /// A collection of settings.
        /// </summary>
        [Output("spaceSettings")]
        public Output<Outputs.SpaceSettings?> SpaceSettings { get; private set; } = null!;

        /// <summary>
        /// A list of tags to apply to the space.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.SpaceTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Space resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Space(string name, SpaceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:Space", name, args ?? new SpaceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Space(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:Space", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Space resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Space Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Space(name, id, options);
        }
    }

    public sealed class SpaceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the associated Domain.
        /// </summary>
        [Input("domainId", required: true)]
        public Input<string> DomainId { get; set; } = null!;

        /// <summary>
        /// A name for the Space.
        /// </summary>
        [Input("spaceName")]
        public Input<string>? SpaceName { get; set; }

        /// <summary>
        /// A collection of settings.
        /// </summary>
        [Input("spaceSettings")]
        public Input<Inputs.SpaceSettingsArgs>? SpaceSettings { get; set; }

        [Input("tags")]
        private InputList<Inputs.SpaceTagArgs>? _tags;

        /// <summary>
        /// A list of tags to apply to the space.
        /// </summary>
        public InputList<Inputs.SpaceTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.SpaceTagArgs>());
            set => _tags = value;
        }

        public SpaceArgs()
        {
        }
        public static new SpaceArgs Empty => new SpaceArgs();
    }
}
