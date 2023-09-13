// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PcaConnectorAd.Inputs
{

    public sealed class TemplateExtensionsV2Args : global::Pulumi.ResourceArgs
    {
        [Input("applicationPolicies")]
        public Input<Inputs.TemplateApplicationPoliciesArgs>? ApplicationPolicies { get; set; }

        [Input("keyUsage", required: true)]
        public Input<Inputs.TemplateKeyUsageArgs> KeyUsage { get; set; } = null!;

        public TemplateExtensionsV2Args()
        {
        }
        public static new TemplateExtensionsV2Args Empty => new TemplateExtensionsV2Args();
    }
}
