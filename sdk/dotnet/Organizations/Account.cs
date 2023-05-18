// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Organizations
{
    /// <summary>
    /// You can use AWS::Organizations::Account to manage accounts in organization.
    /// </summary>
    [AwsNativeResourceType("aws-native:organizations:Account")]
    public partial class Account : global::Pulumi.CustomResource
    {
        /// <summary>
        /// If the account was created successfully, the unique identifier (ID) of the new account.
        /// </summary>
        [Output("accountId")]
        public Output<string> AccountId { get; private set; } = null!;

        /// <summary>
        /// The friendly name of the member account.
        /// </summary>
        [Output("accountName")]
        public Output<string> AccountName { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the account.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The email address of the owner to assign to the new member account.
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// The method by which the account joined the organization.
        /// </summary>
        [Output("joinedMethod")]
        public Output<Pulumi.AwsNative.Organizations.AccountJoinedMethod> JoinedMethod { get; private set; } = null!;

        /// <summary>
        /// The date the account became a part of the organization.
        /// </summary>
        [Output("joinedTimestamp")]
        public Output<string> JoinedTimestamp { get; private set; } = null!;

        /// <summary>
        /// List of parent nodes for the member account. Currently only one parent at a time is supported. Default is root.
        /// </summary>
        [Output("parentIds")]
        public Output<ImmutableArray<string>> ParentIds { get; private set; } = null!;

        /// <summary>
        /// The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. Default name is OrganizationAccountAccessRole if not specified.
        /// </summary>
        [Output("roleName")]
        public Output<string?> RoleName { get; private set; } = null!;

        /// <summary>
        /// The status of the account in the organization.
        /// </summary>
        [Output("status")]
        public Output<Pulumi.AwsNative.Organizations.AccountStatus> Status { get; private set; } = null!;

        /// <summary>
        /// A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.AccountTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Account resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Account(string name, AccountArgs args, CustomResourceOptions? options = null)
            : base("aws-native:organizations:Account", name, args ?? new AccountArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Account(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:organizations:Account", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Account resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Account Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Account(name, id, options);
        }
    }

    public sealed class AccountArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The friendly name of the member account.
        /// </summary>
        [Input("accountName")]
        public Input<string>? AccountName { get; set; }

        /// <summary>
        /// The email address of the owner to assign to the new member account.
        /// </summary>
        [Input("email", required: true)]
        public Input<string> Email { get; set; } = null!;

        [Input("parentIds")]
        private InputList<string>? _parentIds;

        /// <summary>
        /// List of parent nodes for the member account. Currently only one parent at a time is supported. Default is root.
        /// </summary>
        public InputList<string> ParentIds
        {
            get => _parentIds ?? (_parentIds = new InputList<string>());
            set => _parentIds = value;
        }

        /// <summary>
        /// The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. Default name is OrganizationAccountAccessRole if not specified.
        /// </summary>
        [Input("roleName")]
        public Input<string>? RoleName { get; set; }

        [Input("tags")]
        private InputList<Inputs.AccountTagArgs>? _tags;

        /// <summary>
        /// A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value.
        /// </summary>
        public InputList<Inputs.AccountTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.AccountTagArgs>());
            set => _tags = value;
        }

        public AccountArgs()
        {
        }
        public static new AccountArgs Empty => new AccountArgs();
    }
}
