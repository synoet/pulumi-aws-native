// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.HealthLake.Outputs
{

    /// <summary>
    /// The preloaded data configuration for the Data Store. Only data preloaded from Synthea is supported.
    /// </summary>
    [OutputType]
    public sealed class FhirDatastorePreloadDataConfig
    {
        /// <summary>
        /// The type of preloaded data. Only Synthea preloaded data is supported.
        /// </summary>
        public readonly Pulumi.AwsNative.HealthLake.FhirDatastorePreloadDataConfigPreloadDataType PreloadDataType;

        [OutputConstructor]
        private FhirDatastorePreloadDataConfig(Pulumi.AwsNative.HealthLake.FhirDatastorePreloadDataConfigPreloadDataType preloadDataType)
        {
            PreloadDataType = preloadDataType;
        }
    }
}
