// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.WAFv2.Outputs
{

    [OutputType]
    public sealed class RuleGroupFieldToMatch
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-allqueryarguments
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string>? AllQueryArguments;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-body
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string>? Body;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-method
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string>? Method;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-querystring
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string>? QueryString;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singleheader
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string>? SingleHeader;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singlequeryargument
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string>? SingleQueryArgument;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-uripath
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string>? UriPath;

        [OutputConstructor]
        private RuleGroupFieldToMatch(
            Union<System.Text.Json.JsonElement, string>? AllQueryArguments,

            Union<System.Text.Json.JsonElement, string>? Body,

            Union<System.Text.Json.JsonElement, string>? Method,

            Union<System.Text.Json.JsonElement, string>? QueryString,

            Union<System.Text.Json.JsonElement, string>? SingleHeader,

            Union<System.Text.Json.JsonElement, string>? SingleQueryArgument,

            Union<System.Text.Json.JsonElement, string>? UriPath)
        {
            this.AllQueryArguments = AllQueryArguments;
            this.Body = Body;
            this.Method = Method;
            this.QueryString = QueryString;
            this.SingleHeader = SingleHeader;
            this.SingleQueryArgument = SingleQueryArgument;
            this.UriPath = UriPath;
        }
    }
}