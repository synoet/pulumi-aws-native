// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GuardDuty.Outputs
{

    [OutputType]
    public sealed class DetectorCfns3LogsConfiguration
    {
        public readonly bool Enable;

        [OutputConstructor]
        private DetectorCfns3LogsConfiguration(bool enable)
        {
            Enable = enable;
        }
    }
}
