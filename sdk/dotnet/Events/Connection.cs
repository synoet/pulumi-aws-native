// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Events
{
    /// <summary>
    /// Resource Type definition for AWS::Events::Connection.
    /// </summary>
    [AwsNativeResourceType("aws-native:events:Connection")]
    public partial class Connection : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The arn of the connection resource.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("authParameters")]
        public Output<Outputs.ConnectionAuthParameters> AuthParameters { get; private set; } = null!;

        [Output("authorizationType")]
        public Output<Pulumi.AwsNative.Events.ConnectionAuthorizationType> AuthorizationType { get; private set; } = null!;

        /// <summary>
        /// Description of the connection.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Name of the connection.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// The arn of the secrets manager secret created in the customer account.
        /// </summary>
        [Output("secretArn")]
        public Output<string> SecretArn { get; private set; } = null!;


        /// <summary>
        /// Create a Connection resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Connection(string name, ConnectionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:events:Connection", name, args ?? new ConnectionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Connection(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:events:Connection", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Connection resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Connection Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Connection(name, id, options);
        }
    }

    public sealed class ConnectionArgs : global::Pulumi.ResourceArgs
    {
        [Input("authParameters", required: true)]
        public Input<Inputs.ConnectionAuthParametersArgs> AuthParameters { get; set; } = null!;

        [Input("authorizationType", required: true)]
        public Input<Pulumi.AwsNative.Events.ConnectionAuthorizationType> AuthorizationType { get; set; } = null!;

        /// <summary>
        /// Description of the connection.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Name of the connection.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ConnectionArgs()
        {
        }
        public static new ConnectionArgs Empty => new ConnectionArgs();
    }
}
