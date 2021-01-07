// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Cognito.Outputs
{

    [OutputType]
    public sealed class UserPoolSchemaAttribute
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-attributedatatype
        /// </summary>
        public readonly string? AttributeDataType;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-developeronlyattribute
        /// </summary>
        public readonly bool? DeveloperOnlyAttribute;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-mutable
        /// </summary>
        public readonly bool? Mutable;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-name
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-numberattributeconstraints
        /// </summary>
        public readonly Outputs.UserPoolNumberAttributeConstraints? NumberAttributeConstraints;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-required
        /// </summary>
        public readonly bool? Required;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-stringattributeconstraints
        /// </summary>
        public readonly Outputs.UserPoolStringAttributeConstraints? StringAttributeConstraints;

        [OutputConstructor]
        private UserPoolSchemaAttribute(
            string? AttributeDataType,

            bool? DeveloperOnlyAttribute,

            bool? Mutable,

            string? Name,

            Outputs.UserPoolNumberAttributeConstraints? NumberAttributeConstraints,

            bool? Required,

            Outputs.UserPoolStringAttributeConstraints? StringAttributeConstraints)
        {
            this.AttributeDataType = AttributeDataType;
            this.DeveloperOnlyAttribute = DeveloperOnlyAttribute;
            this.Mutable = Mutable;
            this.Name = Name;
            this.NumberAttributeConstraints = NumberAttributeConstraints;
            this.Required = Required;
            this.StringAttributeConstraints = StringAttributeConstraints;
        }
    }
}