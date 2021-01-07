// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ApiGateway.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-apistage.html
    /// </summary>
    public sealed class UsagePlanApiStageArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-apistage.html#cfn-apigateway-usageplan-apistage-apiid
        /// </summary>
        [Input("ApiId")]
        public Input<string>? ApiId { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-apistage.html#cfn-apigateway-usageplan-apistage-stage
        /// </summary>
        [Input("Stage")]
        public Input<string>? Stage { get; set; }

        [Input("Throttle")]
        private InputMap<Inputs.UsagePlanThrottleSettingsArgs>? _Throttle;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-apistage.html#cfn-apigateway-usageplan-apistage-throttle
        /// </summary>
        public InputMap<Inputs.UsagePlanThrottleSettingsArgs> Throttle
        {
            get => _Throttle ?? (_Throttle = new InputMap<Inputs.UsagePlanThrottleSettingsArgs>());
            set => _Throttle = value;
        }

        public UsagePlanApiStageArgs()
        {
        }
    }
}