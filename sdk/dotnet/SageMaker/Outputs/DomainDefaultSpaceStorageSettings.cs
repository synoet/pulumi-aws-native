// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Outputs
{

    /// <summary>
    /// Default storage settings for a space.
    /// </summary>
    [OutputType]
    public sealed class DomainDefaultSpaceStorageSettings
    {
        public readonly Outputs.DomainDefaultEbsStorageSettings? DefaultEbsStorageSettings;

        [OutputConstructor]
        private DomainDefaultSpaceStorageSettings(Outputs.DomainDefaultEbsStorageSettings? defaultEbsStorageSettings)
        {
            DefaultEbsStorageSettings = defaultEbsStorageSettings;
        }
    }
}
