// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.MediaPackage.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html
    /// </summary>
    public sealed class OriginEndpointHlsEncryptionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-constantinitializationvector
        /// </summary>
        [Input("ConstantInitializationVector")]
        public Input<string>? ConstantInitializationVector { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-encryptionmethod
        /// </summary>
        [Input("EncryptionMethod")]
        public Input<string>? EncryptionMethod { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-keyrotationintervalseconds
        /// </summary>
        [Input("KeyRotationIntervalSeconds")]
        public Input<int>? KeyRotationIntervalSeconds { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-repeatextxkey
        /// </summary>
        [Input("RepeatExtXKey")]
        public Input<bool>? RepeatExtXKey { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-spekekeyprovider
        /// </summary>
        [Input("SpekeKeyProvider", required: true)]
        public Input<Inputs.OriginEndpointSpekeKeyProviderArgs> SpekeKeyProvider { get; set; } = null!;

        public OriginEndpointHlsEncryptionArgs()
        {
        }
    }
}