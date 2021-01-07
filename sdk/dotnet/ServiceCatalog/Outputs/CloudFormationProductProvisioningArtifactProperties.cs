// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ServiceCatalog.Outputs
{

    [OutputType]
    public sealed class CloudFormationProductProvisioningArtifactProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-description
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-disabletemplatevalidation
        /// </summary>
        public readonly bool? DisableTemplateValidation;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-info
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string> Info;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-name
        /// </summary>
        public readonly string? Name;

        [OutputConstructor]
        private CloudFormationProductProvisioningArtifactProperties(
            string? Description,

            bool? DisableTemplateValidation,

            Union<System.Text.Json.JsonElement, string> Info,

            string? Name)
        {
            this.Description = Description;
            this.DisableTemplateValidation = DisableTemplateValidation;
            this.Info = Info;
            this.Name = Name;
        }
    }
}