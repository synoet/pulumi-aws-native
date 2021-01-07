// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.WAFv2.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html
    /// </summary>
    public sealed class RuleGroupRegexPatternSetReferenceStatementArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-arn
        /// </summary>
        [Input("Arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch
        /// </summary>
        [Input("FieldToMatch", required: true)]
        public Input<Inputs.RuleGroupFieldToMatchArgs> FieldToMatch { get; set; } = null!;

        [Input("TextTransformations", required: true)]
        private InputList<Inputs.RuleGroupTextTransformationArgs>? _TextTransformations;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-texttransformations
        /// </summary>
        public InputList<Inputs.RuleGroupTextTransformationArgs> TextTransformations
        {
            get => _TextTransformations ?? (_TextTransformations = new InputList<Inputs.RuleGroupTextTransformationArgs>());
            set => _TextTransformations = value;
        }

        public RuleGroupRegexPatternSetReferenceStatementArgs()
        {
        }
    }
}