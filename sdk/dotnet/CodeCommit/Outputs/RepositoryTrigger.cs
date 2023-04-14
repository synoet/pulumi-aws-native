// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeCommit.Outputs
{

    [OutputType]
    public sealed class RepositoryTrigger
    {
        public readonly ImmutableArray<string> Branches;
        public readonly string? CustomData;
        public readonly string DestinationArn;
        public readonly ImmutableArray<string> Events;
        public readonly string Name;

        [OutputConstructor]
        private RepositoryTrigger(
            ImmutableArray<string> branches,

            string? customData,

            string destinationArn,

            ImmutableArray<string> events,

            string name)
        {
            Branches = branches;
            CustomData = customData;
            DestinationArn = destinationArn;
            Events = events;
            Name = name;
        }
    }
}
