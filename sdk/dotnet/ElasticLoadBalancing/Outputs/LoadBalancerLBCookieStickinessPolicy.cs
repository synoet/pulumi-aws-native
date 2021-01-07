// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ElasticLoadBalancing.Outputs
{

    [OutputType]
    public sealed class LoadBalancerLBCookieStickinessPolicy
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-LBCookieStickinessPolicy.html#cfn-elb-lbcookiestickinesspolicy-cookieexpirationperiod
        /// </summary>
        public readonly string? CookieExpirationPeriod;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-LBCookieStickinessPolicy.html#cfn-elb-lbcookiestickinesspolicy-policyname
        /// </summary>
        public readonly string? PolicyName;

        [OutputConstructor]
        private LoadBalancerLBCookieStickinessPolicy(
            string? CookieExpirationPeriod,

            string? PolicyName)
        {
            this.CookieExpirationPeriod = CookieExpirationPeriod;
            this.PolicyName = PolicyName;
        }
    }
}