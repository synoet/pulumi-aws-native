// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    /// <summary>
    /// Resource Type definition for AWS::EC2::InternetGateway
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:InternetGateway")]
    public partial class InternetGateway : global::Pulumi.CustomResource
    {
        /// <summary>
        /// ID of internet gateway.
        /// </summary>
        [Output("internetGatewayId")]
        public Output<string> InternetGatewayId { get; private set; } = null!;

        /// <summary>
        /// Any tags to assign to the internet gateway.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.InternetGatewayTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a InternetGateway resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public InternetGateway(string name, InternetGatewayArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:ec2:InternetGateway", name, args ?? new InternetGatewayArgs(), MakeResourceOptions(options, ""))
        {
        }

        private InternetGateway(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:InternetGateway", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing InternetGateway resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static InternetGateway Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new InternetGateway(name, id, options);
        }
    }

    public sealed class InternetGatewayArgs : global::Pulumi.ResourceArgs
    {
        [Input("tags")]
        private InputList<Inputs.InternetGatewayTagArgs>? _tags;

        /// <summary>
        /// Any tags to assign to the internet gateway.
        /// </summary>
        public InputList<Inputs.InternetGatewayTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.InternetGatewayTagArgs>());
            set => _tags = value;
        }

        public InternetGatewayArgs()
        {
        }
        public static new InternetGatewayArgs Empty => new InternetGatewayArgs();
    }
}
