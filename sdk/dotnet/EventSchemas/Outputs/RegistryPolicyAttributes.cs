// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EventSchemas.Outputs
{

    [OutputType]
    public sealed class RegistryPolicyAttributes
    {
        public readonly string Id;

        [OutputConstructor]
        private RegistryPolicyAttributes(string Id)
        {
            this.Id = Id;
        }
    }
}