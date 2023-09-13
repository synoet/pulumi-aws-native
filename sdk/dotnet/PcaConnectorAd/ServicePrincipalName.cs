// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PcaConnectorAd
{
    /// <summary>
    /// Definition of AWS::PCAConnectorAD::ServicePrincipalName Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:pcaconnectorad:ServicePrincipalName")]
    public partial class ServicePrincipalName : global::Pulumi.CustomResource
    {
        [Output("connectorArn")]
        public Output<string?> ConnectorArn { get; private set; } = null!;

        [Output("directoryRegistrationArn")]
        public Output<string?> DirectoryRegistrationArn { get; private set; } = null!;


        /// <summary>
        /// Create a ServicePrincipalName resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServicePrincipalName(string name, ServicePrincipalNameArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:pcaconnectorad:ServicePrincipalName", name, args ?? new ServicePrincipalNameArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServicePrincipalName(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:pcaconnectorad:ServicePrincipalName", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "connectorArn",
                    "directoryRegistrationArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ServicePrincipalName resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServicePrincipalName Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ServicePrincipalName(name, id, options);
        }
    }

    public sealed class ServicePrincipalNameArgs : global::Pulumi.ResourceArgs
    {
        [Input("connectorArn")]
        public Input<string>? ConnectorArn { get; set; }

        [Input("directoryRegistrationArn")]
        public Input<string>? DirectoryRegistrationArn { get; set; }

        public ServicePrincipalNameArgs()
        {
        }
        public static new ServicePrincipalNameArgs Empty => new ServicePrincipalNameArgs();
    }
}
