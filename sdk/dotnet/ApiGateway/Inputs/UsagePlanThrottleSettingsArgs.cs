// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway.Inputs
{

    public sealed class UsagePlanThrottleSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The maximum API request rate limit over a time ranging from one to a few seconds. The maximum API request rate limit depends on whether the underlying token bucket is at its full capacity.
        /// </summary>
        [Input("burstLimit")]
        public Input<int>? BurstLimit { get; set; }

        /// <summary>
        /// The API request steady-state rate limit (average requests per second over an extended period of time).
        /// </summary>
        [Input("rateLimit")]
        public Input<double>? RateLimit { get; set; }

        public UsagePlanThrottleSettingsArgs()
        {
        }
        public static new UsagePlanThrottleSettingsArgs Empty => new UsagePlanThrottleSettingsArgs();
    }
}
