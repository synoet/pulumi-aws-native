// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WafRegional.Outputs
{

    [OutputType]
    public sealed class XssMatchSetXssMatchTuple
    {
        public readonly Outputs.XssMatchSetFieldToMatch FieldToMatch;
        public readonly string TextTransformation;

        [OutputConstructor]
        private XssMatchSetXssMatchTuple(
            Outputs.XssMatchSetFieldToMatch fieldToMatch,

            string textTransformation)
        {
            FieldToMatch = fieldToMatch;
            TextTransformation = textTransformation;
        }
    }
}
