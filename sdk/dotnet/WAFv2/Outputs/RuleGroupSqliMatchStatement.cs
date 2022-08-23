// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Outputs
{

    /// <summary>
    /// Sqli Match Statement.
    /// </summary>
    [OutputType]
    public sealed class RuleGroupSqliMatchStatement
    {
        public readonly Outputs.RuleGroupFieldToMatch FieldToMatch;
        public readonly Pulumi.AwsNative.WAFv2.RuleGroupSensitivityLevel? SensitivityLevel;
        public readonly ImmutableArray<Outputs.RuleGroupTextTransformation> TextTransformations;

        [OutputConstructor]
        private RuleGroupSqliMatchStatement(
            Outputs.RuleGroupFieldToMatch fieldToMatch,

            Pulumi.AwsNative.WAFv2.RuleGroupSensitivityLevel? sensitivityLevel,

            ImmutableArray<Outputs.RuleGroupTextTransformation> textTransformations)
        {
            FieldToMatch = fieldToMatch;
            SensitivityLevel = sensitivityLevel;
            TextTransformations = textTransformations;
        }
    }
}
