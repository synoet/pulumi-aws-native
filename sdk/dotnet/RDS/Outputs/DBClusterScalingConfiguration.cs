// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS.Outputs
{

    /// <summary>
    /// The ScalingConfiguration property type specifies the scaling configuration of an Aurora Serverless DB cluster.
    /// </summary>
    [OutputType]
    public sealed class DBClusterScalingConfiguration
    {
        /// <summary>
        /// A value that indicates whether to allow or disallow automatic pause for an Aurora DB cluster in serverless DB engine mode. A DB cluster can be paused only when it's idle (it has no connections).
        /// </summary>
        public readonly bool? AutoPause;
        /// <summary>
        /// The maximum capacity for an Aurora DB cluster in serverless DB engine mode.
        /// For Aurora MySQL, valid capacity values are 1, 2, 4, 8, 16, 32, 64, 128, and 256.
        /// For Aurora PostgreSQL, valid capacity values are 2, 4, 8, 16, 32, 64, 192, and 384.
        /// The maximum capacity must be greater than or equal to the minimum capacity.
        /// </summary>
        public readonly int? MaxCapacity;
        /// <summary>
        /// The minimum capacity for an Aurora DB cluster in serverless DB engine mode.
        /// For Aurora MySQL, valid capacity values are 1, 2, 4, 8, 16, 32, 64, 128, and 256.
        /// For Aurora PostgreSQL, valid capacity values are 2, 4, 8, 16, 32, 64, 192, and 384.
        /// The minimum capacity must be less than or equal to the maximum capacity.
        /// </summary>
        public readonly int? MinCapacity;
        /// <summary>
        /// The amount of time, in seconds, that Aurora Serverless v1 tries to find a scaling point to perform seamless scaling before enforcing the timeout action.
        /// The default is 300.
        /// </summary>
        public readonly int? SecondsBeforeTimeout;
        /// <summary>
        /// The time, in seconds, before an Aurora DB cluster in serverless mode is paused.
        /// </summary>
        public readonly int? SecondsUntilAutoPause;
        /// <summary>
        /// The action to take when the timeout is reached, either ForceApplyCapacityChange or RollbackCapacityChange.
        /// ForceApplyCapacityChange sets the capacity to the specified value as soon as possible.
        /// RollbackCapacityChange, the default, ignores the capacity change if a scaling point isn't found in the timeout period.
        /// 
        /// For more information, see Autoscaling for Aurora Serverless v1 in the Amazon Aurora User Guide.
        /// </summary>
        public readonly string? TimeoutAction;

        [OutputConstructor]
        private DBClusterScalingConfiguration(
            bool? autoPause,

            int? maxCapacity,

            int? minCapacity,

            int? secondsBeforeTimeout,

            int? secondsUntilAutoPause,

            string? timeoutAction)
        {
            AutoPause = autoPause;
            MaxCapacity = maxCapacity;
            MinCapacity = minCapacity;
            SecondsBeforeTimeout = secondsBeforeTimeout;
            SecondsUntilAutoPause = secondsUntilAutoPause;
            TimeoutAction = timeoutAction;
        }
    }
}
