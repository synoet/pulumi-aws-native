// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.OpsWorks.Outputs
{

    [OutputType]
    public sealed class LayerShutdownEventConfiguration
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration-delayuntilelbconnectionsdrained
        /// </summary>
        public readonly bool? DelayUntilElbConnectionsDrained;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration-executiontimeout
        /// </summary>
        public readonly int? ExecutionTimeout;

        [OutputConstructor]
        private LayerShutdownEventConfiguration(
            bool? DelayUntilElbConnectionsDrained,

            int? ExecutionTimeout)
        {
            this.DelayUntilElbConnectionsDrained = DelayUntilElbConnectionsDrained;
            this.ExecutionTimeout = ExecutionTimeout;
        }
    }
}