// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lambda
{
    /// <summary>
    /// Resource Type definition for AWS::Lambda::Permission
    /// </summary>
    [AwsNativeResourceType("aws-native:lambda:Permission")]
    public partial class Permission : global::Pulumi.CustomResource
    {
        [Output("action")]
        public Output<string> Action { get; private set; } = null!;

        [Output("eventSourceToken")]
        public Output<string?> EventSourceToken { get; private set; } = null!;

        [Output("functionName")]
        public Output<string> FunctionName { get; private set; } = null!;

        [Output("functionUrlAuthType")]
        public Output<string?> FunctionUrlAuthType { get; private set; } = null!;

        [Output("principal")]
        public Output<string> Principal { get; private set; } = null!;

        [Output("principalOrgID")]
        public Output<string?> PrincipalOrgID { get; private set; } = null!;

        [Output("sourceAccount")]
        public Output<string?> SourceAccount { get; private set; } = null!;

        [Output("sourceArn")]
        public Output<string?> SourceArn { get; private set; } = null!;


        /// <summary>
        /// Create a Permission resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Permission(string name, PermissionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lambda:Permission", name, args ?? new PermissionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Permission(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lambda:Permission", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Permission resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Permission Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Permission(name, id, options);
        }
    }

    public sealed class PermissionArgs : global::Pulumi.ResourceArgs
    {
        [Input("action", required: true)]
        public Input<string> Action { get; set; } = null!;

        [Input("eventSourceToken")]
        public Input<string>? EventSourceToken { get; set; }

        [Input("functionName", required: true)]
        public Input<string> FunctionName { get; set; } = null!;

        [Input("functionUrlAuthType")]
        public Input<string>? FunctionUrlAuthType { get; set; }

        [Input("principal", required: true)]
        public Input<string> Principal { get; set; } = null!;

        [Input("principalOrgID")]
        public Input<string>? PrincipalOrgID { get; set; }

        [Input("sourceAccount")]
        public Input<string>? SourceAccount { get; set; }

        [Input("sourceArn")]
        public Input<string>? SourceArn { get; set; }

        public PermissionArgs()
        {
        }
        public static new PermissionArgs Empty => new PermissionArgs();
    }
}
