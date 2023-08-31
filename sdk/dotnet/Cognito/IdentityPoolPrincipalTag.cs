// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito
{
    /// <summary>
    /// Resource Type definition for AWS::Cognito::IdentityPoolPrincipalTag
    /// </summary>
    [AwsNativeResourceType("aws-native:cognito:IdentityPoolPrincipalTag")]
    public partial class IdentityPoolPrincipalTag : global::Pulumi.CustomResource
    {
        [Output("identityPoolId")]
        public Output<string> IdentityPoolId { get; private set; } = null!;

        [Output("identityProviderName")]
        public Output<string> IdentityProviderName { get; private set; } = null!;

        [Output("principalTags")]
        public Output<object?> PrincipalTags { get; private set; } = null!;

        [Output("useDefaults")]
        public Output<bool?> UseDefaults { get; private set; } = null!;


        /// <summary>
        /// Create a IdentityPoolPrincipalTag resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IdentityPoolPrincipalTag(string name, IdentityPoolPrincipalTagArgs args, CustomResourceOptions? options = null)
            : base("aws-native:cognito:IdentityPoolPrincipalTag", name, args ?? new IdentityPoolPrincipalTagArgs(), MakeResourceOptions(options, ""))
        {
        }

        private IdentityPoolPrincipalTag(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cognito:IdentityPoolPrincipalTag", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "identityPoolId",
                    "identityProviderName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing IdentityPoolPrincipalTag resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IdentityPoolPrincipalTag Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new IdentityPoolPrincipalTag(name, id, options);
        }
    }

    public sealed class IdentityPoolPrincipalTagArgs : global::Pulumi.ResourceArgs
    {
        [Input("identityPoolId", required: true)]
        public Input<string> IdentityPoolId { get; set; } = null!;

        [Input("identityProviderName", required: true)]
        public Input<string> IdentityProviderName { get; set; } = null!;

        [Input("principalTags")]
        public Input<object>? PrincipalTags { get; set; }

        [Input("useDefaults")]
        public Input<bool>? UseDefaults { get; set; }

        public IdentityPoolPrincipalTagArgs()
        {
        }
        public static new IdentityPoolPrincipalTagArgs Empty => new IdentityPoolPrincipalTagArgs();
    }
}
