// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SupportApp
{
    /// <summary>
    /// An AWS Support App resource that creates, updates, reads, and deletes a customer's account alias.
    /// </summary>
    [AwsNativeResourceType("aws-native:supportapp:AccountAlias")]
    public partial class AccountAlias : global::Pulumi.CustomResource
    {
        /// <summary>
        /// An account alias associated with a customer's account.
        /// </summary>
        [Output("accountAlias")]
        public Output<string> AccountAliasValue { get; private set; } = null!;

        /// <summary>
        /// Unique identifier representing an alias tied to an account
        /// </summary>
        [Output("accountAliasResourceId")]
        public Output<string> AccountAliasResourceId { get; private set; } = null!;


        /// <summary>
        /// Create a AccountAlias resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AccountAlias(string name, AccountAliasArgs args, CustomResourceOptions? options = null)
            : base("aws-native:supportapp:AccountAlias", name, args ?? new AccountAliasArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AccountAlias(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:supportapp:AccountAlias", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing AccountAlias resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AccountAlias Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AccountAlias(name, id, options);
        }
    }

    public sealed class AccountAliasArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// An account alias associated with a customer's account.
        /// </summary>
        [Input("accountAlias", required: true)]
        public Input<string> AccountAliasValue { get; set; } = null!;

        public AccountAliasArgs()
        {
        }
        public static new AccountAliasArgs Empty => new AccountAliasArgs();
    }
}
