// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAF.Inputs
{

    public sealed class SqlInjectionMatchSetSqlInjectionMatchTupleArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldToMatch", required: true)]
        public Input<Inputs.SqlInjectionMatchSetFieldToMatchArgs> FieldToMatch { get; set; } = null!;

        [Input("textTransformation", required: true)]
        public Input<string> TextTransformation { get; set; } = null!;

        public SqlInjectionMatchSetSqlInjectionMatchTupleArgs()
        {
        }
        public static new SqlInjectionMatchSetSqlInjectionMatchTupleArgs Empty => new SqlInjectionMatchSetSqlInjectionMatchTupleArgs();
    }
}
