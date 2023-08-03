// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticLoadBalancing.Outputs
{

    [OutputType]
    public sealed class LoadBalancerLbCookieStickinessPolicy
    {
        public readonly string? CookieExpirationPeriod;
        public readonly string? PolicyName;

        [OutputConstructor]
        private LoadBalancerLbCookieStickinessPolicy(
            string? cookieExpirationPeriod,

            string? policyName)
        {
            CookieExpirationPeriod = cookieExpirationPeriod;
            PolicyName = policyName;
        }
    }
}
