// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ApiGateway.Outputs
{

    [OutputType]
    public sealed class RequestValidatorProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html#cfn-apigateway-requestvalidator-name
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html#cfn-apigateway-requestvalidator-restapiid
        /// </summary>
        public readonly string RestApiId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html#cfn-apigateway-requestvalidator-validaterequestbody
        /// </summary>
        public readonly bool? ValidateRequestBody;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html#cfn-apigateway-requestvalidator-validaterequestparameters
        /// </summary>
        public readonly bool? ValidateRequestParameters;

        [OutputConstructor]
        private RequestValidatorProperties(
            string? Name,

            string RestApiId,

            bool? ValidateRequestBody,

            bool? ValidateRequestParameters)
        {
            this.Name = Name;
            this.RestApiId = RestApiId;
            this.ValidateRequestBody = ValidateRequestBody;
            this.ValidateRequestParameters = ValidateRequestParameters;
        }
    }
}