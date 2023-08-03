// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Waf
{
    /// <summary>
    /// Resource Type definition for AWS::WAF::IPSet
    /// </summary>
    [Obsolete(@"IpSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:waf:IpSet")]
    public partial class IpSet : global::Pulumi.CustomResource
    {
        [Output("ipSetDescriptors")]
        public Output<ImmutableArray<Outputs.IpSetIpSetDescriptor>> IpSetDescriptors { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a IpSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IpSet(string name, IpSetArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:waf:IpSet", name, args ?? new IpSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private IpSet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:waf:IpSet", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing IpSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IpSet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new IpSet(name, id, options);
        }
    }

    public sealed class IpSetArgs : global::Pulumi.ResourceArgs
    {
        [Input("ipSetDescriptors")]
        private InputList<Inputs.IpSetIpSetDescriptorArgs>? _ipSetDescriptors;
        public InputList<Inputs.IpSetIpSetDescriptorArgs> IpSetDescriptors
        {
            get => _ipSetDescriptors ?? (_ipSetDescriptors = new InputList<Inputs.IpSetIpSetDescriptorArgs>());
            set => _ipSetDescriptors = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public IpSetArgs()
        {
        }
        public static new IpSetArgs Empty => new IpSetArgs();
    }
}
