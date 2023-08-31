// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WafRegional
{
    /// <summary>
    /// Resource Type definition for AWS::WAFRegional::XssMatchSet
    /// </summary>
    [Obsolete(@"XssMatchSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:wafregional:XssMatchSet")]
    public partial class XssMatchSet : global::Pulumi.CustomResource
    {
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("xssMatchTuples")]
        public Output<ImmutableArray<Outputs.XssMatchSetXssMatchTuple>> XssMatchTuples { get; private set; } = null!;


        /// <summary>
        /// Create a XssMatchSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public XssMatchSet(string name, XssMatchSetArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:wafregional:XssMatchSet", name, args ?? new XssMatchSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private XssMatchSet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:wafregional:XssMatchSet", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing XssMatchSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static XssMatchSet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new XssMatchSet(name, id, options);
        }
    }

    public sealed class XssMatchSetArgs : global::Pulumi.ResourceArgs
    {
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("xssMatchTuples")]
        private InputList<Inputs.XssMatchSetXssMatchTupleArgs>? _xssMatchTuples;
        public InputList<Inputs.XssMatchSetXssMatchTupleArgs> XssMatchTuples
        {
            get => _xssMatchTuples ?? (_xssMatchTuples = new InputList<Inputs.XssMatchSetXssMatchTupleArgs>());
            set => _xssMatchTuples = value;
        }

        public XssMatchSetArgs()
        {
        }
        public static new XssMatchSetArgs Empty => new XssMatchSetArgs();
    }
}
