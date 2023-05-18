// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VpcLattice
{
    /// <summary>
    /// Retrieves information about the resource policy. The resource policy is an IAM policy created by AWS RAM on behalf of the resource owner when they share a resource.
    /// </summary>
    [AwsNativeResourceType("aws-native:vpclattice:ResourcePolicy")]
    public partial class ResourcePolicy : global::Pulumi.CustomResource
    {
        [Output("policy")]
        public Output<object> Policy { get; private set; } = null!;

        [Output("resourceArn")]
        public Output<string> ResourceArn { get; private set; } = null!;


        /// <summary>
        /// Create a ResourcePolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ResourcePolicy(string name, ResourcePolicyArgs args, CustomResourceOptions? options = null)
            : base("aws-native:vpclattice:ResourcePolicy", name, args ?? new ResourcePolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ResourcePolicy(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:vpclattice:ResourcePolicy", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ResourcePolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ResourcePolicy Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ResourcePolicy(name, id, options);
        }
    }

    public sealed class ResourcePolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("policy", required: true)]
        public Input<object> Policy { get; set; } = null!;

        [Input("resourceArn", required: true)]
        public Input<string> ResourceArn { get; set; } = null!;

        public ResourcePolicyArgs()
        {
        }
        public static new ResourcePolicyArgs Empty => new ResourcePolicyArgs();
    }
}
