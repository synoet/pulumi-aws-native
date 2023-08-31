// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MemoryDb
{
    /// <summary>
    /// Resource Type definition for AWS::MemoryDB::User
    /// </summary>
    [AwsNativeResourceType("aws-native:memorydb:User")]
    public partial class User : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Access permissions string used for this user account.
        /// </summary>
        [Output("accessString")]
        public Output<string?> AccessString { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the user account.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("authenticationMode")]
        public Output<Outputs.AuthenticationModeProperties?> AuthenticationMode { get; private set; } = null!;

        /// <summary>
        /// Indicates the user status. Can be "active", "modifying" or "deleting".
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this user.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.UserTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The name of the user.
        /// </summary>
        [Output("userName")]
        public Output<string> UserName { get; private set; } = null!;


        /// <summary>
        /// Create a User resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public User(string name, UserArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:memorydb:User", name, args ?? new UserArgs(), MakeResourceOptions(options, ""))
        {
        }

        private User(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:memorydb:User", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "userName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing User resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static User Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new User(name, id, options);
        }
    }

    public sealed class UserArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Access permissions string used for this user account.
        /// </summary>
        [Input("accessString")]
        public Input<string>? AccessString { get; set; }

        [Input("authenticationMode")]
        public Input<Inputs.AuthenticationModePropertiesArgs>? AuthenticationMode { get; set; }

        [Input("tags")]
        private InputList<Inputs.UserTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this user.
        /// </summary>
        public InputList<Inputs.UserTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.UserTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The name of the user.
        /// </summary>
        [Input("userName")]
        public Input<string>? UserName { get; set; }

        public UserArgs()
        {
        }
        public static new UserArgs Empty => new UserArgs();
    }
}
