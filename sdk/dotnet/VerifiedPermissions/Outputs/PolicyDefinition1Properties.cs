// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VerifiedPermissions.Outputs
{

    [OutputType]
    public sealed class PolicyDefinition1Properties
    {
        public readonly Outputs.PolicyTemplateLinkedPolicyDefinition TemplateLinked;

        [OutputConstructor]
        private PolicyDefinition1Properties(Outputs.PolicyTemplateLinkedPolicyDefinition templateLinked)
        {
            TemplateLinked = templateLinked;
        }
    }
}
