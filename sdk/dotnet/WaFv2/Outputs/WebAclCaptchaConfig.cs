// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Outputs
{

    [OutputType]
    public sealed class WebAclCaptchaConfig
    {
        public readonly Outputs.WebAclImmunityTimeProperty? ImmunityTimeProperty;

        [OutputConstructor]
        private WebAclCaptchaConfig(Outputs.WebAclImmunityTimeProperty? immunityTimeProperty)
        {
            ImmunityTimeProperty = immunityTimeProperty;
        }
    }
}
