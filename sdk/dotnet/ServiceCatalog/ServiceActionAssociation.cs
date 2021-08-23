// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ServiceCatalog
{
    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html
    /// </summary>
    [AwsNativeResourceType("aws-native:servicecatalog:ServiceActionAssociation")]
    public partial class ServiceActionAssociation : Pulumi.CustomResource
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-productid
        /// </summary>
        [Output("productId")]
        public Output<string> ProductId { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-provisioningartifactid
        /// </summary>
        [Output("provisioningArtifactId")]
        public Output<string> ProvisioningArtifactId { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-serviceactionid
        /// </summary>
        [Output("serviceActionId")]
        public Output<string> ServiceActionId { get; private set; } = null!;


        /// <summary>
        /// Create a ServiceActionAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServiceActionAssociation(string name, ServiceActionAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:servicecatalog:ServiceActionAssociation", name, args ?? new ServiceActionAssociationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServiceActionAssociation(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:servicecatalog:ServiceActionAssociation", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ServiceActionAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServiceActionAssociation Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ServiceActionAssociation(name, id, options);
        }
    }

    public sealed class ServiceActionAssociationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-productid
        /// </summary>
        [Input("productId", required: true)]
        public Input<string> ProductId { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-provisioningartifactid
        /// </summary>
        [Input("provisioningArtifactId", required: true)]
        public Input<string> ProvisioningArtifactId { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-serviceactionid
        /// </summary>
        [Input("serviceActionId", required: true)]
        public Input<string> ServiceActionId { get; set; } = null!;

        public ServiceActionAssociationArgs()
        {
        }
    }
}
