// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS
{
    /// <summary>
    /// The AWS::RDS::CustomDBEngineVersion resource creates an Amazon RDS custom DB engine version.
    /// </summary>
    [AwsNativeResourceType("aws-native:rds:CustomDBEngineVersion")]
    public partial class CustomDBEngineVersion : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
        /// </summary>
        [Output("databaseInstallationFilesS3BucketName")]
        public Output<string> DatabaseInstallationFilesS3BucketName { get; private set; } = null!;

        /// <summary>
        /// The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
        /// </summary>
        [Output("databaseInstallationFilesS3Prefix")]
        public Output<string?> DatabaseInstallationFilesS3Prefix { get; private set; } = null!;

        /// <summary>
        /// The ARN of the custom engine version.
        /// </summary>
        [Output("dbEngineVersionArn")]
        public Output<string> DbEngineVersionArn { get; private set; } = null!;

        /// <summary>
        /// An optional description of your CEV.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
        /// </summary>
        [Output("engine")]
        public Output<string> Engine { get; private set; } = null!;

        /// <summary>
        /// The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
        /// </summary>
        [Output("engineVersion")]
        public Output<string> EngineVersion { get; private set; } = null!;

        /// <summary>
        /// The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
        /// </summary>
        [Output("manifest")]
        public Output<string?> Manifest { get; private set; } = null!;

        /// <summary>
        /// The availability status to be assigned to the CEV.
        /// </summary>
        [Output("status")]
        public Output<Pulumi.AwsNative.RDS.CustomDBEngineVersionStatus?> Status { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.CustomDBEngineVersionTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a CustomDBEngineVersion resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CustomDBEngineVersion(string name, CustomDBEngineVersionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:rds:CustomDBEngineVersion", name, args ?? new CustomDBEngineVersionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CustomDBEngineVersion(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:rds:CustomDBEngineVersion", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing CustomDBEngineVersion resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CustomDBEngineVersion Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new CustomDBEngineVersion(name, id, options);
        }
    }

    public sealed class CustomDBEngineVersionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
        /// </summary>
        [Input("databaseInstallationFilesS3BucketName", required: true)]
        public Input<string> DatabaseInstallationFilesS3BucketName { get; set; } = null!;

        /// <summary>
        /// The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
        /// </summary>
        [Input("databaseInstallationFilesS3Prefix")]
        public Input<string>? DatabaseInstallationFilesS3Prefix { get; set; }

        /// <summary>
        /// An optional description of your CEV.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
        /// </summary>
        [Input("engine", required: true)]
        public Input<string> Engine { get; set; } = null!;

        /// <summary>
        /// The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
        /// </summary>
        [Input("engineVersion", required: true)]
        public Input<string> EngineVersion { get; set; } = null!;

        /// <summary>
        /// The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
        /// </summary>
        [Input("manifest")]
        public Input<string>? Manifest { get; set; }

        /// <summary>
        /// The availability status to be assigned to the CEV.
        /// </summary>
        [Input("status")]
        public Input<Pulumi.AwsNative.RDS.CustomDBEngineVersionStatus>? Status { get; set; }

        [Input("tags")]
        private InputList<Inputs.CustomDBEngineVersionTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.CustomDBEngineVersionTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.CustomDBEngineVersionTagArgs>());
            set => _tags = value;
        }

        public CustomDBEngineVersionArgs()
        {
        }
        public static new CustomDBEngineVersionArgs Empty => new CustomDBEngineVersionArgs();
    }
}
