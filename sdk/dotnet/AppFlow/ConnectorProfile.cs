// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow
{
    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html
    /// </summary>
    [AwsNativeResourceType("aws-native:appflow:ConnectorProfile")]
    public partial class ConnectorProfile : Pulumi.CustomResource
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectionmode
        /// </summary>
        [Output("connectionMode")]
        public Output<string> ConnectionMode { get; private set; } = null!;

        [Output("connectorProfileArn")]
        public Output<string> ConnectorProfileArn { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectorprofileconfig
        /// </summary>
        [Output("connectorProfileConfig")]
        public Output<Outputs.ConnectorProfileConnectorProfileConfig?> ConnectorProfileConfig { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectorprofilename
        /// </summary>
        [Output("connectorProfileName")]
        public Output<string> ConnectorProfileName { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectortype
        /// </summary>
        [Output("connectorType")]
        public Output<string> ConnectorType { get; private set; } = null!;

        [Output("credentialsArn")]
        public Output<string> CredentialsArn { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-kmsarn
        /// </summary>
        [Output("kMSArn")]
        public Output<string?> KMSArn { get; private set; } = null!;


        /// <summary>
        /// Create a ConnectorProfile resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ConnectorProfile(string name, ConnectorProfileArgs args, CustomResourceOptions? options = null)
            : base("aws-native:appflow:ConnectorProfile", name, args ?? new ConnectorProfileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ConnectorProfile(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:appflow:ConnectorProfile", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ConnectorProfile resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ConnectorProfile Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ConnectorProfile(name, id, options);
        }
    }

    public sealed class ConnectorProfileArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectionmode
        /// </summary>
        [Input("connectionMode", required: true)]
        public Input<string> ConnectionMode { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectorprofileconfig
        /// </summary>
        [Input("connectorProfileConfig")]
        public Input<Inputs.ConnectorProfileConnectorProfileConfigArgs>? ConnectorProfileConfig { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectorprofilename
        /// </summary>
        [Input("connectorProfileName", required: true)]
        public Input<string> ConnectorProfileName { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectortype
        /// </summary>
        [Input("connectorType", required: true)]
        public Input<string> ConnectorType { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-kmsarn
        /// </summary>
        [Input("kMSArn")]
        public Input<string>? KMSArn { get; set; }

        public ConnectorProfileArgs()
        {
        }
    }
}
