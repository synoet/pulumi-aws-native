// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Outputs
{

    /// <summary>
    /// Sqli Match Statement.
    /// </summary>
    [OutputType]
    public sealed class WebAclSqliMatchStatement
    {
        public readonly Outputs.WebAclFieldToMatch FieldToMatch;
        public readonly Pulumi.AwsNative.WaFv2.WebAclSensitivityLevel? SensitivityLevel;
        public readonly ImmutableArray<Outputs.WebAclTextTransformation> TextTransformations;

        [OutputConstructor]
        private WebAclSqliMatchStatement(
            Outputs.WebAclFieldToMatch fieldToMatch,

            Pulumi.AwsNative.WaFv2.WebAclSensitivityLevel? sensitivityLevel,

            ImmutableArray<Outputs.WebAclTextTransformation> textTransformations)
        {
            FieldToMatch = fieldToMatch;
            SensitivityLevel = sensitivityLevel;
            TextTransformations = textTransformations;
        }
    }
}
