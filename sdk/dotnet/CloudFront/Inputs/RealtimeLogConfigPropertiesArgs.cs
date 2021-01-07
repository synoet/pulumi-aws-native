// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.CloudFront.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html
    /// </summary>
    public sealed class RealtimeLogConfigPropertiesArgs : Pulumi.ResourceArgs
    {
        [Input("EndPoints", required: true)]
        private InputList<Inputs.RealtimeLogConfigEndPointArgs>? _EndPoints;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-endpoints
        /// </summary>
        public InputList<Inputs.RealtimeLogConfigEndPointArgs> EndPoints
        {
            get => _EndPoints ?? (_EndPoints = new InputList<Inputs.RealtimeLogConfigEndPointArgs>());
            set => _EndPoints = value;
        }

        [Input("Fields", required: true)]
        private InputList<string>? _Fields;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-fields
        /// </summary>
        public InputList<string> Fields
        {
            get => _Fields ?? (_Fields = new InputList<string>());
            set => _Fields = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-name
        /// </summary>
        [Input("Name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-samplingrate
        /// </summary>
        [Input("SamplingRate", required: true)]
        public Input<double> SamplingRate { get; set; } = null!;

        public RealtimeLogConfigPropertiesArgs()
        {
        }
    }
}