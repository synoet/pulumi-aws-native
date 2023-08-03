// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Outputs
{

    /// <summary>
    /// The minimum and maximum amount of total local storage, in GB.
    /// </summary>
    [OutputType]
    public sealed class LaunchTemplateTotalLocalStorageGb
    {
        public readonly double? Max;
        public readonly double? Min;

        [OutputConstructor]
        private LaunchTemplateTotalLocalStorageGb(
            double? max,

            double? min)
        {
            Max = max;
            Min = min;
        }
    }
}
