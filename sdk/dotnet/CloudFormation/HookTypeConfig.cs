// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFormation
{
    /// <summary>
    /// Specifies the configuration data for a registered hook in CloudFormation Registry.
    /// </summary>
    [AwsNativeResourceType("aws-native:cloudformation:HookTypeConfig")]
    public partial class HookTypeConfig : Pulumi.CustomResource
    {
        /// <summary>
        /// The configuration data for the extension, in this account and region.
        /// </summary>
        [Output("configuration")]
        public Output<string?> Configuration { get; private set; } = null!;

        /// <summary>
        /// An alias by which to refer to this extension configuration data.
        /// </summary>
        [Output("configurationAlias")]
        public Output<Pulumi.AwsNative.CloudFormation.HookTypeConfigConfigurationAlias?> ConfigurationAlias { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) for the configuration data, in this account and region.
        /// </summary>
        [Output("configurationArn")]
        public Output<string> ConfigurationArn { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the type version.
        /// </summary>
        [Output("typeArn")]
        public Output<string?> TypeArn { get; private set; } = null!;

        /// <summary>
        /// The name of the type being registered.
        /// 
        /// We recommend that type names adhere to the following pattern: company_or_organization::service::type.
        /// </summary>
        [Output("typeName")]
        public Output<string?> TypeName { get; private set; } = null!;


        /// <summary>
        /// Create a HookTypeConfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public HookTypeConfig(string name, HookTypeConfigArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:cloudformation:HookTypeConfig", name, args ?? new HookTypeConfigArgs(), MakeResourceOptions(options, ""))
        {
        }

        private HookTypeConfig(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cloudformation:HookTypeConfig", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing HookTypeConfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static HookTypeConfig Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new HookTypeConfig(name, id, options);
        }
    }

    public sealed class HookTypeConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The configuration data for the extension, in this account and region.
        /// </summary>
        [Input("configuration")]
        public Input<string>? Configuration { get; set; }

        /// <summary>
        /// An alias by which to refer to this extension configuration data.
        /// </summary>
        [Input("configurationAlias")]
        public Input<Pulumi.AwsNative.CloudFormation.HookTypeConfigConfigurationAlias>? ConfigurationAlias { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the type version.
        /// </summary>
        [Input("typeArn")]
        public Input<string>? TypeArn { get; set; }

        /// <summary>
        /// The name of the type being registered.
        /// 
        /// We recommend that type names adhere to the following pattern: company_or_organization::service::type.
        /// </summary>
        [Input("typeName")]
        public Input<string>? TypeName { get; set; }

        public HookTypeConfigArgs()
        {
        }
    }
}
