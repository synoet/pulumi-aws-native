// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.OpsWorksCm
{
    /// <summary>
    /// Resource Type definition for AWS::OpsWorksCM::Server
    /// </summary>
    [AwsNativeResourceType("aws-native:opsworkscm:Server")]
    public partial class Server : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("associatePublicIpAddress")]
        public Output<bool?> AssociatePublicIpAddress { get; private set; } = null!;

        [Output("backupId")]
        public Output<string?> BackupId { get; private set; } = null!;

        [Output("backupRetentionCount")]
        public Output<int?> BackupRetentionCount { get; private set; } = null!;

        [Output("customCertificate")]
        public Output<string?> CustomCertificate { get; private set; } = null!;

        [Output("customDomain")]
        public Output<string?> CustomDomain { get; private set; } = null!;

        [Output("customPrivateKey")]
        public Output<string?> CustomPrivateKey { get; private set; } = null!;

        [Output("disableAutomatedBackup")]
        public Output<bool?> DisableAutomatedBackup { get; private set; } = null!;

        [Output("endpoint")]
        public Output<string> Endpoint { get; private set; } = null!;

        [Output("engine")]
        public Output<string?> Engine { get; private set; } = null!;

        [Output("engineAttributes")]
        public Output<ImmutableArray<Outputs.ServerEngineAttribute>> EngineAttributes { get; private set; } = null!;

        [Output("engineModel")]
        public Output<string?> EngineModel { get; private set; } = null!;

        [Output("engineVersion")]
        public Output<string?> EngineVersion { get; private set; } = null!;

        [Output("instanceProfileArn")]
        public Output<string> InstanceProfileArn { get; private set; } = null!;

        [Output("instanceType")]
        public Output<string> InstanceType { get; private set; } = null!;

        [Output("keyPair")]
        public Output<string?> KeyPair { get; private set; } = null!;

        [Output("preferredBackupWindow")]
        public Output<string?> PreferredBackupWindow { get; private set; } = null!;

        [Output("preferredMaintenanceWindow")]
        public Output<string?> PreferredMaintenanceWindow { get; private set; } = null!;

        [Output("securityGroupIds")]
        public Output<ImmutableArray<string>> SecurityGroupIds { get; private set; } = null!;

        [Output("serverName")]
        public Output<string> ServerName { get; private set; } = null!;

        [Output("serviceRoleArn")]
        public Output<string> ServiceRoleArn { get; private set; } = null!;

        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.ServerTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Server resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Server(string name, ServerArgs args, CustomResourceOptions? options = null)
            : base("aws-native:opsworkscm:Server", name, args ?? new ServerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Server(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:opsworkscm:Server", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "associatePublicIpAddress",
                    "backupId",
                    "customCertificate",
                    "customDomain",
                    "customPrivateKey",
                    "engine",
                    "engineModel",
                    "engineVersion",
                    "instanceProfileArn",
                    "instanceType",
                    "keyPair",
                    "securityGroupIds[*]",
                    "serverName",
                    "serviceRoleArn",
                    "subnetIds[*]",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Server resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Server Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Server(name, id, options);
        }
    }

    public sealed class ServerArgs : global::Pulumi.ResourceArgs
    {
        [Input("associatePublicIpAddress")]
        public Input<bool>? AssociatePublicIpAddress { get; set; }

        [Input("backupId")]
        public Input<string>? BackupId { get; set; }

        [Input("backupRetentionCount")]
        public Input<int>? BackupRetentionCount { get; set; }

        [Input("customCertificate")]
        public Input<string>? CustomCertificate { get; set; }

        [Input("customDomain")]
        public Input<string>? CustomDomain { get; set; }

        [Input("customPrivateKey")]
        public Input<string>? CustomPrivateKey { get; set; }

        [Input("disableAutomatedBackup")]
        public Input<bool>? DisableAutomatedBackup { get; set; }

        [Input("engine")]
        public Input<string>? Engine { get; set; }

        [Input("engineAttributes")]
        private InputList<Inputs.ServerEngineAttributeArgs>? _engineAttributes;
        public InputList<Inputs.ServerEngineAttributeArgs> EngineAttributes
        {
            get => _engineAttributes ?? (_engineAttributes = new InputList<Inputs.ServerEngineAttributeArgs>());
            set => _engineAttributes = value;
        }

        [Input("engineModel")]
        public Input<string>? EngineModel { get; set; }

        [Input("engineVersion")]
        public Input<string>? EngineVersion { get; set; }

        [Input("instanceProfileArn", required: true)]
        public Input<string> InstanceProfileArn { get; set; } = null!;

        [Input("instanceType", required: true)]
        public Input<string> InstanceType { get; set; } = null!;

        [Input("keyPair")]
        public Input<string>? KeyPair { get; set; }

        [Input("preferredBackupWindow")]
        public Input<string>? PreferredBackupWindow { get; set; }

        [Input("preferredMaintenanceWindow")]
        public Input<string>? PreferredMaintenanceWindow { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        [Input("serverName")]
        public Input<string>? ServerName { get; set; }

        [Input("serviceRoleArn", required: true)]
        public Input<string> ServiceRoleArn { get; set; } = null!;

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputList<Inputs.ServerTagArgs>? _tags;
        public InputList<Inputs.ServerTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ServerTagArgs>());
            set => _tags = value;
        }

        public ServerArgs()
        {
        }
        public static new ServerArgs Empty => new ServerArgs();
    }
}
