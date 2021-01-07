// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Events.Outputs
{

    [OutputType]
    public sealed class EventBusAttributes
    {
        public readonly string Arn;
        public readonly string Name;
        public readonly string Policy;

        [OutputConstructor]
        private EventBusAttributes(
            string Arn,

            string Name,

            string Policy)
        {
            this.Arn = Arn;
            this.Name = Name;
            this.Policy = Policy;
        }
    }
}