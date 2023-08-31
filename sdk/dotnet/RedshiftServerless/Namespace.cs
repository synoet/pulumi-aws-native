// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RedshiftServerless
{
    /// <summary>
    /// Definition of AWS::RedshiftServerless::Namespace Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:redshiftserverless:Namespace")]
    public partial class Namespace : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The password associated with the admin user for the namespace that is being created. Password must be at least 8 characters in length, should be any printable ASCII character. Must contain at least one lowercase letter, one uppercase letter and one decimal digit.
        /// </summary>
        [Output("adminUserPassword")]
        public Output<string?> AdminUserPassword { get; private set; } = null!;

        /// <summary>
        /// The user name associated with the admin user for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.
        /// </summary>
        [Output("adminUsername")]
        public Output<string?> AdminUsername { get; private set; } = null!;

        /// <summary>
        /// The database name associated for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.
        /// </summary>
        [Output("dbName")]
        public Output<string?> DbName { get; private set; } = null!;

        /// <summary>
        /// The default IAM role ARN for the namespace that is being created.
        /// </summary>
        [Output("defaultIamRoleArn")]
        public Output<string?> DefaultIamRoleArn { get; private set; } = null!;

        /// <summary>
        /// The name of the namespace the source snapshot was created from. Please specify the name if needed before deleting namespace
        /// </summary>
        [Output("finalSnapshotName")]
        public Output<string?> FinalSnapshotName { get; private set; } = null!;

        /// <summary>
        /// The number of days to retain automated snapshot in the destination region after they are copied from the source region. If the value is -1, the manual snapshot is retained indefinitely. The value must be either -1 or an integer between 1 and 3,653.
        /// </summary>
        [Output("finalSnapshotRetentionPeriod")]
        public Output<int?> FinalSnapshotRetentionPeriod { get; private set; } = null!;

        /// <summary>
        /// A list of AWS Identity and Access Management (IAM) roles that can be used by the namespace to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. The Default role limit for each request is 10.
        /// </summary>
        [Output("iamRoles")]
        public Output<ImmutableArray<string>> IamRoles { get; private set; } = null!;

        /// <summary>
        /// The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the namespace.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// The collection of log types to be exported provided by the customer. Should only be one of the three supported log types: userlog, useractivitylog and connectionlog
        /// </summary>
        [Output("logExports")]
        public Output<ImmutableArray<Pulumi.AwsNative.RedshiftServerless.NamespaceLogExport>> LogExports { get; private set; } = null!;

        [Output("namespace")]
        public Output<Outputs.Namespace> NamespaceValue { get; private set; } = null!;

        /// <summary>
        /// A unique identifier for the namespace. You use this identifier to refer to the namespace for any subsequent namespace operations such as deleting or modifying. All alphabetical characters must be lower case. Namespace name should be unique for all namespaces within an AWS account.
        /// </summary>
        [Output("namespaceName")]
        public Output<string> NamespaceName { get; private set; } = null!;

        /// <summary>
        /// The list of tags for the namespace.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.NamespaceTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Namespace resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Namespace(string name, NamespaceArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:redshiftserverless:Namespace", name, args ?? new NamespaceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Namespace(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:redshiftserverless:Namespace", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "namespaceName",
                    "tags[*]",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Namespace resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Namespace Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Namespace(name, id, options);
        }
    }

    public sealed class NamespaceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The password associated with the admin user for the namespace that is being created. Password must be at least 8 characters in length, should be any printable ASCII character. Must contain at least one lowercase letter, one uppercase letter and one decimal digit.
        /// </summary>
        [Input("adminUserPassword")]
        public Input<string>? AdminUserPassword { get; set; }

        /// <summary>
        /// The user name associated with the admin user for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.
        /// </summary>
        [Input("adminUsername")]
        public Input<string>? AdminUsername { get; set; }

        /// <summary>
        /// The database name associated for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.
        /// </summary>
        [Input("dbName")]
        public Input<string>? DbName { get; set; }

        /// <summary>
        /// The default IAM role ARN for the namespace that is being created.
        /// </summary>
        [Input("defaultIamRoleArn")]
        public Input<string>? DefaultIamRoleArn { get; set; }

        /// <summary>
        /// The name of the namespace the source snapshot was created from. Please specify the name if needed before deleting namespace
        /// </summary>
        [Input("finalSnapshotName")]
        public Input<string>? FinalSnapshotName { get; set; }

        /// <summary>
        /// The number of days to retain automated snapshot in the destination region after they are copied from the source region. If the value is -1, the manual snapshot is retained indefinitely. The value must be either -1 or an integer between 1 and 3,653.
        /// </summary>
        [Input("finalSnapshotRetentionPeriod")]
        public Input<int>? FinalSnapshotRetentionPeriod { get; set; }

        [Input("iamRoles")]
        private InputList<string>? _iamRoles;

        /// <summary>
        /// A list of AWS Identity and Access Management (IAM) roles that can be used by the namespace to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. The Default role limit for each request is 10.
        /// </summary>
        public InputList<string> IamRoles
        {
            get => _iamRoles ?? (_iamRoles = new InputList<string>());
            set => _iamRoles = value;
        }

        /// <summary>
        /// The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the namespace.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("logExports")]
        private InputList<Pulumi.AwsNative.RedshiftServerless.NamespaceLogExport>? _logExports;

        /// <summary>
        /// The collection of log types to be exported provided by the customer. Should only be one of the three supported log types: userlog, useractivitylog and connectionlog
        /// </summary>
        public InputList<Pulumi.AwsNative.RedshiftServerless.NamespaceLogExport> LogExports
        {
            get => _logExports ?? (_logExports = new InputList<Pulumi.AwsNative.RedshiftServerless.NamespaceLogExport>());
            set => _logExports = value;
        }

        /// <summary>
        /// A unique identifier for the namespace. You use this identifier to refer to the namespace for any subsequent namespace operations such as deleting or modifying. All alphabetical characters must be lower case. Namespace name should be unique for all namespaces within an AWS account.
        /// </summary>
        [Input("namespaceName")]
        public Input<string>? NamespaceName { get; set; }

        [Input("tags")]
        private InputList<Inputs.NamespaceTagArgs>? _tags;

        /// <summary>
        /// The list of tags for the namespace.
        /// </summary>
        public InputList<Inputs.NamespaceTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.NamespaceTagArgs>());
            set => _tags = value;
        }

        public NamespaceArgs()
        {
        }
        public static new NamespaceArgs Empty => new NamespaceArgs();
    }
}
