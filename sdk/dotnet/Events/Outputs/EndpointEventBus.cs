// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Events.Outputs
{

    [OutputType]
    public sealed class EndpointEventBus
    {
        public readonly string EventBusArn;

        [OutputConstructor]
        private EndpointEventBus(string eventBusArn)
        {
            EventBusArn = eventBusArn;
        }
    }
}
