// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.OpenSearchService
{
    /// <summary>
    /// An example resource schema demonstrating some basic constructs and validation rules.
    /// </summary>
    [AwsNativeResourceType("aws-native:opensearchservice:Domain")]
    public partial class Domain : global::Pulumi.CustomResource
    {
        [Output("accessPolicies")]
        public Output<object?> AccessPolicies { get; private set; } = null!;

        [Output("advancedOptions")]
        public Output<object?> AdvancedOptions { get; private set; } = null!;

        [Output("advancedSecurityOptions")]
        public Output<Outputs.DomainAdvancedSecurityOptionsInput?> AdvancedSecurityOptions { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("clusterConfig")]
        public Output<Outputs.DomainClusterConfig?> ClusterConfig { get; private set; } = null!;

        [Output("cognitoOptions")]
        public Output<Outputs.DomainCognitoOptions?> CognitoOptions { get; private set; } = null!;

        [Output("domainArn")]
        public Output<string> DomainArn { get; private set; } = null!;

        [Output("domainEndpoint")]
        public Output<string> DomainEndpoint { get; private set; } = null!;

        [Output("domainEndpointOptions")]
        public Output<Outputs.DomainEndpointOptions?> DomainEndpointOptions { get; private set; } = null!;

        [Output("domainEndpoints")]
        public Output<object> DomainEndpoints { get; private set; } = null!;

        [Output("domainName")]
        public Output<string?> DomainName { get; private set; } = null!;

        [Output("ebsOptions")]
        public Output<Outputs.DomainEbsOptions?> EbsOptions { get; private set; } = null!;

        [Output("encryptionAtRestOptions")]
        public Output<Outputs.DomainEncryptionAtRestOptions?> EncryptionAtRestOptions { get; private set; } = null!;

        [Output("engineVersion")]
        public Output<string?> EngineVersion { get; private set; } = null!;

        [Output("logPublishingOptions")]
        public Output<object?> LogPublishingOptions { get; private set; } = null!;

        [Output("nodeToNodeEncryptionOptions")]
        public Output<Outputs.DomainNodeToNodeEncryptionOptions?> NodeToNodeEncryptionOptions { get; private set; } = null!;

        [Output("offPeakWindowOptions")]
        public Output<Outputs.DomainOffPeakWindowOptions?> OffPeakWindowOptions { get; private set; } = null!;

        [Output("serviceSoftwareOptions")]
        public Output<Outputs.DomainServiceSoftwareOptions> ServiceSoftwareOptions { get; private set; } = null!;

        [Output("snapshotOptions")]
        public Output<Outputs.DomainSnapshotOptions?> SnapshotOptions { get; private set; } = null!;

        [Output("softwareUpdateOptions")]
        public Output<Outputs.DomainSoftwareUpdateOptions?> SoftwareUpdateOptions { get; private set; } = null!;

        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this Domain.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.DomainTag>> Tags { get; private set; } = null!;

        [Output("vpcOptions")]
        public Output<Outputs.DomainVpcOptions?> VpcOptions { get; private set; } = null!;


        /// <summary>
        /// Create a Domain resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Domain(string name, DomainArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:opensearchservice:Domain", name, args ?? new DomainArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Domain(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:opensearchservice:Domain", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "domainName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Domain resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Domain Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Domain(name, id, options);
        }
    }

    public sealed class DomainArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessPolicies")]
        public Input<object>? AccessPolicies { get; set; }

        [Input("advancedOptions")]
        public Input<object>? AdvancedOptions { get; set; }

        [Input("advancedSecurityOptions")]
        public Input<Inputs.DomainAdvancedSecurityOptionsInputArgs>? AdvancedSecurityOptions { get; set; }

        [Input("clusterConfig")]
        public Input<Inputs.DomainClusterConfigArgs>? ClusterConfig { get; set; }

        [Input("cognitoOptions")]
        public Input<Inputs.DomainCognitoOptionsArgs>? CognitoOptions { get; set; }

        [Input("domainEndpointOptions")]
        public Input<Inputs.DomainEndpointOptionsArgs>? DomainEndpointOptions { get; set; }

        [Input("domainName")]
        public Input<string>? DomainName { get; set; }

        [Input("ebsOptions")]
        public Input<Inputs.DomainEbsOptionsArgs>? EbsOptions { get; set; }

        [Input("encryptionAtRestOptions")]
        public Input<Inputs.DomainEncryptionAtRestOptionsArgs>? EncryptionAtRestOptions { get; set; }

        [Input("engineVersion")]
        public Input<string>? EngineVersion { get; set; }

        [Input("logPublishingOptions")]
        public Input<object>? LogPublishingOptions { get; set; }

        [Input("nodeToNodeEncryptionOptions")]
        public Input<Inputs.DomainNodeToNodeEncryptionOptionsArgs>? NodeToNodeEncryptionOptions { get; set; }

        [Input("offPeakWindowOptions")]
        public Input<Inputs.DomainOffPeakWindowOptionsArgs>? OffPeakWindowOptions { get; set; }

        [Input("snapshotOptions")]
        public Input<Inputs.DomainSnapshotOptionsArgs>? SnapshotOptions { get; set; }

        [Input("softwareUpdateOptions")]
        public Input<Inputs.DomainSoftwareUpdateOptionsArgs>? SoftwareUpdateOptions { get; set; }

        [Input("tags")]
        private InputList<Inputs.DomainTagArgs>? _tags;

        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this Domain.
        /// </summary>
        public InputList<Inputs.DomainTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DomainTagArgs>());
            set => _tags = value;
        }

        [Input("vpcOptions")]
        public Input<Inputs.DomainVpcOptionsArgs>? VpcOptions { get; set; }

        public DomainArgs()
        {
        }
        public static new DomainArgs Empty => new DomainArgs();
    }
}
