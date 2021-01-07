// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.NetworkManager.Outputs
{

    [OutputType]
    public sealed class LinkBandwidth
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-downloadspeed
        /// </summary>
        public readonly int? DownloadSpeed;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-uploadspeed
        /// </summary>
        public readonly int? UploadSpeed;

        [OutputConstructor]
        private LinkBandwidth(
            int? DownloadSpeed,

            int? UploadSpeed)
        {
            this.DownloadSpeed = DownloadSpeed;
            this.UploadSpeed = UploadSpeed;
        }
    }
}