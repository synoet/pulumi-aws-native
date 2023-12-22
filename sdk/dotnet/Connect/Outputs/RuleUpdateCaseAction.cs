// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect.Outputs
{

    /// <summary>
    /// The definition for update case action.
    /// </summary>
    [OutputType]
    public sealed class RuleUpdateCaseAction
    {
        public readonly ImmutableArray<Outputs.RuleField> Fields;

        [OutputConstructor]
        private RuleUpdateCaseAction(ImmutableArray<Outputs.RuleField> fields)
        {
            Fields = fields;
        }
    }
}
