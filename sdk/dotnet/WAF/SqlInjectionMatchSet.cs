// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAF
{
    /// <summary>
    /// Resource Type definition for AWS::WAF::SqlInjectionMatchSet
    /// </summary>
    [Obsolete(@"SqlInjectionMatchSet is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:waf:SqlInjectionMatchSet")]
    public partial class SqlInjectionMatchSet : Pulumi.CustomResource
    {
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("sqlInjectionMatchTuples")]
        public Output<ImmutableArray<Outputs.SqlInjectionMatchSetSqlInjectionMatchTuple>> SqlInjectionMatchTuples { get; private set; } = null!;


        /// <summary>
        /// Create a SqlInjectionMatchSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SqlInjectionMatchSet(string name, SqlInjectionMatchSetArgs args, CustomResourceOptions? options = null)
            : base("aws-native:waf:SqlInjectionMatchSet", name, args ?? new SqlInjectionMatchSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SqlInjectionMatchSet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:waf:SqlInjectionMatchSet", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing SqlInjectionMatchSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SqlInjectionMatchSet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SqlInjectionMatchSet(name, id, options);
        }
    }

    public sealed class SqlInjectionMatchSetArgs : Pulumi.ResourceArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("sqlInjectionMatchTuples")]
        private InputList<Inputs.SqlInjectionMatchSetSqlInjectionMatchTupleArgs>? _sqlInjectionMatchTuples;
        public InputList<Inputs.SqlInjectionMatchSetSqlInjectionMatchTupleArgs> SqlInjectionMatchTuples
        {
            get => _sqlInjectionMatchTuples ?? (_sqlInjectionMatchTuples = new InputList<Inputs.SqlInjectionMatchSetSqlInjectionMatchTupleArgs>());
            set => _sqlInjectionMatchTuples = value;
        }

        public SqlInjectionMatchSetArgs()
        {
        }
    }
}
