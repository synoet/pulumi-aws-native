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
    public sealed class SignalCatalogNode1Properties
    {
        public readonly Outputs.SignalCatalogSensor? Sensor;

        [OutputConstructor]
        private SignalCatalogNode1Properties(Outputs.SignalCatalogSensor? sensor)
        {
            Sensor = sensor;
        }
    }
}
