// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PcaConnectorAd.Outputs
{

    [OutputType]
    public sealed class TemplateApplicationPolicy1Properties
    {
        public readonly string PolicyObjectIdentifier;

        [OutputConstructor]
        private TemplateApplicationPolicy1Properties(string policyObjectIdentifier)
        {
            PolicyObjectIdentifier = policyObjectIdentifier;
        }
    }
}
