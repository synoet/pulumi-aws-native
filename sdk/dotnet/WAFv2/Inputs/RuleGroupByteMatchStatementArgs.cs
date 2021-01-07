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
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html
    /// </summary>
    public sealed class RuleGroupByteMatchStatementArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-fieldtomatch
        /// </summary>
        [Input("FieldToMatch", required: true)]
        public Input<Inputs.RuleGroupFieldToMatchArgs> FieldToMatch { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-positionalconstraint
        /// </summary>
        [Input("PositionalConstraint", required: true)]
        public Input<string> PositionalConstraint { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstring
        /// </summary>
        [Input("SearchString")]
        public Input<string>? SearchString { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstringbase64
        /// </summary>
        [Input("SearchStringBase64")]
        public Input<string>? SearchStringBase64 { get; set; }

        [Input("TextTransformations", required: true)]
        private InputList<Inputs.RuleGroupTextTransformationArgs>? _TextTransformations;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-texttransformations
        /// </summary>
        public InputList<Inputs.RuleGroupTextTransformationArgs> TextTransformations
        {
            get => _TextTransformations ?? (_TextTransformations = new InputList<Inputs.RuleGroupTextTransformationArgs>());
            set => _TextTransformations = value;
        }

        public RuleGroupByteMatchStatementArgs()
        {
        }
    }
}