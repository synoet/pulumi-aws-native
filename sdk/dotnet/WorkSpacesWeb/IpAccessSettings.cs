// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WorkSpacesWeb
{
    /// <summary>
    /// Definition of AWS::WorkSpacesWeb::IpAccessSettings Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:workspacesweb:IpAccessSettings")]
    public partial class IpAccessSettings : global::Pulumi.CustomResource
    {
        [Output("additionalEncryptionContext")]
        public Output<Outputs.IpAccessSettingsEncryptionContextMap?> AdditionalEncryptionContext { get; private set; } = null!;

        [Output("associatedPortalArns")]
        public Output<ImmutableArray<string>> AssociatedPortalArns { get; private set; } = null!;

        [Output("creationDate")]
        public Output<string> CreationDate { get; private set; } = null!;

        [Output("customerManagedKey")]
        public Output<string?> CustomerManagedKey { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("displayName")]
        public Output<string?> DisplayName { get; private set; } = null!;

        [Output("ipAccessSettingsArn")]
        public Output<string> IpAccessSettingsArn { get; private set; } = null!;

        [Output("ipRules")]
        public Output<ImmutableArray<Outputs.IpAccessSettingsIpRule>> IpRules { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.IpAccessSettingsTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a IpAccessSettings resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IpAccessSettings(string name, IpAccessSettingsArgs args, CustomResourceOptions? options = null)
            : base("aws-native:workspacesweb:IpAccessSettings", name, args ?? new IpAccessSettingsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private IpAccessSettings(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:workspacesweb:IpAccessSettings", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "additionalEncryptionContext",
                    "customerManagedKey",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing IpAccessSettings resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IpAccessSettings Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new IpAccessSettings(name, id, options);
        }
    }

    public sealed class IpAccessSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("additionalEncryptionContext")]
        public Input<Inputs.IpAccessSettingsEncryptionContextMapArgs>? AdditionalEncryptionContext { get; set; }

        [Input("customerManagedKey")]
        public Input<string>? CustomerManagedKey { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        [Input("ipRules", required: true)]
        private InputList<Inputs.IpAccessSettingsIpRuleArgs>? _ipRules;
        public InputList<Inputs.IpAccessSettingsIpRuleArgs> IpRules
        {
            get => _ipRules ?? (_ipRules = new InputList<Inputs.IpAccessSettingsIpRuleArgs>());
            set => _ipRules = value;
        }

        [Input("tags")]
        private InputList<Inputs.IpAccessSettingsTagArgs>? _tags;
        public InputList<Inputs.IpAccessSettingsTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.IpAccessSettingsTagArgs>());
            set => _tags = value;
        }

        public IpAccessSettingsArgs()
        {
        }
        public static new IpAccessSettingsArgs Empty => new IpAccessSettingsArgs();
    }
}
