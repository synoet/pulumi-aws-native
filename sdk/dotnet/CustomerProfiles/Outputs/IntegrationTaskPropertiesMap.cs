// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CustomerProfiles.Outputs
{

    [OutputType]
    public sealed class IntegrationTaskPropertiesMap
    {
        public readonly Pulumi.AwsNative.CustomerProfiles.IntegrationOperatorPropertiesKeys OperatorPropertyKey;
        public readonly string Property;

        [OutputConstructor]
        private IntegrationTaskPropertiesMap(
            Pulumi.AwsNative.CustomerProfiles.IntegrationOperatorPropertiesKeys operatorPropertyKey,

            string property)
        {
            OperatorPropertyKey = operatorPropertyKey;
            Property = property;
        }
    }
}
