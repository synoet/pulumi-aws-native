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
    public sealed class SizeConstraintSetSizeConstraint
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-comparisonoperator
        /// </summary>
        public readonly string ComparisonOperator;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch
        /// </summary>
        public readonly Outputs.SizeConstraintSetFieldToMatch FieldToMatch;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-size
        /// </summary>
        public readonly int Size;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-texttransformation
        /// </summary>
        public readonly string TextTransformation;

        [OutputConstructor]
        private SizeConstraintSetSizeConstraint(
            string ComparisonOperator,

            Outputs.SizeConstraintSetFieldToMatch FieldToMatch,

            int Size,

            string TextTransformation)
        {
            this.ComparisonOperator = ComparisonOperator;
            this.FieldToMatch = FieldToMatch;
            this.Size = Size;
            this.TextTransformation = TextTransformation;
        }
    }
}