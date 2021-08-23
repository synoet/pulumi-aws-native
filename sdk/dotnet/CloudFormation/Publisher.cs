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
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html
    /// </summary>
    [AwsNativeResourceType("aws-native:cloudformation:Publisher")]
    public partial class Publisher : Pulumi.CustomResource
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-accepttermsandconditions
        /// </summary>
        [Output("acceptTermsAndConditions")]
        public Output<bool> AcceptTermsAndConditions { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-connectionarn
        /// </summary>
        [Output("connectionArn")]
        public Output<string?> ConnectionArn { get; private set; } = null!;

        [Output("identityProvider")]
        public Output<string> IdentityProvider { get; private set; } = null!;

        [Output("publisherId")]
        public Output<string> PublisherId { get; private set; } = null!;

        [Output("publisherProfile")]
        public Output<string> PublisherProfile { get; private set; } = null!;

        [Output("publisherStatus")]
        public Output<string> PublisherStatus { get; private set; } = null!;


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
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-accepttermsandconditions
        /// </summary>
        [Input("acceptTermsAndConditions", required: true)]
        public Input<bool> AcceptTermsAndConditions { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-connectionarn
        /// </summary>
        [Input("connectionArn")]
        public Input<string>? ConnectionArn { get; set; }

        public PublisherArgs()
        {
        }
    }
}
