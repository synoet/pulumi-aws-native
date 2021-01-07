// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.WAF.Outputs
{

    [OutputType]
    public sealed class WebACLProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-defaultaction
        /// </summary>
        public readonly Outputs.WebACLWafAction DefaultAction;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-metricname
        /// </summary>
        public readonly string MetricName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-name
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-rules
        /// </summary>
        public readonly ImmutableArray<Outputs.WebACLActivatedRule> Rules;

        [OutputConstructor]
        private WebACLProperties(
            Outputs.WebACLWafAction DefaultAction,

            string MetricName,

            string Name,

            ImmutableArray<Outputs.WebACLActivatedRule> Rules)
        {
            this.DefaultAction = DefaultAction;
            this.MetricName = MetricName;
            this.Name = Name;
            this.Rules = Rules;
        }
    }
}