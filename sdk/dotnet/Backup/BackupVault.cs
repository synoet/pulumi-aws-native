// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Backup
{
    /// <summary>
    /// Resource Type definition for AWS::Backup::BackupVault
    /// </summary>
    [AwsNativeResourceType("aws-native:backup:BackupVault")]
    public partial class BackupVault : global::Pulumi.CustomResource
    {
        [Output("accessPolicy")]
        public Output<object?> AccessPolicy { get; private set; } = null!;

        [Output("backupVaultArn")]
        public Output<string> BackupVaultArn { get; private set; } = null!;

        [Output("backupVaultName")]
        public Output<string> BackupVaultName { get; private set; } = null!;

        [Output("backupVaultTags")]
        public Output<object?> BackupVaultTags { get; private set; } = null!;

        [Output("encryptionKeyArn")]
        public Output<string?> EncryptionKeyArn { get; private set; } = null!;

        [Output("lockConfiguration")]
        public Output<Outputs.BackupVaultLockConfigurationType?> LockConfiguration { get; private set; } = null!;

        [Output("notifications")]
        public Output<Outputs.BackupVaultNotificationObjectType?> Notifications { get; private set; } = null!;


        /// <summary>
        /// Create a BackupVault resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BackupVault(string name, BackupVaultArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:backup:BackupVault", name, args ?? new BackupVaultArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BackupVault(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:backup:BackupVault", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "backupVaultName",
                    "encryptionKeyArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BackupVault resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BackupVault Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new BackupVault(name, id, options);
        }
    }

    public sealed class BackupVaultArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessPolicy")]
        public Input<object>? AccessPolicy { get; set; }

        [Input("backupVaultName")]
        public Input<string>? BackupVaultName { get; set; }

        [Input("backupVaultTags")]
        public Input<object>? BackupVaultTags { get; set; }

        [Input("encryptionKeyArn")]
        public Input<string>? EncryptionKeyArn { get; set; }

        [Input("lockConfiguration")]
        public Input<Inputs.BackupVaultLockConfigurationTypeArgs>? LockConfiguration { get; set; }

        [Input("notifications")]
        public Input<Inputs.BackupVaultNotificationObjectTypeArgs>? Notifications { get; set; }

        public BackupVaultArgs()
        {
        }
        public static new BackupVaultArgs Empty => new BackupVaultArgs();
    }
}
