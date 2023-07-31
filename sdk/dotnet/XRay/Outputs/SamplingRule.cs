// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.XRay.Outputs
{

    [OutputType]
    public sealed class SamplingRule
    {
        /// <summary>
        /// Matches attributes derived from the request.
        /// </summary>
        public readonly object? Attributes;
        /// <summary>
        /// The percentage of matching requests to instrument, after the reservoir is exhausted.
        /// </summary>
        public readonly double FixedRate;
        /// <summary>
        /// Matches the hostname from a request URL.
        /// </summary>
        public readonly string Host;
        /// <summary>
        /// Matches the HTTP method from a request URL.
        /// </summary>
        public readonly string HttpMethod;
        /// <summary>
        /// The priority of the sampling rule.
        /// </summary>
        public readonly int Priority;
        /// <summary>
        /// A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.
        /// </summary>
        public readonly int ReservoirSize;
        /// <summary>
        /// Matches the ARN of the AWS resource on which the service runs.
        /// </summary>
        public readonly string ResourceArn;
        public readonly string? RuleArn;
        public readonly string? RuleName;
        /// <summary>
        /// Matches the name that the service uses to identify itself in segments.
        /// </summary>
        public readonly string ServiceName;
        /// <summary>
        /// Matches the origin that the service uses to identify its type in segments.
        /// </summary>
        public readonly string ServiceType;
        /// <summary>
        /// Matches the path from a request URL.
        /// </summary>
        public readonly string UrlPath;
        /// <summary>
        /// The version of the sampling rule format (1)
        /// </summary>
        public readonly int? Version;

        [OutputConstructor]
        private SamplingRule(
            object? attributes,

            double fixedRate,

            string host,

            string httpMethod,

            int priority,

            int reservoirSize,

            string resourceArn,

            string? ruleArn,

            string? ruleName,

            string serviceName,

            string serviceType,

            string urlPath,

            int? version)
        {
            Attributes = attributes;
            FixedRate = fixedRate;
            Host = host;
            HttpMethod = httpMethod;
            Priority = priority;
            ReservoirSize = reservoirSize;
            ResourceArn = resourceArn;
            RuleArn = ruleArn;
            RuleName = ruleName;
            ServiceName = serviceName;
            ServiceType = serviceType;
            UrlPath = urlPath;
            Version = version;
        }
    }
}
