// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise.Outputs
{

    [OutputType]
    public sealed class SignalCatalogNode3Properties
    {
        public readonly Outputs.SignalCatalogAttribute? Attribute;

        [OutputConstructor]
        private SignalCatalogNode3Properties(Outputs.SignalCatalogAttribute? attribute)
        {
            Attribute = attribute;
        }
    }
}
