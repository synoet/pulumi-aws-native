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
    public sealed class WebAclImmunityTimeProperty
    {
        public readonly int ImmunityTime;

        [OutputConstructor]
        private WebAclImmunityTimeProperty(int immunityTime)
        {
            ImmunityTime = immunityTime;
        }
    }
}
