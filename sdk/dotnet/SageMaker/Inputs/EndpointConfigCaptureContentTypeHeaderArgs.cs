// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.SageMaker.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html
    /// </summary>
    public sealed class EndpointConfigCaptureContentTypeHeaderArgs : Pulumi.ResourceArgs
    {
        [Input("CsvContentTypes")]
        private InputList<string>? _CsvContentTypes;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader-csvcontenttypes
        /// </summary>
        public InputList<string> CsvContentTypes
        {
            get => _CsvContentTypes ?? (_CsvContentTypes = new InputList<string>());
            set => _CsvContentTypes = value;
        }

        [Input("JsonContentTypes")]
        private InputList<string>? _JsonContentTypes;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader-jsoncontenttypes
        /// </summary>
        public InputList<string> JsonContentTypes
        {
            get => _JsonContentTypes ?? (_JsonContentTypes = new InputList<string>());
            set => _JsonContentTypes = value;
        }

        public EndpointConfigCaptureContentTypeHeaderArgs()
        {
        }
    }
}