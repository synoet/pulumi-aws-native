// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFormation
{
    /// <summary>
    /// Register as a publisher in the CloudFormation Registry.
    /// </summary>
    [AwsNativeResourceType("aws-native:cloudformation:Publisher")]
    public partial class Publisher : Pulumi.CustomResource
    {
        /// <summary>
        /// Whether you accept the terms and conditions for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to publish public extensions to the CloudFormation registry. The terms and conditions can be found at https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf
        /// </summary>
        [Output("acceptTermsAndConditions")]
        public Output<bool> AcceptTermsAndConditions { get; private set; } = null!;

        /// <summary>
        /// If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.
        /// </summary>
        [Output("connectionArn")]
        public Output<string?> ConnectionArn { get; private set; } = null!;

        /// <summary>
        /// The type of account used as the identity provider when registering this publisher with CloudFormation.
        /// </summary>
        [Output("identityProvider")]
        public Output<Pulumi.AwsNative.CloudFormation.PublisherIdentityProvider> IdentityProvider { get; private set; } = null!;

        /// <summary>
        /// The publisher id assigned by CloudFormation for publishing in this region.
        /// </summary>
        [Output("publisherId")]
        public Output<string> PublisherId { get; private set; } = null!;

        /// <summary>
        /// The URL to the publisher's profile with the identity provider.
        /// </summary>
        [Output("publisherProfile")]
        public Output<string> PublisherProfile { get; private set; } = null!;

        /// <summary>
        /// Whether the publisher is verified.
        /// </summary>
        [Output("publisherStatus")]
        public Output<Pulumi.AwsNative.CloudFormation.PublisherPublisherStatus> PublisherStatus { get; private set; } = null!;


        /// <summary>
        /// Create a Publisher resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Publisher(string name, PublisherArgs args, CustomResourceOptions? options = null)
            : base("aws-native:cloudformation:Publisher", name, args ?? new PublisherArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Publisher(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cloudformation:Publisher", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Publisher resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Publisher Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Publisher(name, id, options);
        }
    }

    public sealed class PublisherArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether you accept the terms and conditions for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to publish public extensions to the CloudFormation registry. The terms and conditions can be found at https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf
        /// </summary>
        [Input("acceptTermsAndConditions", required: true)]
        public Input<bool> AcceptTermsAndConditions { get; set; } = null!;

        /// <summary>
        /// If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.
        /// </summary>
        [Input("connectionArn")]
        public Input<string>? ConnectionArn { get; set; }

        public PublisherArgs()
        {
        }
    }
}
