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
    /// Definition of AWS::PCAConnectorAD::TemplateGroupAccessControlEntry Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:pcaconnectorad:TemplateGroupAccessControlEntry")]
    public partial class TemplateGroupAccessControlEntry : global::Pulumi.CustomResource
    {
        [Output("accessRights")]
        public Output<Outputs.TemplateGroupAccessControlEntryAccessRights> AccessRights { get; private set; } = null!;

        [Output("groupDisplayName")]
        public Output<string> GroupDisplayName { get; private set; } = null!;

        [Output("groupSecurityIdentifier")]
        public Output<string?> GroupSecurityIdentifier { get; private set; } = null!;

        [Output("templateArn")]
        public Output<string?> TemplateArn { get; private set; } = null!;


        /// <summary>
        /// Create a TemplateGroupAccessControlEntry resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TemplateGroupAccessControlEntry(string name, TemplateGroupAccessControlEntryArgs args, CustomResourceOptions? options = null)
            : base("aws-native:pcaconnectorad:TemplateGroupAccessControlEntry", name, args ?? new TemplateGroupAccessControlEntryArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TemplateGroupAccessControlEntry(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:pcaconnectorad:TemplateGroupAccessControlEntry", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "groupSecurityIdentifier",
                    "templateArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TemplateGroupAccessControlEntry resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TemplateGroupAccessControlEntry Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new TemplateGroupAccessControlEntry(name, id, options);
        }
    }

    public sealed class TemplateGroupAccessControlEntryArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessRights", required: true)]
        public Input<Inputs.TemplateGroupAccessControlEntryAccessRightsArgs> AccessRights { get; set; } = null!;

        [Input("groupDisplayName", required: true)]
        public Input<string> GroupDisplayName { get; set; } = null!;

        [Input("groupSecurityIdentifier")]
        public Input<string>? GroupSecurityIdentifier { get; set; }

        [Input("templateArn")]
        public Input<string>? TemplateArn { get; set; }

        public TemplateGroupAccessControlEntryArgs()
        {
        }
        public static new TemplateGroupAccessControlEntryArgs Empty => new TemplateGroupAccessControlEntryArgs();
    }
}
